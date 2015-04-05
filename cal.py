#! /usr/bin/env python

import sys

import os
import json
import gflags
import httplib2
import arrow

from ConfigParser import ConfigParser

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS


class Calendar(object):
    def __init__(self, client_id, client_secret, api_key, cal_id, creds_file):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_key = api_key
        self.creds_file = creds_file
        self.calendar_id = cal_id
        self.service = None

    def auth(self, force=False):
        if self.service != None or force:
            return self.service

        FLOW = OAuth2WebServerFlow(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope='https://www.googleapis.com/auth/calendar',
            user_agent='DIMVA2015/1.0')

        storage = Storage(self.creds_file)
        credentials = storage.get()

        if credentials is None or credentials.invalid == True:
            credentials = run(FLOW, storage)

        http = credentials.authorize(httplib2.Http())

        service = build(
            serviceName='calendar',
            version='v3',
            http=http,
            developerKey=self.api_key)

        return service

    def events(self):
        self.service = self.auth()

        page_token = None

        while True:
            events = self.service.events().list(
                orderBy='startTime',
                singleEvents=True,
                calendarId=self.calendar_id,
                pageToken=page_token).execute()

            for event in events['items']:
                yield event

            page_token = events.get('nextPageToken')

            if not page_token:
                break


class Event(object):
    def __init__(self, d, tz='Europe/Rome'):
        self.start = d['start']['dateTime']
        self.end = d['end']['dateTime']
        self.summary = d['summary']

        if 'description' in d:
            self.description = d['description']
        else:
            self.description = ''

        self.tz = tz

        self.parse()

    def __repr__(self):
        return '<Event %(summary)s \n %(start)s-%(end)s \n %(d)s>' % {
            'summary': self.summary,
            'start': self.start.format('YYYY-MM-DD HH:mm ZZ'),
            'end': self.end.format('YYYY-MM-DD HH:mm ZZ'),
            'd': self.description
        }

    def parse(self):
        self.start = arrow.get(self.start).to(self.tz)
        self.end = arrow.get(self.end).to(self.tz)
        self.day = self.start.floor('day')


class CalendarSerializer(object):
    DEFAULT_CONF_FILE = '~/.google-calendar-dimva'
    DEFAULT_CREDS_FILE = '~/.google-calendar-dimva.creds'

    def __init__(self, conf_file=DEFAULT_CONF_FILE, \
                creds_file=DEFAULT_CREDS_FILE):
        self.conf_file = conf_file
        self.creds_file = creds_file
        self.cal = None
        self.agenda_by_day = {}

        self.connect()

    def get_agenda(self):
        if not isinstance(self.cal, Calendar):
            return None
        return iter([Event(x) for x in self.cal.events()])

    def get_agenda_by_day(self):
        agenda = self.get_agenda()

        for event in agenda:
            if event.day in self.agenda_by_day:
                self.agenda_by_day[event.day].append(event)
            else:
                self.agenda_by_day[event.day] = [event]

        return self.agenda_by_day

    def connect(self):
        try:
            config = ConfigParser()
            config.read(os.path.expanduser(self.conf_file))

            CLIENT_ID = config.get('Calendar', 'client_id')
            CLIENT_SECRET = config.get('Calendar', 'client_secret')
            API_KEY = config.get('Calendar', 'api_key')
            CAL_ID = config.get('Calendar', 'calendar_id')

            self.creds_file = os.path.expanduser(self.creds_file)
        except Exception, e:
            sys.stdout.write('Error: %s\n' %  e)
            return False

        self.cal = Calendar(
            CLIENT_ID, CLIENT_SECRET, API_KEY, CAL_ID, self.creds_file)

        return True


def main():
    cs = CalendarSerializer()
    import pprint; pprint.pprint([x for x in cs.get_agenda()])
    return 0

if __name__ == '__main__':
    sys.exit(main())
