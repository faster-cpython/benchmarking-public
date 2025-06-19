# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.003x slower
- HPT reliability: 94.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 185 ms                                                                | 186 ms: 1.00x slower                                                          |
| docutils       | 1.51 sec                                                              | 1.52 sec: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager | 72.0 ms                                                               | 71.8 ms: 1.00x faster                                                         |
| async_generators | 287 ms                                                                | 289 ms: 1.00x slower                                                          |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (17): async_tree_none, async_tree_memoization, async_tree_eager_io, coroutines, asyncio_websockets, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 58.6 ms                                                               | 58.2 ms: 1.01x faster                                                         |
| pidigits       | 285 ms                                                                | 284 ms: 1.00x faster                                                          |
| nbody          | 74.6 ms                                                               | 76.2 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x faster                                                          |
| regex_compile  | 79.3 ms                                                               | 79.4 ms: 1.00x slower                                                         |
| regex_effbot   | 2.35 ms                                                               | 2.36 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                              | 1.28 sec: 1.05x faster                                                        |
| xml_etree_generate   | 51.7 ms                                                               | 52.0 ms: 1.01x slower                                                         |
| xml_etree_process    | 37.4 ms                                                               | 37.9 ms: 1.01x slower                                                         |
| unpickle_pure_python | 138 us                                                                | 142 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_loads, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 14.0 ms                                                               | 14.1 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 6.94 ms                                                               | 7.29 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20250619-darwin-arm64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads              | 1.35 sec                                                              | 1.28 sec: 1.05x faster                                                        |
| hexiom                   | 5.02 ms                                                               | 4.82 ms: 1.04x faster                                                         |
| shortest_path            | 339 ms                                                                | 329 ms: 1.03x faster                                                          |
| connected_components     | 310 ms                                                                | 303 ms: 1.03x faster                                                          |
| k_core                   | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                        |
| meteor_contest           | 77.5 ms                                                               | 76.5 ms: 1.01x faster                                                         |
| nqueens                  | 69.5 ms                                                               | 68.8 ms: 1.01x faster                                                         |
| generators               | 31.9 ms                                                               | 31.6 ms: 1.01x faster                                                         |
| sympy_integrate          | 11.4 ms                                                               | 11.3 ms: 1.01x faster                                                         |
| float                    | 58.6 ms                                                               | 58.2 ms: 1.01x faster                                                         |
| logging_silent           | 345 ns                                                                | 344 ns: 1.01x faster                                                          |
| sympy_sum                | 81.2 ms                                                               | 80.8 ms: 1.00x faster                                                         |
| pyflate                  | 313 ms                                                                | 311 ms: 1.00x faster                                                          |
| pidigits                 | 285 ms                                                                | 284 ms: 1.00x faster                                                          |
| mdp                      | 820 ms                                                                | 817 ms: 1.00x faster                                                          |
| async_tree_eager         | 72.0 ms                                                               | 71.8 ms: 1.00x faster                                                         |
| raytrace                 | 210 ms                                                                | 210 ms: 1.00x faster                                                          |
| regex_dna                | 143 ms                                                                | 143 ms: 1.00x faster                                                          |
| richards_super           | 41.9 ms                                                               | 41.8 ms: 1.00x faster                                                         |
| regex_compile            | 79.3 ms                                                               | 79.4 ms: 1.00x slower                                                         |
| bpe_tokeniser            | 3.07 sec                                                              | 3.08 sec: 1.00x slower                                                        |
| chaos                    | 46.6 ms                                                               | 46.7 ms: 1.00x slower                                                         |
| logging_simple           | 4.09 us                                                               | 4.10 us: 1.00x slower                                                         |
| scimark_monte_carlo      | 52.9 ms                                                               | 53.0 ms: 1.00x slower                                                         |
| docutils                 | 1.51 sec                                                              | 1.52 sec: 1.00x slower                                                        |
| dulwich_log              | 26.8 ms                                                               | 26.8 ms: 1.00x slower                                                         |
| 2to3                     | 185 ms                                                                | 186 ms: 1.00x slower                                                          |
| sqlglot_v2_optimize      | 36.6 ms                                                               | 36.7 ms: 1.00x slower                                                         |
| gc_traversal             | 3.18 ms                                                               | 3.19 ms: 1.00x slower                                                         |
| spectral_norm            | 72.3 ms                                                               | 72.6 ms: 1.00x slower                                                         |
| python_startup_no_site   | 14.0 ms                                                               | 14.1 ms: 1.00x slower                                                         |
| logging_format           | 4.37 us                                                               | 4.39 us: 1.00x slower                                                         |
| async_generators         | 287 ms                                                                | 289 ms: 1.00x slower                                                          |
| regex_effbot             | 2.35 ms                                                               | 2.36 ms: 1.00x slower                                                         |
| sympy_expand             | 263 ms                                                                | 265 ms: 1.01x slower                                                          |
| xml_etree_generate       | 51.7 ms                                                               | 52.0 ms: 1.01x slower                                                         |
| scimark_sor              | 88.9 ms                                                               | 89.5 ms: 1.01x slower                                                         |
| many_optionals           | 504 us                                                                | 508 us: 1.01x slower                                                          |
| create_gc_cycles         | 1.35 ms                                                               | 1.36 ms: 1.01x slower                                                         |
| fannkuch                 | 300 ms                                                                | 303 ms: 1.01x slower                                                          |
| crypto_pyaes             | 57.2 ms                                                               | 57.7 ms: 1.01x slower                                                         |
| sqlglot_v2_transpile     | 1.07 ms                                                               | 1.08 ms: 1.01x slower                                                         |
| xml_etree_process        | 37.4 ms                                                               | 37.9 ms: 1.01x slower                                                         |
| sqlite_synth             | 1.58 us                                                               | 1.60 us: 1.01x slower                                                         |
| sqlglot_v2_parse         | 879 us                                                                | 893 us: 1.02x slower                                                          |
| coverage                 | 49.1 ms                                                               | 49.9 ms: 1.02x slower                                                         |
| telco                    | 4.53 ms                                                               | 4.62 ms: 1.02x slower                                                         |
| nbody                    | 74.6 ms                                                               | 76.2 ms: 1.02x slower                                                         |
| unpickle_pure_python     | 138 us                                                                | 142 us: 1.03x slower                                                          |
| typing_runtime_protocols | 104 us                                                                | 108 us: 1.03x slower                                                          |
| comprehensions           | 13.1 us                                                               | 13.5 us: 1.03x slower                                                         |
| scimark_fft              | 199 ms                                                                | 205 ms: 1.03x slower                                                          |
| pprint_safe_repr         | 591 ms                                                                | 613 ms: 1.04x slower                                                          |
| pprint_pformat           | 1.19 sec                                                              | 1.24 sec: 1.04x slower                                                        |
| mako                     | 6.94 ms                                                               | 7.29 ms: 1.05x slower                                                         |
| scimark_sparse_mat_mult  | 3.54 ms                                                               | 3.72 ms: 1.05x slower                                                         |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (45): deltablue, async_tree_none, async_tree_memoization, genshi_text, pycparser, xml_etree_iterparse, go, json_loads, json, sphinx, async_tree_eager_io, deepcopy, genshi_xml, json_dumps, regex_v8, deepcopy_reduce, coroutines, asyncio_websockets, sqlglot_v2_normalize, async_tree_eager_io_tg, xml_etree_parse, pickle_pure_python, pylint, richards, scimark_lu, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, sympy_str, async_tree_eager_tg, python_startup, deepcopy_memo, dask, async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_eager_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_io_tg, django_template, thrift, async_tree_cpu_io_mixed_tg, pathlib, subparsers, html5lib

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 94.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x