--------------------------- MODULE InsuranceContract ---------------------------

EXTENDS Naturals, FiniteSets

VARIABLES
    contractState,
    beliefs,
    desires,
    intentions,
    oracleObservation


(* Initial State *)


Init ==
    /\ contractState = "Submitted"
    /\ beliefs = {}
    /\ desires = {"ValidSettlement"}
    /\ intentions = {}
    /\ oracleObservation = "uncertain"

(* Contract Actions *)

Submit ==
    /\ contractState = "Submitted"
    /\ contractState' = "Verified"

    /\ beliefs' = beliefs
    /\ desires' = desires
    /\ intentions' = intentions
    /\ oracleObservation' = oracleObservation

Verify ==
    /\ contractState = "Verified"

    /\ contractState' = "FraudCheck"

    /\ beliefs' = beliefs \cup {"EvidenceVerified"}

    /\ desires' = desires

    /\ intentions' = intentions

    /\ oracleObservation' = "valid"

Approve ==
    /\ contractState = "FraudCheck"

    /\ oracleObservation = "valid"

    /\ contractState' = "Approved"

    /\ beliefs' = beliefs

    /\ desires' = desires

    /\ intentions'
       = intentions \cup {"AuthorizePayment"}

    /\ oracleObservation' = oracleObservation

Dispute ==
    /\ contractState = "FraudCheck"

    /\ oracleObservation = "invalid"

    /\ contractState' = "Disputed"

    /\ beliefs'
       = beliefs \cup {"FraudDetected"}

    /\ desires' = desires

    /\ intentions'
       = intentions \cup {"InitiateArbitration"}

    /\ oracleObservation' = oracleObservation

Pay ==
    /\ contractState = "Approved"

    /\ "AuthorizePayment" \in intentions

    /\ contractState' = "Paid"

    /\ UNCHANGED
       <<beliefs,
         desires,
         intentions,
         oracleObservation>>

Stutter ==
    /\ contractState \in {"Paid","Disputed"}

    /\ UNCHANGED
       <<contractState,
         beliefs,
         desires,
         intentions,
         oracleObservation>>

Next ==
      Submit
   \/ Verify
   \/ Approve
   \/ Dispute
   \/ Pay
   \/ Stutter

Spec ==
    Init /\ [][Next]_<<contractState,
                      beliefs,
                      desires,
                      intentions,
                      oracleObservation>>

(***************************************************************************)
(* Verification Properties                                                 *)
(***************************************************************************)

TypeInvariant ==

    /\ contractState \in
        {
            "Submitted",
            "Verified",
            "FraudCheck",
            "Approved",
            "Disputed",
            "Paid"
        }

    /\ beliefs \subseteq
        {
            "EvidenceVerified",
            "FraudDetected",
            "OracleValidated"
        }

    /\ desires \subseteq
        {
            "ValidSettlement",
            "FraudPrevention",
            "RegulatoryCompliance"
        }

    /\ intentions \subseteq
        {
            "AuthorizePayment",
            "InitiateArbitration",
            "RequestAdditionalEvidence"
        }

    /\ oracleObservation \in
        {
            "valid",
            "invalid",
            "uncertain"
        }


(* Safety Properties *)

PaymentAuthorized ==
    contractState = "Paid"
        => "AuthorizePayment" \in intentions

OracleObservationValid ==
    oracleObservation \in
        {
            "valid",
            "invalid",
            "uncertain"
        }

BeliefsWellTyped ==
    beliefs \subseteq
        {
            "EvidenceVerified",
            "FraudDetected",
            "OracleValidated"
        }

DesiresWellTyped ==
    desires \subseteq
        {
            "ValidSettlement",
            "FraudPrevention",
            "RegulatoryCompliance"
        }

IntentionsWellTyped ==
    intentions \subseteq
        {
            "AuthorizePayment",
            "InitiateArbitration",
            "RequestAdditionalEvidence"
        }

=============================================================================
