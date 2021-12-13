# Push Events to Syslog Daemon
The push events to syslog daemon example provides the base for users to view a history of [events](https://developer.automox.com/openapi/axconsole/operation/getEvents/) happening on their Automox instance in their preferred syslog environments. This use case is intended to provide an example of how to use the SDK with Automox events, track them, and send off to a third-party. Due to the varying ways to send data to a SIEM this script will likely need modified to meet environment and/or data needs.

There are two components that need to be ran:
1. Automox Events Client ([`pull_events.py`](./pull_events.py))
2. Syslog Server ([`syslog.py`](./syslog.py))

## Running the Scripts
To run the scripts, first make sure Python 3 is installed on the host system and clone this repository locally then
follow the below steps:
1. Create a virtual environment: `python3 -m venv venv`
2. Source virtual environment: `source venv/bin/activate`
3. Install the Automox Console SDK: `pip install automox-console-sdk`
4. Navigate to the script directory: `cd examples/use-cases/push_events_to_syslog`
5. Run the first script: `python syslog.py`
6. In a separate terminal run the other script: `python pull_events.py`

This will execute the scripts and prompt for inputs. Validation will be performed to ensure there
are alerts for improper input(s) if encountered.

Both the Automox API Key and Organization ID inputs can be defined as environment variables prior to running the `pull_events.py` script
to avoid continual prompting. This can be accomplished by exporting the AUTOMOX_API_KEY and AUTOMOX_ORGANIZATION_ID environment
variables:
```shell
AUTOMOX_API_KEY=<API KEY HERE> AUTOMOX_ORGANIZATION_ID=<ORG ID HERE> python pull_events.py
```

## Script Output
When running the script, output will be sent to standard out in the case of an input issue, errors, or informational
messages. This output could be redirected to a file for storing on disk as needed. Every 10 seconds `pull_events.py` will look for new events to report, indicated by the following:
```
Getting recent events...
Found 1 new event(s)
```

If an a new event is pulled from the API, it will be sent to the listening syslog daemon. The corresponding output will look similar to this.
```
Dec 09 2021 00:29:35: system.policy.action ({"text": "foo", "status": "0"})
```

The event name and data payload will differ based on the type of event triggered; for more information about the different types of events view the [Automox Official API Documentation](https://developer.automox.com/openapi/axconsole/operation/getEvents/)
