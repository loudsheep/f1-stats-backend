import json
from fastf1.ergast import Ergast
import fastf1
import numpy


def get_race_results(season: int, round: int):
    ergast = Ergast()

    results = ergast.get_race_results(season, round)

    if results.total_results == 0:
        return []

    content = results.content[0].replace({numpy.nan: None})

    return content.to_dict(orient="records")


def get_session_results(season: int, round: int, session_name: str):
    session = fastf1.get_session(season, round, session_name)
    session.load(laps=False, telemetry=False, weather=False, messages=False)

    results = session.results

    content = results.replace({numpy.nan: None})

    return content.to_dict(orient="records")
