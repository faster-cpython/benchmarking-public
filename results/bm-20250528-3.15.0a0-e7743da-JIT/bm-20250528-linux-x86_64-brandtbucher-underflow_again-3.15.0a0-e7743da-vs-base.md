# Results vs. base

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: e7743da
- commit date: 2025-05-28
- overall geometric mean: 1.014x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 260 ms: 1.00x slower                                                   |
| docutils       | 2.63 sec                                                              | 1.02 sec: 2.58x faster                                                 |
| html5lib       | 61.8 ms                                                               | 62.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators                 | 426 ms                                                                | 428 ms: 1.01x slower                                                   |
| async_tree_eager_memoization_tg  | 279 ms                                                                | 283 ms: 1.02x slower                                                   |
| async_tree_eager_memoization     | 202 ms                                                                | 206 ms: 1.02x slower                                                   |
| async_tree_io                    | 597 ms                                                                | 608 ms: 1.02x slower                                                   |
| async_tree_eager_tg              | 214 ms                                                                | 218 ms: 1.02x slower                                                   |
| async_tree_eager                 | 104 ms                                                                | 106 ms: 1.02x slower                                                   |
| async_tree_memoization           | 313 ms                                                                | 320 ms: 1.02x slower                                                   |
| async_tree_none_tg               | 247 ms                                                                | 253 ms: 1.03x slower                                                   |
| coroutines                       | 25.2 ms                                                               | 26.0 ms: 1.03x slower                                                  |
| async_tree_none                  | 259 ms                                                                | 268 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 457 ms                                                                | 474 ms: 1.04x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 383 ms                                                                | 398 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed          | 488 ms                                                                | 507 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 481 ms                                                                | 501 ms: 1.04x slower                                                   |
| Geometric mean                   | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (5): async_tree_io_tg, asyncio_websockets, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                | 191 ms: 1.02x faster                                                   |
| nbody          | 89.5 ms                                                               | 89.0 ms: 1.01x faster                                                  |
| float          | 64.0 ms                                                               | 64.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.10 ms                                                               | 3.08 ms: 1.01x faster                                                  |
| regex_v8       | 21.9 ms                                                               | 22.0 ms: 1.00x slower                                                  |
| regex_dna      | 187 ms                                                                | 189 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                  |
| unpickle_pure_python | 199 us                                                                | 200 us: 1.01x slower                                                   |
| pickle_pure_python   | 321 us                                                                | 325 us: 1.01x slower                                                   |
| tomli_loads          | 1.90 sec                                                              | 1.96 sec: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (5): json_loads, xml_etree_iterparse, xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.93 ms                                                               | 6.95 ms: 1.00x slower                                                  |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 49.7 ms                                                               | 50.1 ms: 1.01x slower                                                  |
| genshi_text    | 21.5 ms                                                               | 21.7 ms: 1.01x slower                                                  |
| mako           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils                         | 2.63 sec                                                              | 1.02 sec: 2.58x faster                                                 |
| generators                       | 31.0 ms                                                               | 29.9 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 76.3 ms                                                               | 74.5 ms: 1.02x faster                                                  |
| pidigits                         | 195 ms                                                                | 191 ms: 1.02x faster                                                   |
| fannkuch                         | 419 ms                                                                | 412 ms: 1.02x faster                                                   |
| connected_components             | 458 ms                                                                | 451 ms: 1.02x faster                                                   |
| scimark_lu                       | 119 ms                                                                | 117 ms: 1.02x faster                                                   |
| json_dumps                       | 11.2 ms                                                               | 11.1 ms: 1.01x faster                                                  |
| json                             | 5.33 ms                                                               | 5.25 ms: 1.01x faster                                                  |
| shortest_path                    | 496 ms                                                                | 490 ms: 1.01x faster                                                   |
| subparsers                       | 23.7 ms                                                               | 23.4 ms: 1.01x faster                                                  |
| regex_effbot                     | 3.10 ms                                                               | 3.08 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult          | 4.98 ms                                                               | 4.95 ms: 1.01x faster                                                  |
| nbody                            | 89.5 ms                                                               | 89.0 ms: 1.01x faster                                                  |
| create_gc_cycles                 | 2.60 ms                                                               | 2.59 ms: 1.00x faster                                                  |
| gc_traversal                     | 5.10 ms                                                               | 5.11 ms: 1.00x slower                                                  |
| python_startup_no_site           | 6.93 ms                                                               | 6.95 ms: 1.00x slower                                                  |
| 2to3                             | 260 ms                                                                | 260 ms: 1.00x slower                                                   |
| python_startup                   | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                  |
| deepcopy                         | 258 us                                                                | 259 us: 1.00x slower                                                   |
| regex_v8                         | 21.9 ms                                                               | 22.0 ms: 1.00x slower                                                  |
| async_generators                 | 426 ms                                                                | 428 ms: 1.01x slower                                                   |
| sympy_sum                        | 149 ms                                                                | 150 ms: 1.01x slower                                                   |
| bench_thread_pool                | 893 us                                                                | 897 us: 1.01x slower                                                   |
| meteor_contest                   | 104 ms                                                                | 105 ms: 1.01x slower                                                   |
| sqlite_synth                     | 2.78 us                                                               | 2.80 us: 1.01x slower                                                  |
| sqlglot_v2_optimize              | 52.6 ms                                                               | 53.0 ms: 1.01x slower                                                  |
| dulwich_log                      | 61.5 ms                                                               | 62.0 ms: 1.01x slower                                                  |
| sqlglot_v2_normalize             | 106 ms                                                                | 106 ms: 1.01x slower                                                   |
| html5lib                         | 61.8 ms                                                               | 62.3 ms: 1.01x slower                                                  |
| genshi_xml                       | 49.7 ms                                                               | 50.1 ms: 1.01x slower                                                  |
| pathlib                          | 17.2 ms                                                               | 17.3 ms: 1.01x slower                                                  |
| dask                             | 919 ms                                                                | 927 ms: 1.01x slower                                                   |
| genshi_text                      | 21.5 ms                                                               | 21.7 ms: 1.01x slower                                                  |
| unpickle_pure_python             | 199 us                                                                | 200 us: 1.01x slower                                                   |
| sympy_expand                     | 462 ms                                                                | 466 ms: 1.01x slower                                                   |
| sympy_str                        | 269 ms                                                                | 271 ms: 1.01x slower                                                   |
| deepcopy_memo                    | 29.3 us                                                               | 29.6 us: 1.01x slower                                                  |
| float                            | 64.0 ms                                                               | 64.6 ms: 1.01x slower                                                  |
| comprehensions                   | 16.9 us                                                               | 17.1 us: 1.01x slower                                                  |
| hexiom                           | 6.40 ms                                                               | 6.47 ms: 1.01x slower                                                  |
| pickle_pure_python               | 321 us                                                                | 325 us: 1.01x slower                                                   |
| mako                             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| scimark_sor                      | 120 ms                                                                | 122 ms: 1.01x slower                                                   |
| logging_format                   | 6.89 us                                                               | 6.98 us: 1.01x slower                                                  |
| coverage                         | 421 ms                                                                | 426 ms: 1.01x slower                                                   |
| sqlglot_v2_parse                 | 1.26 ms                                                               | 1.28 ms: 1.01x slower                                                  |
| logging_simple                   | 6.15 us                                                               | 6.24 us: 1.02x slower                                                  |
| regex_dna                        | 187 ms                                                                | 189 ms: 1.02x slower                                                   |
| async_tree_eager_memoization_tg  | 279 ms                                                                | 283 ms: 1.02x slower                                                   |
| async_tree_eager_memoization     | 202 ms                                                                | 206 ms: 1.02x slower                                                   |
| deltablue                        | 3.06 ms                                                               | 3.12 ms: 1.02x slower                                                  |
| async_tree_io                    | 597 ms                                                                | 608 ms: 1.02x slower                                                   |
| pprint_pformat                   | 1.42 us                                                               | 1.45 us: 1.02x slower                                                  |
| async_tree_eager_tg              | 214 ms                                                                | 218 ms: 1.02x slower                                                   |
| async_tree_eager                 | 104 ms                                                                | 106 ms: 1.02x slower                                                   |
| chaos                            | 61.3 ms                                                               | 62.7 ms: 1.02x slower                                                  |
| raytrace                         | 270 ms                                                                | 277 ms: 1.02x slower                                                   |
| async_tree_memoization           | 313 ms                                                                | 320 ms: 1.02x slower                                                   |
| spectral_norm                    | 100 ms                                                                | 103 ms: 1.03x slower                                                   |
| async_tree_none_tg               | 247 ms                                                                | 253 ms: 1.03x slower                                                   |
| deepcopy_reduce                  | 2.70 us                                                               | 2.78 us: 1.03x slower                                                  |
| coroutines                       | 25.2 ms                                                               | 26.0 ms: 1.03x slower                                                  |
| nqueens                          | 81.8 ms                                                               | 84.3 ms: 1.03x slower                                                  |
| pprint_safe_repr                 | 835 ns                                                                | 861 ns: 1.03x slower                                                   |
| scimark_monte_carlo              | 66.4 ms                                                               | 68.4 ms: 1.03x slower                                                  |
| async_tree_none                  | 259 ms                                                                | 268 ms: 1.03x slower                                                   |
| telco                            | 7.65 ms                                                               | 7.91 ms: 1.03x slower                                                  |
| tomli_loads                      | 1.90 sec                                                              | 1.96 sec: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 457 ms                                                                | 474 ms: 1.04x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 383 ms                                                                | 398 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed          | 488 ms                                                                | 507 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 481 ms                                                                | 501 ms: 1.04x slower                                                   |
| pycparser                        | 1.11 sec                                                              | 1.17 sec: 1.06x slower                                                 |
| richards                         | 33.6 ms                                                               | 35.7 ms: 1.06x slower                                                  |
| pyflate                          | 409 ms                                                                | 441 ms: 1.08x slower                                                   |
| richards_super                   | 37.9 ms                                                               | 41.4 ms: 1.09x slower                                                  |
| go                               | 121 ms                                                                | 135 ms: 1.12x slower                                                   |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (24): async_tree_io_tg, json_loads, django_template, k_core, logging_silent, pylint, typing_runtime_protocols, sympy_integrate, xml_etree_iterparse, asyncio_websockets, mdp, sphinx, bpe_tokeniser, bench_mp_pool, thrift, xml_etree_parse, xml_etree_generate, many_optionals, scimark_fft, xml_etree_process, sqlglot_v2_transpile, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager_io_tg

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x