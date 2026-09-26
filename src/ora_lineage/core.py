from __future__ import annotations
from dataclasses import dataclass,asdict
import re
from ora_core import analyze_sql, normalize_identifier

@dataclass(frozen=True)
class LineageEdge:
    source: str
    target: str
    level: str = "table"
    def to_dict(self): return asdict(self)

def table_lineage(sql: str) -> list[LineageEdge]:
    a=analyze_sql(sql)
    return [LineageEdge(r,w) for r in a.read_objects for w in a.write_objects]

def simple_column_lineage(sql: str) -> list[LineageEdge]:
    m=re.search(r"INSERT\s+INTO\s+([\w.$#]+)\s*\((.*?)\)\s*SELECT\s+(.*?)\s+FROM\s+([\w.$#]+)(?:\s+\w+)?",sql,re.I|re.S)
    if not m: return []
    target=normalize_identifier(m.group(1)); source=normalize_identifier(m.group(4))
    targets=[x.strip().upper() for x in m.group(2).split(",")]
    exprs=[x.strip() for x in m.group(3).split(",")]
    if len(targets)!=len(exprs): return []
    edges=[]
    for t,e in zip(targets,exprs):
        col=re.fullmatch(r'(?:[A-Za-z][\w$#]*\.)?([A-Za-z][\w$#]*)',e)
        if col: edges.append(LineageEdge(f"{source}.{col.group(1).upper()}",f"{target}.{t}","column"))
    return edges
