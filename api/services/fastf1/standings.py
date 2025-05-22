import json

import fastf1
from fastf1.ergast import Ergast
from api.seriallizers import ConstructorStandingSerializer, DriverStandingSerializer
from rest_framework.renderers import JSONRenderer

# Why the hell doesn't this work 0_0?
def get_drivers_standings(season: int):
    ergast = Ergast()
    standings = ergast.get_driver_standings(season)

    if len(standings.content) == 0:
        return []


    result = standings.content[0].to_dict(orient="records")
    serializer = DriverStandingSerializer(data=result, many=True)

    if serializer.is_valid():
        return serializer.data
    return {"error": serializer.errors}

def get_constructors_standings(season: int):
    ergast = Ergast()
    standings = ergast.get_constructor_standings(season)

    if len(standings.content) == 0:
        return []

    # result = standings.content[0].to_json(orient="records", date_format="iso")
    result = standings.content[0].to_dict(orient="records")
    serializer = ConstructorStandingSerializer(data=result, many=True)
    if serializer.is_valid():
        return serializer.data

    return []


# if __name__ == "__main__":
#     get_drivers_standings(2019)
#     print(get_constructors_standings(2019))