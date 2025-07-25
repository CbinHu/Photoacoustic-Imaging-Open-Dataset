#!/usr/bin/env python3
import yaml, datetime, pathlib, textwrap, os

URL = 'https://github.com/CbinHu/general_PAID'

def shield(t, v): return f'https://img.shields.io/{t}/{v}?style=flat-square&color=blue'

def gen_table(data):
    header = '| Dataset | Paper | Year / Venue | Modality | Tasks | Samples | Link |'
    sep    = '|---------|-------|--------------|----------|-------|---------|------|'
    rows = [f"| {d['name']} | {d['title']} | {d['year_venue']} | {d['modality']} | {d['tasks']} | {d['samples']} | {d['link']} |"
            for d in data]
    return '\n'.join([header, sep, *rows])

if __name__ == '__main__':
    data = yaml.safe_load(open('datasets.yml'))
    tbl  = gen_table(data)
    readme = textwrap.dedent(f"""
    # 🧪 Photoacoustic Dataset Bench
    > Curated list of open-source photoacoustic imaging datasets.

    ![Stars]({shield('github/stars', URL)})
    ![Forks]({shield('github/forks', URL)})
    ![License]({shield('github/license', URL)})  
    ![Last Commit]({shield('github/last-commit', URL)})

    ## 📊 Dataset Summary
    {tbl}

    ## 🤝 Contribution
    Open an issue or PR to add new datasets!
    """).strip()
    pathlib.Path('README.md').write_text(readme, encoding='utf-8')