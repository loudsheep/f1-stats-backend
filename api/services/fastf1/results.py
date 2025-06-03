import json
from fastf1.ergast import Ergast
import numpy

def get_race_results(season: int, round: int):
    ergast = Ergast()

    results = ergast.get_race_results(season, round)

    if results.total_results == 0:
        return []
    
    content = results.content[0].replace({numpy.nan: None})

    return content.to_dict(orient="records")