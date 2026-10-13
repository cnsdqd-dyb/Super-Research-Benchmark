# Task Visualizer

The Super Research Task Visualizer opens one structured research task at a time. It presents the final report together with the evidence graph, source distribution, reasoning depth, editable evaluation items, and task-level usage statistics.

## Open the visualizer

Use the [hosted visualizer](https://cnsdqd-dyb.github.io/Super-Research-Benchmark/ui.html), or serve the repository locally:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/ui.html`. Choose **Load Example** to inspect the included `annotation.json`, or choose **Import Task JSON** to open your own task. Processing stays in the browser; importing a task does not upload the file.

## JSON structure

The visualizer accepts one JSON object with these top-level fields:

| Field | Required | Description |
|---|---:|---|
| `root_question` | Recommended | Research question shown by the task data |
| `final_report` | Yes | Complete report in Markdown |
| `global_graph.nodes` | Yes | Evidence and conclusion nodes |
| `global_graph.links` | Yes | Directed relationships between node IDs |
| `merged_quiz` | Optional | Evaluation items associated with the task |
| `total_usage` | Optional | `total_tokens`, `input_tokens`, and `output_tokens` |

Minimal example:

```json
{
  "root_question": "What explains the observed outcome?",
  "final_report": "# Finding\n\nThe evidence supports ...",
  "global_graph": {
    "nodes": [
      {"id": "source_1", "type": "url", "content": "https://example.org/source"},
      {"id": "fact_1", "type": "fact", "content": "Observed evidence"},
      {"id": "conclusion_1", "type": "global_conclusion", "content": "Supported conclusion"}
    ],
    "links": [
      {"source": "source_1", "target": "fact_1"},
      {"source": "fact_1", "target": "conclusion_1"}
    ]
  },
  "merged_quiz": [],
  "total_usage": {"total_tokens": 0, "input_tokens": 0, "output_tokens": 0}
}
```

Node IDs must be unique. Every link's `source` and `target` must match an existing node ID. Common node types are `url`, `fact`, `intermediate_conclusion`, and `global_conclusion`.

## Validate before import

```bash
python scripts/benchmark.py visualize-check --input annotation.json
python scripts/benchmark.py visualize-check --input path/to/your_task.json
```

The command checks required report and graph fields, unique node IDs, valid link endpoints, and the evaluation-item array. The included `annotation.json` is a complete reference example.

## Views

- **Report** renders the Markdown report and links citations to graph nodes.
- **Graph** provides an interactive evidence and conclusion graph with node inspection.
- **Editor** lets researchers revise the report and evaluation items, then export the updated task JSON.
- **Evaluate** imports compatible task-level evaluation output for score, source, and item-level inspection.
