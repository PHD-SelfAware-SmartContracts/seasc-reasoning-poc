"""
==========================================================
Oracle Simulator

Produces runtime oracle observations for the
SEASC reasoning prototype.

==========================================================
"""

from model.semantic_model import OracleObservation


class OracleSimulator:

    def __init__(self):

        pass

    def verified_claim(self):

        return [

            OracleObservation(
                source="MedicalOracle",
                evidence="evidenceVerified",
                confidence=0.98
            )

        ]

    def fraud_detected(self):

        return [

            OracleObservation(
                source="FraudEngine",
                evidence="fraudDetected",
                confidence=0.99
            )

        ]

    def conflicting_evidence(self):

        return [

            OracleObservation(
                source="MedicalOracle",
                evidence="evidenceConflict",
                confidence=0.92
            )

        ]

    def low_confidence(self):

        return [

            OracleObservation(
                source="MedicalOracle",
                evidence="evidenceVerified",
                confidence=0.45
            )

        ]

    def timeout(self):

        return [

            OracleObservation(
                source="MedicalOracle",
                evidence="oracleTimeout",
                confidence=0.00
            )

        ]
