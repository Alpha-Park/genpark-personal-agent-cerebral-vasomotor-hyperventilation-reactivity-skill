"""
Example Usage: Cerebrovascular Hypocapnic Hyperventilation Vasomotor Reactivity.
Demonstrates zero-dependency calculation of TCD MCA velocity drop, CVR_hypo reactivity index, and respiratory alkalosis buffering.
"""

from client import CerebralHyperventilationReactivityClient


def main():
    client = CerebralHyperventilationReactivityClient()
    print("=== Cerebrovascular Hypocapnic Reactivity Demo ===")

    # Test Case 1: Healthy normal hypocapnic vasomotor constriction
    res1 = client.evaluate_hypocapnic_reactivity(
        baseline_etco2_mmhg=40.5,
        hyperventilation_etco2_mmhg=26.0,
        baseline_mca_velocity_cm_s=64.0,
        hyperventilation_mca_velocity_cm_s=41.5,
        mean_arterial_pressure_mmhg=94.0
    )
    print("\nTest Case 1: Normal Hypocapnic Vasomotor Reactivity")
    print(f"  EtCO2 Shift: {res1['baseline_etco2_mmhg']} -> {res1['hyperventilation_etco2_mmhg']} mmHg (Delta: {res1['delta_etco2_mmhg']} mmHg)")
    print(f"  MCA Flow Velocity: {res1['baseline_mca_velocity_cm_s']} -> {res1['hyperventilation_mca_velocity_cm_s']} cm/s (Drop: {res1['pct_fv_drop']}%)")
    print(f"  CVR Hypocapnic Index: {res1['cvr_hypocapnic_pct_per_mmhg']} %/mmHg")
    print(f"  Hypocapnic Buffer Score: {res1['hypocapnic_buffer_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Hyper-reactive vasoconstriction (panic attack lightheadedness pattern)
    res2 = client.evaluate_hypocapnic_reactivity(
        baseline_etco2_mmhg=39.0,
        hyperventilation_etco2_mmhg=27.5,
        baseline_mca_velocity_cm_s=60.0,
        hyperventilation_mca_velocity_cm_s=27.0,
        mean_arterial_pressure_mmhg=96.0
    )
    print("\nTest Case 2: Excessive Hypocapnic Vasospasm Pattern")
    print(f"  CVR Index: {res2['cvr_hypocapnic_pct_per_mmhg']} %/mmHg (Drop: {res2['pct_fv_drop']}%)")
    print(f"  Hypocapnic Buffer Score: {res2['hypocapnic_buffer_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
