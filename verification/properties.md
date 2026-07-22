# Verified Properties

| ID | Property | Verification | Paper Mapping |
|----|----------|--------------|---------------|
| INV-1 | TypeInvariant | TLC | Formal Contract Model |
| INV-2 | PaymentAuthorized | TLC | BDI Execution |
| INV-3 | OracleObservationValid | TLC | Oracle Semantics |
| INV-4 | BeliefsWellTyped | TLC | BDI Reasoning |
| INV-5 | DesiresWellTyped | TLC | BDI Reasoning |
| INV-6 | IntentionsWellTyped | TLC | BDI Reasoning |
| LIVE-1 | EventuallyResolved | TLC | Verification & Evaluation |

## Fairness Assumptions

The specification adopts weak fairness for the following actions.

- Submit
- Verify
- OracleAccept
- OracleReject
- Pay

These assumptions guarantee progress whenever an action remains continuously enabled.
