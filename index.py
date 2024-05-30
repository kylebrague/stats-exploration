import numpy as np
from pprint import pprint
from src.types.FantasyRecord import FantasyRecord


def simulate_future_games(
    lower_bound: float,
    upper_bound: float,
    num_games=100,
):
    mu = (lower_bound + upper_bound) / 2
    alpha = 10
    beta = alpha * (1 - mu) / mu
    beta_samples = np.random.beta(alpha, beta, num_games)
    # Simulate future games # 1 for win, 0 for loss
    results = np.random.uniform(0, 1, num_games) < beta_samples
    simulated_wins = sum(results)
    simulated_losses = num_games - simulated_wins
    win_prob = simulated_wins / num_games
    return simulated_wins, simulated_losses, win_prob


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
        # lower_bound, upper_bound = compute_by_record(record)
        results = simulate_future_games(
            *record.compute_confidence_interval(), num_games=12
        )
        pprint((record.name, results))

    bounds = fantasy_records["Kyle"].compute_confidence_interval()
    results = [simulate_future_games(*bounds, num_games=12) for _ in range(10000)]
    average_wins = sum(results[0] for results in results) / len(results)
    average_losses = sum(results[1] for results in results) / len(results)
    print("Average wins:", average_wins)
    print("Average losses:", average_losses)


if __name__ == "__main__":
    main()
