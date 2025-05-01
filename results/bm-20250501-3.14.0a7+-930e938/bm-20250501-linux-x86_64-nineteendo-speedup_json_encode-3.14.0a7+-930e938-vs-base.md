# Results vs. base

- fork: nineteendo
- ref: speedup_json_encode
- machine: linux-x86_64
- commit hash: 930e938
- commit date: 2025-05-01
- overall geometric mean: 1.002x faster
- HPT reliability: 60.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 256 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                       | 25.3 ms                                                                | 24.9 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed          | 498 ms                                                                 | 493 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 491 ms                                                                 | 487 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 463 ms                                                                 | 460 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 386 ms                                                                 | 384 ms: 1.01x faster                                                      |
| async_tree_memoization_tg        | 306 ms                                                                 | 309 ms: 1.01x slower                                                      |
| async_tree_eager_io_tg           | 613 ms                                                                 | 619 ms: 1.01x slower                                                      |
| async_tree_eager                 | 102 ms                                                                 | 105 ms: 1.03x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (11): async_generators, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_none_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_io, async_tree_eager_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 70.0 ms: 1.02x faster                                                     |
| nbody          | 98.0 ms                                                                | 99.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                                | 3.31 ms: 1.00x faster                                                     |
| regex_dna      | 206 ms                                                                 | 205 ms: 1.00x faster                                                      |
| regex_v8       | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.0 ms                                                                | 10.5 ms: 1.14x faster                                                     |
| tomli_loads          | 2.02 sec                                                               | 2.00 sec: 1.01x faster                                                    |
| xml_etree_generate   | 86.1 ms                                                                | 85.4 ms: 1.01x faster                                                     |
| xml_etree_process    | 60.2 ms                                                                | 59.9 ms: 1.01x faster                                                     |
| unpickle_pure_python | 220 us                                                                 | 219 us: 1.00x faster                                                      |
| pickle_pure_python   | 320 us                                                                 | 321 us: 1.01x slower                                                      |
| xml_etree_parse      | 141 ms                                                                 | 143 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                                | 6.93 ms: 1.00x slower                                                     |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| genshi_xml     | 49.5 ms                                                                | 50.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 | bm-20250501-linux-x86_64-nineteendo-speedup_json_encode-3.14.0a7+-930e938 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps                       | 12.0 ms                                                                | 10.5 ms: 1.14x faster                                                     |
| spectral_norm                    | 109 ms                                                                 | 105 ms: 1.03x faster                                                      |
| scimark_lu                       | 118 ms                                                                 | 116 ms: 1.02x faster                                                      |
| scimark_fft                      | 378 ms                                                                 | 371 ms: 1.02x faster                                                      |
| coroutines                       | 25.3 ms                                                                | 24.9 ms: 1.02x faster                                                     |
| gc_traversal                     | 4.89 ms                                                                | 4.81 ms: 1.02x faster                                                     |
| float                            | 71.1 ms                                                                | 70.0 ms: 1.02x faster                                                     |
| logging_silent                   | 98.7 ns                                                                | 97.2 ns: 1.02x faster                                                     |
| scimark_sor                      | 122 ms                                                                 | 120 ms: 1.01x faster                                                      |
| shortest_path                    | 509 ms                                                                 | 502 ms: 1.01x faster                                                      |
| coverage                         | 93.3 ms                                                                | 92.0 ms: 1.01x faster                                                     |
| crypto_pyaes                     | 75.9 ms                                                                | 74.8 ms: 1.01x faster                                                     |
| deltablue                        | 3.45 ms                                                                | 3.41 ms: 1.01x faster                                                     |
| tomli_loads                      | 2.02 sec                                                               | 2.00 sec: 1.01x faster                                                    |
| sqlglot_v2_parse                 | 1.25 ms                                                                | 1.24 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult          | 5.18 ms                                                                | 5.12 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed          | 498 ms                                                                 | 493 ms: 1.01x faster                                                      |
| bpe_tokeniser                    | 4.56 sec                                                               | 4.52 sec: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 491 ms                                                                 | 487 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 463 ms                                                                 | 460 ms: 1.01x faster                                                      |
| mako                             | 11.7 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| xml_etree_generate               | 86.1 ms                                                                | 85.4 ms: 1.01x faster                                                     |
| typing_runtime_protocols         | 168 us                                                                 | 167 us: 1.01x faster                                                      |
| sympy_sum                        | 150 ms                                                                 | 149 ms: 1.01x faster                                                      |
| richards                         | 43.7 ms                                                                | 43.4 ms: 1.01x faster                                                     |
| mdp                              | 1.24 sec                                                               | 1.24 sec: 1.01x faster                                                    |
| hexiom                           | 6.31 ms                                                                | 6.27 ms: 1.01x faster                                                     |
| sqlglot_v2_transpile             | 1.56 ms                                                                | 1.55 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 386 ms                                                                 | 384 ms: 1.01x faster                                                      |
| xml_etree_process                | 60.2 ms                                                                | 59.9 ms: 1.01x faster                                                     |
| sympy_integrate                  | 19.2 ms                                                                | 19.1 ms: 1.01x faster                                                     |
| comprehensions                   | 17.1 us                                                                | 17.0 us: 1.00x faster                                                     |
| meteor_contest                   | 107 ms                                                                 | 107 ms: 1.00x faster                                                      |
| nqueens                          | 82.3 ms                                                                | 81.9 ms: 1.00x faster                                                     |
| create_gc_cycles                 | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                                     |
| regex_effbot                     | 3.32 ms                                                                | 3.31 ms: 1.00x faster                                                     |
| unpickle_pure_python             | 220 us                                                                 | 219 us: 1.00x faster                                                      |
| regex_dna                        | 206 ms                                                                 | 205 ms: 1.00x faster                                                      |
| fannkuch                         | 421 ms                                                                 | 421 ms: 1.00x slower                                                      |
| python_startup_no_site           | 6.91 ms                                                                | 6.93 ms: 1.00x slower                                                     |
| 2to3                             | 255 ms                                                                 | 256 ms: 1.00x slower                                                      |
| python_startup                   | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                     |
| sqlalchemy_declarative           | 133 ms                                                                 | 133 ms: 1.00x slower                                                      |
| pyflate                          | 451 ms                                                                 | 453 ms: 1.00x slower                                                      |
| many_optionals                   | 937 us                                                                 | 941 us: 1.00x slower                                                      |
| sqlglot_v2_optimize              | 53.1 ms                                                                | 53.3 ms: 1.01x slower                                                     |
| pickle_pure_python               | 320 us                                                                 | 321 us: 1.01x slower                                                      |
| bench_mp_pool                    | 82.6 ms                                                                | 83.1 ms: 1.01x slower                                                     |
| sqlglot_v2_normalize             | 107 ms                                                                 | 108 ms: 1.01x slower                                                      |
| logging_simple                   | 5.57 us                                                                | 5.62 us: 1.01x slower                                                     |
| regex_v8                         | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                     |
| go                               | 113 ms                                                                 | 114 ms: 1.01x slower                                                      |
| async_tree_memoization_tg        | 306 ms                                                                 | 309 ms: 1.01x slower                                                      |
| dulwich_log                      | 60.1 ms                                                                | 60.6 ms: 1.01x slower                                                     |
| async_tree_eager_io_tg           | 613 ms                                                                 | 619 ms: 1.01x slower                                                      |
| xml_etree_parse                  | 141 ms                                                                 | 143 ms: 1.01x slower                                                      |
| telco                            | 7.93 ms                                                                | 8.01 ms: 1.01x slower                                                     |
| deepcopy                         | 257 us                                                                 | 260 us: 1.01x slower                                                      |
| nbody                            | 98.0 ms                                                                | 99.1 ms: 1.01x slower                                                     |
| genshi_xml                       | 49.5 ms                                                                | 50.1 ms: 1.01x slower                                                     |
| chaos                            | 59.6 ms                                                                | 60.7 ms: 1.02x slower                                                     |
| deepcopy_reduce                  | 2.72 us                                                                | 2.79 us: 1.02x slower                                                     |
| subparsers                       | 20.9 ms                                                                | 21.5 ms: 1.03x slower                                                     |
| raytrace                         | 272 ms                                                                 | 280 ms: 1.03x slower                                                      |
| async_tree_eager                 | 102 ms                                                                 | 105 ms: 1.03x slower                                                      |
| generators                       | 29.0 ms                                                                | 30.5 ms: 1.05x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (37): sqlite_synth, json, deepcopy_memo, connected_components, django_template, json_loads, pycparser, pathlib, async_generators, async_tree_memoization, sphinx, scimark_monte_carlo, async_tree_io_tg, docutils, regex_compile, bench_thread_pool, pidigits, asyncio_websockets, k_core, xml_etree_iterparse, sympy_str, html5lib, richards_super, pprint_safe_repr, sympy_expand, pylint, genshi_text, sqlalchemy_imperative, pprint_pformat, logging_format, async_tree_none, async_tree_none_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_io, async_tree_eager_tg, async_tree_eager_memoization_tg

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 60.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x