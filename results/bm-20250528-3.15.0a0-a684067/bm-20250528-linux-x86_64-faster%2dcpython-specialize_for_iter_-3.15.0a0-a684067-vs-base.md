# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.001x faster
- HPT reliability: 98.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| docutils       | 2.58 sec                                                              | 2.57 sec: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                | 483 ms: 1.02x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 390 ms                                                                | 383 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed          | 500 ms                                                                | 493 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                | 460 ms: 1.01x faster                                                            |
| async_generators                 | 405 ms                                                                | 403 ms: 1.01x faster                                                            |
| async_tree_eager_memoization     | 198 ms                                                                | 201 ms: 1.01x slower                                                            |
| async_tree_eager                 | 103 ms                                                                | 105 ms: 1.02x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (12): async_tree_eager_tg, asyncio_websockets, coroutines, async_tree_none_tg, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_io, async_tree_eager_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 188 ms: 1.02x faster                                                            |
| float          | 70.5 ms                                                               | 71.4 ms: 1.01x slower                                                           |
| nbody          | 97.6 ms                                                               | 100 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x faster                                                            |
| regex_v8       | 23.0 ms                                                               | 23.5 ms: 1.02x slower                                                           |
| regex_dna      | 191 ms                                                                | 210 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 30.0 us                                                               | 29.0 us: 1.03x faster                                                           |
| tomli_loads          | 2.02 sec                                                              | 1.98 sec: 1.02x faster                                                          |
| xml_etree_generate   | 85.3 ms                                                               | 84.4 ms: 1.01x faster                                                           |
| unpickle_pure_python | 219 us                                                                | 217 us: 1.01x faster                                                            |
| json_dumps           | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| xml_etree_parse      | 140 ms                                                                | 141 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 98.0 ms                                                               | 99.0 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                           |
| mako            | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| django_template | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json                             | 5.37 ms                                                               | 5.14 ms: 1.05x faster                                                           |
| json_loads                       | 30.0 us                                                               | 29.0 us: 1.03x faster                                                           |
| deltablue                        | 3.52 ms                                                               | 3.43 ms: 1.03x faster                                                           |
| fannkuch                         | 423 ms                                                                | 413 ms: 1.02x faster                                                            |
| richards_super                   | 50.3 ms                                                               | 49.2 ms: 1.02x faster                                                           |
| richards                         | 43.8 ms                                                               | 42.8 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult          | 5.09 ms                                                               | 4.98 ms: 1.02x faster                                                           |
| deepcopy_reduce                  | 2.74 us                                                               | 2.68 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                | 483 ms: 1.02x faster                                                            |
| pidigits                         | 191 ms                                                                | 188 ms: 1.02x faster                                                            |
| tomli_loads                      | 2.02 sec                                                              | 1.98 sec: 1.02x faster                                                          |
| sympy_sum                        | 150 ms                                                                | 147 ms: 1.02x faster                                                            |
| scimark_fft                      | 379 ms                                                                | 372 ms: 1.02x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 390 ms                                                                | 383 ms: 1.02x faster                                                            |
| pyflate                          | 430 ms                                                                | 423 ms: 1.02x faster                                                            |
| nqueens                          | 81.4 ms                                                               | 80.2 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed          | 500 ms                                                                | 493 ms: 1.01x faster                                                            |
| crypto_pyaes                     | 75.1 ms                                                               | 74.0 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 467 ms                                                                | 460 ms: 1.01x faster                                                            |
| hexiom                           | 6.06 ms                                                               | 5.99 ms: 1.01x faster                                                           |
| logging_format                   | 6.80 us                                                               | 6.71 us: 1.01x faster                                                           |
| chaos                            | 60.8 ms                                                               | 60.1 ms: 1.01x faster                                                           |
| xml_etree_generate               | 85.3 ms                                                               | 84.4 ms: 1.01x faster                                                           |
| unpickle_pure_python             | 219 us                                                                | 217 us: 1.01x faster                                                            |
| pprint_safe_repr                 | 795 ms                                                                | 787 ms: 1.01x faster                                                            |
| bpe_tokeniser                    | 4.49 sec                                                              | 4.45 sec: 1.01x faster                                                          |
| sqlglot_v2_transpile             | 1.55 ms                                                               | 1.54 ms: 1.01x faster                                                           |
| pathlib                          | 17.2 ms                                                               | 17.1 ms: 1.01x faster                                                           |
| pprint_pformat                   | 1.62 sec                                                              | 1.61 sec: 1.01x faster                                                          |
| coverage                         | 426 ms                                                                | 423 ms: 1.01x faster                                                            |
| go                               | 112 ms                                                                | 111 ms: 1.01x faster                                                            |
| json_dumps                       | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| async_generators                 | 405 ms                                                                | 403 ms: 1.01x faster                                                            |
| deepcopy_memo                    | 29.6 us                                                               | 29.5 us: 1.01x faster                                                           |
| sqlglot_v2_parse                 | 1.24 ms                                                               | 1.24 ms: 1.00x faster                                                           |
| sympy_integrate                  | 19.0 ms                                                               | 18.9 ms: 1.00x faster                                                           |
| sympy_expand                     | 450 ms                                                                | 448 ms: 1.00x faster                                                            |
| docutils                         | 2.58 sec                                                              | 2.57 sec: 1.00x faster                                                          |
| sqlglot_v2_optimize              | 52.2 ms                                                               | 52.0 ms: 1.00x faster                                                           |
| raytrace                         | 270 ms                                                                | 269 ms: 1.00x faster                                                            |
| 2to3                             | 255 ms                                                                | 254 ms: 1.00x faster                                                            |
| regex_compile                    | 127 ms                                                                | 127 ms: 1.00x faster                                                            |
| python_startup                   | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| python_startup_no_site           | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| thrift                           | 148 ms                                                                | 149 ms: 1.00x slower                                                            |
| deepcopy                         | 253 us                                                                | 254 us: 1.00x slower                                                            |
| xml_etree_parse                  | 140 ms                                                                | 141 ms: 1.01x slower                                                            |
| scimark_sor                      | 119 ms                                                                | 120 ms: 1.01x slower                                                            |
| meteor_contest                   | 104 ms                                                                | 104 ms: 1.01x slower                                                            |
| dulwich_log                      | 59.6 ms                                                               | 60.0 ms: 1.01x slower                                                           |
| genshi_text                      | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                           |
| telco                            | 7.92 ms                                                               | 7.99 ms: 1.01x slower                                                           |
| create_gc_cycles                 | 2.57 ms                                                               | 2.59 ms: 1.01x slower                                                           |
| scimark_lu                       | 119 ms                                                                | 120 ms: 1.01x slower                                                            |
| xml_etree_iterparse              | 98.0 ms                                                               | 99.0 ms: 1.01x slower                                                           |
| logging_silent                   | 467 ns                                                                | 471 ns: 1.01x slower                                                            |
| sqlite_synth                     | 2.85 us                                                               | 2.88 us: 1.01x slower                                                           |
| mako                             | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| float                            | 70.5 ms                                                               | 71.4 ms: 1.01x slower                                                           |
| subparsers                       | 23.3 ms                                                               | 23.6 ms: 1.01x slower                                                           |
| async_tree_eager_memoization     | 198 ms                                                                | 201 ms: 1.01x slower                                                            |
| django_template                  | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                                           |
| generators                       | 29.1 ms                                                               | 29.6 ms: 1.02x slower                                                           |
| comprehensions                   | 15.9 us                                                               | 16.1 us: 1.02x slower                                                           |
| async_tree_eager                 | 103 ms                                                                | 105 ms: 1.02x slower                                                            |
| regex_v8                         | 23.0 ms                                                               | 23.5 ms: 1.02x slower                                                           |
| nbody                            | 97.6 ms                                                               | 100 ms: 1.02x slower                                                            |
| gc_traversal                     | 4.92 ms                                                               | 5.18 ms: 1.05x slower                                                           |
| regex_dna                        | 191 ms                                                                | 210 ms: 1.10x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (34): sphinx, async_tree_eager_tg, pycparser, pylint, html5lib, scimark_monte_carlo, dask, genshi_xml, asyncio_websockets, sympy_str, mdp, coroutines, async_tree_none_tg, async_tree_memoization, logging_simple, pickle_pure_python, many_optionals, bench_mp_pool, shortest_path, xml_etree_process, bench_thread_pool, async_tree_eager_memoization_tg, regex_effbot, async_tree_io, connected_components, sqlglot_v2_normalize, k_core, spectral_norm, async_tree_eager_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_none, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 98.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x