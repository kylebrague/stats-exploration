from dataclasses import dataclass, field
from statsmodels.stats.proportion import proportion_confint
from numpy import random


@dataclass(frozen=False)
class FantasyRecord:
    name: str
    wins: int
    losses: int
    lower_bound: float = field(init=False, repr=False)
    upper_bound: float = field(init=False, repr=False)

    def compute_confidence_interval(self, confidence=0.95, method="jeffreys"):
        return proportion_confint(
            count=self.wins,
            nobs=self.wins + self.losses,
            alpha=1 - confidence,
            method=method,
        )

    def simulate_future_games(
        self,
        num_games=100,
        alpha=10,
    ):
        if self.lower_bound is None or self.upper_bound is None:
            self.lower_bound, self.upper_bound = self.compute_confidence_interval()
        mu = (self.lower_bound + self.upper_bound) / 2
        beta = alpha * (1 - mu) / mu
        beta_samples = random.beta(alpha, beta, num_games)
        # Simulate future games # 1 for win, 0 for loss
        results = random.uniform(0, 1, num_games) < beta_samples
        simulated_wins = sum(results)
        simulated_losses = num_games - simulated_wins
        win_prob = simulated_wins / num_games
        return simulated_wins, simulated_losses, win_prob

    def __post_init__(self):
        if self.wins < 0 or self.losses < 0:
            raise ValueError("Wins and losses must be non-negative.")
        if self.wins + self.losses == 0:
            raise ValueError("At least one game must be played.")
        self.lower_bound, self.upper_bound = self.compute_confidence_interval()

    def __str__(self) -> str:
        return f"{self.name}: {self.wins}-{self.losses}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, FantasyRecord):
            return False
        return (
            self.name == value.name
            and self.wins == value.wins
            and self.losses == value.losses
        )

    def __aprxeq__(self, value: object) -> bool:
        return (
            self.name == value.name
            and self.wins == value.wins
            and self.losses == value.losses
        )
