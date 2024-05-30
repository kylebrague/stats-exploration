from dataclasses import dataclass, field
from statsmodels.stats.proportion import proportion_confint


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

    def __aprx__(self, value: object) -> bool:
        return (
            self.name == value.name
            and self.wins == value.wins
            and self.losses == value.losses
        )
