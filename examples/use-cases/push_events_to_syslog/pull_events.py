import automox_console_sdk as automox
import os
import time
import socket
import json

from automox_console_sdk import EventsApi
from getpass import getpass

def getRecentEvents(event_id=None):
    try:
        page = 0

        while True:
            recent_events = []
            events_page = events_api.get_events(o=organization, limit=500, page=page)

            if len(events_page) == 0:
                return recent_events

            for event in events_page:
                # Stop looking for new events when we see one we know
                if event.id == event_id:
                    return recent_events

                recent_events.append(event)

            page += 1
    except Exception as e:
        print(f"Error - Could not retrieve events: {e}")

def createSyslogPayload(recent_events):
    payload_string = ""

    for event in recent_events:
        payload = {
            "date"    : event.create_time.strftime("%b %d %Y %H:%M:%S"),
            "message" : event.name,
            "data"    : json.dumps(event.data)
        }

        payload_string += f"{payload['date']}: {payload['message']} ({payload['data']})\n"

    payload = str.encode(payload_string)

    return payload

try:
    # Prompt for inputs
    api_secret   = os.getenv('AUTOMOX_API_KEY') or getpass('Enter your API Key: ')
    organization = os.getenv('AUTOMOX_ORGANIZATION_ID') or input("Enter your Organization ID: ")

    config = automox.Configuration()
    client = automox.ApiClient(configuration=config)

    client.default_headers['Authorization'] = f"Bearer {api_secret}"

    events_api = EventsApi(client)

    # Initial placeholder value. Gets overwritten in the main loop.
    top_id = None

    # Our main loop will run every 10 seconds to check for new events
    while True:
        try:
            if not top_id:
                events = events_api.get_events(o=organization, page=0, limit=1)
                top_id = events[0].id
        except Exception as e:
            print(f"Error - Could not retrieve events: {e}")

        print("Getting recent events...")
        recent_events = getRecentEvents(top_id)

        print(f"Found {len(recent_events)} new event(s)")

        # Move the marker event_id for the most recent event.
        if len(recent_events) > 0:
            top_id = recent_events[0].id

            # Prepare the data for the syslog service
            payload = createSyslogPayload(recent_events)

            # Send data to the listening syslog server.
            udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            udp_client_socket.sendto(payload, ("127.0.0.1", 514))

        time.sleep(10)
except Exception as e:
    print(f"Error: {e}")
