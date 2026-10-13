---
pretty_name: Super Research Benchmark
license: other
language:
- en
task_categories:
- question-answering
- text-generation
tags:
- deep-research
- research-agents
- long-form-generation
- benchmark
- reasoning
configs:
- config_name: questions
  data_files:
  - split: test
    path: questions.jsonl
- config_name: reports
  data_files:
  - split: test
    path: reports.jsonl
- config_name: systems
  data_files:
  - split: test
    path: systems.jsonl
---

# Super Research Benchmark

Super Research evaluates autonomous research on complex, open-ended questions that require broad evidence gathering, deep investigation, cross-source synthesis, and coherent long-form reporting.

This release contains:

- **300 English research questions** across ten domains.
- **12 research systems** with recorded provider and model identifiers.
- **3,600 complete agent reports**, with 300 reports for every included system.
- Stable task IDs and SHA-256 hashes for questions, reports, and archived report inputs.

## Dataset configurations

| Configuration | Rows | Contents |
|---|---:|---|
| `questions` | 300 | Task IDs, domains, English questions, and question hashes |
| `reports` | 3,600 | Questions, system metadata, complete reports, inputs, and hashes |
| `systems` | 12 | Provider, model, system ID, and report count |

```python
from datasets import load_dataset

questions = load_dataset(
    "FreeFrank/Super-Research-Benchmark",
    "questions",
    split="test",
)

reports = load_dataset(
    "FreeFrank/Super-Research-Benchmark",
    "reports",
    split="test",
)
```

## Fields

Question rows contain `task_id`, `language`, `domain`, `question`, and `question_sha256`.

Report rows contain the corresponding question fields together with `system_id`, `provider`, `model`, `report_text`, `report_sha256`, `report_input`, and `report_input_sha256`.

## Resources

- [Project website](https://cnsdqd-dyb.github.io/Super-Research-Benchmark/)
- [Interactive task visualizer](https://cnsdqd-dyb.github.io/Super-Research-Benchmark/ui.html)
- [GitHub repository](https://github.com/cnsdqd-dyb/Super-Research-Benchmark)
- [Paper](https://arxiv.org/abs/2603.00582)

## Citation

```bibtex
@article{superresearch2026,
  title={Super Research: Answering Highly Complex Questions with Large Language Models through Super Deep and Super Wide Research},
  author={Dong, Yubo and You, Nianhao and Hou, Yuxuan and Sun, Zixun and Zhang, Yue and Zhang, Liang and Zhao, Siyuan and Fan, Hehe},
  journal={arXiv preprint arXiv:2603.00582},
  year={2026},
  url={https://arxiv.org/abs/2603.00582}
}
```
