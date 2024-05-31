from pprint import pprint
from src.types.FantasyRecord import FantasyRecord


def main():
    # Example usage
    fantasy_records: dict[str, FantasyRecord] = {
        "Kyle": FantasyRecord("Kyle", 8, 0),
        "Jason": FantasyRecord("Jason", 5, 3),
        "Jonah": FantasyRecord("Jonah", 4, 4),
        "Trevor": FantasyRecord("Trevor", 3, 5),
        "Maurice": FantasyRecord("Maurice", 2, 6),
        "Varun": FantasyRecord("Varun", 0, 8),
    }

    for record in fantasy_records.values():
        results = record.simulate_future_games(num_games=12)
        pprint((record.name, results))

    # Simulate future games for Kyle
    results = [
        fantasy_records["Kyle"].simulate_future_games(num_games=12)
        for _ in range(10000)
    ]
    average_wins = sum(results[0] for results in results) / len(results)
    average_losses = sum(results[1] for results in results) / len(results)
    print("Average wins:", average_wins)
    print("Average losses:", average_losses)


if __name__ == "__main__":
    main()
