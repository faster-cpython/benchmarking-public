# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.004x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                                   | 1.66 sec: 1.00x slower                                                             |
| html5lib       | 38.5 ms                                                                    | 38.8 ms: 1.01x slower                                                              |
| sphinx         | 634 ms                                                                     | 643 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| coroutines                 | 14.5 ms                                                                    | 14.6 ms: 1.01x slower                                                              |
| async_tree_memoization     | 204 ms                                                                     | 206 ms: 1.01x slower                                                               |
| async_tree_io_tg           | 387 ms                                                                     | 397 ms: 1.03x slower                                                               |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                     | 343 ms: 1.03x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (7): async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 54.1 ms                                                                    | 43.6 ms: 1.24x faster                                                              |
| pidigits       | 145 ms                                                                     | 147 ms: 1.01x slower                                                               |
| float          | 44.3 ms                                                                    | 45.1 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.07x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                                    | 1.52 ms: 1.05x faster                                                              |
| regex_dna      | 118 ms                                                                     | 120 ms: 1.01x slower                                                               |
| regex_compile  | 78.2 ms                                                                    | 79.6 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|---------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads          | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                              |
| pickle_pure_python  | 204 us                                                                     | 206 us: 1.01x slower                                                               |
| xml_etree_process   | 34.9 ms                                                                    | 35.5 ms: 1.02x slower                                                              |
| xml_etree_iterparse | 62.9 ms                                                                    | 64.4 ms: 1.02x slower                                                              |
| json_dumps          | 5.36 ms                                                                    | 5.50 ms: 1.03x slower                                                              |
| tomli_loads         | 1.09 sec                                                                   | 1.12 sec: 1.03x slower                                                             |
| xml_etree_parse     | 85.8 ms                                                                    | 88.4 ms: 1.03x slower                                                              |
| Geometric mean      | (ref)                                                                      | 1.02x slower                                                                       |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.2 ms                                                                    | 26.5 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text    | 15.3 ms                                                                    | 15.5 ms: 1.02x slower                                                              |
| genshi_xml     | 34.1 ms                                                                    | 34.8 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                      | 54.1 ms                                                                    | 43.6 ms: 1.24x faster                                                              |
| fannkuch                   | 217 ms                                                                     | 206 ms: 1.05x faster                                                               |
| regex_effbot               | 1.58 ms                                                                    | 1.52 ms: 1.05x faster                                                              |
| nqueens                    | 61.2 ms                                                                    | 58.9 ms: 1.04x faster                                                              |
| pprint_pformat             | 869 ms                                                                     | 845 ms: 1.03x faster                                                               |
| richards_super             | 31.7 ms                                                                    | 30.9 ms: 1.02x faster                                                              |
| pprint_safe_repr           | 429 ms                                                                     | 421 ms: 1.02x faster                                                               |
| pyflate                    | 265 ms                                                                     | 260 ms: 1.02x faster                                                               |
| thrift                     | 500 us                                                                     | 493 us: 1.01x faster                                                               |
| pathlib                    | 29.8 ms                                                                    | 29.5 ms: 1.01x faster                                                              |
| bpe_tokeniser              | 2.52 sec                                                                   | 2.51 sec: 1.00x faster                                                             |
| telco                      | 4.03 ms                                                                    | 4.01 ms: 1.00x faster                                                              |
| docutils                   | 1.66 sec                                                                   | 1.66 sec: 1.00x slower                                                             |
| sympy_expand               | 295 ms                                                                     | 296 ms: 1.01x slower                                                               |
| sqlglot_v2_normalize       | 71.3 ms                                                                    | 71.7 ms: 1.01x slower                                                              |
| html5lib                   | 38.5 ms                                                                    | 38.8 ms: 1.01x slower                                                              |
| json_loads                 | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                              |
| coroutines                 | 14.5 ms                                                                    | 14.6 ms: 1.01x slower                                                              |
| gc_traversal               | 2.09 ms                                                                    | 2.11 ms: 1.01x slower                                                              |
| create_gc_cycles           | 1.28 ms                                                                    | 1.30 ms: 1.01x slower                                                              |
| mdp                        | 802 ms                                                                     | 810 ms: 1.01x slower                                                               |
| sqlglot_v2_optimize        | 34.7 ms                                                                    | 35.0 ms: 1.01x slower                                                              |
| async_tree_memoization     | 204 ms                                                                     | 206 ms: 1.01x slower                                                               |
| dulwich_log                | 40.2 ms                                                                    | 40.6 ms: 1.01x slower                                                              |
| sympy_str                  | 169 ms                                                                     | 171 ms: 1.01x slower                                                               |
| python_startup             | 26.2 ms                                                                    | 26.5 ms: 1.01x slower                                                              |
| sympy_integrate            | 12.6 ms                                                                    | 12.8 ms: 1.01x slower                                                              |
| pidigits                   | 145 ms                                                                     | 147 ms: 1.01x slower                                                               |
| sympy_sum                  | 86.9 ms                                                                    | 87.9 ms: 1.01x slower                                                              |
| shortest_path              | 352 ms                                                                     | 356 ms: 1.01x slower                                                               |
| pickle_pure_python         | 204 us                                                                     | 206 us: 1.01x slower                                                               |
| chaos                      | 40.2 ms                                                                    | 40.8 ms: 1.01x slower                                                              |
| sphinx                     | 634 ms                                                                     | 643 ms: 1.01x slower                                                               |
| deepcopy                   | 173 us                                                                     | 175 us: 1.01x slower                                                               |
| regex_dna                  | 118 ms                                                                     | 120 ms: 1.01x slower                                                               |
| logging_format             | 6.42 us                                                                    | 6.51 us: 1.01x slower                                                              |
| scimark_sparse_mat_mult    | 2.24 ms                                                                    | 2.28 ms: 1.02x slower                                                              |
| float                      | 44.3 ms                                                                    | 45.1 ms: 1.02x slower                                                              |
| raytrace                   | 174 ms                                                                     | 176 ms: 1.02x slower                                                               |
| genshi_text                | 15.3 ms                                                                    | 15.5 ms: 1.02x slower                                                              |
| comprehensions             | 10.4 us                                                                    | 10.6 us: 1.02x slower                                                              |
| regex_compile              | 78.2 ms                                                                    | 79.6 ms: 1.02x slower                                                              |
| xml_etree_process          | 34.9 ms                                                                    | 35.5 ms: 1.02x slower                                                              |
| genshi_xml                 | 34.1 ms                                                                    | 34.8 ms: 1.02x slower                                                              |
| meteor_contest             | 71.8 ms                                                                    | 73.4 ms: 1.02x slower                                                              |
| xml_etree_iterparse        | 62.9 ms                                                                    | 64.4 ms: 1.02x slower                                                              |
| json_dumps                 | 5.36 ms                                                                    | 5.50 ms: 1.03x slower                                                              |
| async_tree_io_tg           | 387 ms                                                                     | 397 ms: 1.03x slower                                                               |
| go                         | 76.3 ms                                                                    | 78.4 ms: 1.03x slower                                                              |
| hexiom                     | 3.96 ms                                                                    | 4.07 ms: 1.03x slower                                                              |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                     | 343 ms: 1.03x slower                                                               |
| typing_runtime_protocols   | 103 us                                                                     | 106 us: 1.03x slower                                                               |
| coverage                   | 49.1 ms                                                                    | 50.5 ms: 1.03x slower                                                              |
| tomli_loads                | 1.09 sec                                                                   | 1.12 sec: 1.03x slower                                                             |
| xml_etree_parse            | 85.8 ms                                                                    | 88.4 ms: 1.03x slower                                                              |
| deepcopy_reduce            | 1.83 us                                                                    | 1.89 us: 1.03x slower                                                              |
| scimark_monte_carlo        | 40.0 ms                                                                    | 41.4 ms: 1.04x slower                                                              |
| spectral_norm              | 65.1 ms                                                                    | 67.5 ms: 1.04x slower                                                              |
| generators                 | 19.5 ms                                                                    | 20.2 ms: 1.04x slower                                                              |
| deltablue                  | 2.17 ms                                                                    | 2.25 ms: 1.04x slower                                                              |
| scimark_lu                 | 57.6 ms                                                                    | 60.1 ms: 1.04x slower                                                              |
| logging_silent             | 53.8 ns                                                                    | 56.7 ns: 1.05x slower                                                              |
| scimark_sor                | 74.8 ms                                                                    | 79.3 ms: 1.06x slower                                                              |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (28): regex_v8, python_startup_no_site, richards, crypto_pyaes, async_generators, many_optionals, django_template, subparsers, k_core, scimark_fft, sqlite_synth, unpickle_pure_python, sqlglot_v2_parse, async_tree_memoization_tg, connected_components, async_tree_cpu_io_mixed, logging_simple, deepcopy_memo, asyncio_websockets, async_tree_none, json, async_tree_io, pylint, sqlglot_v2_transpile, mako, 2to3, xml_etree_generate, async_tree_none_tg
Ignored benchmarks (1) of results/bm-20250821-3.15.0a0-a8d9d94-JIT/bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94.json: pycparser

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown