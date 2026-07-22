--------------------------- MODULE InsuranceContract ---------------------------

EXTENDS Naturals, FiniteSets

VARIABLES
    contractState,
    beliefs,
    desires,
    intentions,
    oracleObservation

vars ==
    <<
        contractState,
        beliefs,
        desires,
        intentions,
        oracleObservation
    >>


(* Initial State *)


Init ==
    /\ contractState = "Submitted"
    /\ beliefs = {}
    /\ desires = {"ValidSettlement"}
    /\ intentions = {}
    /\ oracleObservation = "uncertain"

(* Contract actions *)

Submit ==
    /\ contractState = "Submitted"
    /\ contractState' = "Verified"
    /\ UNCHANGED
       <<beliefs,
         desires,
         intentions,
         oracleObservation>>

Verify ==
    /\ contractState = "Verified"
    /\ contractState' = "FraudCheck"
    /\ beliefs' = beliefs \cup {"EvidenceVerified"}
    /\ desires' = desires
    /\ intentions' = intentions
    /\ oracleObservation' = "uncertain"

OracleAccept ==
    /\ contractState = "FraudCheck"
    /\ oracleObservation = "uncertain"
    /\ contractState' = "Approved"
    /\ beliefs' = beliefs \cup {"OracleValidated"}
    /\ desires' = desires
    /\ intentions' = intentions \cup {"AuthorizePayment"}
    /\ oracleObservation' = "valid"

OracleReject ==
    /\ contractState = "FraudCheck"
    /\ oracleObservation = "uncertain"
    /\ contractState' = "Disputed"
    /\ beliefs' = beliefs \cup {"FraudDetected"}
    /\ desires' = desires
    /\ intentions' = intentions \cup {"InitiateArbitration"}
    /\ oracleObservation' = "invalid"

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
    /\ UNCHANGED vars

Next ==
      Submit
   \/ Verify
   \/ OracleAccept
   \/ OracleReject
   \/ Pay
   \/ Stutter

Spec ==
    Init
    /\ [][Next]_vars
    /\ WF_vars(Submit)
    /\ WF_vars(Verify)
    /\ WF_vars(OracleAccept)
    /\ WF_vars(OracleReject)
    /\ WF_vars(Pay)


(* Verification Properties *)

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

(* Liveness properties *)

EventuallyResolved ==
    <>(
        contractState = "Paid"
        \/
        contractState = "Disputed"
    )



=============================================================================
