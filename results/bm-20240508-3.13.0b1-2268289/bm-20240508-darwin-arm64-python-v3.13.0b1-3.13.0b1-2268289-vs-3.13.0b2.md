# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b1
- machine: darwin-arm64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.01x slower
- HPT reliability: 99.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 179 ms: 1.11x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.35 ms: 1.02x slower                                      |
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                     |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                      |
| Geometric mean                   | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (13): async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                      |
| nbody          | 59.6 ms                                                    | 65.7 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 139 ms: 1.08x faster                                       |
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                      |
| regex_effbot   | 2.58 ms                                                    | 2.55 ms: 1.01x faster                                      |
| regex_compile  | 68.5 ms                                                    | 68.2 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 97.6 ms: 1.08x faster                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 67.5 ms: 1.06x faster                                      |
| xml_etree_generate   | 52.7 ms                                                    | 51.8 ms: 1.02x faster                                      |
| tomli_loads          | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                     |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| unpickle_pure_python | 141 us                                                     | 141 us: 1.00x slower                                       |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                      |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.02x slower                                       |
| json_dumps           | 6.23 ms                                                    | 6.35 ms: 1.02x slower                                      |
| json_loads           | 16.8 us                                                    | 17.3 us: 1.03x slower                                      |
| unpickle             | 9.12 us                                                    | 9.70 us: 1.06x slower                                      |
| unpickle_list        | 2.88 us                                                    | 3.31 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                      |
| python_startup         | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                      |
| Geometric mean         | (ref)                                                      | 1.06x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 6.99 ms                                                    | 6.88 ms: 1.02x faster                                      |
| genshi_text    | 13.9 ms                                                    | 13.8 ms: 1.00x faster                                      |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse                  | 106 ms                                                     | 97.6 ms: 1.08x faster                                      |
| regex_dna                        | 149 ms                                                     | 139 ms: 1.08x faster                                       |
| python_startup_no_site           | 12.3 ms                                                    | 11.6 ms: 1.06x faster                                      |
| xml_etree_iterparse              | 71.5 ms                                                    | 67.5 ms: 1.06x faster                                      |
| python_startup                   | 15.2 ms                                                    | 14.3 ms: 1.06x faster                                      |
| bench_mp_pool                    | 47.2 ms                                                    | 45.2 ms: 1.04x faster                                      |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                      |
| pathlib                          | 23.3 ms                                                    | 22.7 ms: 1.03x faster                                      |
| mdp                              | 1.53 sec                                                   | 1.50 sec: 1.02x faster                                     |
| xml_etree_generate               | 52.7 ms                                                    | 51.8 ms: 1.02x faster                                      |
| mako                             | 6.99 ms                                                    | 6.88 ms: 1.02x faster                                      |
| deepcopy_reduce                  | 1.82 us                                                    | 1.79 us: 1.02x faster                                      |
| regex_effbot                     | 2.58 ms                                                    | 2.55 ms: 1.01x faster                                      |
| create_gc_cycles                 | 897 us                                                     | 884 us: 1.01x faster                                       |
| async_generators                 | 281 ms                                                     | 278 ms: 1.01x faster                                       |
| generators                       | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                      |
| tomli_loads                      | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                     |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                      |
| deepcopy_memo                    | 22.6 us                                                    | 22.4 us: 1.01x faster                                      |
| telco                            | 4.60 ms                                                    | 4.56 ms: 1.01x faster                                      |
| dulwich_log                      | 27.6 ms                                                    | 27.3 ms: 1.01x faster                                      |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| regex_compile                    | 68.5 ms                                                    | 68.2 ms: 1.01x faster                                      |
| go                               | 101 ms                                                     | 100 ms: 1.00x faster                                       |
| pyflate                          | 321 ms                                                     | 319 ms: 1.00x faster                                       |
| genshi_text                      | 13.9 ms                                                    | 13.8 ms: 1.00x faster                                      |
| thrift                           | 435 us                                                     | 434 us: 1.00x faster                                       |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                       |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                      |
| unpickle_pure_python             | 141 us                                                     | 141 us: 1.00x slower                                       |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                       |
| meteor_contest                   | 70.3 ms                                                    | 70.6 ms: 1.00x slower                                      |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.00x slower                                      |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.1 ms: 1.01x slower                                      |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 333 ms: 1.01x slower                                       |
| logging_simple                   | 3.04 us                                                    | 3.06 us: 1.01x slower                                      |
| pprint_safe_repr                 | 465 ms                                                     | 468 ms: 1.01x slower                                       |
| hexiom                           | 4.06 ms                                                    | 4.09 ms: 1.01x slower                                      |
| float                            | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                      |
| sqlglot_transpile                | 891 us                                                     | 897 us: 1.01x slower                                       |
| sympy_str                        | 131 ms                                                     | 133 ms: 1.01x slower                                       |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                      |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                       |
| sqlglot_parse                    | 732 us                                                     | 739 us: 1.01x slower                                       |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                      |
| nqueens                          | 52.2 ms                                                    | 52.8 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                      |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                       |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.01x slower                                     |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.0 ms: 1.01x slower                                      |
| fannkuch                         | 248 ms                                                     | 252 ms: 1.01x slower                                       |
| scimark_sor                      | 94.9 ms                                                    | 96.3 ms: 1.01x slower                                      |
| logging_format                   | 3.31 us                                                    | 3.36 us: 1.01x slower                                      |
| sympy_sum                        | 69.2 ms                                                    | 70.2 ms: 1.01x slower                                      |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.02x slower                                       |
| crypto_pyaes                     | 49.5 ms                                                    | 50.3 ms: 1.02x slower                                      |
| chameleon                        | 4.27 ms                                                    | 4.35 ms: 1.02x slower                                      |
| raytrace                         | 147 ms                                                     | 150 ms: 1.02x slower                                       |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                      |
| json_dumps                       | 6.23 ms                                                    | 6.35 ms: 1.02x slower                                      |
| json                             | 2.93 ms                                                    | 2.99 ms: 1.02x slower                                      |
| scimark_lu                       | 66.9 ms                                                    | 68.3 ms: 1.02x slower                                      |
| json_loads                       | 16.8 us                                                    | 17.3 us: 1.03x slower                                      |
| spectral_norm                    | 66.4 ms                                                    | 68.2 ms: 1.03x slower                                      |
| coverage                         | 45.0 ms                                                    | 46.5 ms: 1.03x slower                                      |
| bench_thread_pool                | 447 us                                                     | 464 us: 1.04x slower                                       |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                       |
| chaos                            | 34.0 ms                                                    | 35.9 ms: 1.05x slower                                      |
| typing_runtime_protocols         | 87.6 us                                                    | 92.5 us: 1.06x slower                                      |
| unpickle                         | 9.12 us                                                    | 9.70 us: 1.06x slower                                      |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                      |
| gunicorn                         | 1.04 ms                                                    | 1.11 ms: 1.07x slower                                      |
| aiohttp                          | 997 us                                                     | 1.10 ms: 1.10x slower                                      |
| nbody                            | 59.6 ms                                                    | 65.7 ms: 1.10x slower                                      |
| 2to3                             | 161 ms                                                     | 179 ms: 1.11x slower                                       |
| unpickle_list                    | 2.88 us                                                    | 3.31 us: 1.15x slower                                      |
| mypy2                            | 379 ms                                                     | 461 ms: 1.22x slower                                       |
| flaskblogging                    | 3.61 ms                                                    | 5.10 ms: 1.41x slower                                      |
| Geometric mean                   | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (31): async_tree_eager_memoization, async_tree_eager_io_tg, dask, pylint, async_tree_memoization, deepcopy, pycparser, django_template, async_tree_none_tg, asyncio_tcp_ssl, richards_super, pickle, sympy_integrate, logging_silent, async_tree_io_tg, pidigits, pprint_pformat, html5lib, xml_etree_process, richards, genshi_xml, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_io, async_tree_eager_memoization_tg, async_tree_memoization_tg, asyncio_tcp, tornado_http
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 99.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x