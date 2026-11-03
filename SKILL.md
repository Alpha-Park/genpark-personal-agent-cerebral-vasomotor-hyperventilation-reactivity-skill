---
name: genpark-personal-agent-cerebral-vasomotor-hyperventilation-reactivity-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Transcranial Doppler (TCD) Hypocapnic Vasomotor Reactivity (CVR_hypo in %/mmHg), velocity drop, and respiratory alkalosis buffering.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cerebrovascular Hypocapnic Hyperventilation Reactivity Skill

A sovereign personal agent capability for evaluating cerebral precapillary arteriolar vasoconstrictive response to hypocapnia, respiratory alkalosis buffering, Transcranial Doppler (TCD) flow velocity drop, and panic attack / hyperventilation presyncope risk.

## Core Capabilities
- **Hypocapnic Vasomotor Reactivity Index (CVR_hypo)**: Formulates sensitivity ($\frac{\Delta FV / FV_{base}}{\Delta EtCO_2} \times 100\%$ in $\%/\text{mmHg}$, normative: $1.8 - 3.5\%/\text{mmHg}$).
- **Acute Cerebral Ischemia Risk Detection**: Detects exaggerated vasoconstrictor sensitivity ($> 4.0\%/\text{mmHg}$) triggering severe cerebral hypoperfusion during rapid breathing.
- **Arteriolar Endothelial Stiffening Screening**: Identifies blunted vasoconstriction ($< 1.3\%/\text{mmHg}$) reflecting microvascular sclerosis or autonomic exhaustion.
- **Stress Hyperventilation Shielding**: Dynamically coaches slow, deep abdominal breathing (4-7-8 rhythm or box breathing) during cognitive anxiety to preserve arterial $PCO_2$.

## Fast Invocation
```python
from client import CerebralHyperventilationReactivityClient

client = CerebralHyperventilationReactivityClient()
res = client.evaluate_hypocapnic_reactivity(
    baseline_etco2_mmhg=40.5,
    hyperventilation_etco2_mmhg=26.0,
    baseline_mca_velocity_cm_s=64.0,
    hyperventilation_mca_velocity_cm_s=41.5
)
print("CVR Hypo Index:", res["cvr_hypocapnic_pct_per_mmhg"], "%/mmHg")
print("Buffer Score:", res["hypocapnic_buffer_score"], "/ 100")
```
