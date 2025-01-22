# Results vs. base

- fork: faster-cpython
- ref: close_escapes
- machine: linux-x86_64
- commit hash: 08894e6
- commit date: 2025-01-22
- overall geometric mean: 1.003x slower
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                       | 281 ms: 1.00x faster                                                            |
| docutils       | 2.89 sec                                                                     | 2.89 sec: 1.00x slower                                                          |
| html5lib       | 68.0 ms                                                                      | 68.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|--------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators   | 398 ms                                                                       | 377 ms: 1.06x faster                                                            |
| coroutines         | 21.4 ms                                                                      | 21.0 ms: 1.02x faster                                                           |
| asyncio_websockets | 386 ms                                                                       | 384 ms: 1.01x faster                                                            |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 86.5 ms                                                                      | 90.7 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.8 ms                                                                      | 25.8 ms: 1.04x faster                                                           |
| regex_dna      | 251 ms                                                                       | 248 ms: 1.01x faster                                                            |
| regex_effbot   | 3.18 ms                                                                      | 3.17 ms: 1.00x faster                                                           |
| regex_compile  | 135 ms                                                                       | 137 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|---------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 97.0 ms                                                                      | 95.4 ms: 1.02x faster                                                           |
| xml_etree_generate  | 83.6 ms                                                                      | 82.5 ms: 1.01x faster                                                           |
| xml_etree_parse     | 135 ms                                                                       | 134 ms: 1.00x faster                                                            |
| json_loads          | 25.4 us                                                                      | 25.5 us: 1.00x slower                                                           |
| json_dumps          | 11.6 ms                                                                      | 11.7 ms: 1.01x slower                                                           |
| tomli_loads         | 2.07 sec                                                                     | 2.09 sec: 1.01x slower                                                          |
| Geometric mean      | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                           |
| python_startup_no_site | 8.98 ms                                                                      | 8.97 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                      | 10.9 ms: 1.01x faster                                                           |
| genshi_text     | 24.8 ms                                                                      | 24.5 ms: 1.01x faster                                                           |
| django_template | 35.2 ms                                                                      | 36.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators       | 398 ms                                                                       | 377 ms: 1.06x faster                                                            |
| coverage               | 79.0 ms                                                                      | 75.3 ms: 1.05x faster                                                           |
| regex_v8               | 26.8 ms                                                                      | 25.8 ms: 1.04x faster                                                           |
| chaos                  | 61.1 ms                                                                      | 59.1 ms: 1.03x faster                                                           |
| coroutines             | 21.4 ms                                                                      | 21.0 ms: 1.02x faster                                                           |
| xml_etree_iterparse    | 97.0 ms                                                                      | 95.4 ms: 1.02x faster                                                           |
| mako                   | 11.0 ms                                                                      | 10.9 ms: 1.01x faster                                                           |
| xml_etree_generate     | 83.6 ms                                                                      | 82.5 ms: 1.01x faster                                                           |
| spectral_norm          | 85.4 ms                                                                      | 84.3 ms: 1.01x faster                                                           |
| crypto_pyaes           | 75.4 ms                                                                      | 74.4 ms: 1.01x faster                                                           |
| genshi_text            | 24.8 ms                                                                      | 24.5 ms: 1.01x faster                                                           |
| sqlglot_optimize       | 58.3 ms                                                                      | 57.7 ms: 1.01x faster                                                           |
| regex_dna              | 251 ms                                                                       | 248 ms: 1.01x faster                                                            |
| dulwich_log            | 67.2 ms                                                                      | 66.7 ms: 1.01x faster                                                           |
| sympy_expand           | 497 ms                                                                       | 494 ms: 1.01x faster                                                            |
| fannkuch               | 364 ms                                                                       | 361 ms: 1.01x faster                                                            |
| asyncio_websockets     | 386 ms                                                                       | 384 ms: 1.01x faster                                                            |
| sympy_str              | 290 ms                                                                       | 289 ms: 1.00x faster                                                            |
| pathlib                | 15.9 ms                                                                      | 15.9 ms: 1.00x faster                                                           |
| regex_effbot           | 3.18 ms                                                                      | 3.17 ms: 1.00x faster                                                           |
| xml_etree_parse        | 135 ms                                                                       | 134 ms: 1.00x faster                                                            |
| sqlglot_normalize      | 117 ms                                                                       | 116 ms: 1.00x faster                                                            |
| sympy_sum              | 152 ms                                                                       | 152 ms: 1.00x faster                                                            |
| deepcopy_memo          | 30.3 us                                                                      | 30.2 us: 1.00x faster                                                           |
| meteor_contest         | 125 ms                                                                       | 125 ms: 1.00x faster                                                            |
| 2to3                   | 282 ms                                                                       | 281 ms: 1.00x faster                                                            |
| go                     | 128 ms                                                                       | 128 ms: 1.00x faster                                                            |
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                           |
| python_startup_no_site | 8.98 ms                                                                      | 8.97 ms: 1.00x faster                                                           |
| docutils               | 2.89 sec                                                                     | 2.89 sec: 1.00x slower                                                          |
| scimark_monte_carlo    | 61.6 ms                                                                      | 61.7 ms: 1.00x slower                                                           |
| json_loads             | 25.4 us                                                                      | 25.5 us: 1.00x slower                                                           |
| json_dumps             | 11.6 ms                                                                      | 11.7 ms: 1.01x slower                                                           |
| sqlalchemy_declarative | 144 ms                                                                       | 145 ms: 1.01x slower                                                            |
| deepcopy_reduce        | 2.93 us                                                                      | 2.95 us: 1.01x slower                                                           |
| mdp                    | 2.44 sec                                                                     | 2.46 sec: 1.01x slower                                                          |
| html5lib               | 68.0 ms                                                                      | 68.5 ms: 1.01x slower                                                           |
| deepcopy               | 283 us                                                                       | 286 us: 1.01x slower                                                            |
| pprint_safe_repr       | 782 ms                                                                       | 789 ms: 1.01x slower                                                            |
| json                   | 5.31 ms                                                                      | 5.36 ms: 1.01x slower                                                           |
| richards               | 45.7 ms                                                                      | 46.1 ms: 1.01x slower                                                           |
| subparsers             | 22.8 ms                                                                      | 23.0 ms: 1.01x slower                                                           |
| tomli_loads            | 2.07 sec                                                                     | 2.09 sec: 1.01x slower                                                          |
| nqueens                | 87.9 ms                                                                      | 88.9 ms: 1.01x slower                                                           |
| connected_components   | 413 ms                                                                       | 418 ms: 1.01x slower                                                            |
| scimark_lu             | 94.3 ms                                                                      | 95.5 ms: 1.01x slower                                                           |
| regex_compile          | 135 ms                                                                       | 137 ms: 1.01x slower                                                            |
| pprint_pformat         | 1.58 sec                                                                     | 1.61 sec: 1.02x slower                                                          |
| pycparser              | 1.24 sec                                                                     | 1.26 sec: 1.02x slower                                                          |
| bpe_tokeniser          | 4.65 sec                                                                     | 4.73 sec: 1.02x slower                                                          |
| logging_format         | 7.14 us                                                                      | 7.27 us: 1.02x slower                                                           |
| scimark_fft            | 295 ms                                                                       | 301 ms: 1.02x slower                                                            |
| shortest_path          | 434 ms                                                                       | 445 ms: 1.02x slower                                                            |
| generators             | 28.1 ms                                                                      | 28.8 ms: 1.03x slower                                                           |
| logging_simple         | 6.44 us                                                                      | 6.61 us: 1.03x slower                                                           |
| comprehensions         | 17.2 us                                                                      | 17.9 us: 1.04x slower                                                           |
| django_template        | 35.2 ms                                                                      | 36.8 ms: 1.04x slower                                                           |
| deltablue              | 3.29 ms                                                                      | 3.44 ms: 1.04x slower                                                           |
| scimark_sor            | 111 ms                                                                       | 116 ms: 1.05x slower                                                            |
| nbody                  | 86.5 ms                                                                      | 90.7 ms: 1.05x slower                                                           |
| pyflate                | 431 ms                                                                       | 457 ms: 1.06x slower                                                            |
| gc_traversal           | 6.11 ms                                                                      | 6.65 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (34): telco, float, bench_thread_pool, xml_etree_process, genshi_xml, unpickle_pure_python, sqlalchemy_imperative, richards_super, k_core, pidigits, many_optionals, async_tree_memoization_tg, sqlglot_parse, logging_silent, sympy_integrate, async_tree_cpu_io_mixed_tg, scimark_sparse_mat_mult, pickle_pure_python, thrift, async_tree_cpu_io_mixed, sqlite_synth, async_tree_none_tg, async_tree_io, sphinx, typing_runtime_protocols, sqlglot_transpile, pylint, hexiom, raytrace, async_tree_memoization, async_tree_none, async_tree_io_tg, create_gc_cycles, bench_mp_pool

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 98.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x