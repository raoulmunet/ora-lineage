from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import table_lineage,simple_column_lineage

def main(argv=None):
    p=argparse.ArgumentParser(description="Oracle SQL lineage.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json","mermaid"),default="text")
    a=p.parse_args(argv); sql=Path(a.source).read_text(encoding="utf-8")
    edges=simple_column_lineage(sql) or table_lineage(sql)
    if a.format=="json": print(json.dumps([e.to_dict() for e in edges],indent=2))
    elif a.format=="mermaid":
        print("flowchart LR")
        for i,e in enumerate(edges): print(f'    S{i}["{e.source}"] --> T{i}["{e.target}"]')
    else:
        for e in edges: print(f"{e.source} -> {e.target} [{e.level}]")
    return 0
if __name__=="__main__": raise SystemExit(main())
