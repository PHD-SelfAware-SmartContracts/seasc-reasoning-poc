"""
==========================================================
Explanation Engine

Transforms BDI reasoning into
human-readable explanations.
==========================================================
"""

from model.semantic_model import (
    SemanticContract,
    Explanation,
)


class ExplanationEngine:

    def __init__(self):
        pass

    def generate(self, contract: SemanticContract):

        contract.explanations.clear()

        beliefs = [
            b.proposition
            for b in contract.beliefs
            if b.truth
        ]

        goals = [
            g.name
            for g in contract.goals
        ]

        intentions = [
            i.action
            for i in contract.intentions
        ]

        if contract.state is None:
            decision = "No decision."
        else:
            decision = contract.state.state

        explanation = Explanation(

            beliefs=beliefs,

            goals=goals,

            intentions=intentions,

            decision=decision

        )

        contract.explanations.append(explanation)

        return contract

    def pretty_print(self, contract: SemanticContract):

        print()

        print("=" * 60)
        print("EXPLANATION")
        print("=" * 60)

        for exp in contract.explanations:

            print()

            print("Beliefs:")

            for b in exp.beliefs:
                print("   •", b)

            print()

            print("Goals:")

            for g in exp.goals:
                print("   •", g)

            print()

            print("Intentions:")

            for i in exp.intentions:
                print("   •", i)

            print()

            print("Decision:")

            print("   ", exp.decision)

            print()
