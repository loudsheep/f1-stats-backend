import json
import os
from definitions import ROOT_DIR
import fastf1
import pycountry

fastf1.Cache.enable_cache(os.path.join(ROOT_DIR, 'f1cache'))


def add_country_code(pd_row):
    if pd_row['Country'] == 'UAE' or pd_row['Country'] == 'Abu Dhabi':
        return 'AE'
    elif pd_row['Country'] == 'UK':
        return 'GB'
    else:
        return pycountry.countries.search_fuzzy(pd_row['Country'])[0].alpha_2


def get_events_remaining():
    events = fastf1.get_events_remaining()

    events['CountryCode'] = events.apply(lambda x: add_country_code(x), axis=1)
    events = events[
        ['RoundNumber', 'Country', 'Location', 'OfficialEventName', 'EventDate', 'EventName', 'EventFormat',
         'CountryCode']].to_json(
        orient="records", date_format="iso")

    return json.loads(events)


def get_event_schedule(year: int):
    events = fastf1.get_event_schedule(year)

    if len(events) == 0:
        return "[]"

    events['CountryCode'] = events.apply(lambda x: add_country_code(x), axis=1)
    events = events[
        ['RoundNumber', 'Country', 'Location', 'OfficialEventName', 'EventDate', 'EventName', 'EventFormat',
         'CountryCode']].to_json(
        orient="records", date_format="iso")

    return json.loads(events)
