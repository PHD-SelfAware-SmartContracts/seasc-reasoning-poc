--------------------------- MODULE BDIExecution ---------------------------

EXTENDS Sequences

(***************************************************************************)
(* BDI Execution Layer                                                     *)
(* Corresponds to Section IV of the paper                                  *)
(* Defines the cognitive vocabulary of the reasoning agent.                *)
(***************************************************************************)

BeliefUniverse ==
{
    "EvidenceVerified",
    "FraudDetected",
    "OracleValidated"
}

DesireUniverse ==
{
    "ValidSettlement",
    "FraudPrevention",
    "RegulatoryCompliance"
}

IntentionUniverse ==
{
    "AuthorizePayment",
    "InitiateArbitration",
    "RequestAdditionalEvidence"
}

ValidBeliefs(B) ==
    B \subseteq BeliefUniverse

ValidDesires(D) ==
    D \subseteq DesireUniverse

ValidIntentions(I) ==
    I \subseteq IntentionUniverse

CanAuthorize(B) ==
    "EvidenceVerified" \in B
    /\ "OracleValidated" \in B

RequiresArbitration(B) ==
    "FraudDetected" \in B

=============================================================================
