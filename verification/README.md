# Formal Verification Artifact

## Overview

This directory contains the formal verification artifact accompanying the paper on the SeASC reasoning framework. The artifact models decentralized contract execution using TLA+ and verifies both safety and liveness properties with the TLC model checker.

## Repository Structure

```
verification/
├── README.md
├── properties.md
├── tla/
│   ├── InsuranceContract.tla
│   ├── InsuranceContract.cfg
│   └── modules/
├── tlc/
└── traces/
```

## Verification Workflow

```
Contract Specification
        │
        ▼
Semantic Translation
        │
        ▼
BDI Reasoning
        │
        ▼
Oracle Decision
        │
        ▼
TLA+ Specification
        │
        ▼
TLC Verification
```

## Components

| Component | Description |
|-----------|-------------|
| InsuranceContract.tla | Executable contract specification |
| SemanticTranslation.tla | Semantic abstraction layer |
| BDIExecution.tla | Belief–Desire–Intention reasoning |
| OracleModel.tla | Oracle decision abstraction |

## Verification

The following aspects are formally verified.

- State consistency
- Oracle correctness
- BDI state consistency
- Payment authorization
- Weak fairness
- Eventual contract resolution

## Running the Verification

1. Open `InsuranceContract.tla` in the TLA+ Toolbox.
2. Open model `InsuranceModel_v2`.
3. Execute TLC.
4. Confirm that all invariants and temporal properties hold.

## Execution Traces

Example traces illustrating representative execution scenarios are available in the `traces/` directory.
