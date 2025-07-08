# Results vs. base

- fork: faster-cpython
- ref: fast_side_exits
- machine: windows-amd64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.001x slower
- HPT reliability: 61.01%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 218 ms: 1.01x faster                                                            |
| docutils       | 1.65 sec                                                                   | 1.64 sec: 1.01x faster                                                          |
| html5lib       | 38.4 ms                                                                    | 38.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 14.8 ms                                                                    | 14.4 ms: 1.03x faster                                                           |
| asyncio_websockets         | 164 ms                                                                     | 161 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                     | 337 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 332 ms                                                                     | 328 ms: 1.01x faster                                                            |
| async_generators           | 243 ms                                                                     | 244 ms: 1.00x slower                                                            |
| async_tree_none            | 167 ms                                                                     | 168 ms: 1.01x slower                                                            |
| async_tree_memoization     | 203 ms                                                                     | 205 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 388 ms                                                                     | 395 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 52.2 ms                                                                    | 53.5 ms: 1.02x slower                                                           |
| float          | 42.6 ms                                                                    | 43.7 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                    | 13.4 ms: 1.07x faster                                                           |
| regex_effbot   | 1.57 ms                                                                    | 1.54 ms: 1.02x faster                                                           |
| regex_dna      | 120 ms                                                                     | 118 ms: 1.01x faster                                                            |
| regex_compile  | 78.1 ms                                                                    | 79.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|--------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process  | 35.6 ms                                                                    | 34.9 ms: 1.02x faster                                                           |
| tomli_loads        | 1.14 sec                                                                   | 1.13 sec: 1.02x faster                                                          |
| json_dumps         | 6.19 ms                                                                    | 6.26 ms: 1.01x slower                                                           |
| pickle_pure_python | 202 us                                                                     | 205 us: 1.02x slower                                                            |
| xml_etree_generate | 50.0 ms                                                                    | 50.9 ms: 1.02x slower                                                           |
| Geometric mean     | (ref)                                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_pure_python, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                                    | 15.3 ms: 1.01x slower                                                           |
| django_template | 23.9 ms                                                                    | 24.1 ms: 1.01x slower                                                           |
| genshi_xml      | 33.4 ms                                                                    | 34.2 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250707-pythonperf1-amd64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf1-amd64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 20.7 ms                                                                    | 19.4 ms: 1.07x faster                                                           |
| regex_v8                   | 14.3 ms                                                                    | 13.4 ms: 1.07x faster                                                           |
| coroutines                 | 14.8 ms                                                                    | 14.4 ms: 1.03x faster                                                           |
| scimark_lu                 | 59.2 ms                                                                    | 57.7 ms: 1.03x faster                                                           |
| typing_runtime_protocols   | 105 us                                                                     | 102 us: 1.03x faster                                                            |
| xml_etree_process          | 35.6 ms                                                                    | 34.9 ms: 1.02x faster                                                           |
| regex_effbot               | 1.57 ms                                                                    | 1.54 ms: 1.02x faster                                                           |
| asyncio_websockets         | 164 ms                                                                     | 161 ms: 1.02x faster                                                            |
| spectral_norm              | 66.9 ms                                                                    | 65.7 ms: 1.02x faster                                                           |
| richards                   | 26.7 ms                                                                    | 26.3 ms: 1.02x faster                                                           |
| tomli_loads                | 1.14 sec                                                                   | 1.13 sec: 1.02x faster                                                          |
| crypto_pyaes               | 46.3 ms                                                                    | 45.6 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                     | 337 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 332 ms                                                                     | 328 ms: 1.01x faster                                                            |
| thrift                     | 494 us                                                                     | 488 us: 1.01x faster                                                            |
| regex_dna                  | 120 ms                                                                     | 118 ms: 1.01x faster                                                            |
| html5lib                   | 38.4 ms                                                                    | 38.0 ms: 1.01x faster                                                           |
| json                       | 3.09 ms                                                                    | 3.05 ms: 1.01x faster                                                           |
| coverage                   | 49.7 ms                                                                    | 49.2 ms: 1.01x faster                                                           |
| 2to3                       | 220 ms                                                                     | 218 ms: 1.01x faster                                                            |
| sympy_expand               | 295 ms                                                                     | 293 ms: 1.01x faster                                                            |
| richards_super             | 30.3 ms                                                                    | 30.2 ms: 1.01x faster                                                           |
| docutils                   | 1.65 sec                                                                   | 1.64 sec: 1.01x faster                                                          |
| scimark_monte_carlo        | 40.9 ms                                                                    | 41.1 ms: 1.00x slower                                                           |
| sympy_str                  | 169 ms                                                                     | 170 ms: 1.00x slower                                                            |
| deepcopy_memo              | 18.4 us                                                                    | 18.5 us: 1.00x slower                                                           |
| async_generators           | 243 ms                                                                     | 244 ms: 1.00x slower                                                            |
| mdp                        | 800 ms                                                                     | 804 ms: 1.01x slower                                                            |
| hexiom                     | 4.06 ms                                                                    | 4.09 ms: 1.01x slower                                                           |
| genshi_text                | 15.2 ms                                                                    | 15.3 ms: 1.01x slower                                                           |
| sqlglot_v2_parse           | 783 us                                                                     | 788 us: 1.01x slower                                                            |
| async_tree_none            | 167 ms                                                                     | 168 ms: 1.01x slower                                                            |
| deltablue                  | 2.19 ms                                                                    | 2.20 ms: 1.01x slower                                                           |
| sympy_sum                  | 86.7 ms                                                                    | 87.4 ms: 1.01x slower                                                           |
| logging_format             | 6.55 us                                                                    | 6.61 us: 1.01x slower                                                           |
| scimark_fft                | 154 ms                                                                     | 156 ms: 1.01x slower                                                            |
| pyflate                    | 251 ms                                                                     | 253 ms: 1.01x slower                                                            |
| async_tree_memoization     | 203 ms                                                                     | 205 ms: 1.01x slower                                                            |
| django_template            | 23.9 ms                                                                    | 24.1 ms: 1.01x slower                                                           |
| json_dumps                 | 6.19 ms                                                                    | 6.26 ms: 1.01x slower                                                           |
| sympy_integrate            | 12.6 ms                                                                    | 12.8 ms: 1.01x slower                                                           |
| create_gc_cycles           | 1.31 ms                                                                    | 1.32 ms: 1.01x slower                                                           |
| sqlglot_v2_transpile       | 986 us                                                                     | 998 us: 1.01x slower                                                            |
| nqueens                    | 59.0 ms                                                                    | 59.7 ms: 1.01x slower                                                           |
| logging_simple             | 6.07 us                                                                    | 6.15 us: 1.01x slower                                                           |
| regex_compile              | 78.1 ms                                                                    | 79.1 ms: 1.01x slower                                                           |
| raytrace                   | 175 ms                                                                     | 177 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 388 ms                                                                     | 395 ms: 1.02x slower                                                            |
| pickle_pure_python         | 202 us                                                                     | 205 us: 1.02x slower                                                            |
| xml_etree_generate         | 50.0 ms                                                                    | 50.9 ms: 1.02x slower                                                           |
| shortest_path              | 356 ms                                                                     | 364 ms: 1.02x slower                                                            |
| nbody                      | 52.2 ms                                                                    | 53.5 ms: 1.02x slower                                                           |
| genshi_xml                 | 33.4 ms                                                                    | 34.2 ms: 1.02x slower                                                           |
| go                         | 75.6 ms                                                                    | 77.5 ms: 1.02x slower                                                           |
| float                      | 42.6 ms                                                                    | 43.7 ms: 1.03x slower                                                           |
| gc_traversal               | 2.11 ms                                                                    | 2.17 ms: 1.03x slower                                                           |
| meteor_contest             | 70.2 ms                                                                    | 72.4 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 452 ms                                                                     | 467 ms: 1.03x slower                                                            |
| scimark_sor                | 75.6 ms                                                                    | 78.1 ms: 1.03x slower                                                           |
| fannkuch                   | 223 ms                                                                     | 235 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 2.26 ms                                                                    | 2.53 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (31): comprehensions, xml_etree_parse, pylint, k_core, pycparser, dulwich_log, bpe_tokeniser, sphinx, many_optionals, mako, async_tree_memoization_tg, chaos, deepcopy_reduce, python_startup_no_site, async_tree_io, sqlglot_v2_optimize, sqlglot_v2_normalize, unpickle_pure_python, sqlite_synth, connected_components, deepcopy, subparsers, logging_silent, pprint_pformat, pidigits, python_startup, pathlib, json_loads, telco, async_tree_none_tg, xml_etree_iterparse

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 61.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown