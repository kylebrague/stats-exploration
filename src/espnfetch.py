import json
import os
from types import SimpleNamespace
import requests
from datetime import datetime

from src.types.espn.LeagueMatchUp import FantasyLeagueData


def fetch_league_data():
    # this might only work if you called this endpoint through the espn website first
    reqUrl = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/flb/seasons/2024/segments/0/leagues/1764665483?view=mMatchupScore&view=mStatus&view=mSettings&view=mTeam&view=modular&view=mNav"
    headersList = {"Accept": "*/*"}
    payload = ""
    return requests.request("GET", reqUrl, data=payload, headers=headersList)


def save_league_data(
    path: str = "./data/espndotcom/league",
    filename: str = f"leagueMatchup{datetime.now().strftime('%Y%m%d')}.json",
):
    response_json = fetch_league_data().json()

    with open(os.path.join(path, filename), "w") as file:
        file.write(json.dumps(response_json, indent=4))


def load_league_data(
    path: str = "./data/espndotcom/league",
    filename: str = f"leagueMatchup{datetime.now().strftime('%Y%m%d')}.json",
) -> FantasyLeagueData:

    if not os.path.exists(os.path.join(path, filename)):
        # get latest file in folder
        files = os.listdir(path)
        files.sort()
        filename = files[-1]
        print(f"File not found, using latest file: {filename}")

    with open(os.path.join(path, filename), "r") as file:
        return json.load(file, object_hook=lambda d: SimpleNamespace(**d))
