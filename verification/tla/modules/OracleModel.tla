--------------------------- MODULE OracleModel ---------------------------

EXTENDS Naturals, Sequences, FiniteSets

(***************************************************************************)
(* Oracle Observation Layer                                                *)
(* Corresponds to Section V-A                                              *)
(***************************************************************************)

CONSTANTS
    valid,
    invalid,
    uncertain

Observations ==
{
    valid,
    invalid,
    uncertain
}

VARIABLES
    OracleObservation

InitOracle ==
    OracleObservation = uncertain

ReceiveValid ==
    /\ OracleObservation # valid
    /\ OracleObservation' = valid

ReceiveInvalid ==
    /\ OracleObservation # invalid
    /\ OracleObservation' = invalid

ReceiveUncertain ==
    /\ OracleObservation # uncertain
    /\ OracleObservation' = uncertain

NextOracle ==
      ReceiveValid
   \/ ReceiveInvalid
   \/ ReceiveUncertain

=============================================================================
