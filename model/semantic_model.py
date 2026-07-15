from dataclasses import dataclass, field
from typing import List, Dict, Optional


# ==========================================================
# Participants
# ==========================================================

@dataclass
class Participant:
    identifier: str
    role: str


# ==========================================================
# Contract Rule
# ==========================================================

@dataclass
class Rule:
    identifier: str
    condition: str
    action: str
    priority: int = 0


# ==========================================================
# Oracle Observation
# ==========================================================

@dataclass
class OracleObservation:
    source: str
    evidence: str
    confidence: float


# ==========================================================
# BDI Components
# ==========================================================

@dataclass
class Belief:
    proposition: str
    truth: bool


@dataclass
class Goal:
    name: str
    priority: int


@dataclass
class Intention:
    action: str
    active: bool = False


# ==========================================================
# Explanation Object
# ==========================================================

@dataclass
class Explanation:

    beliefs: List[str]

    goals: List[str]

    intentions: List[str]

    decision: str


# ==========================================================
# Runtime Contract State
# ==========================================================

@dataclass
class ContractState:

    state: str

    verified: bool = False

    fraud: bool = False

    arbitration: bool = False

    payout: bool = False


# ==========================================================
# Complete Semantic Contract
# ==========================================================

@dataclass
class SemanticContract:

    participants: List[Participant] = field(default_factory=list)

    rules: List[Rule] = field(default_factory=list)

    beliefs: List[Belief] = field(default_factory=list)

    goals: List[Goal] = field(default_factory=list)

    intentions: List[Intention] = field(default_factory=list)

    oracle_observations: List[OracleObservation] = field(default_factory=list)

    explanations: List[Explanation] = field(default_factory=list)

    state: Optional[ContractState] = None

    metadata: Dict = field(default_factory=dict)
