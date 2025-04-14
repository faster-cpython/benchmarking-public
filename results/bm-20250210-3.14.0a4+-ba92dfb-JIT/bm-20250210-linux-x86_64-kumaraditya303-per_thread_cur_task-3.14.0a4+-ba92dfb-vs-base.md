# Results vs. base

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.004x faster
- HPT reliability: 98.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                                          |
| docutils       | 2.69 sec                                                               | 2.66 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 269 ms                                                                 | 264 ms: 1.02x faster                                                          |
| coroutines              | 23.0 ms                                                                | 22.6 ms: 1.02x faster                                                         |
| async_tree_io           | 627 ms                                                                 | 617 ms: 1.02x faster                                                          |
| async_tree_none_tg      | 260 ms                                                                 | 256 ms: 1.02x faster                                                          |
| async_tree_memoization  | 328 ms                                                                 | 324 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed | 494 ms                                                                 | 497 ms: 1.01x slower                                                          |
| async_generators        | 411 ms                                                                 | 416 ms: 1.01x slower                                                          |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 96.6 ms                                                                | 94.5 ms: 1.02x faster                                                         |
| float          | 69.9 ms                                                                | 70.8 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 125 ms: 1.02x faster                                                          |
| regex_dna      | 209 ms                                                                 | 212 ms: 1.01x slower                                                          |
| regex_effbot   | 3.09 ms                                                                | 3.23 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_process    | 56.1 ms                                                                | 55.1 ms: 1.02x faster                                                         |
| unpickle_pure_python | 201 us                                                                 | 198 us: 1.01x faster                                                          |
| pickle_pure_python   | 318 us                                                                 | 315 us: 1.01x faster                                                          |
| xml_etree_generate   | 79.1 ms                                                                | 78.5 ms: 1.01x faster                                                         |
| xml_etree_parse      | 137 ms                                                                 | 138 ms: 1.01x slower                                                          |
| xml_etree_iterparse  | 95.0 ms                                                                | 96.0 ms: 1.01x slower                                                         |
| json_dumps           | 11.8 ms                                                                | 12.0 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                         |
| python_startup_no_site | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text    | 22.3 ms                                                                | 21.8 ms: 1.02x faster                                                         |
| mako           | 9.83 ms                                                                | 10.2 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| logging_silent           | 110 ns                                                                 | 106 ns: 1.04x faster                                                          |
| pycparser                | 1.16 sec                                                               | 1.11 sec: 1.04x faster                                                        |
| richards                 | 45.5 ms                                                                | 44.1 ms: 1.03x faster                                                         |
| spectral_norm            | 98.5 ms                                                                | 95.7 ms: 1.03x faster                                                         |
| richards_super           | 51.6 ms                                                                | 50.3 ms: 1.03x faster                                                         |
| logging_format           | 6.24 us                                                                | 6.10 us: 1.02x faster                                                         |
| nbody                    | 96.6 ms                                                                | 94.5 ms: 1.02x faster                                                         |
| logging_simple           | 5.63 us                                                                | 5.51 us: 1.02x faster                                                         |
| scimark_sparse_mat_mult  | 4.57 ms                                                                | 4.48 ms: 1.02x faster                                                         |
| genshi_text              | 22.3 ms                                                                | 21.8 ms: 1.02x faster                                                         |
| async_tree_none          | 269 ms                                                                 | 264 ms: 1.02x faster                                                          |
| xml_etree_process        | 56.1 ms                                                                | 55.1 ms: 1.02x faster                                                         |
| regex_compile            | 127 ms                                                                 | 125 ms: 1.02x faster                                                          |
| coroutines               | 23.0 ms                                                                | 22.6 ms: 1.02x faster                                                         |
| go                       | 131 ms                                                                 | 129 ms: 1.02x faster                                                          |
| async_tree_io            | 627 ms                                                                 | 617 ms: 1.02x faster                                                          |
| raytrace                 | 281 ms                                                                 | 276 ms: 1.02x faster                                                          |
| async_tree_none_tg       | 260 ms                                                                 | 256 ms: 1.02x faster                                                          |
| deltablue                | 3.44 ms                                                                | 3.38 ms: 1.02x faster                                                         |
| unpickle_pure_python     | 201 us                                                                 | 198 us: 1.01x faster                                                          |
| deepcopy                 | 261 us                                                                 | 257 us: 1.01x faster                                                          |
| hexiom                   | 6.95 ms                                                                | 6.86 ms: 1.01x faster                                                         |
| pathlib                  | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                                         |
| nqueens                  | 89.4 ms                                                                | 88.2 ms: 1.01x faster                                                         |
| sqlalchemy_imperative    | 16.9 ms                                                                | 16.7 ms: 1.01x faster                                                         |
| async_tree_memoization   | 328 ms                                                                 | 324 ms: 1.01x faster                                                          |
| docutils                 | 2.69 sec                                                               | 2.66 sec: 1.01x faster                                                        |
| meteor_contest           | 109 ms                                                                 | 107 ms: 1.01x faster                                                          |
| scimark_lu               | 115 ms                                                                 | 114 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 107 ms                                                                 | 106 ms: 1.01x faster                                                          |
| subparsers               | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                         |
| typing_runtime_protocols | 163 us                                                                 | 162 us: 1.01x faster                                                          |
| pickle_pure_python       | 318 us                                                                 | 315 us: 1.01x faster                                                          |
| sympy_integrate          | 20.3 ms                                                                | 20.1 ms: 1.01x faster                                                         |
| sympy_expand             | 472 ms                                                                 | 468 ms: 1.01x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                                | 2.66 us: 1.01x faster                                                         |
| xml_etree_generate       | 79.1 ms                                                                | 78.5 ms: 1.01x faster                                                         |
| coverage                 | 90.2 ms                                                                | 89.5 ms: 1.01x faster                                                         |
| chaos                    | 58.8 ms                                                                | 58.4 ms: 1.01x faster                                                         |
| scimark_sor              | 119 ms                                                                 | 119 ms: 1.01x faster                                                          |
| scimark_fft              | 315 ms                                                                 | 313 ms: 1.01x faster                                                          |
| thrift                   | 772 us                                                                 | 768 us: 1.01x faster                                                          |
| connected_components     | 445 ms                                                                 | 443 ms: 1.00x faster                                                          |
| sqlglot_optimize         | 53.7 ms                                                                | 53.5 ms: 1.00x faster                                                         |
| dulwich_log              | 66.2 ms                                                                | 66.0 ms: 1.00x faster                                                         |
| 2to3                     | 258 ms                                                                 | 257 ms: 1.00x faster                                                          |
| bench_thread_pool        | 888 us                                                                 | 885 us: 1.00x faster                                                          |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                         |
| python_startup_no_site   | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                                         |
| generators               | 28.3 ms                                                                | 28.4 ms: 1.00x slower                                                         |
| sqlite_synth             | 2.73 us                                                                | 2.74 us: 1.00x slower                                                         |
| pyflate                  | 444 ms                                                                 | 446 ms: 1.01x slower                                                          |
| crypto_pyaes             | 69.6 ms                                                                | 70.0 ms: 1.01x slower                                                         |
| xml_etree_parse          | 137 ms                                                                 | 138 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed  | 494 ms                                                                 | 497 ms: 1.01x slower                                                          |
| json                     | 5.18 ms                                                                | 5.22 ms: 1.01x slower                                                         |
| async_generators         | 411 ms                                                                 | 416 ms: 1.01x slower                                                          |
| xml_etree_iterparse      | 95.0 ms                                                                | 96.0 ms: 1.01x slower                                                         |
| float                    | 69.9 ms                                                                | 70.8 ms: 1.01x slower                                                         |
| create_gc_cycles         | 2.45 ms                                                                | 2.48 ms: 1.01x slower                                                         |
| regex_dna                | 209 ms                                                                 | 212 ms: 1.01x slower                                                          |
| json_dumps               | 11.8 ms                                                                | 12.0 ms: 1.02x slower                                                         |
| gc_traversal             | 4.63 ms                                                                | 4.72 ms: 1.02x slower                                                         |
| mako                     | 9.83 ms                                                                | 10.2 ms: 1.04x slower                                                         |
| regex_effbot             | 3.09 ms                                                                | 3.23 ms: 1.04x slower                                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (31): async_tree_io_tg, sphinx, tomli_loads, telco, comprehensions, many_optionals, sympy_str, regex_v8, html5lib, asyncio_websockets, sqlglot_transpile, deepcopy_memo, mdp, pylint, scimark_monte_carlo, shortest_path, pidigits, fannkuch, bpe_tokeniser, pprint_safe_repr, sqlalchemy_declarative, genshi_xml, k_core, sympy_sum, sqlglot_parse, bench_mp_pool, django_template, pprint_pformat, async_tree_cpu_io_mixed_tg, json_loads, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 98.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x