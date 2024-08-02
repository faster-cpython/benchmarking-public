# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.00x faster
- HPT reliability: 97.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| chameleon      | 4.27 ms                                                    | 4.29 ms: 1.00x slower                                                 |
| html5lib       | 31.2 ms                                                    | 31.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_memoization, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                                 |
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 60.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 68.2 ms: 1.01x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 52.2 ms: 1.01x faster                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.46 sec: 1.01x faster                                                |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.01x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                 |
| pickle               | 7.48 us                                                    | 7.45 us: 1.00x faster                                                 |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.29 ms: 1.01x slower                                                 |
| pickle_list          | 2.96 us                                                    | 3.00 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.33 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (3): pickle_pure_python, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 14.0 ms: 1.08x faster                                                 |
| python_startup_no_site | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| mako           | 6.99 ms                                                    | 6.91 ms: 1.01x faster                                                 |
| genshi_xml     | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup                   | 15.2 ms                                                    | 14.0 ms: 1.08x faster                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                 |
| flaskblogging                    | 3.61 ms                                                    | 3.40 ms: 1.06x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 22.5 ms: 1.04x faster                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 45.7 ms: 1.03x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.49 sec: 1.03x faster                                                |
| richards                         | 31.8 ms                                                    | 31.1 ms: 1.02x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.79 us: 1.02x faster                                                 |
| deepcopy                         | 204 us                                                     | 200 us: 1.02x faster                                                  |
| thrift                           | 435 us                                                     | 428 us: 1.02x faster                                                  |
| genshi_text                      | 13.9 ms                                                    | 13.7 ms: 1.01x faster                                                 |
| xml_etree_parse                  | 106 ms                                                     | 104 ms: 1.01x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.91 ms: 1.01x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 52.2 ms: 1.01x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 94.0 ms: 1.01x faster                                                 |
| float                            | 48.6 ms                                                    | 48.2 ms: 1.01x faster                                                 |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                |
| meteor_contest                   | 70.3 ms                                                    | 69.8 ms: 1.01x faster                                                 |
| genshi_xml                       | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.46 sec: 1.01x faster                                                |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 31.0 ms: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                  |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.01x faster                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 42.2 ms: 1.01x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 68.2 ms: 1.01x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 462 ms: 1.00x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 943 ms: 1.00x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                 |
| pyflate                          | 321 ms                                                     | 320 ms: 1.00x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.45 us: 1.00x faster                                                 |
| go                               | 101 ms                                                     | 100 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| raytrace                         | 147 ms                                                     | 147 ms: 1.00x faster                                                  |
| logging_silent                   | 60.1 ns                                                    | 60.0 ns: 1.00x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| generators                       | 22.9 ms                                                    | 22.9 ms: 1.00x faster                                                 |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.61 ms: 1.00x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| regex_v8                         | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 49.6 ms: 1.00x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 15.9 ms: 1.00x slower                                                 |
| fannkuch                         | 248 ms                                                     | 249 ms: 1.00x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                 |
| chameleon                        | 4.27 ms                                                    | 4.29 ms: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                  |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.01x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.08 ms: 1.01x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 52.6 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                 |
| chaos                            | 34.0 ms                                                    | 34.3 ms: 1.01x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.29 ms: 1.01x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 69.9 ms: 1.01x slower                                                 |
| nbody                            | 59.6 ms                                                    | 60.3 ms: 1.01x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 3.00 us: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 910 us: 1.01x slower                                                  |
| coverage                         | 45.0 ms                                                    | 45.9 ms: 1.02x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.33 us: 1.02x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 463 us: 1.04x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 91.7 us: 1.05x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.7 us: 1.05x slower                                                 |
| 2to3                             | 161 ms                                                     | 182 ms: 1.13x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (32): async_tree_eager_io, dask, tornado_http, async_tree_memoization, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, scimark_sparse_mat_mult, pickle_pure_python, sympy_integrate, deltablue, pycparser, async_tree_eager_memoization_tg, docutils, scimark_lu, pickle_dict, async_tree_eager_memoization, scimark_fft, deepcopy_memo, async_tree_io_tg, django_template, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, async_tree_cpu_io_mixed, sqlglot_transpile, sympy_str, sqlglot_parse, async_tree_eager_tg, async_tree_io, pylint, asyncio_tcp
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2

# HPT report

- Reliability score: 97.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.33x