# Results vs. base

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 956b4a4
- commit date: 2025-03-18
- overall geometric mean: 1.016x faster
- HPT reliability: 84.13%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

| Benchmark | bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6+-f819900 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-956b4a4 |
|-----------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp       | 2.52 sec                                                                     | 2.49 sec: 1.02x faster                                             |

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 84.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown