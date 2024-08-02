# Results vs. 3.13.0b2

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-x86_64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x slower
- HPT reliability: 98.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 292 ms: 1.00x slower                                                         |
| chameleon      | 7.40 ms                                                          | 7.49 ms: 1.01x slower                                                        |
| html5lib       | 74.7 ms                                                          | 74.2 ms: 1.01x faster                                                        |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io  | 873 ms                                                           | 897 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                         |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                                         |
| regex_v8       | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.1 us: 1.09x faster                                                        |
| unpickle_pure_python | 224 us                                                           | 210 us: 1.07x faster                                                         |
| pickle_list          | 4.44 us                                                          | 4.30 us: 1.03x faster                                                        |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                        |
| unpickle             | 15.7 us                                                          | 15.4 us: 1.02x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.39 sec: 1.01x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 85.5 ms: 1.00x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 59.9 ms: 1.00x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 103 ms: 1.01x slower                                                         |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| unpickle_list        | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.82 ms: 1.00x faster                                                        |
| python_startup         | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                            | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                        |
| django_template | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict              | 32.8 us                                                          | 30.1 us: 1.09x faster                                                        |
| unpickle_pure_python     | 224 us                                                           | 210 us: 1.07x faster                                                         |
| genshi_xml               | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                        |
| gc_traversal             | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                        |
| go                       | 165 ms                                                           | 158 ms: 1.04x faster                                                         |
| pickle_list              | 4.44 us                                                          | 4.30 us: 1.03x faster                                                        |
| pickle                   | 10.6 us                                                          | 10.3 us: 1.03x faster                                                        |
| richards_super           | 61.2 ms                                                          | 59.8 ms: 1.02x faster                                                        |
| asyncio_websockets       | 395 ms                                                           | 387 ms: 1.02x faster                                                         |
| json                     | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                                        |
| unpickle                 | 15.7 us                                                          | 15.4 us: 1.02x faster                                                        |
| regex_dna                | 249 ms                                                           | 245 ms: 1.02x faster                                                         |
| json_loads               | 25.0 us                                                          | 24.6 us: 1.02x faster                                                        |
| deltablue                | 3.37 ms                                                          | 3.33 ms: 1.01x faster                                                        |
| tornado_http             | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| generators               | 33.5 ms                                                          | 33.2 ms: 1.01x faster                                                        |
| json_dumps               | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| scimark_sor              | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| tomli_loads              | 2.40 sec                                                         | 2.39 sec: 1.01x faster                                                       |
| hexiom                   | 6.35 ms                                                          | 6.31 ms: 1.01x faster                                                        |
| html5lib                 | 74.7 ms                                                          | 74.2 ms: 1.01x faster                                                        |
| regex_compile            | 144 ms                                                           | 143 ms: 1.01x faster                                                         |
| sympy_sum                | 155 ms                                                           | 154 ms: 1.00x faster                                                         |
| spectral_norm            | 97.3 ms                                                          | 96.9 ms: 1.00x faster                                                        |
| float                    | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                                        |
| coroutines               | 22.0 ms                                                          | 21.9 ms: 1.00x faster                                                        |
| python_startup_no_site   | 8.85 ms                                                          | 8.82 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                       |
| xml_etree_generate       | 85.7 ms                                                          | 85.5 ms: 1.00x faster                                                        |
| python_startup           | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| 2to3                     | 291 ms                                                           | 292 ms: 1.00x slower                                                         |
| xml_etree_process        | 59.7 ms                                                          | 59.9 ms: 1.00x slower                                                        |
| nqueens                  | 88.4 ms                                                          | 88.7 ms: 1.00x slower                                                        |
| meteor_contest           | 128 ms                                                           | 129 ms: 1.00x slower                                                         |
| regex_v8                 | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                        |
| sympy_expand             | 501 ms                                                           | 504 ms: 1.01x slower                                                         |
| pprint_safe_repr         | 818 ms                                                           | 823 ms: 1.01x slower                                                         |
| sqlglot_optimize         | 59.5 ms                                                          | 59.9 ms: 1.01x slower                                                        |
| pprint_pformat           | 1.66 sec                                                         | 1.67 sec: 1.01x slower                                                       |
| sympy_integrate          | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 103 ms                                                           | 103 ms: 1.01x slower                                                         |
| scimark_lu               | 97.5 ms                                                          | 98.4 ms: 1.01x slower                                                        |
| deepcopy_reduce          | 3.39 us                                                          | 3.43 us: 1.01x slower                                                        |
| mdp                      | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                       |
| django_template          | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                        |
| xml_etree_parse          | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| pycparser                | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                       |
| chameleon                | 7.40 ms                                                          | 7.49 ms: 1.01x slower                                                        |
| sqlite_synth             | 2.80 us                                                          | 2.84 us: 1.01x slower                                                        |
| sqlglot_normalize        | 120 ms                                                           | 122 ms: 1.02x slower                                                         |
| thrift                   | 880 us                                                           | 896 us: 1.02x slower                                                         |
| logging_simple           | 6.40 us                                                          | 6.52 us: 1.02x slower                                                        |
| deepcopy_memo            | 37.3 us                                                          | 38.0 us: 1.02x slower                                                        |
| unpickle_list            | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| pickle_pure_python       | 307 us                                                           | 314 us: 1.02x slower                                                         |
| typing_runtime_protocols | 171 us                                                           | 175 us: 1.02x slower                                                         |
| regex_effbot             | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                        |
| scimark_monte_carlo      | 65.5 ms                                                          | 67.1 ms: 1.02x slower                                                        |
| sqlglot_transpile        | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                        |
| telco                    | 8.40 ms                                                          | 8.61 ms: 1.03x slower                                                        |
| sqlglot_parse            | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                        |
| async_tree_io            | 873 ms                                                           | 897 ms: 1.03x slower                                                         |
| create_gc_cycles         | 2.00 ms                                                          | 2.06 ms: 1.03x slower                                                        |
| chaos                    | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.42 ms: 1.03x slower                                                        |
| fannkuch                 | 353 ms                                                           | 368 ms: 1.04x slower                                                         |
| raytrace                 | 260 ms                                                           | 276 ms: 1.06x slower                                                         |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (34): bench_mp_pool, bench_thread_pool, flaskblogging, genshi_text, logging_silent, scimark_fft, logging_format, mako, richards, pyflate, crypto_pyaes, pidigits, docutils, async_generators, asyncio_tcp, dulwich_log, deepcopy, sympy_str, pathlib, comprehensions, pylint, coverage, async_tree_none_tg, gunicorn, mypy2, aiohttp, async_tree_none, dask, async_tree_cpu_io_mixed_tg, async_tree_io_tg, nbody, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 98.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x