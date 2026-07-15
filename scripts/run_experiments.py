"""
==========================================================
Run Experiments

SEASC RQ2 Proof-of-Concept

Executes multiple oracle scenarios and records
evaluation metrics for the paper.

==========================================================
"""

import sys
import csv
import time
from pathlib import Path

# ---------------------------------------------------------
# Make repository root importable
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------

from parser.ace_parser import ACEParser
from reasoning.oracle_simulator import OracleSimulator
from reasoning.reasoning_engine import ReasoningEngine
from reasoning.explanation_engine import ExplanationEngine

# ---------------------------------------------------------
# Output Directory
# ---------------------------------------------------------

RESULT_DIR = ROOT / "evaluation"

RESULT_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# Execute One Scenario
# ---------------------------------------------------------


def run_scenario(name, observations):

    parser = ACEParser()

    contract = parser.parse(
        "input/insurance_contract.ace"
    )

    # Replace observations produced by parser
    contract.oracle_observations = observations

    engine = ReasoningEngine()

    start = time.perf_counter()

    contract = engine.reason(contract)

    runtime = (time.perf_counter() - start) * 1000

    explainer = ExplanationEngine()

    contract = explainer.generate(contract)

    if contract.state is not None:
        decision = contract.state.state
    else:
        decision = "Unknown"

    result = {

        "Scenario":
            name,

        "Beliefs":
            len(contract.beliefs),

        "Goals":
            len(contract.goals),

        "Intentions":
            len(contract.intentions),

        "Decision":
            decision,

        "Runtime(ms)":
            round(runtime, 3),

        "ReasoningDepth":
            contract.metadata.get(
                "reasoning_depth",
                0
            ),

        "ActivatedRules":
            ",".join(
                contract.metadata.get(
                    "activated_rules",
                    []
                )
            ),

        "ExplanationComplete":

            "Yes"

            if len(contract.explanations) > 0

            else

            "No"

    }

    return result


# ---------------------------------------------------------
# Main Experiment
# ---------------------------------------------------------


def main():

    oracle = OracleSimulator()

    scenarios = [

        (
            "Verified Claim",
            oracle.verified_claim()
        ),

        (
            "Fraud Detected",
            oracle.fraud_detected()
        ),

        (
            "Evidence Conflict",
            oracle.conflicting_evidence()
        ),

        (
            "Low Confidence",
            oracle.low_confidence()
        ),

        (
            "Oracle Timeout",
            oracle.timeout()
        )

    ]

    results = []

    print()
    print("=" * 72)
    print("SEASC RQ2 EXPERIMENTS")
    print("=" * 72)

    for name, obs in scenarios:

        result = run_scenario(
            name,
            obs
        )

        results.append(result)

        print()

        print(f"Scenario           : {result['Scenario']}")
        print(f"Decision           : {result['Decision']}")
        print(f"Beliefs            : {result['Beliefs']}")
        print(f"Goals              : {result['Goals']}")
        print(f"Intentions         : {result['Intentions']}")
        print(f"Reasoning Depth    : {result['ReasoningDepth']}")
        print(f"Activated Rules    : {result['ActivatedRules']}")
        print(f"Explanation        : {result['ExplanationComplete']}")
        print(f"Runtime            : {result['Runtime(ms)']} ms")

    csv_file = RESULT_DIR / "results.csv"

    with open(csv_file, "w", newline="") as file:

        writer = csv.DictWriter(

            file,

            fieldnames=[

                "Scenario",

                "Beliefs",

                "Goals",

                "Intentions",

                "Decision",

                "Runtime(ms)",

                "ReasoningDepth",

                "ActivatedRules",

                "ExplanationComplete"

            ]

        )

        writer.writeheader()

        writer.writerows(results)

    print()
    print("=" * 72)
    print(f"Results written to {csv_file}")
    print("=" * 72)


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    main()
