"""
Checking who can still win the world championship
"""
from typing import Any
import math
import json
from datetime import datetime

import fastf1
from fastf1.ergast import Ergast
from api.seriallizers import DriverCanWinSerializer

def get_gp_by_name(year: int, gpnumber: int)-> str:
    """
    Getting gp name by year and round number
    """
    schedule = fastf1.get_event_schedule(year)
    gp_row = schedule[schedule['RoundNumber'] == gpnumber]
    if not gp_row.empty:
        return gp_row['EventName'].iloc[0]
    raise ValueError(f"No event found for year {year} and GP number {gpnumber}")

def get_driver_standings(season: int, gpnumber: int) -> Any:
    """
    Getting driver standings by season and round number
    """
    ergast = Ergast()
    standings = ergast.get_driver_standings(season=season, round=gpnumber)
    return standings.content[0]

def get_season_events_points(season: int, gpnumber: int, points_race: int = 25, points_sprint: int = 33) -> int:
    """
    Calculate total available points for remaining events in the season.
    Default values for points are set for 2025 season. RIP point for fastest lap.
    """
    # Had to set backend to ergast, because for some f*cking reason it didn't work with default backend
    events = fastf1.get_event_schedule(season, backend="ergast")
    events = events[events['RoundNumber'] > gpnumber]
    sprint_events = len(events.loc[events["EventFormat"] == "sprint_shootout"])
    conventional_events = len(events.loc[events["EventFormat"] == "conventional"])
    sprint_points = points_sprint * sprint_events
    gp_points = points_race * conventional_events
    return sprint_points + gp_points

def calculate_remaining_points(season: int, gpnumber: int) -> int:
    """
    Calculate the remaining points available in the current season
    """
    return get_season_events_points(season, gpnumber, 25,33)

def calculate_who_can_win(driver_standings: Any, max_points: int, season: int, gpnumber: int) -> list[dict[str, str]]:
    """
    Calculates which drivers can still win the championship.
    """
    gp_name = get_gp_by_name(season, gpnumber)
    leader_points = int(driver_standings.loc[0]['points'])
    results = []

    # Max points for each driver
    for i, _ in enumerate(driver_standings.iterrows()):
        driver = driver_standings.loc[i]
        if math.isnan(driver['position']):
            driver['position'] = None
        driver_max_points = int(driver["points"]) + max_points
        can_win = 'Yes' if driver_max_points >= leader_points else 'No'

        driver_info = {
            "position": str(driver["position"]),
            "driver_name": f"{driver['givenName']} {driver['familyName']}",
            "current_points": str(driver["points"]),
            "theoretical_max_points": str(driver_max_points),
            "can_win": can_win,
            "gp_name": str(gp_name),
        }
        results.append(driver_info)

    return results

def who_can_still_win() -> list[dict[str, str]]:
    """
    Calculate championship contenders for the latest event
    """
    year_w = datetime.today().year
    get_last_event = fastf1.get_event_schedule(year_w)
    get_last_event = get_last_event[get_last_event['Session5DateUtc'] < datetime.now()]
    get_latest_event = get_last_event.iloc[-1]
    gp_w = get_latest_event['RoundNumber']
    driver_standings = get_driver_standings(year_w, gp_w)
    remaining_points = calculate_remaining_points(year_w, gp_w)
    result = calculate_who_can_win(driver_standings, remaining_points, year_w, gp_w)

    #Serializer implementation, because of Django
    serializer = DriverCanWinSerializer(result, many=True)
    return serializer.data

if __name__ == "__main__":
    year = 2025
    gp = 1
    print(who_can_still_win())

