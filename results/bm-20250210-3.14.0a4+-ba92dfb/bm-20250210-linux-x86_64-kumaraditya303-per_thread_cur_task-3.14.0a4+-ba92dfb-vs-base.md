# Results vs. base

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.002x faster
- HPT reliability: 53.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                          |
| docutils       | 2.60 sec                                                               | 2.58 sec: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg     | 257 ms                                                                 | 249 ms: 1.03x faster                                                          |
| async_tree_io          | 619 ms                                                                 | 605 ms: 1.02x faster                                                          |
| async_tree_none        | 264 ms                                                                 | 259 ms: 1.02x faster                                                          |
| coroutines             | 23.3 ms                                                                | 23.0 ms: 1.02x faster                                                         |
| async_tree_memoization | 323 ms                                                                 | 318 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                          |
| nbody          | 92.6 ms                                                                | 94.3 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.40 ms                                                                | 3.24 ms: 1.05x faster                                                         |
| regex_v8       | 25.1 ms                                                                | 24.3 ms: 1.03x faster                                                         |
| regex_dna      | 215 ms                                                                 | 216 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| unpickle_pure_python | 217 us                                                                 | 218 us: 1.00x slower                                                          |
| xml_etree_generate   | 83.1 ms                                                                | 83.6 ms: 1.01x slower                                                         |
| xml_etree_process    | 58.0 ms                                                                | 58.6 ms: 1.01x slower                                                         |
| tomli_loads          | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                         |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 10.6 ms: 1.03x faster                                                         |
| genshi_text    | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                                         |
| genshi_xml     | 47.9 ms                                                                | 47.8 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot             | 3.40 ms                                                                | 3.24 ms: 1.05x faster                                                         |
| pyflate                  | 461 ms                                                                 | 443 ms: 1.04x faster                                                          |
| gc_traversal             | 4.95 ms                                                                | 4.78 ms: 1.04x faster                                                         |
| regex_v8                 | 25.1 ms                                                                | 24.3 ms: 1.03x faster                                                         |
| pycparser                | 1.16 sec                                                               | 1.13 sec: 1.03x faster                                                        |
| mako                     | 11.0 ms                                                                | 10.6 ms: 1.03x faster                                                         |
| async_tree_none_tg       | 257 ms                                                                 | 249 ms: 1.03x faster                                                          |
| telco                    | 7.94 ms                                                                | 7.76 ms: 1.02x faster                                                         |
| async_tree_io            | 619 ms                                                                 | 605 ms: 1.02x faster                                                          |
| async_tree_none          | 264 ms                                                                 | 259 ms: 1.02x faster                                                          |
| generators               | 28.1 ms                                                                | 27.5 ms: 1.02x faster                                                         |
| logging_format           | 6.11 us                                                                | 5.99 us: 1.02x faster                                                         |
| coroutines               | 23.3 ms                                                                | 23.0 ms: 1.02x faster                                                         |
| async_tree_memoization   | 323 ms                                                                 | 318 ms: 1.02x faster                                                          |
| logging_simple           | 5.48 us                                                                | 5.42 us: 1.01x faster                                                         |
| logging_silent           | 107 ns                                                                 | 105 ns: 1.01x faster                                                          |
| deltablue                | 3.19 ms                                                                | 3.15 ms: 1.01x faster                                                         |
| meteor_contest           | 105 ms                                                                 | 104 ms: 1.01x faster                                                          |
| json_dumps               | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                         |
| comprehensions           | 16.3 us                                                                | 16.2 us: 1.01x faster                                                         |
| mdp                      | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                        |
| spectral_norm            | 97.8 ms                                                                | 97.1 ms: 1.01x faster                                                         |
| docutils                 | 2.60 sec                                                               | 2.58 sec: 1.01x faster                                                        |
| genshi_text              | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                                         |
| create_gc_cycles         | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                                         |
| python_startup_no_site   | 7.05 ms                                                                | 7.02 ms: 1.00x faster                                                         |
| richards                 | 44.1 ms                                                                | 44.0 ms: 1.00x faster                                                         |
| genshi_xml               | 47.9 ms                                                                | 47.8 ms: 1.00x faster                                                         |
| go                       | 117 ms                                                                 | 116 ms: 1.00x faster                                                          |
| sqlalchemy_declarative   | 127 ms                                                                 | 127 ms: 1.00x faster                                                          |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                         |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.00x slower                                                          |
| 2to3                     | 251 ms                                                                 | 252 ms: 1.00x slower                                                          |
| many_optionals           | 927 us                                                                 | 929 us: 1.00x slower                                                          |
| sqlglot_transpile        | 1.54 ms                                                                | 1.55 ms: 1.00x slower                                                         |
| dulwich_log              | 64.0 ms                                                                | 64.2 ms: 1.00x slower                                                         |
| scimark_fft              | 340 ms                                                                 | 341 ms: 1.00x slower                                                          |
| sqlglot_normalize        | 103 ms                                                                 | 103 ms: 1.00x slower                                                          |
| unpickle_pure_python     | 217 us                                                                 | 218 us: 1.00x slower                                                          |
| sqlalchemy_imperative    | 16.2 ms                                                                | 16.3 ms: 1.01x slower                                                         |
| xml_etree_generate       | 83.1 ms                                                                | 83.6 ms: 1.01x slower                                                         |
| raytrace                 | 272 ms                                                                 | 274 ms: 1.01x slower                                                          |
| scimark_sor              | 121 ms                                                                 | 122 ms: 1.01x slower                                                          |
| regex_dna                | 215 ms                                                                 | 216 ms: 1.01x slower                                                          |
| scimark_monte_carlo      | 67.2 ms                                                                | 67.7 ms: 1.01x slower                                                         |
| shortest_path            | 474 ms                                                                 | 478 ms: 1.01x slower                                                          |
| fannkuch                 | 403 ms                                                                 | 407 ms: 1.01x slower                                                          |
| xml_etree_process        | 58.0 ms                                                                | 58.6 ms: 1.01x slower                                                         |
| pprint_pformat           | 1.46 sec                                                               | 1.48 sec: 1.01x slower                                                        |
| deepcopy_memo            | 30.6 us                                                                | 30.9 us: 1.01x slower                                                         |
| pprint_safe_repr         | 716 ms                                                                 | 724 ms: 1.01x slower                                                          |
| deepcopy_reduce          | 2.67 us                                                                | 2.71 us: 1.01x slower                                                         |
| thrift                   | 767 us                                                                 | 779 us: 1.01x slower                                                          |
| chaos                    | 57.7 ms                                                                | 58.6 ms: 1.02x slower                                                         |
| deepcopy                 | 258 us                                                                 | 262 us: 1.02x slower                                                          |
| bpe_tokeniser            | 4.35 sec                                                               | 4.42 sec: 1.02x slower                                                        |
| nbody                    | 92.6 ms                                                                | 94.3 ms: 1.02x slower                                                         |
| typing_runtime_protocols | 156 us                                                                 | 159 us: 1.02x slower                                                          |
| tomli_loads              | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                        |
| hexiom                   | 6.11 ms                                                                | 6.24 ms: 1.02x slower                                                         |
| scimark_lu               | 115 ms                                                                 | 118 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult  | 4.74 ms                                                                | 4.87 ms: 1.03x slower                                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (34): async_tree_memoization_tg, async_tree_io_tg, json, float, sqlite_synth, pylint, richards_super, sphinx, html5lib, pickle_pure_python, sympy_expand, async_tree_cpu_io_mixed, subparsers, async_tree_cpu_io_mixed_tg, xml_etree_parse, regex_compile, xml_etree_iterparse, django_template, bench_thread_pool, sympy_str, asyncio_websockets, sympy_integrate, sqlglot_optimize, nqueens, sympy_sum, crypto_pyaes, pathlib, async_generators, bench_mp_pool, sqlglot_parse, json_loads, connected_components, coverage, k_core

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 53.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x