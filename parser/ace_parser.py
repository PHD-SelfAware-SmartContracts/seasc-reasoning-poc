"""
==========================================================
ACE Parser

Parses the controlled-English insurance contract and
constructs the canonical SemanticContract object.

SEASC RQ2 Proof-of-Concept
==========================================================
"""

from pathlib import Path

from model.semantic_model import (
    SemanticContract,
    Participant,
    Rule,
    ContractState,
    OracleObservation,
)


class ACEParser:
    """
    Parser for the controlled-English insurance contract.
    """

    def __init__(self):

        self.contract = SemanticContract()

    def parse(self, filename):

        # Create a fresh contract every time
        self.contract = SemanticContract()

        lines = Path(filename).read_text().splitlines()

        mode = None

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.upper() == "PARTICIPANTS":
                mode = "participants"
                continue

            if line.upper() == "RULES":
                mode = "rules"
                continue

            if mode == "participants":

                self.contract.participants.append(

                    Participant(
                        identifier=line,
                        role=line
                    )
                )

            elif mode == "rules":

                self._parse_rule(line)

        self.contract.state = ContractState(
            state="Submitted"
        )

        return self.contract

    # -----------------------------------------------------
    # Parse Individual Rule
    # -----------------------------------------------------

    def _parse_rule(self, text):

        text = text.rstrip(".")

        # -------------------------------------------------
        # Conditional Rule
        # -------------------------------------------------

        if text.startswith("If"):

            body = text[3:]

            condition, action = body.split(" then ")

            condition = condition.strip()
            action = action.strip()

            self.contract.rules.append(

                Rule(
                    identifier=f"R{len(self.contract.rules)+1}",
                    condition=condition,
                    action=action,
                )
            )

            # Oracle observations used by reasoning engine

            if condition == "evidenceVerified":

                self.contract.oracle_observations.append(

                    OracleObservation(
                        source="MedicalOracle",
                        evidence="evidenceVerified",
                        confidence=0.95,
                    )
                )

            elif condition == "fraudDetected":

                self.contract.oracle_observations.append(

                    OracleObservation(
                        source="FraudEngine",
                        evidence="fraudDetected",
                        confidence=0.99,
                    )
                )

            elif condition == "evidenceConflict":

                self.contract.oracle_observations.append(

                    OracleObservation(
                        source="MedicalOracle",
                        evidence="evidenceConflict",
                        confidence=0.90,
                    )
                )

            elif condition == "oracleTimeout":

                self.contract.oracle_observations.append(

                    OracleObservation(
                        source="MedicalOracle",
                        evidence="oracleTimeout",
                        confidence=0.00,
                    )
                )

        # -------------------------------------------------
        # Obligation Rule
        # -------------------------------------------------

        elif "must" in text:

            actor, action = text.split(" must ")

            self.contract.rules.append(

                Rule(
                    identifier=f"R{len(self.contract.rules)+1}",
                    condition=actor.strip(),
                    action=action.strip(),
                )
            )

        # -------------------------------------------------
        # Simple Rule
        # -------------------------------------------------

        else:

            self.contract.rules.append(

                Rule(
                    identifier=f"R{len(self.contract.rules)+1}",
                    condition="",
                    action=text.strip(),
                )
            )
