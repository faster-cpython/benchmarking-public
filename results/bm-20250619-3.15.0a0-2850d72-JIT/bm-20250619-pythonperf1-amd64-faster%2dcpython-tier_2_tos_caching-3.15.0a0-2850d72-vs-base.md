# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.004x faster
- HPT reliability: 96.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                   | 1.67 sec: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                       |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines                 | 14.4 ms                                                                    | 14.5 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                     | 342 ms: 1.01x slower                                                               |
| async_generators           | 242 ms                                                                     | 246 ms: 1.02x slower                                                               |
| asyncio_websockets         | 157 ms                                                                     | 163 ms: 1.03x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 52.4 ms                                                                    | 44.8 ms: 1.17x faster                                                              |
| pidigits       | 150 ms                                                                     | 146 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.60 ms                                                                    | 1.59 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 14.5 us                                                                    | 14.0 us: 1.04x faster                                                              |
| pickle_pure_python   | 207 us                                                                     | 204 us: 1.01x faster                                                               |
| xml_etree_iterparse  | 63.8 ms                                                                    | 63.1 ms: 1.01x faster                                                              |
| xml_etree_parse      | 88.8 ms                                                                    | 87.8 ms: 1.01x faster                                                              |
| xml_etree_process    | 36.2 ms                                                                    | 35.9 ms: 1.01x faster                                                              |
| unpickle_pure_python | 112 us                                                                     | 113 us: 1.01x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.2 ms                                                                    | 25.6 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                                    | 23.5 ms: 1.03x faster                                                              |
| mako            | 5.67 ms                                                                    | 5.61 ms: 1.01x faster                                                              |
| genshi_xml      | 34.6 ms                                                                    | 35.2 ms: 1.02x slower                                                              |
| genshi_text     | 15.1 ms                                                                    | 15.5 ms: 1.03x slower                                                              |
| Geometric mean  | (ref)                                                                      | 1.00x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                      | 52.4 ms                                                                    | 44.8 ms: 1.17x faster                                                              |
| json                       | 3.10 ms                                                                    | 2.96 ms: 1.05x faster                                                              |
| pathlib                    | 33.1 ms                                                                    | 31.8 ms: 1.04x faster                                                              |
| gc_traversal               | 2.22 ms                                                                    | 2.14 ms: 1.04x faster                                                              |
| json_loads                 | 14.5 us                                                                    | 14.0 us: 1.04x faster                                                              |
| telco                      | 4.36 ms                                                                    | 4.22 ms: 1.03x faster                                                              |
| logging_silent             | 319 ns                                                                     | 311 ns: 1.03x faster                                                               |
| pidigits                   | 150 ms                                                                     | 146 ms: 1.03x faster                                                               |
| django_template            | 24.1 ms                                                                    | 23.5 ms: 1.03x faster                                                              |
| coverage                   | 51.8 ms                                                                    | 50.6 ms: 1.02x faster                                                              |
| python_startup             | 26.2 ms                                                                    | 25.6 ms: 1.02x faster                                                              |
| logging_format             | 6.95 us                                                                    | 6.81 us: 1.02x faster                                                              |
| spectral_norm              | 66.5 ms                                                                    | 65.2 ms: 1.02x faster                                                              |
| crypto_pyaes               | 47.2 ms                                                                    | 46.5 ms: 1.02x faster                                                              |
| generators                 | 19.8 ms                                                                    | 19.5 ms: 1.02x faster                                                              |
| scimark_lu                 | 60.6 ms                                                                    | 59.7 ms: 1.02x faster                                                              |
| subparsers                 | 17.2 ms                                                                    | 17.0 ms: 1.01x faster                                                              |
| pickle_pure_python         | 207 us                                                                     | 204 us: 1.01x faster                                                               |
| docutils                   | 1.69 sec                                                                   | 1.67 sec: 1.01x faster                                                             |
| xml_etree_iterparse        | 63.8 ms                                                                    | 63.1 ms: 1.01x faster                                                              |
| xml_etree_parse            | 88.8 ms                                                                    | 87.8 ms: 1.01x faster                                                              |
| raytrace                   | 177 ms                                                                     | 176 ms: 1.01x faster                                                               |
| logging_simple             | 6.38 us                                                                    | 6.32 us: 1.01x faster                                                              |
| dulwich_log                | 41.4 ms                                                                    | 41.0 ms: 1.01x faster                                                              |
| mako                       | 5.67 ms                                                                    | 5.61 ms: 1.01x faster                                                              |
| hexiom                     | 4.21 ms                                                                    | 4.17 ms: 1.01x faster                                                              |
| sympy_expand               | 296 ms                                                                     | 294 ms: 1.01x faster                                                               |
| sqlglot_v2_optimize        | 34.4 ms                                                                    | 34.1 ms: 1.01x faster                                                              |
| xml_etree_process          | 36.2 ms                                                                    | 35.9 ms: 1.01x faster                                                              |
| deltablue                  | 2.18 ms                                                                    | 2.17 ms: 1.01x faster                                                              |
| sqlglot_v2_normalize       | 70.1 ms                                                                    | 69.6 ms: 1.01x faster                                                              |
| richards                   | 27.3 ms                                                                    | 27.2 ms: 1.01x faster                                                              |
| regex_effbot               | 1.60 ms                                                                    | 1.59 ms: 1.00x faster                                                              |
| unpickle_pure_python       | 112 us                                                                     | 113 us: 1.01x slower                                                               |
| deepcopy_reduce            | 1.80 us                                                                    | 1.81 us: 1.01x slower                                                              |
| coroutines                 | 14.4 ms                                                                    | 14.5 ms: 1.01x slower                                                              |
| bpe_tokeniser              | 2.61 sec                                                                   | 2.62 sec: 1.01x slower                                                             |
| sqlglot_v2_parse           | 791 us                                                                     | 796 us: 1.01x slower                                                               |
| comprehensions             | 10.9 us                                                                    | 11.0 us: 1.01x slower                                                              |
| sqlite_synth               | 1.54 us                                                                    | 1.55 us: 1.01x slower                                                              |
| chaos                      | 40.5 ms                                                                    | 40.8 ms: 1.01x slower                                                              |
| sympy_integrate            | 12.7 ms                                                                    | 12.8 ms: 1.01x slower                                                              |
| scimark_sparse_mat_mult    | 2.29 ms                                                                    | 2.31 ms: 1.01x slower                                                              |
| scimark_sor                | 75.9 ms                                                                    | 76.7 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 338 ms                                                                     | 342 ms: 1.01x slower                                                               |
| create_gc_cycles           | 1.32 ms                                                                    | 1.34 ms: 1.01x slower                                                              |
| deepcopy_memo              | 18.0 us                                                                    | 18.3 us: 1.01x slower                                                              |
| async_generators           | 242 ms                                                                     | 246 ms: 1.02x slower                                                               |
| genshi_xml                 | 34.6 ms                                                                    | 35.2 ms: 1.02x slower                                                              |
| meteor_contest             | 73.5 ms                                                                    | 75.8 ms: 1.03x slower                                                              |
| genshi_text                | 15.1 ms                                                                    | 15.5 ms: 1.03x slower                                                              |
| asyncio_websockets         | 157 ms                                                                     | 163 ms: 1.03x slower                                                               |
| scimark_monte_carlo        | 39.8 ms                                                                    | 42.5 ms: 1.07x slower                                                              |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                       |

Benchmark hidden because not significant (39): python_startup_no_site, sphinx, tomli_loads, async_tree_memoization, k_core, pylint, sympy_str, shortest_path, async_tree_none, mdp, thrift, pycparser, async_tree_none_tg, connected_components, 2to3, sqlglot_v2_transpile, many_optionals, richards_super, go, sympy_sum, nqueens, pprint_safe_repr, fannkuch, deepcopy, async_tree_io_tg, async_tree_cpu_io_mixed, regex_dna, async_tree_memoization_tg, regex_compile, typing_runtime_protocols, pprint_pformat, scimark_fft, xml_etree_generate, regex_v8, float, json_dumps, html5lib, async_tree_io, pyflate

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 96.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown