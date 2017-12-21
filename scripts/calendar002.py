#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Calendar API.
Command-line application that retrieves the list of the user's calendars."""

import sys

from oauth2client import client
from googleapiclient import sample_tools
import sys
import time






def main(argv,start,end,event_name):
    print('call',argv,start,end)
    file = open('./testfile.txt','a')
    file.write('TEST')
    evente = {
        "summary": "Openhab Event",
        "location": event_name,
        "description": "Markus was Present here",
        "start": {
#            "dateTime": "2017-12-28T09:00:00-07:00",
            "dateTime": start,
            "timeZone": "Europe/Zurich"
        },
        "end": {
 #           "dateTime": "2017-12-28T17:00:00-07:00",
            "dateTime": end,
            "timeZone": "Europe/Zurich"
        },
        "attendees": [
            {"email": "markus.schiesser@swisscom.com"},
            {"email": "m.schiesser@gmail.com"}
        ],

    }
    # Authenticate and construct service.
    __file__ ='/etc/openhab2/scripts/client_secrets.json'
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar')

    try:
        page_token = None
        while True:
            calendar_list = service.calendarList().list(
                pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                print('fail')
                break
        event = service.events().insert(calendarId='primary', body=evente).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        file.write(event.get('htmlLink'))
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
       # print('Event',events)
        print('True')
        file.close()


    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')
        file.write('The credentials have been revoked or expired, please re-run'
                              'the application to re-authorize.')
        file.close()

if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    start_time= time.strftime('%Y-%m-%dT%H:%M:%S+01:00', time.localtime(int(sys.argv[1])))
    end_time = time.strftime('%Y-%m-%dT%H:%M:%S+01:00', time.localtime(int(sys.argv[2])))
    event_name = str(sys.argv[3])
    print(sys.argv[0],start_time,end_time, event_name)

    main([sys.argv[0]],start_time,end_time, event_name)
#    return 0

