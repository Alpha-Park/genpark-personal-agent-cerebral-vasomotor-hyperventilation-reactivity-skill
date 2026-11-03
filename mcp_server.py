"""
MCP Server for Cerebrovascular Hypocapnic Hyperventilation Reactivity Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating TCD hypocapnic reactivity, velocity drop, and buffering scores.
"""

import sys
import json
from typing import Dict, Any
from client import CerebralHyperventilationReactivityClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_hypocapnic_reactivity",
                "description": "Calculates Cerebrovascular Hypocapnic Vasomotor Reactivity (CVR_hypo in %/mmHg), MCA velocity drop %, and alkalosis buffering score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_etco2_mmhg": {
                            "type": "number",
                            "description": "Baseline resting end-tidal CO2 in mmHg (e.g. 40.0 mmHg, normative 36-44 mmHg)."
                        },
                        "hyperventilation_etco2_mmhg": {
                            "type": "number",
                            "description": "End-tidal CO2 reached during voluntary hyperventilation in mmHg (e.g. 25.0 mmHg)."
                        },
                        "baseline_mca_velocity_cm_s": {
                            "type": "number",
                            "description": "Baseline Middle Cerebral Artery (MCA) mean flow velocity in cm/s (e.g. 62.0 cm/s)."
                        },
                        "hyperventilation_mca_velocity_cm_s": {
                            "type": "number",
                            "description": "MCA mean flow velocity at hyperventilation nadir in cm/s (e.g. 41.0 cm/s)."
                        },
                        "mean_arterial_pressure_mmhg": {
                            "type": "number",
                            "description": "Systemic mean arterial pressure in mmHg (default: 92.0 mmHg).",
                            "default": 92.0
                        }
                    },
                    "required": [
                        "baseline_etco2_mmhg",
                        "hyperventilation_etco2_mmhg",
                        "baseline_mca_velocity_cm_s",
                        "hyperventilation_mca_velocity_cm_s"
                    ]
                }
            }
        ]
    }


def handle_request(client: CerebralHyperventilationReactivityClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_hypocapnic_reactivity":
            res = client.evaluate_hypocapnic_reactivity(
                baseline_etco2_mmhg=float(args.get("baseline_etco2_mmhg", 40.0)),
                hyperventilation_etco2_mmhg=float(args.get("hyperventilation_etco2_mmhg", 26.0)),
                baseline_mca_velocity_cm_s=float(args.get("baseline_mca_velocity_cm_s", 62.0)),
                hyperventilation_mca_velocity_cm_s=float(args.get("hyperventilation_mca_velocity_cm_s", 42.0)),
                mean_arterial_pressure_mmhg=float(args.get("mean_arterial_pressure_mmhg", 92.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CerebralHyperventilationReactivityClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
