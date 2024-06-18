from uuid import UUID
from typing import List, Optional, Any, Dict
from enum import Enum


class DraftDetail:
    complete_date: int
    drafted: bool
    in_progress: bool

    def __init__(self, complete_date: int, drafted: bool, in_progress: bool) -> None:
        self.complete_date = complete_date
        self.drafted = drafted
        self.in_progress = in_progress


class NotificationSetting:
    enabled: bool
    id: UUID
    type: str

    def __init__(self, enabled: bool, id: UUID, type: str) -> None:
        self.enabled = enabled
        self.id = id
        self.type = type


class Member:
    display_name: str
    first_name: str
    id: str
    is_league_creator: bool
    is_league_manager: bool
    last_name: str
    teams: List[int]
    notification_settings: List[NotificationSetting]

    def __init__(
        self,
        display_name: str,
        first_name: str,
        id: str,
        is_league_creator: bool,
        is_league_manager: bool,
        last_name: str,
        notification_settings: List[NotificationSetting],
    ) -> None:
        self.display_name = display_name
        self.first_name = first_name
        self.id = id
        self.is_league_creator = is_league_creator
        self.is_league_manager = is_league_manager
        self.last_name = last_name
        self.notification_settings = notification_settings


class PitcherLimitStat:
    exceeded_on_scoring_period: int
    limit_exceeded: bool
    stat_id: int
    value: int

    def __init__(
        self,
        exceeded_on_scoring_period: int,
        limit_exceeded: bool,
        stat_id: int,
        value: int,
    ) -> None:
        self.exceeded_on_scoring_period = exceeded_on_scoring_period
        self.limit_exceeded = limit_exceeded
        self.stat_id = stat_id
        self.value = value


class StatBySlot:
    the_22: PitcherLimitStat

    def __init__(self, the_22: PitcherLimitStat) -> None:
        self.the_22 = the_22


class CumulativeScore:
    losses: int
    stat_by_slot: Optional[StatBySlot]
    ties: int
    wins: int

    def __init__(
        self, losses: int, stat_by_slot: Optional[StatBySlot], ties: int, wins: int
    ) -> None:
        self.losses = losses
        self.stat_by_slot = stat_by_slot
        self.ties = ties
        self.wins = wins


class Player:
    stats: List[Any]

    def __init__(self, stats: List[Any]) -> None:
        self.stats = stats


class PlayerPoolEntry:
    player: Player

    def __init__(self, player: Player) -> None:
        self.player = player


class Entry:
    lineup_slot_id: int
    player_pool_entry: PlayerPoolEntry

    def __init__(self, lineup_slot_id: int, player_pool_entry: PlayerPoolEntry) -> None:
        self.lineup_slot_id = lineup_slot_id
        self.player_pool_entry = player_pool_entry


class RosterForCurrentScoringPeriod:
    applied_stat_total: int
    entries: List[Entry]

    def __init__(self, applied_stat_total: int, entries: List[Entry]) -> None:
        self.applied_stat_total = applied_stat_total
        self.entries = entries


class RosterForMatchupPeriodDelayed:
    entries: List[Any]

    def __init__(self, entries: List[Any]) -> None:
        self.entries = entries


class Participant:
    adjustment: int
    cumulativeScore: Optional[CumulativeScore]
    points_by_scoring_period: Optional[Dict[str, int]]
    teamId: int
    tiebreak: int
    totalPoints: int
    roster_for_current_scoring_period: Optional[RosterForCurrentScoringPeriod]
    roster_for_matchup_period_delayed: Optional[RosterForMatchupPeriodDelayed]
    totalPointsLive: Optional[int]

    def __init__(
        self,
        adjustment: int,
        cumulative_score: Optional[CumulativeScore],
        points_by_scoring_period: Optional[Dict[str, int]],
        team_id: int,
        tiebreak: int,
        total_points: int,
        roster_for_current_scoring_period: Optional[RosterForCurrentScoringPeriod],
        roster_for_matchup_period_delayed: Optional[RosterForMatchupPeriodDelayed],
        total_points_live: Optional[int],
    ) -> None:
        self.adjustment = adjustment
        self.cumulativeScore = cumulative_score
        self.points_by_scoring_period = points_by_scoring_period
        self.teamId = team_id
        self.tiebreak = tiebreak
        self.totalPoints = total_points
        self.roster_for_current_scoring_period = roster_for_current_scoring_period
        self.roster_for_matchup_period_delayed = roster_for_matchup_period_delayed
        self.totalPointsLive = total_points_live


class PlayoffTierType(Enum):
    NONE = "NONE"


class Winner(Enum):
    AWAY = "AWAY"
    HOME = "HOME"
    TIE = "TIE"
    UNDECIDED = "UNDECIDED"


