# SEASC Reasoning PoC

**Proof-of-Concept Implementation for Research Question 2**

**Human-Manageable, Explainable Smart Contract Reasoning**

---

## Overview

This repository contains the proof-of-concept implementation accompanying the paper on **human-manageable decentralized smart contracts**. The prototype operationalizes the proposed semantic reasoning pipeline by transforming controlled-English contractual specifications into executable semantic models, explainable BDI reasoning, LegalRuleML representations, and reproducible evaluation artifacts.

Unlike conventional smart-contract implementations, this prototype emphasizes **semantic transparency**, **explainable reasoning**, and **reproducible experimentation**.

---

## Research Objective

The prototype addresses **Research Question 2**:

> **What reasoning structures let a smart contract behave interpretably and justify its decisions during execution?**

The implementation demonstrates how BDI reasoning can provide transparent execution decisions while preserving contractual semantics.

---

## Prototype Architecture

```
ACE Contract
      │
      ▼
Semantic Parser
      │
      ▼
Semantic Contract Model
      │
      ▼
Oracle Simulator
      │
      ▼
BDI Reasoning Engine
      │
      ▼
Explanation Engine
      │
      ▼
LegalRuleML Generator
      │
      ▼
Evaluation Artifacts
```

---

## Repository Structure

```
input/
model/
parser/
reasoning/
translator/
generated/
evaluation/
scripts/
```

---

## Mapping to the Paper

| Repository Component | Paper Contribution |
|----------------------|-------------------|
| ACE Parser | Semantic Translation |
| Semantic Model | Contract Representation |
| Oracle Simulator | Oracle-aware Reasoning |
| BDI Reasoning Engine | Explainable Execution |
| Explanation Engine | Human-manageability |
| LegalRuleML Generator | Semantic Preservation |
| Experiment Runner | Evaluation |
| Generated Reports | Reproducibility |

---

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Running the Prototype

```bash
python3 main.py
```

---

## Running the Experiments

```bash
python3 -m scripts.run_experiments
```

---

## Generating Paper Artifacts

```bash
python3 evaluation/generate_latex_table.py

python3 scripts/report_generator.py
```

---

## Generated Artifacts

The prototype automatically generates:

```
generated/legalruleml/
    insurance.xml

generated/reports/
    contract_summary.txt
    reasoning_report.txt
    experiment_summary.txt

evaluation/
    results.csv
    results_table.tex
```

---

## Reproducibility

All reported experimental artifacts are generated directly from the implementation without manual modification.

The repository therefore provides reproducible evidence supporting the evaluation presented in the accompanying paper.

---

## Citation

If you use this repository, please cite the accompanying conference paper.

---

## License

MIT License.
