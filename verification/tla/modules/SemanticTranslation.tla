------------------------- MODULE SemanticTranslation -------------------------

EXTENDS Naturals, Sequences, FiniteSets

(***************************************************************************)
(* Semantic Translation Layer                                               *)
(* Corresponds to Section III of the paper                                  *)
(* Defines the contractual state space and translation vocabulary           *)
(***************************************************************************)

CONSTANTS
    Submitted,
    Verified,
    FraudCheck,
    Approved,
    Disputed,
    Paid

States ==
{
    Submitted,
    Verified,
    FraudCheck,
    Approved,
    Disputed,
    Paid
}

CONSTANTS
    submit,
    verify,
    flag,
    approve,
    dispute,
    pay

Events ==
{
    submit,
    verify,
    flag,
    approve,
    dispute,
    pay
}

(***************************************************************************)
(* Translation Layers                                                      *)
(***************************************************************************)

TranslationLayers ==
{
    "ACE",
    "LegalRuleML",
    "SmartContract"
}

(***************************************************************************)
(* Semantic Preservation Relation                                          *)
(***************************************************************************)

SemanticEquivalent(src, dst) ==
    src = dst

(***************************************************************************)
(* Observable Behaviour                                                    *)
(***************************************************************************)

ObservableStates ==
States

=========================================