class Ballgame:
    away: Participant
    home: Participant
    id: int
    matchup_period_id: int
    playoff_tier_type: PlayoffTierType
    winner: Winner

    def __init__(
        self,
        away: Optional[Participant],
        home: Participant,
        id: int,
        matchup_period_id: int,
        playoff_tier_type: PlayoffTierType,
        winner: Winner,
    ) -> None:
        self.away = away
        self.home = home
        self.id = id
        self.matchup_period_id = matchup_period_id
        self.playoff_tier_type = playoff_tier_type
        self.winner = winner


class AcquisitionSettings:
    is_using_acquisition_budget: bool

    def __init__(self, is_using_acquisition_budget: bool) -> None:
        self.is_using_acquisition_budget = is_using_acquisition_budget


class DraftSettings:
    keeper_count: int

    def __init__(self, keeper_count: int) -> None:
        self.keeper_count = keeper_count


class RosterSettings:
    is_using_undroppable_list: bool

    def __init__(self, is_using_undroppable_list: bool) -> None:
        self.is_using_undroppable_list = is_using_undroppable_list


class ScoringSettings:
    scoring_type: str

    def __init__(self, scoring_type: str) -> None:
        self.scoring_type = scoring_type


class Settings:
    acquisition_settings: AcquisitionSettings
    draft_settings: DraftSettings
    is_customizable: bool
    is_public: bool
    name: str
    roster_settings: RosterSettings
    scoring_settings: ScoringSettings

    def __init__(
        self,
        acquisition_settings: AcquisitionSettings,
        draft_settings: DraftSettings,
        is_customizable: bool,
        is_public: bool,
        name: str,
        roster_settings: RosterSettings,
        scoring_settings: ScoringSettings,
    ) -> None:
        self.acquisition_settings = acquisition_settings
        self.draft_settings = draft_settings
        self.is_customizable = is_customizable
        self.is_public = is_public
        self.name = name
        self.roster_settings = roster_settings
        self.scoring_settings = scoring_settings


class Info:
    client_address: None
    platform: str
    source: str

    def __init__(self, client_address: None, platform: str, source: str) -> None:
        self.client_address = client_address
        self.platform = platform
        self.source = source


class Status:
    activated_date: int
    created_as_league_type: int
    creation_info: Info
    current_league_type: int
    current_matchup_period: int
    final_scoring_period: int
    first_scoring_period: int
    is_active: bool
    is_expired: bool
    is_full: bool
    is_playoff_matchup_edited: bool
    is_to_be_deleted: bool
    is_viewable: bool
    is_waiver_order_edited: bool
    last_update_info: Info
    latest_scoring_period: int
    previous_seasons: List[Any]
    standings_update_date: int
    teams_joined: int
    transaction_scoring_period: int
    waiver_last_execution_date: int
    waiver_process_status: Dict[str, int]

    def __init__(
        self,
        activated_date: int,
        created_as_league_type: int,
        creation_info: Info,
        current_league_type: int,
        current_matchup_period: int,
        final_scoring_period: int,
        first_scoring_period: int,
        is_active: bool,
        is_expired: bool,
        is_full: bool,
        is_playoff_matchup_edited: bool,
        is_to_be_deleted: bool,
        is_viewable: bool,
        is_waiver_order_edited: bool,
        last_update_info: Info,
        latest_scoring_period: int,
        previous_seasons: List[Any],
        standings_update_date: int,
        teams_joined: int,
        transaction_scoring_period: int,
        waiver_last_execution_date: int,
        waiver_process_status: Dict[str, int],
    ) -> None:
        self.activated_date = activated_date
        self.created_as_league_type = created_as_league_type
        self.creation_info = creation_info
        self.current_league_type = current_league_type
        self.current_matchup_period = current_matchup_period
        self.final_scoring_period = final_scoring_period
        self.first_scoring_period = first_scoring_period
        self.is_active = is_active
        self.is_expired = is_expired
        self.is_full = is_full
        self.is_playoff_matchup_edited = is_playoff_matchup_edited
        self.is_to_be_deleted = is_to_be_deleted
        self.is_viewable = is_viewable
        self.is_waiver_order_edited = is_waiver_order_edited
        self.last_update_info = last_update_info
        self.latest_scoring_period = latest_scoring_period
        self.previous_seasons = previous_seasons
        self.standings_update_date = standings_update_date
        self.teams_joined = teams_joined
        self.transaction_scoring_period = transaction_scoring_period
        self.waiver_last_execution_date = waiver_last_execution_date
        self.waiver_process_status = waiver_process_status


class DraftStrategy:
    pass

    def __init__(
        self,
    ) -> None:
        pass


class LogoType(Enum):
    CUSTOM_VALID = "CUSTOM_VALID"
    VECTOR = "VECTOR"


class StreakType(Enum):
    LOSS = "LOSS"
    WIN = "WIN"


