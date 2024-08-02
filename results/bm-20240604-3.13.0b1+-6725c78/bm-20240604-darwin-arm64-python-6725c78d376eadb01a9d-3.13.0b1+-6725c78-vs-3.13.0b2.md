# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.00x faster
- HPT reliability: 58.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 4.27 ms                                                    | 4.31 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                 |
| html5lib       | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (13): async_tree_eager_io_tg, async_tree_eager_io, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                  |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 102 ms: 1.03x faster                                                   |
| tomli_loads          | 1.47 sec                                                   | 1.44 sec: 1.02x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 178 us: 1.00x faster                                                   |
| xml_etree_process    | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                                  |
| unpickle             | 9.12 us                                                    | 9.22 us: 1.01x slower                                                  |
| pickle_dict          | 18.3 us                                                    | 18.5 us: 1.01x slower                                                  |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                   |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.42 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (2): pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.2 ms: 1.10x faster                                                  |
| python_startup         | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                  |
| genshi_text    | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| flaskblogging                    | 3.61 ms                                                    | 3.06 ms: 1.18x faster                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 11.2 ms: 1.10x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.41 sec: 1.09x faster                                                 |
| python_startup                   | 15.2 ms                                                    | 14.2 ms: 1.07x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                 |
| pathlib                          | 23.3 ms                                                    | 22.5 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 102 ms: 1.03x faster                                                   |
| dask                             | 221 ms                                                     | 217 ms: 1.02x faster                                                   |
| tomli_loads                      | 1.47 sec                                                   | 1.44 sec: 1.02x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.80 us: 1.01x faster                                                  |
| pyflate                          | 321 ms                                                     | 317 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                    | 1.53 us: 1.01x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 942 ms: 1.00x faster                                                   |
| docutils                         | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.58 ms: 1.00x faster                                                  |
| meteor_contest                   | 70.3 ms                                                    | 70.0 ms: 1.00x faster                                                  |
| pickle_pure_python               | 179 us                                                     | 178 us: 1.00x faster                                                   |
| regex_dna                        | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| sympy_expand                     | 226 ms                                                     | 226 ms: 1.00x slower                                                   |
| nqueens                          | 52.2 ms                                                    | 52.4 ms: 1.00x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 332 ms: 1.00x slower                                                   |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                                   |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.4 ms: 1.00x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 901 us: 1.01x slower                                                   |
| deltablue                        | 2.14 ms                                                    | 2.15 ms: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 66.8 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 69.7 ms: 1.01x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 897 us: 1.01x slower                                                   |
| xml_etree_process                | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 738 us: 1.01x slower                                                   |
| html5lib                         | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.09 ms: 1.01x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 49.9 ms: 1.01x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.07 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                                  |
| chameleon                        | 4.27 ms                                                    | 4.31 ms: 1.01x slower                                                  |
| generators                       | 22.9 ms                                                    | 23.1 ms: 1.01x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.22 us: 1.01x slower                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.5 us: 1.01x slower                                                  |
| pycparser                        | 632 ms                                                     | 639 ms: 1.01x slower                                                   |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                   |
| scimark_fft                      | 181 ms                                                     | 183 ms: 1.01x slower                                                   |
| unpickle_pure_python             | 141 us                                                     | 142 us: 1.01x slower                                                   |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                  |
| nbody                            | 59.6 ms                                                    | 60.9 ms: 1.02x slower                                                  |
| chaos                            | 34.0 ms                                                    | 34.8 ms: 1.02x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 61.6 ns: 1.02x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 459 us: 1.03x slower                                                   |
| gunicorn                         | 1.04 ms                                                    | 1.06 ms: 1.03x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.42 ms: 1.03x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 90.5 us: 1.03x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (45): async_tree_eager_io_tg, async_tree_eager_io, tornado_http, bench_mp_pool, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, pylint, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_generators, django_template, genshi_xml, scimark_lu, pprint_safe_repr, thrift, dulwich_log, async_tree_eager_memoization_tg, scimark_sor, richards_super, sympy_str, deepcopy_memo, async_tree_cpu_io_mixed_tg, regex_compile, richards, asyncio_websockets, deepcopy, 2to3, mypy2, regex_v8, scimark_monte_carlo, pidigits, go, fannkuch, pickle, async_tree_eager_cpu_io_mixed, float, xml_etree_iterparse, aiohttp, coverage, json, asyncio_tcp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 58.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.52x