from pprint import pprint
from statistics import mean
from src.espnfetch import load_league_data
from src.types.FantasyRecord import FantasyRecord

fantasy_records: dict[str, FantasyRecord] = {
    "Kyle": FantasyRecord("Kyle", 11, 0),
    "Jason": FantasyRecord("Jason", 7, 4),
    "Jonah": FantasyRecord("Jonah", 6, 5),
    "Trevor": FantasyRecord("Trevor", 3, 8),
    "Maurice": FantasyRecord("Maurice", 5, 6),
    "Varun": FantasyRecord("Varun", 0, 11),
}


def calculate_win_loss_prob(
    fantasy_record: FantasyRecord, total_games_per_season: int = 20
):
    # Example library usage:
    games_left = total_games_per_season - fantasy_record.wins - fantasy_record.losses
    for record in fantasy_records.values():
        results = record.simulate_future_games(num_games=games_left)
        pprint((record.name, results))

    # Simulate future games for Kyle
    results = [record.simulate_future_games(num_games=games_left) for _ in range(10000)]
    print(record.compute_confidence_interval())
    average_wins = mean(float(result_triplet[0]) for result_triplet in results)
    average_losses = mean(float(result_triplet[1]) for result_triplet in results)
    print("Average wins:", average_wins)
    print("Average losses:", average_losses)


# TODO - Add leagueMatchup data/scores and predict future games off of that.
def main():
    matchups = load_league_data()
    teams = matchups.teams
    teams_with_scores = dict(
        [
            (
                team.name,
                [
                    {
                        "week": None,
                        "home_or_away": None,
                        "home_score": 0,
                        "away_score": 0,
                        "outcome": None,
                    }
                ],
            )
            for team in teams
        ]
    )
    total_schedule = list(
        filter(
            lambda game: hasattr(game, "away") and hasattr(game, "home"),
            matchups.schedule,
        )
    )
    teams_with_scores = dict({team.name: {} for team in teams})

    for team in teams:
        schedule = list(
            filter(
                lambda game: team.id in [game.home.teamId, game.away.teamId],
                total_schedule,
            )
        )
        scores = [
            (
                team.name,
                (
                    game.home.teamId,
                    game.home.totalPoints,
                    "SELF" if game.home.teamId == team.id else "OPPONENT",
                ),
                (
                    game.away.teamId,
                    game.away.totalPoints,
                    "SELF" if game.away.teamId == team.id else "OPPONENT",
                ),
            )
            for game in schedule
        ]

        self_first_scores = []
        for score in scores:
            this_team_scores = [score[1][1] if score[1][2] == "SELF" else score[2][1]]
            opp_scores = [score[1][1] if score[1][2] == "OPPONENT" else score[2][1]]
            self_first_scores.extend(
                (team.name, self_score, opp_score)
                for self_score, opp_score in zip(this_team_scores, opp_scores)
            )
        self_first_scores = list(
            filter(lambda x: x[1] != 0 and x[2] != 0, self_first_scores)
        )
        teams_with_scores[team.name] = [
            (self_score, opp_score) for name, self_score, opp_score in self_first_scores
        ]
    pprint(teams_with_scores)
    for team in teams_with_scores:
        print(team)
        print(
            "Average Points Scored: "
            + str(round(mean([score[0] for score in teams_with_scores[team]]), 2))
        )
        print(
            "Average Points Against: "
            + str(round(mean([score[1] for score in teams_with_scores[team]]), 2))
        )
        print()


if __name__ == "__main__":
    main()