class Away:
    games_back: float
    losses: int
    percentage: float
    points_against: int
    points_for: int
    streak_length: int
    streak_type: StreakType
    ties: int
    wins: int

    def __init__(
        self,
        games_back: float,
        losses: int,
        percentage: float,
        points_against: int,
        points_for: int,
        streak_length: int,
        streak_type: StreakType,
        ties: int,
        wins: int,
    ) -> None:
        self.games_back = games_back
        self.losses = losses
        self.percentage = percentage
        self.points_against = points_against
        self.points_for = points_for
        self.streak_length = streak_length
        self.streak_type = streak_type
        self.ties = ties
        self.wins = wins


class Record:
    away: Away
    division: Away
    home: Away
    overall: Away

    def __init__(self, away: Away, division: Away, home: Away, overall: Away) -> None:
        self.away = away
        self.division = division
        self.home = home
        self.overall = overall


class Players:
    the_32801: str

    def __init__(self, the_32801: str) -> None:
        self.the_32801 = the_32801


class TradeBlock:
    players: Optional[Players]

    def __init__(self, players: Optional[Players]) -> None:
        self.players = players


class TransactionCounter:
    acquisition_budget_spent: int
    acquisitions: int
    drops: int
    matchup_acquisition_totals: Dict[str, int]
    misc: int
    move_to_active: int
    move_to_ir: int
    paid: int
    team_charges: int
    trades: int

    def __init__(
        self,
        acquisition_budget_spent: int,
        acquisitions: int,
        drops: int,
        matchup_acquisition_totals: Dict[str, int],
        misc: int,
        move_to_active: int,
        move_to_ir: int,
        paid: int,
        team_charges: int,
        trades: int,
    ) -> None:
        self.acquisition_budget_spent = acquisition_budget_spent
        self.acquisitions = acquisitions
        self.drops = drops
        self.matchup_acquisition_totals = matchup_acquisition_totals
        self.misc = misc
        self.move_to_active = move_to_active
        self.move_to_ir = move_to_ir
        self.paid = paid
        self.team_charges = team_charges
        self.trades = trades


class Team:
    abbrev: str
    current_projected_rank: int
    division_id: int
    draft_day_projected_rank: int
    draft_strategy: Optional[DraftStrategy]
    id: int
    is_active: bool
    logo: str
    logo_type: LogoType
    name: str
    owners: List[str]
    playoff_seed: int
    points: int
    points_adjusted: int
    points_delta: int
    primary_owner: str
    rank_calculated_final: int
    rank_final: int
    record: Record
    trade_block: Optional[TradeBlock]
    transaction_counter: TransactionCounter
    values_by_stat: Dict[str, int]
    waiver_rank: int
    watch_list: Optional[List[int]]

    def __init__(
        self,
        abbrev: str,
        current_projected_rank: int,
        division_id: int,
        draft_day_projected_rank: int,
        draft_strategy: Optional[DraftStrategy],
        id: int,
        is_active: bool,
        logo: str,
        logo_type: LogoType,
        name: str,
        owners: List[str],
        playoff_seed: int,
        points: int,
        points_adjusted: int,
        points_delta: int,
        primary_owner: str,
        rank_calculated_final: int,
        rank_final: int,
        record: Record,
        trade_block: Optional[TradeBlock],
        transaction_counter: TransactionCounter,
        values_by_stat: Dict[str, int],
        waiver_rank: int,
        watch_list: Optional[List[int]],
    ) -> None:
        self.abbrev = abbrev
        self.current_projected_rank = current_projected_rank
        self.division_id = division_id
        self.draft_day_projected_rank = draft_day_projected_rank
        self.draft_strategy = draft_strategy
        self.id = id
        self.is_active = is_active
        self.logo = logo
        self.logo_type = logo_type
        self.name = name
        self.owners = owners
        self.playoff_seed = playoff_seed
        self.points = points
        self.points_adjusted = points_adjusted
        self.points_delta = points_delta
        self.primary_owner = primary_owner
        self.rank_calculated_final = rank_calculated_final
        self.rank_final = rank_final
        self.record = record
        self.trade_block = trade_block
        self.transaction_counter = transaction_counter
        self.values_by_stat = values_by_stat
        self.waiver_rank = waiver_rank
        self.watch_list = watch_list


class FantasyLeagueData:
    draft_detail: DraftDetail
    game_id: int
    id: int
    members: List[Member]
    schedule: List[Ballgame]
    scoring_period_id: int
    season_id: int
    segment_id: int
    settings: Settings
    status: Status
    teams: List[Team]

    def __init__(
        self,
        draft_detail: DraftDetail,
        game_id: int,
        id: int,
        members: List[Member],
        schedule: List[Ballgame],
        scoring_period_id: int,
        season_id: int,
        segment_id: int,
        settings: Settings,
        status: Status,
        teams: List[Team],
    ) -> None:
        self.draft_detail = draft_detail
        self.game_id = game_id
        self.id = id
        self.members = members
        self.schedule = schedule
        self.scoring_period_id = scoring_period_id
        self.season_id = season_id
        self.segment_id = segment_id
        self.settings = settings
        self.status = status
        self.teams = teams
