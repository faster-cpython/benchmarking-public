# Results vs. base

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 0cb6e84
- commit date: 2025-04-28
- overall geometric mean: 1.000x slower
- HPT reliability: 54.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 468 ms                                                                 | 450 ms: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 375 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 477 ms: 1.03x faster                                                |
| coroutines                       | 24.6 ms                                                                | 23.8 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 482 ms: 1.03x faster                                                |
| async_generators                 | 399 ms                                                                 | 396 ms: 1.01x faster                                                |
| async_tree_memoization_tg        | 309 ms                                                                 | 307 ms: 1.01x faster                                                |
| async_tree_eager                 | 101 ms                                                                 | 101 ms: 1.00x faster                                                |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_none, async_tree_memoization, asyncio_websockets, async_tree_eager_memoization, async_tree_io, async_tree_eager_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                 | 190 ms: 1.00x faster                                                |
| float          | 68.7 ms                                                                | 69.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.4 ms                                                                | 22.2 ms: 1.05x faster                                               |
| regex_effbot   | 3.22 ms                                                                | 3.14 ms: 1.02x faster                                               |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| regex_dna      | 210 ms                                                                 | 208 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                 | 215 us: 1.01x faster                                                |
| xml_etree_process    | 59.5 ms                                                                | 59.0 ms: 1.01x faster                                               |
| xml_etree_generate   | 84.8 ms                                                                | 84.3 ms: 1.01x faster                                               |
| tomli_loads          | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                              |
| json_dumps           | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                               |
| json_loads           | 29.8 us                                                                | 30.4 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.00x slower                                               |
| python_startup_no_site | 8.21 ms                                                                | 8.24 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 31.7 ms                                                                | 31.5 ms: 1.00x faster                                               |
| mako            | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| genshi_text     | 20.9 ms                                                                | 21.4 ms: 1.02x slower                                               |
| genshi_xml      | 48.7 ms                                                                | 49.9 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                        | bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7+-5f50541 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8                         | 23.4 ms                                                                | 22.2 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 468 ms                                                                 | 450 ms: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 375 ms: 1.04x faster                                                |
| shortest_path                    | 508 ms                                                                 | 491 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 477 ms: 1.03x faster                                                |
| coroutines                       | 24.6 ms                                                                | 23.8 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 482 ms: 1.03x faster                                                |
| generators                       | 30.3 ms                                                                | 29.5 ms: 1.03x faster                                               |
| regex_effbot                     | 3.22 ms                                                                | 3.14 ms: 1.02x faster                                               |
| typing_runtime_protocols         | 172 us                                                                 | 168 us: 1.02x faster                                                |
| deepcopy_reduce                  | 2.70 us                                                                | 2.65 us: 1.02x faster                                               |
| telco                            | 7.93 ms                                                                | 7.79 ms: 1.02x faster                                               |
| gc_traversal                     | 5.06 ms                                                                | 4.98 ms: 1.02x faster                                               |
| comprehensions                   | 16.8 us                                                                | 16.5 us: 1.02x faster                                               |
| coverage                         | 93.7 ms                                                                | 92.3 ms: 1.02x faster                                               |
| chaos                            | 56.6 ms                                                                | 56.0 ms: 1.01x faster                                               |
| regex_compile                    | 126 ms                                                                 | 125 ms: 1.01x faster                                                |
| unpickle_pure_python             | 217 us                                                                 | 215 us: 1.01x faster                                                |
| deltablue                        | 3.36 ms                                                                | 3.32 ms: 1.01x faster                                               |
| deepcopy                         | 254 us                                                                 | 252 us: 1.01x faster                                                |
| sqlite_synth                     | 2.83 us                                                                | 2.81 us: 1.01x faster                                               |
| mdp                              | 1.22 sec                                                               | 1.21 sec: 1.01x faster                                              |
| regex_dna                        | 210 ms                                                                 | 208 ms: 1.01x faster                                                |
| crypto_pyaes                     | 73.7 ms                                                                | 73.1 ms: 1.01x faster                                               |
| nqueens                          | 80.9 ms                                                                | 80.2 ms: 1.01x faster                                               |
| xml_etree_process                | 59.5 ms                                                                | 59.0 ms: 1.01x faster                                               |
| async_generators                 | 399 ms                                                                 | 396 ms: 1.01x faster                                                |
| xml_etree_generate               | 84.8 ms                                                                | 84.3 ms: 1.01x faster                                               |
| connected_components             | 457 ms                                                                 | 454 ms: 1.01x faster                                                |
| async_tree_memoization_tg        | 309 ms                                                                 | 307 ms: 1.01x faster                                                |
| raytrace                         | 262 ms                                                                 | 260 ms: 1.01x faster                                                |
| fannkuch                         | 420 ms                                                                 | 418 ms: 1.01x faster                                                |
| django_template                  | 31.7 ms                                                                | 31.5 ms: 1.00x faster                                               |
| pidigits                         | 191 ms                                                                 | 190 ms: 1.00x faster                                                |
| async_tree_eager                 | 101 ms                                                                 | 101 ms: 1.00x faster                                                |
| sqlalchemy_declarative           | 132 ms                                                                 | 131 ms: 1.00x faster                                                |
| bpe_tokeniser                    | 4.47 sec                                                               | 4.45 sec: 1.00x faster                                              |
| many_optionals                   | 935 us                                                                 | 933 us: 1.00x faster                                                |
| create_gc_cycles                 | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| sympy_str                        | 264 ms                                                                 | 265 ms: 1.00x slower                                                |
| python_startup                   | 13.2 ms                                                                | 13.3 ms: 1.00x slower                                               |
| python_startup_no_site           | 8.21 ms                                                                | 8.24 ms: 1.00x slower                                               |
| sympy_expand                     | 449 ms                                                                 | 451 ms: 1.00x slower                                                |
| scimark_monte_carlo              | 67.5 ms                                                                | 68.0 ms: 1.01x slower                                               |
| pprint_pformat                   | 1.45 sec                                                               | 1.46 sec: 1.01x slower                                              |
| sympy_sum                        | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| pyflate                          | 449 ms                                                                 | 454 ms: 1.01x slower                                                |
| pathlib                          | 17.1 ms                                                                | 17.3 ms: 1.01x slower                                               |
| richards                         | 42.7 ms                                                                | 43.2 ms: 1.01x slower                                               |
| float                            | 68.7 ms                                                                | 69.4 ms: 1.01x slower                                               |
| sympy_integrate                  | 18.8 ms                                                                | 19.0 ms: 1.01x slower                                               |
| mako                             | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| tomli_loads                      | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                              |
| logging_simple                   | 5.49 us                                                                | 5.56 us: 1.01x slower                                               |
| richards_super                   | 49.0 ms                                                                | 49.7 ms: 1.01x slower                                               |
| logging_format                   | 6.03 us                                                                | 6.13 us: 1.02x slower                                               |
| json_dumps                       | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                               |
| sqlglot_v2_parse                 | 1.21 ms                                                                | 1.24 ms: 1.02x slower                                               |
| json_loads                       | 29.8 us                                                                | 30.4 us: 1.02x slower                                               |
| sqlglot_v2_transpile             | 1.52 ms                                                                | 1.55 ms: 1.02x slower                                               |
| spectral_norm                    | 103 ms                                                                 | 104 ms: 1.02x slower                                                |
| deepcopy_memo                    | 28.1 us                                                                | 28.7 us: 1.02x slower                                               |
| genshi_text                      | 20.9 ms                                                                | 21.4 ms: 1.02x slower                                               |
| genshi_xml                       | 48.7 ms                                                                | 49.9 ms: 1.03x slower                                               |
| pycparser                        | 1.12 sec                                                               | 1.16 sec: 1.03x slower                                              |
| scimark_lu                       | 120 ms                                                                 | 124 ms: 1.04x slower                                                |
| scimark_sor                      | 117 ms                                                                 | 122 ms: 1.04x slower                                                |
| scimark_fft                      | 354 ms                                                                 | 382 ms: 1.08x slower                                                |
| scimark_sparse_mat_mult          | 5.01 ms                                                                | 5.50 ms: 1.10x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (34): async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, html5lib, async_tree_io_tg, sphinx, sqlalchemy_imperative, pickle_pure_python, xml_etree_parse, bench_mp_pool, async_tree_none, async_tree_memoization, dulwich_log, asyncio_websockets, 2to3, logging_silent, bench_thread_pool, hexiom, pylint, sqlglot_v2_optimize, sqlglot_v2_normalize, go, async_tree_eager_memoization, docutils, async_tree_io, async_tree_eager_io_tg, subparsers, meteor_contest, async_tree_eager_io, json, pprint_safe_repr, xml_etree_iterparse, nbody, k_core

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 54.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x