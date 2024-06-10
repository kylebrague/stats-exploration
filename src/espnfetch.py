import requests


def fetch_league_data():
    reqUrl = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/flb/seasons/2024/segments/0/leagues/1764665483?view=mMatchupScore&view=mStatus&view=mSettings&view=mTeam&view=modular&view=mNav"

    headersList = {"Accept": "*/*"}

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)

    return response
