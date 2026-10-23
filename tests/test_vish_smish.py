"""
=============================================================================
PEER'S VISH & SMISH SIMULATOR — AUTOMATED UNIT TEST SUITE
Sqrock IT Solution | Alpha 2 Cybersecurity Internship (Day 04)
Author: Md Peer Siddiqui
=============================================================================
"""

import os
import sys
import unittest

# Add parent directory to path so vish_smish can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vish_smish import (
    load_scenarios,
    get_scenario_by_id,
    calculate_trigger_composite_score,
    calculate_sms_segments,
    run_benchmark_audit
)


class TestVishSmishSimulator(unittest.TestCase):
    """Automated unit test suite verifying scenario data, trigger math, and parser integrity."""

    @classmethod
    def setUpClass(cls):
        cls.scenarios = load_scenarios()

    def test_database_loads_all_10_categories(self):
        """Verify that all 10 social engineering industry categories exist."""
        self.assertGreaterEqual(len(self.scenarios), 10)
        expected_ids = {
            "it_support", "banking_fraud", "gov_tax", "parcel_delivery",
            "hr_payroll", "healthcare_copay", "executive_ceo", "telecom_carrier",
            "ecommerce_retail", "utility_services"
        }
        loaded_ids = {sc.get("id") for sc in self.scenarios}
        self.assertTrue(expected_ids.issubset(loaded_ids), f"Missing scenario IDs: {expected_ids - loaded_ids}")

    def test_scenario_required_keys_present(self):
        """Verify each scenario possesses all required structural fields."""
        required_keys = [
            "id", "category", "title", "caller_persona", "spoofed_caller_id",
            "target_persona", "vishing_script", "smishing_lure",
            "psychological_triggers", "technical_indicators", "defensive_countermeasures"
        ]
        for sc in self.scenarios:
            for k in required_keys:
                self.assertIn(k, sc, f"Scenario '{sc.get('id')}' missing required key: '{k}'")

    def test_vishing_dialogue_all_5_phases_present(self):
        """Ensure all 5 phases of attack progression exist in every vishing script."""
        phases = ["phase_1_intro", "phase_2_hook", "phase_3_the_ask", "phase_4_objections", "phase_5_exit"]
        for sc in self.scenarios:
            v_script = sc.get("vishing_script", {})
            for p in phases:
                self.assertIn(p, v_script, f"Scenario '{sc.get('id')}' missing dialogue phase: '{p}'")
                if p == "phase_4_objections":
                    self.assertIsInstance(v_script[p], dict)
                    self.assertGreaterEqual(len(v_script[p]), 2, f"Scenario '{sc.get('id')}' must have >= 2 objections")
                else:
                    self.assertIsInstance(v_script[p], str)
                    self.assertGreater(len(v_script[p]), 10)

    def test_smishing_payload_integrity(self):
        """Ensure every smishing lure contains sender ID, body, and valid deceptive link."""
        for sc in self.scenarios:
            lure = sc.get("smishing_lure", {})
            self.assertIn("sender_id", lure)
            self.assertIn("message_body", lure)
            self.assertIn("deceptive_url", lure)
            self.assertTrue(lure["deceptive_url"].startswith("http"), f"Invalid URL in {sc.get('id')}")

    def test_sms_character_segmentation_calculation(self):
        """Validate GSM-7 160-character single SMS and concatenated multi-segment logic."""
        short_msg = "Your parcel delivery failed. Track here: https://ex.com"
        chars, segs, single = calculate_sms_segments(short_msg)
        self.assertLessEqual(chars, 160)
        self.assertEqual(segs, 1)
        self.assertTrue(single)

        long_msg = "A" * 200
        chars, segs, single = calculate_sms_segments(long_msg)
        self.assertEqual(chars, 200)
        self.assertEqual(segs, 2)
        self.assertFalse(single)

    def test_trigger_scoring_boundaries(self):
        """Ensure composite psychological intensity scores remain bounded between 0 and 100."""
        for sc in self.scenarios:
            triggers = sc.get("psychological_triggers", {})
            score, tier = calculate_trigger_composite_score(triggers)
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 100)
            self.assertIn(tier, [
                "Critical Manipulation",
                "High Psychological Pressure",
                "Moderate Psychological Coercion",
                "Low / Subtle Elicitation"
            ])

    def test_get_scenario_by_id_valid_and_invalid(self):
        """Validate case-insensitive retrieval and handling of missing IDs."""
        sc = get_scenario_by_id(self.scenarios, "IT_SUPPORT")
        self.assertIsNotNone(sc)
        self.assertEqual(sc.get("id"), "it_support")

        sc_fake = get_scenario_by_id(self.scenarios, "non_existent_category")
        self.assertIsNone(sc_fake)

    def test_defensive_countermeasures_count(self):
        """Ensure every scenario provides at least 2 actionable enterprise defensive controls."""
        for sc in self.scenarios:
            defenses = sc.get("defensive_countermeasures", [])
            self.assertGreaterEqual(len(defenses), 2, f"Scenario '{sc.get('id')}' lacks sufficient defensive controls")

    def test_benchmark_audit_runner(self):
        """Verify the benchmark audit executes without error across all 10 scenarios."""
        results = run_benchmark_audit(self.scenarios, export_reports=False)
        self.assertEqual(len(results), len(self.scenarios))
        for res in results:
            self.assertIn("intensity_score", res)
            self.assertIn("risk_tier", res)
            self.assertIn("sms_characters", res)


if __name__ == "__main__":
    unittest.main()
