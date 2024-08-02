# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.00x slower
- HPT reliability: 98.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| chameleon      | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.00 sec: 1.00x slower                                                       |
| html5lib       | 74.7 ms                                                          | 73.6 ms: 1.01x faster                                                        |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 365 ms                                                           | 372 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed | 604 ms                                                           | 615 ms: 1.02x slower                                                         |
| Geometric mean          | (ref)                                                            | 1.02x slower                                                                 |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 248 ms: 1.01x faster                                                         |
| regex_v8       | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 211 us: 1.07x faster                                                         |
| pickle_dict          | 32.8 us                                                          | 30.8 us: 1.07x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.3 us: 1.03x faster                                                        |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.38 sec: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| pickle_list          | 4.44 us                                                          | 4.41 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 103 ms: 1.01x slower                                                         |
| unpickle             | 15.7 us                                                          | 15.8 us: 1.01x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                                         |
| xml_etree_process    | 59.7 ms                                                          | 60.4 ms: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| xml_etree_generate   | 85.7 ms                                                          | 86.8 ms: 1.01x slower                                                        |
| unpickle_list        | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.83 ms: 1.00x faster                                                        |
| python_startup         | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                            | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 56.3 ms: 1.03x faster                                                        |
| django_template | 39.0 ms                                                          | 38.1 ms: 1.02x faster                                                        |
| mako            | 10.4 ms                                                          | 10.3 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python     | 224 us                                                           | 211 us: 1.07x faster                                                         |
| pickle_dict              | 32.8 us                                                          | 30.8 us: 1.07x faster                                                        |
| gc_traversal             | 4.69 ms                                                          | 4.51 ms: 1.04x faster                                                        |
| go                       | 165 ms                                                           | 160 ms: 1.03x faster                                                         |
| genshi_xml               | 58.1 ms                                                          | 56.3 ms: 1.03x faster                                                        |
| json_loads               | 25.0 us                                                          | 24.3 us: 1.03x faster                                                        |
| pickle                   | 10.6 us                                                          | 10.3 us: 1.03x faster                                                        |
| generators               | 33.5 ms                                                          | 32.7 ms: 1.03x faster                                                        |
| richards_super           | 61.2 ms                                                          | 59.8 ms: 1.02x faster                                                        |
| django_template          | 39.0 ms                                                          | 38.1 ms: 1.02x faster                                                        |
| asyncio_websockets       | 395 ms                                                           | 388 ms: 1.02x faster                                                         |
| logging_format           | 7.11 us                                                          | 6.99 us: 1.02x faster                                                        |
| logging_simple           | 6.40 us                                                          | 6.31 us: 1.02x faster                                                        |
| html5lib                 | 74.7 ms                                                          | 73.6 ms: 1.01x faster                                                        |
| json                     | 5.35 ms                                                          | 5.29 ms: 1.01x faster                                                        |
| meteor_contest           | 128 ms                                                           | 127 ms: 1.01x faster                                                         |
| sqlglot_normalize        | 120 ms                                                           | 119 ms: 1.01x faster                                                         |
| mako                     | 10.4 ms                                                          | 10.3 ms: 1.01x faster                                                        |
| tornado_http             | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| sympy_sum                | 155 ms                                                           | 153 ms: 1.01x faster                                                         |
| scimark_monte_carlo      | 65.5 ms                                                          | 64.9 ms: 1.01x faster                                                        |
| tomli_loads              | 2.40 sec                                                         | 2.38 sec: 1.01x faster                                                       |
| asyncio_tcp              | 378 ms                                                           | 375 ms: 1.01x faster                                                         |
| json_dumps               | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| pyflate                  | 482 ms                                                           | 478 ms: 1.01x faster                                                         |
| pickle_list              | 4.44 us                                                          | 4.41 us: 1.01x faster                                                        |
| richards                 | 53.4 ms                                                          | 53.1 ms: 1.01x faster                                                        |
| regex_dna                | 249 ms                                                           | 248 ms: 1.01x faster                                                         |
| dulwich_log              | 67.3 ms                                                          | 67.0 ms: 1.00x faster                                                        |
| python_startup_no_site   | 8.85 ms                                                          | 8.83 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.27 ms: 1.00x faster                                                        |
| python_startup           | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                       |
| sqlglot_optimize         | 59.5 ms                                                          | 59.7 ms: 1.00x slower                                                        |
| sympy_str                | 295 ms                                                           | 296 ms: 1.00x slower                                                         |
| chameleon                | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                                        |
| pprint_pformat           | 1.66 sec                                                         | 1.67 sec: 1.00x slower                                                       |
| docutils                 | 2.98 sec                                                         | 3.00 sec: 1.00x slower                                                       |
| xml_etree_iterparse      | 103 ms                                                           | 103 ms: 1.01x slower                                                         |
| sympy_integrate          | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                                        |
| logging_silent           | 96.3 ns                                                          | 96.8 ns: 1.01x slower                                                        |
| nqueens                  | 88.4 ms                                                          | 88.9 ms: 1.01x slower                                                        |
| sympy_expand             | 501 ms                                                           | 504 ms: 1.01x slower                                                         |
| sqlglot_parse            | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                        |
| unpickle                 | 15.7 us                                                          | 15.8 us: 1.01x slower                                                        |
| sqlglot_transpile        | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                        |
| deepcopy_reduce          | 3.39 us                                                          | 3.42 us: 1.01x slower                                                        |
| scimark_lu               | 97.5 ms                                                          | 98.4 ms: 1.01x slower                                                        |
| pprint_safe_repr         | 818 ms                                                           | 825 ms: 1.01x slower                                                         |
| deepcopy_memo            | 37.3 us                                                          | 37.6 us: 1.01x slower                                                        |
| pickle_pure_python       | 307 us                                                           | 311 us: 1.01x slower                                                         |
| float                    | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                        |
| xml_etree_process        | 59.7 ms                                                          | 60.4 ms: 1.01x slower                                                        |
| xml_etree_parse          | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| deepcopy                 | 377 us                                                           | 382 us: 1.01x slower                                                         |
| spectral_norm            | 97.3 ms                                                          | 98.6 ms: 1.01x slower                                                        |
| xml_etree_generate       | 85.7 ms                                                          | 86.8 ms: 1.01x slower                                                        |
| hexiom                   | 6.35 ms                                                          | 6.44 ms: 1.01x slower                                                        |
| pathlib                  | 17.1 ms                                                          | 17.4 ms: 1.01x slower                                                        |
| fannkuch                 | 353 ms                                                           | 358 ms: 1.02x slower                                                         |
| async_tree_none          | 365 ms                                                           | 372 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 615 ms: 1.02x slower                                                         |
| regex_v8                 | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                        |
| chaos                    | 59.6 ms                                                          | 60.7 ms: 1.02x slower                                                        |
| unpickle_list            | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| thrift                   | 880 us                                                           | 897 us: 1.02x slower                                                         |
| sqlite_synth             | 2.80 us                                                          | 2.85 us: 1.02x slower                                                        |
| coverage                 | 83.5 ms                                                          | 85.3 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 171 us                                                           | 174 us: 1.02x slower                                                         |
| raytrace                 | 260 ms                                                           | 277 ms: 1.06x slower                                                         |
| regex_effbot             | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                        |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (30): bench_thread_pool, bench_mp_pool, gunicorn, pycparser, regex_compile, aiohttp, crypto_pyaes, flaskblogging, pidigits, deltablue, genshi_text, 2to3, scimark_sor, create_gc_cycles, comprehensions, telco, mdp, async_generators, coroutines, scimark_fft, pylint, mypy2, dask, async_tree_io_tg, async_tree_io, nbody, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 98.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x