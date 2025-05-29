# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 08419ee
- commit date: 2025-05-29
- overall geometric mean: 1.002x slower
- HPT reliability: 93.46%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 256 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 390 ms                                                                | 385 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed       | 500 ms                                                                | 495 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg    | 493 ms                                                                | 489 ms: 1.01x faster                                                            |
| async_tree_eager_memoization  | 198 ms                                                                | 200 ms: 1.01x slower                                                            |
| async_tree_eager              | 103 ms                                                                | 104 ms: 1.01x slower                                                            |
| async_generators              | 405 ms                                                                | 411 ms: 1.01x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (13): async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_tg, asyncio_websockets, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_eager_io, coroutines, async_tree_none, async_tree_none_tg, async_tree_eager_io_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 188 ms: 1.02x faster                                                            |
| nbody          | 97.6 ms                                                               | 100 ms: 1.03x slower                                                            |
| float          | 70.5 ms                                                               | 73.0 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.22 ms                                                               | 3.23 ms: 1.00x slower                                                           |
| regex_v8       | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                           |
| regex_dna      | 191 ms                                                                | 209 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 59.9 ms                                                               | 59.5 ms: 1.01x faster                                                           |
| xml_etree_generate  | 85.3 ms                                                               | 84.8 ms: 1.01x faster                                                           |
| json_loads          | 30.0 us                                                               | 29.8 us: 1.01x faster                                                           |
| tomli_loads         | 2.02 sec                                                              | 2.01 sec: 1.00x faster                                                          |
| pickle_pure_python  | 316 us                                                                | 319 us: 1.01x slower                                                            |
| xml_etree_iterparse | 98.0 ms                                                               | 99.2 ms: 1.01x slower                                                           |
| json_dumps          | 11.1 ms                                                               | 11.2 ms: 1.01x slower                                                           |
| xml_etree_parse     | 140 ms                                                                | 143 ms: 1.02x slower                                                            |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                     | bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250529-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-08419ee |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| shortest_path                 | 521 ms                                                                | 493 ms: 1.06x faster                                                            |
| fannkuch                      | 423 ms                                                                | 408 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult       | 5.09 ms                                                               | 4.93 ms: 1.03x faster                                                           |
| pathlib                       | 17.2 ms                                                               | 16.7 ms: 1.03x faster                                                           |
| chaos                         | 60.8 ms                                                               | 59.6 ms: 1.02x faster                                                           |
| pidigits                      | 191 ms                                                                | 188 ms: 1.02x faster                                                            |
| crypto_pyaes                  | 75.1 ms                                                               | 73.9 ms: 1.02x faster                                                           |
| richards_super                | 50.3 ms                                                               | 49.8 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed | 390 ms                                                                | 385 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed       | 500 ms                                                                | 495 ms: 1.01x faster                                                            |
| scimark_monte_carlo           | 68.4 ms                                                               | 67.8 ms: 1.01x faster                                                           |
| logging_format                | 6.80 us                                                               | 6.74 us: 1.01x faster                                                           |
| logging_simple                | 6.11 us                                                               | 6.06 us: 1.01x faster                                                           |
| sympy_sum                     | 150 ms                                                                | 149 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg    | 493 ms                                                                | 489 ms: 1.01x faster                                                            |
| xml_etree_process             | 59.9 ms                                                               | 59.5 ms: 1.01x faster                                                           |
| xml_etree_generate            | 85.3 ms                                                               | 84.8 ms: 1.01x faster                                                           |
| json_loads                    | 30.0 us                                                               | 29.8 us: 1.01x faster                                                           |
| bpe_tokeniser                 | 4.49 sec                                                              | 4.46 sec: 1.01x faster                                                          |
| tomli_loads                   | 2.02 sec                                                              | 2.01 sec: 1.00x faster                                                          |
| nqueens                       | 81.4 ms                                                               | 81.0 ms: 1.00x faster                                                           |
| richards                      | 43.8 ms                                                               | 43.6 ms: 1.00x faster                                                           |
| pyflate                       | 430 ms                                                                | 429 ms: 1.00x faster                                                            |
| python_startup_no_site        | 6.93 ms                                                               | 6.92 ms: 1.00x faster                                                           |
| python_startup                | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                           |
| create_gc_cycles              | 2.57 ms                                                               | 2.57 ms: 1.00x slower                                                           |
| bench_thread_pool             | 885 us                                                                | 887 us: 1.00x slower                                                            |
| 2to3                          | 255 ms                                                                | 256 ms: 1.00x slower                                                            |
| hexiom                        | 6.06 ms                                                               | 6.09 ms: 1.00x slower                                                           |
| regex_effbot                  | 3.22 ms                                                               | 3.23 ms: 1.00x slower                                                           |
| sqlglot_v2_transpile          | 1.55 ms                                                               | 1.56 ms: 1.01x slower                                                           |
| pprint_safe_repr              | 795 ms                                                                | 800 ms: 1.01x slower                                                            |
| dulwich_log                   | 59.6 ms                                                               | 59.9 ms: 1.01x slower                                                           |
| scimark_fft                   | 379 ms                                                                | 381 ms: 1.01x slower                                                            |
| sqlglot_v2_parse              | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                                           |
| sqlglot_v2_optimize           | 52.2 ms                                                               | 52.5 ms: 1.01x slower                                                           |
| coverage                      | 426 ms                                                                | 428 ms: 1.01x slower                                                            |
| raytrace                      | 270 ms                                                                | 272 ms: 1.01x slower                                                            |
| pickle_pure_python            | 316 us                                                                | 319 us: 1.01x slower                                                            |
| mdp                           | 1.22 sec                                                              | 1.23 sec: 1.01x slower                                                          |
| regex_v8                      | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                           |
| sqlglot_v2_normalize          | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| deltablue                     | 3.52 ms                                                               | 3.55 ms: 1.01x slower                                                           |
| async_tree_eager_memoization  | 198 ms                                                                | 200 ms: 1.01x slower                                                            |
| async_tree_eager              | 103 ms                                                                | 104 ms: 1.01x slower                                                            |
| sqlite_synth                  | 2.85 us                                                               | 2.88 us: 1.01x slower                                                           |
| pprint_pformat                | 1.62 sec                                                              | 1.64 sec: 1.01x slower                                                          |
| xml_etree_iterparse           | 98.0 ms                                                               | 99.2 ms: 1.01x slower                                                           |
| spectral_norm                 | 109 ms                                                                | 110 ms: 1.01x slower                                                            |
| json                          | 5.37 ms                                                               | 5.44 ms: 1.01x slower                                                           |
| deepcopy                      | 253 us                                                                | 257 us: 1.01x slower                                                            |
| async_generators              | 405 ms                                                                | 411 ms: 1.01x slower                                                            |
| scimark_sor                   | 119 ms                                                                | 121 ms: 1.01x slower                                                            |
| mako                          | 11.1 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| json_dumps                    | 11.1 ms                                                               | 11.2 ms: 1.01x slower                                                           |
| go                            | 112 ms                                                                | 114 ms: 1.02x slower                                                            |
| meteor_contest                | 104 ms                                                                | 105 ms: 1.02x slower                                                            |
| subparsers                    | 23.3 ms                                                               | 23.6 ms: 1.02x slower                                                           |
| logging_silent                | 467 ns                                                                | 477 ns: 1.02x slower                                                            |
| generators                    | 29.1 ms                                                               | 29.8 ms: 1.02x slower                                                           |
| comprehensions                | 15.9 us                                                               | 16.2 us: 1.02x slower                                                           |
| xml_etree_parse               | 140 ms                                                                | 143 ms: 1.02x slower                                                            |
| nbody                         | 97.6 ms                                                               | 100 ms: 1.03x slower                                                            |
| gc_traversal                  | 4.92 ms                                                               | 5.08 ms: 1.03x slower                                                           |
| float                         | 70.5 ms                                                               | 73.0 ms: 1.04x slower                                                           |
| pycparser                     | 1.12 sec                                                              | 1.16 sec: 1.04x slower                                                          |
| regex_dna                     | 191 ms                                                                | 209 ms: 1.09x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (36): async_tree_eager_cpu_io_mixed_tg, genshi_xml, async_tree_memoization, sphinx, async_tree_eager_tg, asyncio_websockets, pylint, docutils, many_optionals, connected_components, deepcopy_memo, dask, async_tree_eager_memoization_tg, deepcopy_reduce, scimark_lu, typing_runtime_protocols, regex_compile, html5lib, sympy_expand, unpickle_pure_python, genshi_text, sympy_str, sympy_integrate, async_tree_memoization_tg, thrift, bench_mp_pool, k_core, django_template, async_tree_eager_io, coroutines, async_tree_none, async_tree_none_tg, async_tree_eager_io_tg, async_tree_io, telco, async_tree_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 93.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x