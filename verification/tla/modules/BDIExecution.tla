--------------------------- MODULE BDIExecution ---------------------------

EXTENDS Naturals, Sequences, FiniteSets

(***************************************************************************)
(* BDI Execution Layer                                                     *)
(* Corresponds to Section IV                                               *)
(***************************************************************************)

CONSTANTS
    EvidenceVerified,
    FraudDetected,
    ValidSettlement,
    AuthorizePayment,
    InitiateArbitration

BeliefUniverse ==
{
    EvidenceVerified,
    FraudDetected
}

DesireUniverse ==
{
    ValidSettlement
}

IntentionUniverse ==
{
    AuthorizePayment,
    InitiateArbitration
}

VARIABLES
    Beliefs,
    Desires,
    Intentions

InitBDI ==
    /\ Beliefs = {}
    /\ Desires = {}
    /\ Intentions = {}

AddVerifiedEvidence ==
    /\ EvidenceVerified \notin Beliefs
    /\ Beliefs' = Beliefs \cup {EvidenceVerified}
    /\ UNCHANGED <<Desires, Intentions>>

CreateSettlementGoal ==
    /\ EvidenceVerified \in Beliefs
    /\ ValidSettlement \notin Desires
    /\ Desires' = Desires \cup {ValidSettlement}
    /\ UNCHANGED <<Beliefs, Intentions>>

Authorize ==
    /\ ValidSettlement \in Desires
    /\ AuthorizePayment \notin Intentions
    /\ Intentions' = Intentions \cup {AuthorizePayment}
    /\ UNCHANGED <<Beliefs, Desires>>

RaiseFraud ==
    /\ FraudDetected \notin Beliefs
    /\ Beliefs' = Beliefs \cup {FraudDetected}
    /\ Intentions' = {InitiateArbitration}
    /\ UNCHANGED Desires

NextBDI ==
      AddVerifiedEvidence
   \/ CreateSettlementGoal
   \/ Authorize
   \/ RaiseFraud

=============================================================================
