# Testing a research agent

Use `data/questions.jsonl` as the task collection. Submit the question text to your research system and retain the complete answer, citations and source links.

## Submission format

Store one JSON object per line with these fields:

| Field | Description |
|---|---|
| `task_id` | Dataset identifier, for example `1:1`. |
| `question_sha256` | Hash copied from the task record. |
| `system_id` | Identifier for your agent configuration. |
| `report_text` | Complete report text, including citations. |

Optional fields include `model`, `run_id`, `timestamp`, and tool configuration. Use a separate system identifier for each configuration. A collection may contain several systems; complete validation requires 300 unique tasks for each included system.

```bash
python scripts/benchmark.py validate --input outputs/my_agent.jsonl --require-complete
```

## Released reports

Use `systems.json` to find a system, then export its report collection:

```bash
python scripts/benchmark.py export --system system_01 --output outputs/alibaba.jsonl
```

Exports include the dataset question hash for collection organization, the original report text, and `report_input` with its own hash for preserving the run context. These fields have distinct meanings. For new agent runs, submit the current dataset question directly.

## Metric assessment

Assess reports with the five dimensions in [METRICS.md](METRICS.md). Retain per-item evidence and evaluator configuration with the results:

- Coverage: reference node IDs, support judgments and exact report quotations.
- Conditional Depth: conclusion and premise quotations, inference chain, advancement level, inference status and premise-support status.
- Utility: task requirements, usability criteria and their report evidence.
- Consistency: reference paths and the support judgments for their constituent nodes.
- Objectivity: assessed claims, reference evidence and agreement judgments.

Record the reference and protocol version for each assessment. Aggregate per system and report the number of assessed tasks and missing values alongside each metric. Keep the five dimensions separate; when reporting an aggregate, specify its included dimensions and weights.

The supplied command-line tool handles data integrity, task export and report validation. It runs offline and makes no model or API requests.
