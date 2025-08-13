# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.026x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                     | 217 ms: 1.03x faster                                                               |
| docutils       | 1.67 sec                                                                   | 1.60 sec: 1.04x faster                                                             |
| html5lib       | 40.1 ms                                                                    | 37.8 ms: 1.06x faster                                                              |
| sphinx         | 650 ms                                                                     | 623 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg        | 387 ms                                                                     | 374 ms: 1.03x faster                                                               |
| asyncio_websockets      | 159 ms                                                                     | 154 ms: 1.03x faster                                                               |
| async_tree_memoization  | 205 ms                                                                     | 199 ms: 1.03x faster                                                               |
| async_tree_io           | 389 ms                                                                     | 379 ms: 1.03x faster                                                               |
| coroutines              | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                              |
| async_tree_none_tg      | 167 ms                                                                     | 164 ms: 1.02x faster                                                               |
| async_generators        | 250 ms                                                                     | 246 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed | 332 ms                                                                     | 328 ms: 1.01x faster                                                               |
| Geometric mean          | (ref)                                                                      | 1.02x faster                                                                       |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 52.8 ms                                                                    | 43.5 ms: 1.21x faster                                                              |
| float          | 44.9 ms                                                                    | 43.0 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.09x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 13.7 ms                                                                    | 13.1 ms: 1.05x faster                                                              |
| regex_dna      | 120 ms                                                                     | 114 ms: 1.05x faster                                                               |
| regex_effbot   | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|--------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_process  | 35.7 ms                                                                    | 34.7 ms: 1.03x faster                                                              |
| xml_etree_generate | 51.1 ms                                                                    | 50.1 ms: 1.02x faster                                                              |
| json_loads         | 14.1 us                                                                    | 13.9 us: 1.02x faster                                                              |
| pickle_pure_python | 204 us                                                                     | 201 us: 1.01x faster                                                               |
| tomli_loads        | 1.09 sec                                                                   | 1.07 sec: 1.01x faster                                                             |
| xml_etree_parse    | 87.9 ms                                                                    | 86.7 ms: 1.01x faster                                                              |
| Geometric mean     | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 26.8 ms                                                                    | 25.2 ms: 1.06x faster                                                              |
| python_startup_no_site | 19.9 ms                                                                    | 19.0 ms: 1.05x faster                                                              |
| Geometric mean         | (ref)                                                                      | 1.06x faster                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml      | 35.0 ms                                                                    | 33.9 ms: 1.03x faster                                                              |
| django_template | 24.4 ms                                                                    | 24.0 ms: 1.02x faster                                                              |
| genshi_text     | 15.6 ms                                                                    | 15.4 ms: 1.01x faster                                                              |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|--------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                    | 52.8 ms                                                                    | 43.5 ms: 1.21x faster                                                              |
| telco                    | 4.75 ms                                                                    | 4.24 ms: 1.12x faster                                                              |
| pathlib                  | 32.1 ms                                                                    | 28.6 ms: 1.12x faster                                                              |
| spectral_norm            | 66.2 ms                                                                    | 60.9 ms: 1.09x faster                                                              |
| python_startup           | 26.8 ms                                                                    | 25.2 ms: 1.06x faster                                                              |
| crypto_pyaes             | 46.3 ms                                                                    | 43.5 ms: 1.06x faster                                                              |
| dulwich_log              | 40.9 ms                                                                    | 38.5 ms: 1.06x faster                                                              |
| sqlite_synth             | 1.61 us                                                                    | 1.52 us: 1.06x faster                                                              |
| html5lib                 | 40.1 ms                                                                    | 37.8 ms: 1.06x faster                                                              |
| python_startup_no_site   | 19.9 ms                                                                    | 19.0 ms: 1.05x faster                                                              |
| regex_v8                 | 13.7 ms                                                                    | 13.1 ms: 1.05x faster                                                              |
| create_gc_cycles         | 1.33 ms                                                                    | 1.27 ms: 1.05x faster                                                              |
| json                     | 3.10 ms                                                                    | 2.96 ms: 1.05x faster                                                              |
| fannkuch                 | 209 ms                                                                     | 200 ms: 1.05x faster                                                               |
| regex_dna                | 120 ms                                                                     | 114 ms: 1.05x faster                                                               |
| float                    | 44.9 ms                                                                    | 43.0 ms: 1.05x faster                                                              |
| sphinx                   | 650 ms                                                                     | 623 ms: 1.04x faster                                                               |
| pycparser                | 694 ms                                                                     | 666 ms: 1.04x faster                                                               |
| sympy_str                | 173 ms                                                                     | 166 ms: 1.04x faster                                                               |
| scimark_fft              | 151 ms                                                                     | 145 ms: 1.04x faster                                                               |
| pylint                   | 199 ms                                                                     | 192 ms: 1.04x faster                                                               |
| docutils                 | 1.67 sec                                                                   | 1.60 sec: 1.04x faster                                                             |
| sqlglot_v2_parse         | 781 us                                                                     | 753 us: 1.04x faster                                                               |
| meteor_contest           | 71.6 ms                                                                    | 69.0 ms: 1.04x faster                                                              |
| gc_traversal             | 2.14 ms                                                                    | 2.07 ms: 1.04x faster                                                              |
| async_tree_io_tg         | 387 ms                                                                     | 374 ms: 1.03x faster                                                               |
| mdp                      | 800 ms                                                                     | 773 ms: 1.03x faster                                                               |
| asyncio_websockets       | 159 ms                                                                     | 154 ms: 1.03x faster                                                               |
| async_tree_memoization   | 205 ms                                                                     | 199 ms: 1.03x faster                                                               |
| genshi_xml               | 35.0 ms                                                                    | 33.9 ms: 1.03x faster                                                              |
| comprehensions           | 10.6 us                                                                    | 10.3 us: 1.03x faster                                                              |
| k_core                   | 1.63 sec                                                                   | 1.58 sec: 1.03x faster                                                             |
| xml_etree_process        | 35.7 ms                                                                    | 34.7 ms: 1.03x faster                                                              |
| shortest_path            | 354 ms                                                                     | 344 ms: 1.03x faster                                                               |
| pprint_pformat           | 893 ms                                                                     | 867 ms: 1.03x faster                                                               |
| regex_effbot             | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                                              |
| 2to3                     | 223 ms                                                                     | 217 ms: 1.03x faster                                                               |
| logging_silent           | 55.3 ns                                                                    | 53.9 ns: 1.03x faster                                                              |
| async_tree_io            | 389 ms                                                                     | 379 ms: 1.03x faster                                                               |
| pyflate                  | 263 ms                                                                     | 257 ms: 1.02x faster                                                               |
| scimark_monte_carlo      | 41.6 ms                                                                    | 40.6 ms: 1.02x faster                                                              |
| nqueens                  | 59.9 ms                                                                    | 58.6 ms: 1.02x faster                                                              |
| pprint_safe_repr         | 440 ms                                                                     | 430 ms: 1.02x faster                                                               |
| typing_runtime_protocols | 103 us                                                                     | 101 us: 1.02x faster                                                               |
| many_optionals           | 571 us                                                                     | 559 us: 1.02x faster                                                               |
| connected_components     | 320 ms                                                                     | 313 ms: 1.02x faster                                                               |
| coroutines               | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                              |
| sympy_sum                | 87.5 ms                                                                    | 85.9 ms: 1.02x faster                                                              |
| sympy_integrate          | 12.7 ms                                                                    | 12.5 ms: 1.02x faster                                                              |
| xml_etree_generate       | 51.1 ms                                                                    | 50.1 ms: 1.02x faster                                                              |
| subparsers               | 29.8 ms                                                                    | 29.3 ms: 1.02x faster                                                              |
| async_tree_none_tg       | 167 ms                                                                     | 164 ms: 1.02x faster                                                               |
| sympy_expand             | 292 ms                                                                     | 288 ms: 1.02x faster                                                               |
| json_loads               | 14.1 us                                                                    | 13.9 us: 1.02x faster                                                              |
| django_template          | 24.4 ms                                                                    | 24.0 ms: 1.02x faster                                                              |
| pickle_pure_python       | 204 us                                                                     | 201 us: 1.01x faster                                                               |
| async_generators         | 250 ms                                                                     | 246 ms: 1.01x faster                                                               |
| sqlglot_v2_normalize     | 70.6 ms                                                                    | 69.5 ms: 1.01x faster                                                              |
| tomli_loads              | 1.09 sec                                                                   | 1.07 sec: 1.01x faster                                                             |
| chaos                    | 40.3 ms                                                                    | 39.8 ms: 1.01x faster                                                              |
| richards                 | 27.3 ms                                                                    | 26.9 ms: 1.01x faster                                                              |
| xml_etree_parse          | 87.9 ms                                                                    | 86.7 ms: 1.01x faster                                                              |
| thrift                   | 496 us                                                                     | 490 us: 1.01x faster                                                               |
| genshi_text              | 15.6 ms                                                                    | 15.4 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed  | 332 ms                                                                     | 328 ms: 1.01x faster                                                               |
| richards_super           | 30.8 ms                                                                    | 30.4 ms: 1.01x faster                                                              |
| deepcopy_memo            | 18.1 us                                                                    | 17.9 us: 1.01x faster                                                              |
| bpe_tokeniser            | 2.49 sec                                                                   | 2.47 sec: 1.01x faster                                                             |
| logging_simple           | 6.04 us                                                                    | 5.98 us: 1.01x faster                                                              |
| scimark_sparse_mat_mult  | 2.33 ms                                                                    | 2.31 ms: 1.01x faster                                                              |
| go                       | 75.7 ms                                                                    | 76.1 ms: 1.01x slower                                                              |
| scimark_sor              | 74.5 ms                                                                    | 75.4 ms: 1.01x slower                                                              |
| coverage                 | 48.5 ms                                                                    | 49.2 ms: 1.01x slower                                                              |
| Geometric mean           | (ref)                                                                      | 1.03x faster                                                                       |

Benchmark hidden because not significant (19): async_tree_none, deepcopy_reduce, sqlglot_v2_transpile, sqlglot_v2_optimize, pidigits, generators, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, unpickle_pure_python, hexiom, deepcopy, mako, deltablue, regex_compile, json_dumps, scimark_lu, xml_etree_iterparse, raytrace, logging_format

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown