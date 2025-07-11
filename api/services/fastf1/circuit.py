from fastf1.ergast import Ergast


def get_circut_info(circut_id: str, season: int, round: int):
    ergast = Ergast()

    total_race_results = ergast.get_race_results(circuit=circut_id, results_position=1).total_results

    if total_race_results == 0:
        return {}

    last_wins = [i.to_dict(orient="records")[0] for i in
                 ergast.get_race_results(circuit=circut_id, results_position=1, limit=5,
                                         offset=max(0, total_race_results - 5)).content]

    circuit = ergast.get_circuits(season, round).to_dict(orient="records")[0]

    return {
        "lastWins": last_wins,
        "info": circuit
    }
