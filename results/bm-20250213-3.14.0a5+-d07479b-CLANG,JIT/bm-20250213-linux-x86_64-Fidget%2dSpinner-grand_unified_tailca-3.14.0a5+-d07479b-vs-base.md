# Results vs. base

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: linux-x86_64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.001x slower
- HPT reliability: 97.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                                             |
| docutils       | 2.62 sec                                                               | 2.64 sec: 1.01x slower                                                           |
| html5lib       | 57.8 ms                                                                | 58.4 ms: 1.01x slower                                                            |
| sphinx         | 987 ms                                                                 | 999 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators | 403 ms                                                                 | 395 ms: 1.02x faster                                                             |
| coroutines       | 22.1 ms                                                                | 22.4 ms: 1.01x slower                                                            |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 92.7 ms                                                                | 86.9 ms: 1.07x faster                                                            |
| pidigits       | 212 ms                                                                 | 222 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 24.6 ms                                                                | 24.3 ms: 1.01x faster                                                            |
| regex_compile  | 123 ms                                                                 | 124 ms: 1.01x slower                                                             |
| regex_effbot   | 3.11 ms                                                                | 3.15 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.3 ms                                                                | 12.2 ms: 1.01x faster                                                            |
| xml_etree_process    | 55.3 ms                                                                | 55.7 ms: 1.01x slower                                                            |
| xml_etree_generate   | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                                            |
| pickle_pure_python   | 309 us                                                                 | 312 us: 1.01x slower                                                             |
| json_loads           | 30.2 us                                                                | 30.6 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.01x slower                                                             |
| unpickle_pure_python | 208 us                                                                 | 211 us: 1.02x slower                                                             |
| xml_etree_parse      | 155 ms                                                                 | 158 ms: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                                | 7.01 ms: 1.00x slower                                                            |
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                            |
| genshi_text     | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| genshi_xml      | 48.0 ms                                                                | 47.6 ms: 1.01x faster                                                            |
| django_template | 30.6 ms                                                                | 30.4 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody                    | 92.7 ms                                                                | 86.9 ms: 1.07x faster                                                            |
| logging_silent           | 91.0 ns                                                                | 86.5 ns: 1.05x faster                                                            |
| deltablue                | 3.25 ms                                                                | 3.14 ms: 1.04x faster                                                            |
| comprehensions           | 17.2 us                                                                | 16.8 us: 1.03x faster                                                            |
| async_generators         | 403 ms                                                                 | 395 ms: 1.02x faster                                                             |
| logging_simple           | 5.39 us                                                                | 5.29 us: 1.02x faster                                                            |
| coverage                 | 80.8 ms                                                                | 79.6 ms: 1.01x faster                                                            |
| pathlib                  | 14.7 ms                                                                | 14.5 ms: 1.01x faster                                                            |
| mako                     | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                            |
| logging_format           | 5.94 us                                                                | 5.87 us: 1.01x faster                                                            |
| hexiom                   | 6.51 ms                                                                | 6.43 ms: 1.01x faster                                                            |
| genshi_text              | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| regex_v8                 | 24.6 ms                                                                | 24.3 ms: 1.01x faster                                                            |
| deepcopy_reduce          | 2.50 us                                                                | 2.47 us: 1.01x faster                                                            |
| genshi_xml               | 48.0 ms                                                                | 47.6 ms: 1.01x faster                                                            |
| django_template          | 30.6 ms                                                                | 30.4 ms: 1.01x faster                                                            |
| go                       | 121 ms                                                                 | 120 ms: 1.01x faster                                                             |
| richards_super           | 47.1 ms                                                                | 46.8 ms: 1.01x faster                                                            |
| chaos                    | 54.3 ms                                                                | 53.9 ms: 1.01x faster                                                            |
| generators               | 27.3 ms                                                                | 27.2 ms: 1.01x faster                                                            |
| spectral_norm            | 81.9 ms                                                                | 81.4 ms: 1.01x faster                                                            |
| richards                 | 40.2 ms                                                                | 40.0 ms: 1.01x faster                                                            |
| json_dumps               | 12.3 ms                                                                | 12.2 ms: 1.01x faster                                                            |
| sqlglot_normalize        | 104 ms                                                                 | 103 ms: 1.00x faster                                                             |
| raytrace                 | 259 ms                                                                 | 258 ms: 1.00x faster                                                             |
| sqlglot_optimize         | 53.1 ms                                                                | 52.9 ms: 1.00x faster                                                            |
| bench_thread_pool        | 839 us                                                                 | 837 us: 1.00x faster                                                             |
| python_startup_no_site   | 7.00 ms                                                                | 7.01 ms: 1.00x slower                                                            |
| python_startup           | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                            |
| 2to3                     | 253 ms                                                                 | 254 ms: 1.00x slower                                                             |
| create_gc_cycles         | 2.53 ms                                                                | 2.54 ms: 1.00x slower                                                            |
| many_optionals           | 930 us                                                                 | 934 us: 1.00x slower                                                             |
| sympy_expand             | 454 ms                                                                 | 456 ms: 1.01x slower                                                             |
| xml_etree_process        | 55.3 ms                                                                | 55.7 ms: 1.01x slower                                                            |
| sqlalchemy_imperative    | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                            |
| mdp                      | 2.88 sec                                                               | 2.90 sec: 1.01x slower                                                           |
| sympy_str                | 265 ms                                                                 | 266 ms: 1.01x slower                                                             |
| sqlite_synth             | 2.63 us                                                                | 2.65 us: 1.01x slower                                                            |
| subparsers               | 20.2 ms                                                                | 20.3 ms: 1.01x slower                                                            |
| thrift                   | 736 us                                                                 | 742 us: 1.01x slower                                                             |
| docutils                 | 2.62 sec                                                               | 2.64 sec: 1.01x slower                                                           |
| sympy_sum                | 146 ms                                                                 | 147 ms: 1.01x slower                                                             |
| xml_etree_generate       | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                                            |
| scimark_fft              | 284 ms                                                                 | 286 ms: 1.01x slower                                                             |
| connected_components     | 457 ms                                                                 | 461 ms: 1.01x slower                                                             |
| shortest_path            | 488 ms                                                                 | 493 ms: 1.01x slower                                                             |
| regex_compile            | 123 ms                                                                 | 124 ms: 1.01x slower                                                             |
| scimark_sor              | 106 ms                                                                 | 107 ms: 1.01x slower                                                             |
| pickle_pure_python       | 309 us                                                                 | 312 us: 1.01x slower                                                             |
| pyflate                  | 403 ms                                                                 | 407 ms: 1.01x slower                                                             |
| html5lib                 | 57.8 ms                                                                | 58.4 ms: 1.01x slower                                                            |
| json_loads               | 30.2 us                                                                | 30.6 us: 1.01x slower                                                            |
| coroutines               | 22.1 ms                                                                | 22.4 ms: 1.01x slower                                                            |
| fannkuch                 | 395 ms                                                                 | 400 ms: 1.01x slower                                                             |
| sphinx                   | 987 ms                                                                 | 999 ms: 1.01x slower                                                             |
| xml_etree_iterparse      | 101 ms                                                                 | 102 ms: 1.01x slower                                                             |
| regex_effbot             | 3.11 ms                                                                | 3.15 ms: 1.01x slower                                                            |
| pprint_pformat           | 1.54 sec                                                               | 1.57 sec: 1.02x slower                                                           |
| unpickle_pure_python     | 208 us                                                                 | 211 us: 1.02x slower                                                             |
| xml_etree_parse          | 155 ms                                                                 | 158 ms: 1.02x slower                                                             |
| sqlglot_transpile        | 1.55 ms                                                                | 1.58 ms: 1.02x slower                                                            |
| typing_runtime_protocols | 153 us                                                                 | 155 us: 1.02x slower                                                             |
| scimark_monte_carlo      | 58.7 ms                                                                | 60.2 ms: 1.02x slower                                                            |
| deepcopy_memo            | 28.2 us                                                                | 28.9 us: 1.03x slower                                                            |
| gc_traversal             | 4.83 ms                                                                | 4.98 ms: 1.03x slower                                                            |
| pidigits                 | 212 ms                                                                 | 222 ms: 1.05x slower                                                             |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (30): async_tree_none, async_tree_none_tg, crypto_pyaes, pycparser, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, regex_dna, async_tree_cpu_io_mixed, deepcopy, tomli_loads, async_tree_memoization, pylint, dulwich_log, bench_mp_pool, sqlalchemy_declarative, asyncio_websockets, sqlglot_parse, sympy_integrate, nqueens, scimark_sparse_mat_mult, scimark_lu, meteor_contest, bpe_tokeniser, pprint_safe_repr, async_tree_io, float, json, k_core, telco, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 97.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x