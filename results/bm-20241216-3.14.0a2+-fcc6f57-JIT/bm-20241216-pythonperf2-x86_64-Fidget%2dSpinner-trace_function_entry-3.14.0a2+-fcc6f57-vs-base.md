# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.004x faster
- HPT reliability: 53.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 290 ms                                                                       | 289 ms: 1.00x faster                                                                   |
| docutils       | 2.99 sec                                                                     | 3.01 sec: 1.01x slower                                                                 |
| html5lib       | 71.5 ms                                                                      | 68.9 ms: 1.04x faster                                                                  |
| sphinx         | 1.16 sec                                                                     | 1.13 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_generators | 465 ms                                                                       | 429 ms: 1.09x faster                                                                   |
| async_tree_none  | 293 ms                                                                       | 296 ms: 1.01x slower                                                                   |
| async_tree_io    | 653 ms                                                                       | 662 ms: 1.01x slower                                                                   |
| coroutines       | 21.0 ms                                                                      | 21.3 ms: 1.01x slower                                                                  |
| async_tree_io_tg | 637 ms                                                                       | 654 ms: 1.03x slower                                                                   |
| Geometric mean   | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (6): async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                       | 251 ms: 1.00x slower                                                                   |
| float          | 72.8 ms                                                                      | 79.3 ms: 1.09x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.24 ms                                                                      | 3.26 ms: 1.01x slower                                                                  |
| regex_compile  | 138 ms                                                                       | 139 ms: 1.01x slower                                                                   |
| regex_dna      | 234 ms                                                                       | 247 ms: 1.06x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 202 us                                                                       | 198 us: 1.02x faster                                                                   |
| xml_etree_generate   | 80.7 ms                                                                      | 79.3 ms: 1.02x faster                                                                  |
| xml_etree_process    | 56.9 ms                                                                      | 56.4 ms: 1.01x faster                                                                  |
| xml_etree_parse      | 136 ms                                                                       | 135 ms: 1.01x faster                                                                   |
| json_dumps           | 11.2 ms                                                                      | 11.2 ms: 1.01x slower                                                                  |
| json_loads           | 25.1 us                                                                      | 25.4 us: 1.01x slower                                                                  |
| xml_etree_iterparse  | 94.0 ms                                                                      | 96.3 ms: 1.02x slower                                                                  |
| tomli_loads          | 2.05 sec                                                                     | 2.10 sec: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                                      | 16.1 ms: 1.01x slower                                                                  |
| python_startup_no_site | 9.02 ms                                                                      | 9.08 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 28.7 ms                                                                      | 25.5 ms: 1.13x faster                                                                  |
| genshi_xml      | 62.8 ms                                                                      | 57.7 ms: 1.09x faster                                                                  |
| django_template | 39.5 ms                                                                      | 38.5 ms: 1.03x faster                                                                  |
| mako            | 9.38 ms                                                                      | 9.47 ms: 1.01x slower                                                                  |
| Geometric mean  | (ref)                                                                        | 1.06x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators               | 39.8 ms                                                                      | 30.4 ms: 1.31x faster                                                                  |
| nqueens                  | 101 ms                                                                       | 89.7 ms: 1.13x faster                                                                  |
| genshi_text              | 28.7 ms                                                                      | 25.5 ms: 1.13x faster                                                                  |
| genshi_xml               | 62.8 ms                                                                      | 57.7 ms: 1.09x faster                                                                  |
| async_generators         | 465 ms                                                                       | 429 ms: 1.09x faster                                                                   |
| dulwich_log              | 67.7 ms                                                                      | 62.9 ms: 1.08x faster                                                                  |
| raytrace                 | 338 ms                                                                       | 315 ms: 1.08x faster                                                                   |
| deepcopy                 | 310 us                                                                       | 291 us: 1.07x faster                                                                   |
| spectral_norm            | 93.6 ms                                                                      | 88.9 ms: 1.05x faster                                                                  |
| hexiom                   | 7.08 ms                                                                      | 6.77 ms: 1.05x faster                                                                  |
| logging_format           | 7.23 us                                                                      | 6.96 us: 1.04x faster                                                                  |
| html5lib                 | 71.5 ms                                                                      | 68.9 ms: 1.04x faster                                                                  |
| mdp                      | 2.60 sec                                                                     | 2.51 sec: 1.04x faster                                                                 |
| logging_simple           | 6.60 us                                                                      | 6.39 us: 1.03x faster                                                                  |
| pyflate                  | 451 ms                                                                       | 437 ms: 1.03x faster                                                                   |
| scimark_sparse_mat_mult  | 5.02 ms                                                                      | 4.89 ms: 1.03x faster                                                                  |
| django_template          | 39.5 ms                                                                      | 38.5 ms: 1.03x faster                                                                  |
| go                       | 145 ms                                                                       | 141 ms: 1.03x faster                                                                   |
| sphinx                   | 1.16 sec                                                                     | 1.13 sec: 1.02x faster                                                                 |
| unpickle_pure_python     | 202 us                                                                       | 198 us: 1.02x faster                                                                   |
| xml_etree_generate       | 80.7 ms                                                                      | 79.3 ms: 1.02x faster                                                                  |
| scimark_fft              | 305 ms                                                                       | 300 ms: 1.02x faster                                                                   |
| fannkuch                 | 379 ms                                                                       | 373 ms: 1.02x faster                                                                   |
| sympy_sum                | 158 ms                                                                       | 156 ms: 1.01x faster                                                                   |
| scimark_lu               | 98.9 ms                                                                      | 97.9 ms: 1.01x faster                                                                  |
| sympy_str                | 305 ms                                                                       | 302 ms: 1.01x faster                                                                   |
| connected_components     | 404 ms                                                                       | 401 ms: 1.01x faster                                                                   |
| xml_etree_process        | 56.9 ms                                                                      | 56.4 ms: 1.01x faster                                                                  |
| xml_etree_parse          | 136 ms                                                                       | 135 ms: 1.01x faster                                                                   |
| sympy_integrate          | 24.0 ms                                                                      | 23.8 ms: 1.01x faster                                                                  |
| deepcopy_reduce          | 2.97 us                                                                      | 2.95 us: 1.01x faster                                                                  |
| pathlib                  | 16.7 ms                                                                      | 16.6 ms: 1.00x faster                                                                  |
| 2to3                     | 290 ms                                                                       | 289 ms: 1.00x faster                                                                   |
| pidigits                 | 251 ms                                                                       | 251 ms: 1.00x slower                                                                   |
| logging_silent           | 101 ns                                                                       | 101 ns: 1.00x slower                                                                   |
| shortest_path            | 437 ms                                                                       | 439 ms: 1.01x slower                                                                   |
| json_dumps               | 11.2 ms                                                                      | 11.2 ms: 1.01x slower                                                                  |
| python_startup           | 16.0 ms                                                                      | 16.1 ms: 1.01x slower                                                                  |
| scimark_monte_carlo      | 62.9 ms                                                                      | 63.3 ms: 1.01x slower                                                                  |
| python_startup_no_site   | 9.02 ms                                                                      | 9.08 ms: 1.01x slower                                                                  |
| regex_effbot             | 3.24 ms                                                                      | 3.26 ms: 1.01x slower                                                                  |
| sqlalchemy_declarative   | 143 ms                                                                       | 144 ms: 1.01x slower                                                                   |
| docutils                 | 2.99 sec                                                                     | 3.01 sec: 1.01x slower                                                                 |
| many_optionals           | 1.06 ms                                                                      | 1.07 ms: 1.01x slower                                                                  |
| json_loads               | 25.1 us                                                                      | 25.4 us: 1.01x slower                                                                  |
| mako                     | 9.38 ms                                                                      | 9.47 ms: 1.01x slower                                                                  |
| bpe_tokeniser            | 4.65 sec                                                                     | 4.69 sec: 1.01x slower                                                                 |
| create_gc_cycles         | 2.69 ms                                                                      | 2.72 ms: 1.01x slower                                                                  |
| regex_compile            | 138 ms                                                                       | 139 ms: 1.01x slower                                                                   |
| comprehensions           | 19.0 us                                                                      | 19.3 us: 1.01x slower                                                                  |
| async_tree_none          | 293 ms                                                                       | 296 ms: 1.01x slower                                                                   |
| async_tree_io            | 653 ms                                                                       | 662 ms: 1.01x slower                                                                   |
| pprint_safe_repr         | 797 ms                                                                       | 808 ms: 1.01x slower                                                                   |
| coroutines               | 21.0 ms                                                                      | 21.3 ms: 1.01x slower                                                                  |
| sqlalchemy_imperative    | 17.9 ms                                                                      | 18.2 ms: 1.01x slower                                                                  |
| meteor_contest           | 130 ms                                                                       | 132 ms: 1.02x slower                                                                   |
| thrift                   | 883 us                                                                       | 898 us: 1.02x slower                                                                   |
| typing_runtime_protocols | 183 us                                                                       | 186 us: 1.02x slower                                                                   |
| sqlglot_optimize         | 61.3 ms                                                                      | 62.5 ms: 1.02x slower                                                                  |
| xml_etree_iterparse      | 94.0 ms                                                                      | 96.3 ms: 1.02x slower                                                                  |
| tomli_loads              | 2.05 sec                                                                     | 2.10 sec: 1.02x slower                                                                 |
| async_tree_io_tg         | 637 ms                                                                       | 654 ms: 1.03x slower                                                                   |
| gc_traversal             | 6.31 ms                                                                      | 6.53 ms: 1.04x slower                                                                  |
| sqlglot_transpile        | 1.82 ms                                                                      | 1.90 ms: 1.04x slower                                                                  |
| regex_dna                | 234 ms                                                                       | 247 ms: 1.06x slower                                                                   |
| sqlglot_parse            | 1.42 ms                                                                      | 1.49 ms: 1.06x slower                                                                  |
| pycparser                | 1.22 sec                                                                     | 1.30 sec: 1.06x slower                                                                 |
| richards_super           | 54.8 ms                                                                      | 59.4 ms: 1.08x slower                                                                  |
| float                    | 72.8 ms                                                                      | 79.3 ms: 1.09x slower                                                                  |
| richards                 | 48.2 ms                                                                      | 52.6 ms: 1.09x slower                                                                  |
| scimark_sor              | 104 ms                                                                       | 115 ms: 1.11x slower                                                                   |
| deltablue                | 3.31 ms                                                                      | 3.70 ms: 1.12x slower                                                                  |
| Geometric mean           | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (26): bench_mp_pool, pylint, bench_thread_pool, k_core, coverage, sqlglot_normalize, pickle_pure_python, telco, async_tree_none_tg, sqlite_synth, sympy_expand, crypto_pyaes, pprint_pformat, djangocms, asyncio_websockets, subparsers, chaos, async_tree_memoization_tg, async_tree_memoization, json, deepcopy_memo, nbody, async_tree_cpu_io_mixed_tg, mypy2, async_tree_cpu_io_mixed, regex_v8

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 53.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x