"""
Cerebrovascular Hypocapnic Hyperventilation Vasomotor Reactivity Engine.
Provides deterministic, zero-dependency modeling of Transcranial Doppler (TCD) MCA velocity,
end-tidal CO2 drop, hypocapnic vasoconstrictive reactivity index (% / mmHg), and respiratory alkalosis buffering.
"""

from typing import Dict, Any, List, Optional


class CerebralHyperventilationReactivityClient:
    """
    Deterministic client for calculating Cerebrovascular Hypocapnic Vasomotor Reactivity (CVR_hypo).
    Assesses cerebral precapillary arteriolar smooth muscle contraction against acute respiratory alkalosis,
    panic/anxiety hyperventilation cerebral hypoperfusion, and cerebrovascular buffering reserve.
    """

    def __init__(self):
        pass

    def evaluate_hypocapnic_reactivity(
        self,
        baseline_etco2_mmhg: float,
        hyperventilation_etco2_mmhg: float,
        baseline_mca_velocity_cm_s: float,
        hyperventilation_mca_velocity_cm_s: float,
        mean_arterial_pressure_mmhg: float = 92.0
    ) -> Dict[str, Any]:
        """
        Calculates hypocapnic reactivity index: CVR_hypo = (% delta FV) / delta EtCO2 (% / mmHg).
        Normative values (during active hyperventilation challenge):
        - Baseline EtCO2: 36.0 - 44.0 mmHg
        - Delta EtCO2: 10.0 - 20.0 mmHg drop
        - Baseline MCA Flow Velocity: 50.0 - 75.0 cm/s
        - Hypocapnic Reactivity (CVR_hypo): 1.8 - 3.5 % / mmHg
        - Excessive reactivity (> 4.2 % / mmHg) risks acute cerebral ischemia/dizziness during panic attacks
        - Blunted reactivity (< 1.2 % / mmHg) indicates microvascular stiffness or autonomic failure
        """
        if baseline_etco2_mmhg <= hyperventilation_etco2_mmhg or hyperventilation_etco2_mmhg <= 0:
            return {"error": "Baseline EtCO2 must strictly exceed hyperventilation EtCO2"}
        if baseline_mca_velocity_cm_s <= hyperventilation_mca_velocity_cm_s or hyperventilation_mca_velocity_cm_s <= 0:
            return {"error": "Baseline MCA velocity must exceed hyperventilation velocity"}

        # 1. Delta EtCO2 (mmHg)
        delta_etco2_mmhg = round(baseline_etco2_mmhg - hyperventilation_etco2_mmhg, 1)

        # 2. Percentage Flow Velocity Drop (%)
        delta_fv_cm_s = round(baseline_mca_velocity_cm_s - hyperventilation_mca_velocity_cm_s, 1)
        pct_fv_drop = round((delta_fv_cm_s / baseline_mca_velocity_cm_s) * 100.0, 1)

        # 3. Hypocapnic Reactivity Index (% / mmHg)
        cvr_hypo_pct_per_mmhg = round(pct_fv_drop / delta_etco2_mmhg, 2)

        # 4. Cerebrovascular Hypocapnic Buffer Score (0 - 100)
        score = 80.0
        if 1.8 <= cvr_hypo_pct_per_mmhg <= 3.4:
            score += 15.0
        elif 1.4 <= cvr_hypo_pct_per_mmhg < 1.8 or 3.4 < cvr_hypo_pct_per_mmhg <= 4.0:
            score += 5.0
        elif cvr_hypo_pct_per_mmhg > 4.6:
            score -= 28.0  # Hyper-reactive vasospasm risk
        elif cvr_hypo_pct_per_mmhg < 1.0:
            score -= 32.0  # Loss of vasomotor reactivity

        if delta_etco2_mmhg >= 8.0:
            score += 5.0
        elif delta_etco2_mmhg < 5.0:
            score -= 10.0  # Insufficient hyperventilation challenge

        hypo_score = round(min(100.0, max(5.0, score)), 1)

        if hypo_score >= 85.0 and 1.8 <= cvr_hypo_pct_per_mmhg <= 3.5:
            tier = "OPTIMAL_HYPOCAPNIC_VASOMOTOR_REACTIVITY"
            interp = f"Balanced arteriolar hypocapnic vasoconstriction (CVR {cvr_hypo_pct_per_mmhg} %/mmHg, FV drop {pct_fv_drop}% for {delta_etco2_mmhg} mmHg EtCO2 drop); physiological precapillary tone modulation."
            guidance = "Superior cerebrovascular alkalosis buffering. Cerebral perfusion adjusts smoothly to respiratory fluctuations."
        elif cvr_hypo_pct_per_mmhg > 4.2:
            tier = "EXCESSIVE_HYPERVENTILATION_VASOCONSTRICTION"
            interp = f"Exaggerated cerebral vasoconstriction (CVR {cvr_hypo_pct_per_mmhg} %/mmHg > 4.0 %/mmHg); steep drop in blood flow velocity predisposing to panic lightheadedness or presyncope."
            guidance = "Hyper-reactive cerebral vasoconstrictor tone. Practice slow nasal diaphragmatic breathing to stabilize alveolar CO2 during stress."
        elif cvr_hypo_pct_per_mmhg < 1.3:
            tier = "BLUNTED_CEREBROVASCULAR_CO2_REACTIVITY"
            interp = f"Severely blunted vasoconstrictive reactivity (CVR {cvr_hypo_pct_per_mmhg} %/mmHg < 1.4 %/mmHg); reflects microvascular endothelial dysfunction, structural arteriolar stiffening, or dysautonomia."
            guidance = "Rigid microvascular bed. Avoid rapid hyperventilation; screen for small-vessel cerebrovascular disease."
        else:
            tier = "MODERATE_HYPOCAPNIC_VASOMOTOR_RESPONSE"
            interp = f"Moderate hypocapnic reactivity (CVR {cvr_hypo_pct_per_mmhg} %/mmHg, Drop {pct_fv_drop}%); acceptable vascular buffering."
            guidance = "Adequate cerebrovascular tone. Maintain aerobic exercise to support microvascular endothelial plasticity."

        return {
            "baseline_etco2_mmhg": baseline_etco2_mmhg,
            "hyperventilation_etco2_mmhg": hyperventilation_etco2_mmhg,
            "delta_etco2_mmhg": delta_etco2_mmhg,
            "baseline_mca_velocity_cm_s": baseline_mca_velocity_cm_s,
            "hyperventilation_mca_velocity_cm_s": hyperventilation_mca_velocity_cm_s,
            "pct_fv_drop": pct_fv_drop,
            "cvr_hypocapnic_pct_per_mmhg": cvr_hypo_pct_per_mmhg,
            "mean_arterial_pressure_mmhg": mean_arterial_pressure_mmhg,
            "hypocapnic_buffer_score": hypo_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
