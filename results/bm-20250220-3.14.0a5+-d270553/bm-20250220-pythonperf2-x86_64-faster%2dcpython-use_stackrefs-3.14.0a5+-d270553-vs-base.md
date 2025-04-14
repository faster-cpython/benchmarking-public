# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.005x slower
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                       | 287 ms: 1.01x slower                                                            |
| docutils       | 2.87 sec                                                                     | 2.88 sec: 1.01x slower                                                          |
| html5lib       | 67.2 ms                                                                      | 68.4 ms: 1.02x slower                                                           |
| sphinx         | 1.09 sec                                                                     | 1.10 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines              | 21.3 ms                                                                      | 20.7 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed | 519 ms                                                                       | 522 ms: 1.01x slower                                                            |
| asyncio_websockets      | 386 ms                                                                       | 389 ms: 1.01x slower                                                            |
| async_generators        | 416 ms                                                                       | 419 ms: 1.01x slower                                                            |
| async_tree_io_tg        | 645 ms                                                                       | 655 ms: 1.02x slower                                                            |
| Geometric mean          | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 70.4 ms                                                                      | 69.9 ms: 1.01x faster                                                           |
| pidigits       | 253 ms                                                                       | 254 ms: 1.00x slower                                                            |
| nbody          | 95.8 ms                                                                      | 101 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                       | 132 ms: 1.02x faster                                                            |
| regex_v8       | 26.4 ms                                                                      | 26.1 ms: 1.01x faster                                                           |
| regex_dna      | 237 ms                                                                       | 250 ms: 1.06x slower                                                            |
| regex_effbot   | 3.05 ms                                                                      | 3.29 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 59.7 ms                                                                      | 59.2 ms: 1.01x faster                                                           |
| pickle_pure_python   | 330 us                                                                       | 333 us: 1.01x slower                                                            |
| xml_etree_parse      | 137 ms                                                                       | 139 ms: 1.01x slower                                                            |
| tomli_loads          | 2.10 sec                                                                     | 2.14 sec: 1.02x slower                                                          |
| unpickle_pure_python | 207 us                                                                       | 211 us: 1.02x slower                                                            |
| json_dumps           | 11.3 ms                                                                      | 11.7 ms: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.07 ms                                                                      | 9.04 ms: 1.00x faster                                                           |
| python_startup         | 16.2 ms                                                                      | 16.2 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 25.3 ms                                                                      | 24.2 ms: 1.04x faster                                                           |
| genshi_xml      | 55.1 ms                                                                      | 55.7 ms: 1.01x slower                                                           |
| mako            | 10.7 ms                                                                      | 10.9 ms: 1.02x slower                                                           |
| django_template | 35.2 ms                                                                      | 36.7 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                        | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20250219-pythonperf2-x86_64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|--------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| richards                 | 48.3 ms                                                                      | 45.9 ms: 1.05x faster                                                           |
| genshi_text              | 25.3 ms                                                                      | 24.2 ms: 1.04x faster                                                           |
| richards_super           | 53.6 ms                                                                      | 51.9 ms: 1.03x faster                                                           |
| coroutines               | 21.3 ms                                                                      | 20.7 ms: 1.03x faster                                                           |
| hexiom                   | 6.16 ms                                                                      | 6.00 ms: 1.03x faster                                                           |
| logging_silent           | 96.8 ns                                                                      | 94.6 ns: 1.02x faster                                                           |
| logging_simple           | 6.51 us                                                                      | 6.38 us: 1.02x faster                                                           |
| regex_compile            | 135 ms                                                                       | 132 ms: 1.02x faster                                                            |
| deepcopy                 | 286 us                                                                       | 280 us: 1.02x faster                                                            |
| scimark_sor              | 109 ms                                                                       | 108 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult  | 4.85 ms                                                                      | 4.77 ms: 1.02x faster                                                           |
| go                       | 131 ms                                                                       | 130 ms: 1.01x faster                                                            |
| deepcopy_memo            | 28.9 us                                                                      | 28.6 us: 1.01x faster                                                           |
| sqlglot_parse            | 1.36 ms                                                                      | 1.34 ms: 1.01x faster                                                           |
| regex_v8                 | 26.4 ms                                                                      | 26.1 ms: 1.01x faster                                                           |
| sqlglot_transpile        | 1.74 ms                                                                      | 1.73 ms: 1.01x faster                                                           |
| xml_etree_process        | 59.7 ms                                                                      | 59.2 ms: 1.01x faster                                                           |
| deltablue                | 3.37 ms                                                                      | 3.34 ms: 1.01x faster                                                           |
| float                    | 70.4 ms                                                                      | 69.9 ms: 1.01x faster                                                           |
| thrift                   | 867 us                                                                       | 860 us: 1.01x faster                                                            |
| sqlglot_optimize         | 56.5 ms                                                                      | 56.1 ms: 1.01x faster                                                           |
| mdp                      | 2.49 sec                                                                     | 2.47 sec: 1.01x faster                                                          |
| pprint_safe_repr         | 794 ms                                                                       | 790 ms: 1.01x faster                                                            |
| sqlglot_normalize        | 113 ms                                                                       | 112 ms: 1.00x faster                                                            |
| sympy_expand             | 493 ms                                                                       | 491 ms: 1.00x faster                                                            |
| many_optionals           | 1.01 ms                                                                      | 1.00 ms: 1.00x faster                                                           |
| python_startup_no_site   | 9.07 ms                                                                      | 9.04 ms: 1.00x faster                                                           |
| python_startup           | 16.2 ms                                                                      | 16.2 ms: 1.00x faster                                                           |
| pidigits                 | 253 ms                                                                       | 254 ms: 1.00x slower                                                            |
| scimark_monte_carlo      | 63.4 ms                                                                      | 63.6 ms: 1.00x slower                                                           |
| spectral_norm            | 84.6 ms                                                                      | 84.8 ms: 1.00x slower                                                           |
| sqlite_synth             | 2.81 us                                                                      | 2.82 us: 1.00x slower                                                           |
| sympy_integrate          | 22.9 ms                                                                      | 23.0 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 2.91 us                                                                      | 2.93 us: 1.01x slower                                                           |
| docutils                 | 2.87 sec                                                                     | 2.88 sec: 1.01x slower                                                          |
| sympy_str                | 287 ms                                                                       | 289 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed  | 519 ms                                                                       | 522 ms: 1.01x slower                                                            |
| pyflate                  | 448 ms                                                                       | 451 ms: 1.01x slower                                                            |
| asyncio_websockets       | 386 ms                                                                       | 389 ms: 1.01x slower                                                            |
| meteor_contest           | 126 ms                                                                       | 127 ms: 1.01x slower                                                            |
| async_generators         | 416 ms                                                                       | 419 ms: 1.01x slower                                                            |
| json                     | 5.40 ms                                                                      | 5.44 ms: 1.01x slower                                                           |
| sphinx                   | 1.09 sec                                                                     | 1.10 sec: 1.01x slower                                                          |
| pickle_pure_python       | 330 us                                                                       | 333 us: 1.01x slower                                                            |
| sqlalchemy_declarative   | 142 ms                                                                       | 144 ms: 1.01x slower                                                            |
| genshi_xml               | 55.1 ms                                                                      | 55.7 ms: 1.01x slower                                                           |
| nqueens                  | 89.9 ms                                                                      | 90.9 ms: 1.01x slower                                                           |
| 2to3                     | 284 ms                                                                       | 287 ms: 1.01x slower                                                            |
| generators               | 28.3 ms                                                                      | 28.6 ms: 1.01x slower                                                           |
| fannkuch                 | 365 ms                                                                       | 370 ms: 1.01x slower                                                            |
| xml_etree_parse          | 137 ms                                                                       | 139 ms: 1.01x slower                                                            |
| async_tree_io_tg         | 645 ms                                                                       | 655 ms: 1.02x slower                                                            |
| mako                     | 10.7 ms                                                                      | 10.9 ms: 1.02x slower                                                           |
| pathlib                  | 16.8 ms                                                                      | 17.0 ms: 1.02x slower                                                           |
| bpe_tokeniser            | 4.60 sec                                                                     | 4.68 sec: 1.02x slower                                                          |
| html5lib                 | 67.2 ms                                                                      | 68.4 ms: 1.02x slower                                                           |
| bench_thread_pool        | 935 us                                                                       | 953 us: 1.02x slower                                                            |
| tomli_loads              | 2.10 sec                                                                     | 2.14 sec: 1.02x slower                                                          |
| subparsers               | 22.5 ms                                                                      | 23.0 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 207 us                                                                       | 211 us: 1.02x slower                                                            |
| scimark_fft              | 305 ms                                                                       | 311 ms: 1.02x slower                                                            |
| pycparser                | 1.23 sec                                                                     | 1.25 sec: 1.02x slower                                                          |
| raytrace                 | 275 ms                                                                       | 282 ms: 1.02x slower                                                            |
| coverage                 | 77.4 ms                                                                      | 79.6 ms: 1.03x slower                                                           |
| telco                    | 7.95 ms                                                                      | 8.17 ms: 1.03x slower                                                           |
| typing_runtime_protocols | 170 us                                                                       | 175 us: 1.03x slower                                                            |
| chaos                    | 60.4 ms                                                                      | 62.4 ms: 1.03x slower                                                           |
| json_dumps               | 11.3 ms                                                                      | 11.7 ms: 1.03x slower                                                           |
| comprehensions           | 16.9 us                                                                      | 17.5 us: 1.04x slower                                                           |
| django_template          | 35.2 ms                                                                      | 36.7 ms: 1.04x slower                                                           |
| regex_dna                | 237 ms                                                                       | 250 ms: 1.06x slower                                                            |
| nbody                    | 95.8 ms                                                                      | 101 ms: 1.06x slower                                                            |
| crypto_pyaes             | 74.7 ms                                                                      | 79.3 ms: 1.06x slower                                                           |
| regex_effbot             | 3.05 ms                                                                      | 3.29 ms: 1.08x slower                                                           |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (22): bench_mp_pool, async_tree_none_tg, logging_format, k_core, async_tree_io, pprint_pformat, sympy_sum, scimark_lu, async_tree_cpu_io_mixed_tg, shortest_path, pylint, xml_etree_generate, dulwich_log, connected_components, json_loads, sqlalchemy_imperative, async_tree_memoization_tg, gc_traversal, async_tree_memoization, xml_etree_iterparse, async_tree_none, create_gc_cycles

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x