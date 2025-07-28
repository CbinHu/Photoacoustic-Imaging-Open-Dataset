#!/usr/bin/env python3
import yaml, textwrap, pathlib, datetime

REPO_URL = "https://github.com/yezanting/Med-VLM-Bench-Summary"

def shield(t, v):
    return f"https://img.shields.io/{t}/{v}?style=flat-square&color=blue"

def gen_table(data):
    header = "| Dataset | Paper | Year / Venue | Modality | Tasks | Samples | Link |"
    sep =   "|:--------|:------|:-------------|:---------|:------|:--------|:-----|"
    rows = [
        f"| {d['name']} | {d['title']} | {d['year_venue']} | {d['modality']} | {d['tasks']} | {d['samples']} | {d['link']} |"
        for d in data
    ]
    return "\n".join([header, sep, *rows])

if __name__ == "__main__":
    with open("datasets.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    table = gen_table(data)

    readme = textwrap.dedent(f"""
        # 🧠 Med-VLM-Bench: A Curated Benchmark Repository for Medical Vision-Language Models

        📚 A comprehensive summary of recent benchmarks for evaluating and training Medical Vision-Language Models (Med-VLMs)

        ![Stars]({shield('github/stars', 'yezanting/Med-VLM-Bench-Summary')})
        ![Forks]({shield('github/forks', 'yezanting/Med-VLM-Bench-Summary')})
        ![License]({shield('github/license', 'yezanting/Med-VLM-Bench-Summary')})
        ![Last Commit]({shield('github/last-commit', 'yezanting/Med-VLM-Bench-Summary')})

        ## 📊 Dataset Summary
        {table}

        ## 🤝 Contribution
        To add a new dataset, please open an issue or submit a pull request with the YAML entry.

        > Last updated: {datetime.date.today().isoformat()}
    """).strip()

    pathlib.Path("README.md").write_text(readme, encoding="utf-8")
    print("✅ README.md 已生成！")