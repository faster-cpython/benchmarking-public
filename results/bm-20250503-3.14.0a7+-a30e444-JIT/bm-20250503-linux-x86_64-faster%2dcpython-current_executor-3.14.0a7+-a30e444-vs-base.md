# Results vs. base

- fork: faster-cpython
- ref: current_executor
- machine: linux-x86_64
- commit hash: a30e444
- commit date: 2025-05-03
- overall geometric mean: 1.004x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                 | 258 ms: 1.00x faster                                                         |
| docutils       | 2.69 sec                                                               | 2.68 sec: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators                 | 434 ms                                                                 | 423 ms: 1.03x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                 | 386 ms: 1.02x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                 | 458 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 496 ms                                                                 | 487 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed          | 500 ms                                                                 | 492 ms: 1.02x faster                                                         |
| async_tree_memoization           | 316 ms                                                                 | 312 ms: 1.02x faster                                                         |
| async_tree_io                    | 601 ms                                                                 | 595 ms: 1.01x faster                                                         |
| async_tree_eager                 | 106 ms                                                                 | 104 ms: 1.01x faster                                                         |
| coroutines                       | 25.7 ms                                                                | 25.5 ms: 1.01x faster                                                        |
| async_tree_eager_io_tg           | 614 ms                                                                 | 616 ms: 1.00x slower                                                         |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (9): async_tree_eager_memoization, async_tree_none, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_tg, async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 186 ms: 1.02x faster                                                         |
| nbody          | 93.5 ms                                                                | 93.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                        |
| regex_effbot   | 3.35 ms                                                                | 3.39 ms: 1.01x slower                                                        |
| regex_dna      | 207 ms                                                                 | 210 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                               | 1.88 sec: 1.01x faster                                                       |
| unpickle_pure_python | 211 us                                                                 | 209 us: 1.01x faster                                                         |
| xml_etree_generate   | 81.2 ms                                                                | 80.6 ms: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): json_loads, json_dumps, xml_etree_process, pickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                                | 6.97 ms: 1.00x slower                                                        |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 49.9 ms                                                                | 49.1 ms: 1.02x faster                                                        |
| genshi_text     | 21.2 ms                                                                | 20.8 ms: 1.02x faster                                                        |
| django_template | 32.9 ms                                                                | 32.4 ms: 1.01x faster                                                        |
| mako            | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7+-a0bc0c4 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions                   | 18.9 us                                                                | 18.3 us: 1.03x faster                                                        |
| logging_silent                   | 99.5 ns                                                                | 96.8 ns: 1.03x faster                                                        |
| meteor_contest                   | 111 ms                                                                 | 108 ms: 1.03x faster                                                         |
| fannkuch                         | 418 ms                                                                 | 407 ms: 1.03x faster                                                         |
| async_generators                 | 434 ms                                                                 | 423 ms: 1.03x faster                                                         |
| deepcopy                         | 260 us                                                                 | 254 us: 1.02x faster                                                         |
| scimark_fft                      | 335 ms                                                                 | 328 ms: 1.02x faster                                                         |
| richards                         | 36.2 ms                                                                | 35.4 ms: 1.02x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 394 ms                                                                 | 386 ms: 1.02x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                 | 458 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 496 ms                                                                 | 487 ms: 1.02x faster                                                         |
| pidigits                         | 190 ms                                                                 | 186 ms: 1.02x faster                                                         |
| sqlite_synth                     | 2.81 us                                                                | 2.76 us: 1.02x faster                                                        |
| sqlglot_v2_normalize             | 109 ms                                                                 | 107 ms: 1.02x faster                                                         |
| richards_super                   | 41.3 ms                                                                | 40.6 ms: 1.02x faster                                                        |
| genshi_xml                       | 49.9 ms                                                                | 49.1 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed          | 500 ms                                                                 | 492 ms: 1.02x faster                                                         |
| genshi_text                      | 21.2 ms                                                                | 20.8 ms: 1.02x faster                                                        |
| async_tree_memoization           | 316 ms                                                                 | 312 ms: 1.02x faster                                                         |
| pprint_safe_repr                 | 758 ms                                                                 | 747 ms: 1.01x faster                                                         |
| tomli_loads                      | 1.91 sec                                                               | 1.88 sec: 1.01x faster                                                       |
| scimark_sparse_mat_mult          | 4.99 ms                                                                | 4.92 ms: 1.01x faster                                                        |
| bpe_tokeniser                    | 4.47 sec                                                               | 4.41 sec: 1.01x faster                                                       |
| django_template                  | 32.9 ms                                                                | 32.4 ms: 1.01x faster                                                        |
| scimark_lu                       | 122 ms                                                                 | 120 ms: 1.01x faster                                                         |
| sqlglot_v2_optimize              | 54.5 ms                                                                | 53.8 ms: 1.01x faster                                                        |
| deepcopy_reduce                  | 2.70 us                                                                | 2.67 us: 1.01x faster                                                        |
| subparsers                       | 22.9 ms                                                                | 22.7 ms: 1.01x faster                                                        |
| dulwich_log                      | 61.6 ms                                                                | 60.9 ms: 1.01x faster                                                        |
| sqlglot_v2_transpile             | 1.59 ms                                                                | 1.57 ms: 1.01x faster                                                        |
| go                               | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| async_tree_io                    | 601 ms                                                                 | 595 ms: 1.01x faster                                                         |
| sqlalchemy_imperative            | 17.5 ms                                                                | 17.4 ms: 1.01x faster                                                        |
| async_tree_eager                 | 106 ms                                                                 | 104 ms: 1.01x faster                                                         |
| unpickle_pure_python             | 211 us                                                                 | 209 us: 1.01x faster                                                         |
| coroutines                       | 25.7 ms                                                                | 25.5 ms: 1.01x faster                                                        |
| mako                             | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                                        |
| xml_etree_generate               | 81.2 ms                                                                | 80.6 ms: 1.01x faster                                                        |
| regex_v8                         | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                        |
| sqlglot_v2_parse                 | 1.27 ms                                                                | 1.26 ms: 1.01x faster                                                        |
| pathlib                          | 17.1 ms                                                                | 17.0 ms: 1.01x faster                                                        |
| connected_components             | 452 ms                                                                 | 449 ms: 1.01x faster                                                         |
| crypto_pyaes                     | 76.6 ms                                                                | 76.2 ms: 1.01x faster                                                        |
| many_optionals                   | 975 us                                                                 | 970 us: 1.01x faster                                                         |
| sympy_integrate                  | 19.4 ms                                                                | 19.3 ms: 1.00x faster                                                        |
| deltablue                        | 3.10 ms                                                                | 3.08 ms: 1.00x faster                                                        |
| docutils                         | 2.69 sec                                                               | 2.68 sec: 1.00x faster                                                       |
| bench_thread_pool                | 897 us                                                                 | 894 us: 1.00x faster                                                         |
| 2to3                             | 259 ms                                                                 | 258 ms: 1.00x faster                                                         |
| create_gc_cycles                 | 2.49 ms                                                                | 2.50 ms: 1.00x slower                                                        |
| async_tree_eager_io_tg           | 614 ms                                                                 | 616 ms: 1.00x slower                                                         |
| raytrace                         | 275 ms                                                                 | 276 ms: 1.00x slower                                                         |
| sympy_str                        | 270 ms                                                                 | 271 ms: 1.00x slower                                                         |
| python_startup_no_site           | 6.94 ms                                                                | 6.97 ms: 1.00x slower                                                        |
| mdp                              | 1.22 sec                                                               | 1.23 sec: 1.00x slower                                                       |
| python_startup                   | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                        |
| sympy_expand                     | 471 ms                                                                 | 473 ms: 1.00x slower                                                         |
| nbody                            | 93.5 ms                                                                | 93.9 ms: 1.01x slower                                                        |
| hexiom                           | 6.70 ms                                                                | 6.74 ms: 1.01x slower                                                        |
| shortest_path                    | 489 ms                                                                 | 492 ms: 1.01x slower                                                         |
| scimark_monte_carlo              | 68.3 ms                                                                | 68.8 ms: 1.01x slower                                                        |
| logging_format                   | 6.30 us                                                                | 6.35 us: 1.01x slower                                                        |
| regex_effbot                     | 3.35 ms                                                                | 3.39 ms: 1.01x slower                                                        |
| regex_dna                        | 207 ms                                                                 | 210 ms: 1.01x slower                                                         |
| typing_runtime_protocols         | 171 us                                                                 | 173 us: 1.01x slower                                                         |
| scimark_sor                      | 119 ms                                                                 | 121 ms: 1.02x slower                                                         |
| logging_simple                   | 5.63 us                                                                | 5.76 us: 1.02x slower                                                        |
| pyflate                          | 432 ms                                                                 | 444 ms: 1.03x slower                                                         |
| gc_traversal                     | 4.91 ms                                                                | 5.08 ms: 1.03x slower                                                        |
| generators                       | 29.0 ms                                                                | 30.0 ms: 1.04x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (33): telco, async_tree_eager_memoization, nqueens, async_tree_none, json_loads, float, sphinx, json, async_tree_io_tg, json_dumps, xml_etree_process, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_tg, pylint, async_tree_none_tg, pprint_pformat, async_tree_memoization_tg, regex_compile, sqlalchemy_declarative, spectral_norm, sympy_sum, asyncio_websockets, k_core, pickle_pure_python, bench_mp_pool, xml_etree_parse, html5lib, chaos, xml_etree_iterparse, coverage, pycparser, deepcopy_memo

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x