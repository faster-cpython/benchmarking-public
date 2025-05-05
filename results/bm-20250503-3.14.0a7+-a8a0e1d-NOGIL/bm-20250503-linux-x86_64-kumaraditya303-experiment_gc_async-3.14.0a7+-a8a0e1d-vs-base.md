# Results vs. base

- fork: kumaraditya303
- ref: experiment_gc_async
- machine: linux-x86_64
- commit hash: a8a0e1d
- commit date: 2025-05-03
- overall geometric mean: 1.000x faster
- HPT reliability: 51.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 290 ms                                                                 | 291 ms: 1.00x slower                                                          |
| docutils       | 2.78 sec                                                               | 2.80 sec: 1.00x slower                                                        |
| html5lib       | 67.3 ms                                                                | 66.4 ms: 1.01x faster                                                         |
| sphinx         | 1.10 sec                                                               | 1.10 sec: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                    | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed      | 508 ms                                                                 | 503 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg   | 467 ms                                                                 | 463 ms: 1.01x faster                                                          |
| async_generators             | 437 ms                                                                 | 434 ms: 1.01x faster                                                          |
| async_tree_io                | 548 ms                                                                 | 552 ms: 1.01x slower                                                          |
| async_tree_eager_memoization | 217 ms                                                                 | 218 ms: 1.01x slower                                                          |
| async_tree_io_tg             | 515 ms                                                                 | 519 ms: 1.01x slower                                                          |
| async_tree_eager_io_tg       | 496 ms                                                                 | 502 ms: 1.01x slower                                                          |
| async_tree_eager             | 127 ms                                                                 | 129 ms: 1.01x slower                                                          |
| async_tree_eager_io          | 524 ms                                                                 | 532 ms: 1.02x slower                                                          |
| Geometric mean               | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, coroutines, async_tree_none, asyncio_websockets, async_tree_eager_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 73.2 ms                                                                | 71.2 ms: 1.03x faster                                                         |
| pidigits       | 182 ms                                                                 | 182 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                                 | 204 ms: 1.04x faster                                                          |
| regex_compile  | 145 ms                                                                 | 144 ms: 1.01x faster                                                          |
| regex_effbot   | 3.34 ms                                                                | 3.32 ms: 1.00x faster                                                         |
| regex_v8       | 22.5 ms                                                                | 22.9 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads        | 2.28 sec                                                               | 2.23 sec: 1.02x faster                                                        |
| pickle_pure_python | 349 us                                                                 | 343 us: 1.02x faster                                                          |
| json_dumps         | 13.3 ms                                                                | 13.1 ms: 1.01x faster                                                         |
| xml_etree_generate | 97.8 ms                                                                | 96.6 ms: 1.01x faster                                                         |
| xml_etree_process  | 68.7 ms                                                                | 68.0 ms: 1.01x faster                                                         |
| Geometric mean     | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 9.11 ms                                                                | 9.11 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 39.9 ms                                                                | 39.7 ms: 1.01x faster                                                         |
| mako            | 16.4 ms                                                                | 16.3 ms: 1.00x faster                                                         |
| genshi_xml      | 57.9 ms                                                                | 58.1 ms: 1.00x slower                                                         |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                    | bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7+-1550c30 | bm-20250503-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7+-a8a0e1d |
|------------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pyflate                      | 502 ms                                                                 | 480 ms: 1.04x faster                                                          |
| regex_dna                    | 212 ms                                                                 | 204 ms: 1.04x faster                                                          |
| logging_silent               | 111 ns                                                                 | 108 ns: 1.03x faster                                                          |
| meteor_contest               | 133 ms                                                                 | 130 ms: 1.03x faster                                                          |
| float                        | 73.2 ms                                                                | 71.2 ms: 1.03x faster                                                         |
| deepcopy_reduce              | 3.15 us                                                                | 3.08 us: 1.02x faster                                                         |
| tomli_loads                  | 2.28 sec                                                               | 2.23 sec: 1.02x faster                                                        |
| typing_runtime_protocols     | 205 us                                                                 | 201 us: 1.02x faster                                                          |
| pickle_pure_python           | 349 us                                                                 | 343 us: 1.02x faster                                                          |
| spectral_norm                | 121 ms                                                                 | 119 ms: 1.01x faster                                                          |
| html5lib                     | 67.3 ms                                                                | 66.4 ms: 1.01x faster                                                         |
| json_dumps                   | 13.3 ms                                                                | 13.1 ms: 1.01x faster                                                         |
| xml_etree_generate           | 97.8 ms                                                                | 96.6 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed      | 508 ms                                                                 | 503 ms: 1.01x faster                                                          |
| xml_etree_process            | 68.7 ms                                                                | 68.0 ms: 1.01x faster                                                         |
| sqlglot_v2_parse             | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                                         |
| deepcopy                     | 300 us                                                                 | 297 us: 1.01x faster                                                          |
| sqlglot_v2_normalize         | 118 ms                                                                 | 117 ms: 1.01x faster                                                          |
| fannkuch                     | 502 ms                                                                 | 498 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg   | 467 ms                                                                 | 463 ms: 1.01x faster                                                          |
| dulwich_log                  | 63.2 ms                                                                | 62.7 ms: 1.01x faster                                                         |
| async_generators             | 437 ms                                                                 | 434 ms: 1.01x faster                                                          |
| regex_compile                | 145 ms                                                                 | 144 ms: 1.01x faster                                                          |
| chaos                        | 68.1 ms                                                                | 67.7 ms: 1.01x faster                                                         |
| nqueens                      | 92.3 ms                                                                | 91.7 ms: 1.01x faster                                                         |
| comprehensions               | 19.8 us                                                                | 19.7 us: 1.01x faster                                                         |
| django_template              | 39.9 ms                                                                | 39.7 ms: 1.01x faster                                                         |
| scimark_sor                  | 134 ms                                                                 | 133 ms: 1.00x faster                                                          |
| regex_effbot                 | 3.34 ms                                                                | 3.32 ms: 1.00x faster                                                         |
| generators                   | 31.8 ms                                                                | 31.7 ms: 1.00x faster                                                         |
| scimark_fft                  | 408 ms                                                                 | 406 ms: 1.00x faster                                                          |
| mako                         | 16.4 ms                                                                | 16.3 ms: 1.00x faster                                                         |
| bpe_tokeniser                | 4.88 sec                                                               | 4.86 sec: 1.00x faster                                                        |
| richards_super               | 60.3 ms                                                                | 60.1 ms: 1.00x faster                                                         |
| pidigits                     | 182 ms                                                                 | 182 ms: 1.00x faster                                                          |
| python_startup_no_site       | 9.11 ms                                                                | 9.11 ms: 1.00x slower                                                         |
| sympy_str                    | 307 ms                                                                 | 308 ms: 1.00x slower                                                          |
| 2to3                         | 290 ms                                                                 | 291 ms: 1.00x slower                                                          |
| sphinx                       | 1.10 sec                                                               | 1.10 sec: 1.00x slower                                                        |
| genshi_xml                   | 57.9 ms                                                                | 58.1 ms: 1.00x slower                                                         |
| hexiom                       | 7.28 ms                                                                | 7.31 ms: 1.00x slower                                                         |
| pprint_safe_repr             | 819 ms                                                                 | 822 ms: 1.00x slower                                                          |
| k_core                       | 2.39 sec                                                               | 2.40 sec: 1.00x slower                                                        |
| docutils                     | 2.78 sec                                                               | 2.80 sec: 1.00x slower                                                        |
| scimark_monte_carlo          | 82.2 ms                                                                | 82.6 ms: 1.00x slower                                                         |
| richards                     | 51.3 ms                                                                | 51.6 ms: 1.00x slower                                                         |
| crypto_pyaes                 | 89.6 ms                                                                | 90.1 ms: 1.01x slower                                                         |
| sympy_expand                 | 521 ms                                                                 | 525 ms: 1.01x slower                                                          |
| logging_simple               | 6.60 us                                                                | 6.64 us: 1.01x slower                                                         |
| pprint_pformat               | 1.69 sec                                                               | 1.70 sec: 1.01x slower                                                        |
| async_tree_io                | 548 ms                                                                 | 552 ms: 1.01x slower                                                          |
| async_tree_eager_memoization | 217 ms                                                                 | 218 ms: 1.01x slower                                                          |
| async_tree_io_tg             | 515 ms                                                                 | 519 ms: 1.01x slower                                                          |
| coverage                     | 123 ms                                                                 | 125 ms: 1.01x slower                                                          |
| subparsers                   | 25.7 ms                                                                | 26.0 ms: 1.01x slower                                                         |
| connected_components         | 527 ms                                                                 | 532 ms: 1.01x slower                                                          |
| deltablue                    | 3.72 ms                                                                | 3.76 ms: 1.01x slower                                                         |
| async_tree_eager_io_tg       | 496 ms                                                                 | 502 ms: 1.01x slower                                                          |
| async_tree_eager             | 127 ms                                                                 | 129 ms: 1.01x slower                                                          |
| async_tree_eager_io          | 524 ms                                                                 | 532 ms: 1.02x slower                                                          |
| regex_v8                     | 22.5 ms                                                                | 22.9 ms: 1.02x slower                                                         |
| shortest_path                | 561 ms                                                                 | 571 ms: 1.02x slower                                                          |
| logging_format               | 7.37 us                                                                | 7.51 us: 1.02x slower                                                         |
| pathlib                      | 17.4 ms                                                                | 17.8 ms: 1.02x slower                                                         |
| pycparser                    | 1.11 sec                                                               | 1.17 sec: 1.05x slower                                                        |
| gc_traversal                 | 2.16 ms                                                                | 2.28 ms: 1.06x slower                                                         |
| Geometric mean               | (ref)                                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (37): async_tree_memoization_tg, sqlglot_v2_transpile, json, async_tree_eager_cpu_io_mixed_tg, sqlglot_v2_optimize, scimark_lu, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, bench_mp_pool, sympy_sum, sympy_integrate, create_gc_cycles, coroutines, mdp, bench_thread_pool, async_tree_none, raytrace, python_startup, xml_etree_iterparse, scimark_sparse_mat_mult, unpickle_pure_python, nbody, asyncio_websockets, async_tree_eager_tg, async_tree_memoization, deepcopy_memo, pylint, sqlalchemy_declarative, json_loads, go, xml_etree_parse, genshi_text, sqlite_synth, many_optionals, telco, async_tree_none_tg, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 51.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x