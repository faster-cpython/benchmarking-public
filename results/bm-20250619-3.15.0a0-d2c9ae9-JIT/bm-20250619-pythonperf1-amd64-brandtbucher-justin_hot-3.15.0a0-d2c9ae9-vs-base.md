# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.080x faster
- HPT reliability: 74.98%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators | 247 ms                                                     | 243 ms: 1.02x faster                                                   |
| coroutines       | 14.5 ms                                                    | 14.3 ms: 1.01x faster                                                  |
| async_tree_io_tg | 393 ms                                                     | 390 ms: 1.01x faster                                                   |
| async_tree_none  | 170 ms                                                     | 171 ms: 1.01x slower                                                   |
| Geometric mean   | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 148 ms                                                     | 149 ms: 1.01x slower                                                   |
| float          | 43.4 ms                                                    | 44.0 ms: 1.02x slower                                                  |
| nbody          | 60.6 ms                                                    | 62.4 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                      | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                    | 78.9 ms: 1.01x slower                                                  |
| regex_dna      | 116 ms                                                     | 120 ms: 1.04x slower                                                   |
| regex_v8       | 13.8 ms                                                    | 14.4 ms: 1.05x slower                                                  |
| regex_effbot   | 1.54 ms                                                    | 1.63 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                      | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate  | 53.3 ms                                                    | 50.7 ms: 1.05x faster                                                  |
| xml_etree_iterparse | 64.0 ms                                                    | 62.8 ms: 1.02x faster                                                  |
| xml_etree_process   | 36.7 ms                                                    | 36.4 ms: 1.01x faster                                                  |
| json_loads          | 14.5 us                                                    | 14.6 us: 1.01x slower                                                  |
| tomli_loads         | 1.14 sec                                                   | 1.16 sec: 1.02x slower                                                 |
| json_dumps          | 6.18 ms                                                    | 6.47 ms: 1.05x slower                                                  |
| Geometric mean      | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 19.5 ms                                                    | 19.3 ms: 1.02x faster                                                  |
| python_startup         | 26.1 ms                                                    | 25.8 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 23.8 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| genshi_xml      | 34.7 ms                                                    | 35.1 ms: 1.01x slower                                                  |
| genshi_text     | 15.4 ms                                                    | 15.7 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                   | 95.2 ms                                                    | 492 us: 193.45x faster                                                 |
| coverage                 | 298 ms                                                     | 50.2 ms: 5.93x faster                                                  |
| xml_etree_generate       | 53.3 ms                                                    | 50.7 ms: 1.05x faster                                                  |
| fannkuch                 | 242 ms                                                     | 232 ms: 1.04x faster                                                   |
| nqueens                  | 60.1 ms                                                    | 58.4 ms: 1.03x faster                                                  |
| meteor_contest           | 73.6 ms                                                    | 71.8 ms: 1.03x faster                                                  |
| logging_format           | 6.81 us                                                    | 6.64 us: 1.03x faster                                                  |
| pprint_safe_repr         | 519 ms                                                     | 507 ms: 1.02x faster                                                   |
| pprint_pformat           | 1.06 sec                                                   | 1.03 sec: 1.02x faster                                                 |
| mdp                      | 812 ms                                                     | 795 ms: 1.02x faster                                                   |
| xml_etree_iterparse      | 64.0 ms                                                    | 62.8 ms: 1.02x faster                                                  |
| async_generators         | 247 ms                                                     | 243 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 105 us                                                     | 103 us: 1.02x faster                                                   |
| deepcopy_memo            | 18.5 us                                                    | 18.2 us: 1.02x faster                                                  |
| deepcopy_reduce          | 1.82 us                                                    | 1.79 us: 1.02x faster                                                  |
| python_startup_no_site   | 19.5 ms                                                    | 19.3 ms: 1.02x faster                                                  |
| json                     | 3.11 ms                                                    | 3.07 ms: 1.01x faster                                                  |
| python_startup           | 26.1 ms                                                    | 25.8 ms: 1.01x faster                                                  |
| generators               | 19.9 ms                                                    | 19.6 ms: 1.01x faster                                                  |
| coroutines               | 14.5 ms                                                    | 14.3 ms: 1.01x faster                                                  |
| comprehensions           | 10.9 us                                                    | 10.8 us: 1.01x faster                                                  |
| logging_simple           | 6.34 us                                                    | 6.27 us: 1.01x faster                                                  |
| pathlib                  | 32.2 ms                                                    | 31.8 ms: 1.01x faster                                                  |
| bpe_tokeniser            | 2.66 sec                                                   | 2.63 sec: 1.01x faster                                                 |
| async_tree_io_tg         | 393 ms                                                     | 390 ms: 1.01x faster                                                   |
| sqlglot_v2_transpile     | 1.01 ms                                                    | 1.00 ms: 1.01x faster                                                  |
| xml_etree_process        | 36.7 ms                                                    | 36.4 ms: 1.01x faster                                                  |
| sqlglot_v2_normalize     | 70.4 ms                                                    | 70.7 ms: 1.00x slower                                                  |
| richards_super           | 30.5 ms                                                    | 30.7 ms: 1.01x slower                                                  |
| json_loads               | 14.5 us                                                    | 14.6 us: 1.01x slower                                                  |
| pidigits                 | 148 ms                                                     | 149 ms: 1.01x slower                                                   |
| scimark_monte_carlo      | 39.9 ms                                                    | 40.2 ms: 1.01x slower                                                  |
| async_tree_none          | 170 ms                                                     | 171 ms: 1.01x slower                                                   |
| sympy_str                | 171 ms                                                     | 172 ms: 1.01x slower                                                   |
| django_template          | 23.8 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| connected_components     | 325 ms                                                     | 328 ms: 1.01x slower                                                   |
| scimark_sor              | 76.2 ms                                                    | 77.0 ms: 1.01x slower                                                  |
| regex_compile            | 78.0 ms                                                    | 78.9 ms: 1.01x slower                                                  |
| genshi_xml               | 34.7 ms                                                    | 35.1 ms: 1.01x slower                                                  |
| sympy_integrate          | 12.7 ms                                                    | 12.8 ms: 1.01x slower                                                  |
| float                    | 43.4 ms                                                    | 44.0 ms: 1.02x slower                                                  |
| deltablue                | 2.21 ms                                                    | 2.24 ms: 1.02x slower                                                  |
| richards                 | 26.7 ms                                                    | 27.2 ms: 1.02x slower                                                  |
| tomli_loads              | 1.14 sec                                                   | 1.16 sec: 1.02x slower                                                 |
| gc_traversal             | 2.13 ms                                                    | 2.17 ms: 1.02x slower                                                  |
| shortest_path            | 352 ms                                                     | 359 ms: 1.02x slower                                                   |
| scimark_fft              | 158 ms                                                     | 161 ms: 1.02x slower                                                   |
| genshi_text              | 15.4 ms                                                    | 15.7 ms: 1.02x slower                                                  |
| go                       | 75.6 ms                                                    | 77.5 ms: 1.03x slower                                                  |
| raytrace                 | 177 ms                                                     | 182 ms: 1.03x slower                                                   |
| pyflate                  | 256 ms                                                     | 263 ms: 1.03x slower                                                   |
| chaos                    | 39.3 ms                                                    | 40.4 ms: 1.03x slower                                                  |
| nbody                    | 60.6 ms                                                    | 62.4 ms: 1.03x slower                                                  |
| regex_dna                | 116 ms                                                     | 120 ms: 1.04x slower                                                   |
| regex_v8                 | 13.8 ms                                                    | 14.4 ms: 1.05x slower                                                  |
| json_dumps               | 6.18 ms                                                    | 6.47 ms: 1.05x slower                                                  |
| regex_effbot             | 1.54 ms                                                    | 1.63 ms: 1.06x slower                                                  |
| Geometric mean           | (ref)                                                      | 1.08x faster                                                           |

Benchmark hidden because not significant (35): dulwich_log, telco, sqlglot_v2_parse, pickle_pure_python, async_tree_cpu_io_mixed_tg, spectral_norm, mako, sphinx, scimark_lu, scimark_sparse_mat_mult, html5lib, sympy_sum, pycparser, async_tree_none_tg, logging_silent, deepcopy, create_gc_cycles, pylint, crypto_pyaes, async_tree_memoization_tg, docutils, xml_etree_parse, many_optionals, sqlglot_v2_optimize, sqlite_synth, async_tree_cpu_io_mixed, hexiom, sympy_expand, 2to3, async_tree_memoization, k_core, asyncio_websockets, async_tree_io, subparsers, unpickle_pure_python

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 74.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown