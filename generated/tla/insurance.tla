------------------------------ MODULE insurance ------------------------------

EXTENDS Naturals, TLC

(***************************************************************************)
(* Contract States                                                         *)
(***************************************************************************)

CONSTANTS

    Submitted,
    Verified,
    Approved,
    Suspended,
    Arbitration,
    Settled,

    valid,
    invalid,
    uncertain

VARIABLES

    contractState,
    oracleState,
    verifiedEvidence,
    fraudFlag,
    payoutExecuted,
    claimBalance

vars ==
<<
contractState,
oracleState,
verifiedEvidence,
fraudFlag,
payoutExecuted,
claimBalance
>>

(***************************************************************************)
(* Initial State                                                           *)
(***************************************************************************)

Init ==

/\ contractState = Submitted

/\ oracleState = uncertain

/\ verifiedEvidence = FALSE

/\ fraudFlag = FALSE

/\ payoutExecuted = FALSE

/\ claimBalance = 1000

(***************************************************************************)
(* Actions                                                                 *)
(***************************************************************************)

Submit ==

/\ contractState = Submitted

/\ contractState' = Verified

/\ UNCHANGED
<<
oracleState,
verifiedEvidence,
fraudFlag,
payoutExecuted,
claimBalance
>>

Verify ==

/\ contractState = Verified

/\ oracleState = valid

/\ verifiedEvidence' = TRUE

/\ contractState' = Approved

/\ UNCHANGED
<<
fraudFlag,
payoutExecuted,
claimBalance,
oracleState
>>

Fraud ==

/\ contractState \in {Verified,Approved}

 /\ oracleState = invalid

/\ fraudFlag' = TRUE

/\ contractState' = Arbitration

/\ UNCHANGED
<<
verifiedEvidence,
payoutExecuted,
claimBalance,
oracleState
>>

Conflict ==

/\ oracleState = uncertain

/\ contractState \in {Verified,Approved}

 /\ contractState' = Suspended

/\ UNCHANGED
<<
verifiedEvidence,
fraudFlag,
payoutExecuted,
claimBalance,
oracleState
>>

Payout ==

/\ contractState = Approved

/\ verifiedEvidence

/\ ~fraudFlag

/\ payoutExecuted' = TRUE

/\ claimBalance' = claimBalance - 100

/\ contractState' = Settled

/\ UNCHANGED
<<
oracleState,
verifiedEvidence,
fraudFlag
>>

Next ==

Submit

\/ Verify

\/ Fraud

\/ Conflict

\/ Payout

(***************************************************************************)
(* Safety                                                                  *)
(***************************************************************************)

Inv1 ==

payoutExecuted => verifiedEvidence

Inv2 ==

fraudFlag => ~payoutExecuted

Inv3 ==

claimBalance >= 0

(***************************************************************************)
(* Specification                                                           *)
(***************************************************************************)

Spec ==

Init /\ [][Next]_vars

=============================================================================
