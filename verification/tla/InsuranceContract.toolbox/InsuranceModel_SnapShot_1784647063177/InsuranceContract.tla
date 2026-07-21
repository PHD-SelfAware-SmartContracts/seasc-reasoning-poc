--------------------------- MODULE InsuranceContract ---------------------------

EXTENDS Naturals

VARIABLE
    contractState

States ==
{
    "Submitted",
    "Verified",
    "FraudCheck",
    "Approved",
    "Disputed",
    "Paid"
}

Init ==
    contractState = "Submitted"

Submit ==
    /\ contractState = "Submitted"
    /\ contractState' = "Verified"

Verify ==
    /\ contractState = "Verified"
    /\ contractState' = "FraudCheck"

Approve ==
    /\ contractState = "FraudCheck"
    /\ contractState' = "Approved"

Dispute ==
    /\ contractState = "FraudCheck"
    /\ contractState' = "Disputed"

Pay ==
    /\ contractState = "Approved"
    /\ contractState' = "Paid"

Next ==
      Submit
   \/ Verify
   \/ Approve
   \/ Dispute
   \/ Pay

Spec ==
    Init /\ [][Next]_<<contractState>>

TypeInvariant ==
    contractState \in States

=============================================================================
