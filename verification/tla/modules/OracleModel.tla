-------------------------- MODULE OracleModel --------------------------

EXTENDS Sequences

(***************************************************************************)
(* Oracle Observation Layer                                                *)
(* Corresponds to Section V-A of the paper                                 *)
(* Defines oracle observations and helper predicates.                      *)
(***************************************************************************)

Observations ==
{
    "valid",
    "invalid",
    "uncertain"
}

OracleAccepts(obs) ==
    obs = "valid"

OracleRejects(obs) ==
    obs = "invalid"

OracleUncertain(obs) ==
    obs = "uncertain"

ValidObservation(obs) ==
    obs \in Observations

=============================================================================
