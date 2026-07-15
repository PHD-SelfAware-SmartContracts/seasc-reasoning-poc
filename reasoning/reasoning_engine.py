"""
==========================================================
Reasoning Engine

SEASC RQ2 Proof-of-Concept

Implements a complete BDI reasoning cycle.

Belief Revision
      ↓
Goal Selection
      ↓
Intention Formation
      ↓
Intention Resolution
      ↓
Execution

==========================================================
"""

from model.semantic_model import (
    SemanticContract,
    Belief,
    Goal,
    Intention,
)


class ReasoningEngine:

    def __init__(self):

        self.reasoning_depth = 0

        self.activated_rules = []

    # -----------------------------------------------------
    # Stage 1 : Belief Revision
    # -----------------------------------------------------

    def update_beliefs(self, contract):

        contract.beliefs.clear()

        self.reasoning_depth += 1

        for obs in contract.oracle_observations:

            # High-confidence observations become beliefs

            if obs.confidence >= 0.80:

                contract.beliefs.append(

                    Belief(
                        proposition=obs.evidence,
                        truth=True
                    )
                )

            else:

                contract.beliefs.append(

                    Belief(
                        proposition=obs.evidence,
                        truth=False
                    )
                )

        return contract

    # -----------------------------------------------------
    # Stage 2 : Goal Selection
    # -----------------------------------------------------

    def select_goals(self, contract):

        contract.goals.clear()

        self.reasoning_depth += 1

        for belief in contract.beliefs:

            if not belief.truth:

                if belief.proposition == "evidenceVerified":

                    contract.goals.append(

                        Goal(
                            name="ManualReview",
                            priority=50
                        )
                    )

                    self.activated_rules.append("LowConfidence")

                continue

            if belief.proposition == "evidenceVerified":

                contract.goals.append(

                    Goal(
                        name="SettleClaim",
                        priority=10
                    )
                )

                self.activated_rules.append("Verified")

            elif belief.proposition == "fraudDetected":

                contract.goals.append(

                    Goal(
                        name="ProtectFunds",
                        priority=100
                    )
                )

                self.activated_rules.append("Fraud")

            elif belief.proposition == "evidenceConflict":

                contract.goals.append(

                    Goal(
                        name="SuspendClaim",
                        priority=80
                    )
                )

                self.activated_rules.append("Conflict")

            elif belief.proposition == "oracleTimeout":

                contract.goals.append(

                    Goal(
                        name="AwaitOracle",
                        priority=60
                    )
                )

                self.activated_rules.append("Timeout")

        return contract

    # -----------------------------------------------------
    # Stage 3 : Intention Formation
    # -----------------------------------------------------

    def form_intentions(self, contract):

        contract.intentions.clear()

        self.reasoning_depth += 1

        # Highest priority first

        ordered = sorted(

            contract.goals,

            key=lambda g: g.priority,

            reverse=True

        )

        for goal in ordered:

            if goal.name == "ProtectFunds":

                contract.intentions.append(

                    Intention(

                        action="initiateArbitration",

                        active=True

                    )

                )

            elif goal.name == "SuspendClaim":

                contract.intentions.append(

                    Intention(

                        action="suspendClaim",

                        active=True

                    )

                )

            elif goal.name == "AwaitOracle":

                contract.intentions.append(

                    Intention(

                        action="wait",

                        active=True

                    )

                )

            elif goal.name == "ManualReview":

                contract.intentions.append(

                    Intention(

                        action="manualReview",

                        active=True

                    )

                )

            elif goal.name == "SettleClaim":

                contract.intentions.append(

                    Intention(

                        action="approvePayout",

                        active=True

                    )

                )

        return contract

    # -----------------------------------------------------
    # Stage 4 : Execute
    # -----------------------------------------------------

    def execute(self, contract):

        self.reasoning_depth += 1

        if contract.state is None:

            return contract

        if len(contract.intentions) == 0:

            return contract

        # Highest-priority intention only

        action = contract.intentions[0].action

        if action == "approvePayout":

            contract.state.state = "Approved"

            contract.state.verified = True

            contract.state.payout = True

        elif action == "initiateArbitration":

            contract.state.state = "Arbitration"

            contract.state.arbitration = True

        elif action == "suspendClaim":

            contract.state.state = "Suspended"

        elif action == "manualReview":

            contract.state.state = "ManualReview"

        elif action == "wait":

            contract.state.state = "Pending"

        # Store evaluation metrics

        contract.metadata["reasoning_depth"] = self.reasoning_depth

        contract.metadata["activated_rules"] = self.activated_rules

        return contract

    # -----------------------------------------------------
    # Complete Reasoning Cycle
    # -----------------------------------------------------

    def reason(self, contract):

        self.reasoning_depth = 0

        self.activated_rules = []

        contract = self.update_beliefs(contract)

        contract = self.select_goals(contract)

        contract = self.form_intentions(contract)

        contract = self.execute(contract)

        return contract
