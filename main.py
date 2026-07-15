"""
==========================================================
SEASC RQ2 Proof-of-Concept

Main Demonstration Program

Pipeline

ACE
   ↓
Semantic Model
   ↓
Oracle Reasoning
   ↓
BDI Reasoning
   ↓
Explanation
   ↓
LegalRuleML

==========================================================
"""

from parser.ace_parser import ACEParser
from reasoning.reasoning_engine import ReasoningEngine
from reasoning.explanation_engine import ExplanationEngine
from translator.legalruleml_generator import LegalRuleMLGenerator


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def print_banner():

    print("=" * 60)
    print("SEASC RQ2 Proof-of-Concept")
    print("=" * 60)


def print_contract_summary(contract):

    print("\nContract Summary")
    print("-" * 30)

    print(f"Participants : {len(contract.participants)}")
    print(f"Rules        : {len(contract.rules)}")
    print(f"Observations : {len(contract.oracle_observations)}")


def print_reasoning_summary(contract):

    print("\nReasoning Summary")
    print("-" * 30)

    print(f"Beliefs      : {len(contract.beliefs)}")
    print(f"Goals        : {len(contract.goals)}")
    print(f"Intentions   : {len(contract.intentions)}")

    if contract.state is not None:
        print(f"Decision     : {contract.state.state}")


# ---------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------

def main():

    print_banner()

    print("\nLoading ACE contract...")

    parser = ACEParser()

    contract = parser.parse(
        "input/insurance_contract.ace"
    )

    print_contract_summary(contract)

    print("\n✓ Contract parsed")

    print("\nExecuting BDI reasoning...")

    engine = ReasoningEngine()

    contract = engine.reason(contract)

    print("✓ Reasoning completed")

    print_reasoning_summary(contract)

    print("\nGenerating explanations...")

    explainer = ExplanationEngine()

    contract = explainer.generate(contract)

    print()

    print("=" * 60)
    print("EXPLANATION")
    print("=" * 60)

    if len(contract.explanations) > 0:

        explanation = contract.explanations[0]

        print()

        print("Beliefs:")

        for belief in explanation.beliefs:
            print(f"   • {belief}")

        print()

        print("Goals:")

        for goal in explanation.goals:
            print(f"   • {goal}")

        print()

        print("Intentions:")

        for intention in explanation.intentions:
            print(f"   • {intention}")

        print()

        print("Decision:")

        print(f"   {explanation.decision}")

    else:

        print("\nNo explanation generated.")

    print("\nGenerating LegalRuleML...")

    generator = LegalRuleMLGenerator()

    print("\nGenerating LegalRuleML...")

    generator = LegalRuleMLGenerator()

    generator.generate(contract)

    print("✓ LegalRuleML generated")

    print("✓ LegalRuleML generated")

    print()

    print("=" * 60)
    print("Pipeline completed successfully.")
    print("=" * 60)


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    main()
