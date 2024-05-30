from math import sqrt

from scipy.special import erfinv
from types.FantasyRecord import FantasyRecord


# The Wilson score interval is an adjustment to the normal approximation interval.
# It is used to calculate the confidence interval of a proportion.
# Below is an algorithm to calculate the Wilson score interval for the sake of understanding.
def wilson_score_interval(wins, total_games, confidence=0.95):
    if total_games == 0:
        return (0, 0)  # No games played, no interval to calculate.

    # Calculate the proportion of wins
    p = wins / total_games

    # The z-score for a 95% confidence level is approximately 1.96.
    # For other confidence levels, you can adjust it based on the normal distribution.
    z = 1.96 if confidence == 0.95 else sqrt(2) * erfinv(confidence)
    # Calculate the interval
    denominator = 1 + z**2 / total_games
    center_adjusted_probability = p + z**2 / (2 * total_games)
    adjusted_standard_deviation = sqrt(
        (p * (1 - p) + z**2 / (4 * total_games)) / total_games
    )

    # Lower and upper bounds
    lower_bound = (
        center_adjusted_probability - z * adjusted_standard_deviation
    ) / denominator
    upper_bound = (
        center_adjusted_probability + z * adjusted_standard_deviation
    ) / denominator

    return (lower_bound, upper_bound)


def main():
    # Example usage:
    fantasy_records: list[FantasyRecord] = [
        FantasyRecord("Team A", 8, 0),
        FantasyRecord("Team B", 7, 1),
        FantasyRecord("Team C", 6, 2),
        FantasyRecord("Team D", 5, 3),
        FantasyRecord("Team E", 4, 4),
        FantasyRecord("Team F", 3, 5),
        FantasyRecord("Team G", 2, 6),
        FantasyRecord("Team H", 1, 7),
        FantasyRecord("Team I", 0, 8),
    ]

    print(
        "95% Confidence Interval:",
        [record.compute_confidence_interval() for record in fantasy_records],
    )
