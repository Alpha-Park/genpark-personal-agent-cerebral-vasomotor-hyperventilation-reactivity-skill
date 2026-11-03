# Cerebrovascular Hypocapnic Hyperventilation Reactivity Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Transcranial Doppler (TCD) Hypocapnic Vasomotor Reactivity (CVR_hypo in %/mmHg), flow velocity drop, and respiratory alkalosis buffering.

```mermaid
flowchart TD
    Hyperventilation["Active Voluntary Hyperventilation (Tachypnea)"] --> DropsEtCO2["End-Tidal CO2 Depletion (Respiratory Alkalosis)"]
    DropsEtCO2 --> Vasoconstriction["Cerebral Precapillary Arteriolar Smooth Muscle Constriction"]
    Vasoconstriction --> TCD_Drop["Transcranial Doppler MCA Mean Flow Velocity Drop"]
    TCD_Drop --> ReactivityCalc["Hypocapnic Reactivity Index (% Delta FV / Delta EtCO2 in %/mmHg)"]
    ReactivityCalc --> HypoScore["Cerebrovascular Hypocapnic Buffering & Presyncope Score"]
    HypoScore --> Agent["OpenClaw / Hermes Personal Agent Box-Breathing Guidance"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Neurovascular Standards**: Implements validated equations for TCD MCA velocity, end-tidal CO2 shift, and hypocapnic vasoconstriction index.
- **Panic Attack & Hyperventilation Lightheadedness Shield**: Early detection of hyper-reactive cerebral vasospasm predisposing to dizziness.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CerebralHyperventilationReactivityClient

client = CerebralHyperventilationReactivityClient()
result = client.evaluate_hypocapnic_reactivity(
    baseline_etco2_mmhg=40.5,
    hyperventilation_etco2_mmhg=26.0,
    baseline_mca_velocity_cm_s=64.0,
    hyperventilation_mca_velocity_cm_s=41.5
)
print("CVR Hypo Index:", result["cvr_hypocapnic_pct_per_mmhg"], "%/mmHg")
print("Buffer Score:", result["hypocapnic_buffer_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
