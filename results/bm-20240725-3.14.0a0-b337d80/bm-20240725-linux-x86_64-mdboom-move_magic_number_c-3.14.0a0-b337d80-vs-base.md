# Results vs. base

- fork: mdboom
- ref: move_magic_number_c
- machine: linux-x86_64
- commit hash: b337d80
- commit date: 2024-07-25
- overall geometric mean: not sig
- HPT reliability: 84.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399 | bm-20240725-linux-x86_64-mdboom-move_magic_number_c-3.14.0a0-b337d80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                |

All benchmarks:
===============

| Benchmark      | bm-20240724-linux-x86_64-python-5592399313c963c11028-3.14.0a0-5592399 | bm-20240725-linux-x86_64-mdboom-move_magic_number_c-3.14.0a0-b337d80 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                |

# HPT report

- Reliability score: 84.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x