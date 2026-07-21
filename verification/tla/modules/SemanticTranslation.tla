------------------------- MODULE SemanticTranslation -------------------------

EXTENDS Sequences

(***************************************************************************)
(* Semantic Translation Layer                                               *)
(* Section III                                                              *)
(* Defines the semantic vocabulary used throughout the specification.       *)
(***************************************************************************)

States ==
{
    "Submitted",
    "Verified",
    "FraudCheck",
    "Approved",
    "Disputed",
    "Paid"
}

Events ==
{
    "submit",
    "verify",
    "flagFraud",
    "approve",
    "dispute",
    "pay"
}

SemanticEquivalent(s1, s2) ==
    s1 = s2

=============================================================================
