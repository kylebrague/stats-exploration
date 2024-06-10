from pprint import pprint
from statistics import mean
from src.types.FantasyRecord import FantasyRecord

fantasy_records: dict[str, FantasyRecord] = {
    "Kyle": FantasyRecord("Kyle", 10, 0),
    "Jason": FantasyRecord("Jason", 7, 3),
    "Jonah": FantasyRecord("Jonah", 6, 4),
    "Trevor": FantasyRecord("Trevor", 3, 7),
    "Maurice": FantasyRecord("Maurice", 4, 6),
    "Varun": FantasyRecord("Varun", 0, 10),
}


# TODO - Add leagueMatchup data and predict future games off of that.
def main():
    # Example usage
    games_left = 10
    for record in fantasy_records.values():
        results = record.simulate_future_games(num_games=games_left)
        pprint((record.name, results))

    # Simulate future games for Kyle
    results = [
        fantasy_records["Kyle"].simulate_future_games(num_games=games_left)
        for _ in range(10000)
    ]
    print(fantasy_records["Kyle"].compute_confidence_interval())
    average_wins = mean(float(result_triplet[0]) for result_triplet in results)
    average_losses = mean(float(result_triplet[1]) for result_triplet in results)
    print("Average wins:", average_wins)
    print("Average losses:", average_losses)


if __name__ == "__main__":
    main()
