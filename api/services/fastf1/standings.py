import json

import fastf1
from fastf1.ergast import Ergast


def get_drivers_standings(season: int):
    ergast = Ergast()
    standings = ergast.get_driver_standings(season)

    if len(standings.content) == 0:
        return []

    result = standings.content[0].to_json(orient="records", date_format="iso")

    return json.loads(result)


def get_constructors_standings(season: int):
    ergast = Ergast()
    standings = ergast.get_constructor_standings(season)

    if len(standings.content) == 0:
        return []

    result = standings.content[0].to_json(orient="records", date_format="iso")

    return json.loads(result)
