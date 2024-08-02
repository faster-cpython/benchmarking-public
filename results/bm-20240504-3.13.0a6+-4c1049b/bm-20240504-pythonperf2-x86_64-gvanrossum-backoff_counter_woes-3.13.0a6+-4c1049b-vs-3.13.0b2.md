# Results vs. 3.13.0b2

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 288 ms: 1.01x faster                                                             |
| chameleon      | 7.40 ms                                                          | 7.86 ms: 1.06x slower                                                            |
| docutils       | 2.98 sec                                                         | 3.02 sec: 1.01x slower                                                           |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 365 ms                                                           | 371 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 604 ms                                                           | 618 ms: 1.02x slower                                                             |
| Geometric mean          | (ref)                                                            | 1.01x slower                                                                     |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 80.6 ms: 1.01x slower                                                            |
| pidigits       | 254 ms                                                           | 257 ms: 1.01x slower                                                             |
| nbody          | 87.8 ms                                                          | 89.9 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                             |
| regex_effbot   | 3.40 ms                                                          | 3.42 ms: 1.01x slower                                                            |
| regex_compile  | 144 ms                                                           | 148 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.9 us: 1.06x faster                                                            |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                            |
| unpickle_pure_python | 224 us                                                           | 215 us: 1.04x faster                                                             |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                            |
| json_loads           | 25.0 us                                                          | 24.8 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                           | 103 ms: 1.01x slower                                                             |
| xml_etree_process    | 59.7 ms                                                          | 60.3 ms: 1.01x slower                                                            |
| pickle_list          | 4.44 us                                                          | 4.52 us: 1.02x slower                                                            |
| unpickle_list        | 4.70 us                                                          | 4.82 us: 1.03x slower                                                            |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                            |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                             |
| xml_etree_generate   | 85.7 ms                                                          | 88.6 ms: 1.03x slower                                                            |
| tomli_loads          | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.8 ms: 1.03x faster                                                            |
| python_startup_no_site | 8.85 ms                                                          | 8.80 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                            | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 56.7 ms: 1.02x faster                                                            |
| django_template | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                            |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                            | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| bench_mp_pool            | 4.91 ms                                                          | 4.57 ms: 1.07x faster                                                            |
| pickle_dict              | 32.8 us                                                          | 30.9 us: 1.06x faster                                                            |
| unpickle                 | 15.7 us                                                          | 14.8 us: 1.06x faster                                                            |
| regex_dna                | 249 ms                                                           | 235 ms: 1.06x faster                                                             |
| scimark_fft              | 312 ms                                                           | 297 ms: 1.05x faster                                                             |
| scimark_sor              | 119 ms                                                           | 113 ms: 1.05x faster                                                             |
| unpickle_pure_python     | 224 us                                                           | 215 us: 1.04x faster                                                             |
| python_startup           | 13.2 ms                                                          | 12.8 ms: 1.03x faster                                                            |
| pickle                   | 10.6 us                                                          | 10.3 us: 1.03x faster                                                            |
| spectral_norm            | 97.3 ms                                                          | 94.7 ms: 1.03x faster                                                            |
| pyflate                  | 482 ms                                                           | 470 ms: 1.02x faster                                                             |
| genshi_xml               | 58.1 ms                                                          | 56.7 ms: 1.02x faster                                                            |
| chaos                    | 59.6 ms                                                          | 58.8 ms: 1.01x faster                                                            |
| 2to3                     | 291 ms                                                           | 288 ms: 1.01x faster                                                             |
| asyncio_websockets       | 395 ms                                                           | 390 ms: 1.01x faster                                                             |
| dulwich_log              | 67.3 ms                                                          | 66.5 ms: 1.01x faster                                                            |
| hexiom                   | 6.35 ms                                                          | 6.29 ms: 1.01x faster                                                            |
| go                       | 165 ms                                                           | 163 ms: 1.01x faster                                                             |
| json_loads               | 25.0 us                                                          | 24.8 us: 1.01x faster                                                            |
| asyncio_tcp              | 378 ms                                                           | 375 ms: 1.01x faster                                                             |
| async_generators         | 363 ms                                                           | 360 ms: 1.01x faster                                                             |
| deltablue                | 3.37 ms                                                          | 3.35 ms: 1.01x faster                                                            |
| pprint_safe_repr         | 818 ms                                                           | 813 ms: 1.01x faster                                                             |
| python_startup_no_site   | 8.85 ms                                                          | 8.80 ms: 1.01x faster                                                            |
| gc_traversal             | 4.69 ms                                                          | 4.67 ms: 1.00x faster                                                            |
| sqlite_synth             | 2.80 us                                                          | 2.79 us: 1.00x faster                                                            |
| coverage                 | 83.5 ms                                                          | 83.2 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                           |
| scimark_monte_carlo      | 65.5 ms                                                          | 65.4 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.30 ms: 1.00x slower                                                            |
| xml_etree_iterparse      | 103 ms                                                           | 103 ms: 1.01x slower                                                             |
| float                    | 80.2 ms                                                          | 80.6 ms: 1.01x slower                                                            |
| regex_effbot             | 3.40 ms                                                          | 3.42 ms: 1.01x slower                                                            |
| raytrace                 | 260 ms                                                           | 262 ms: 1.01x slower                                                             |
| thrift                   | 880 us                                                           | 886 us: 1.01x slower                                                             |
| django_template          | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                            |
| logging_silent           | 96.3 ns                                                          | 97.1 ns: 1.01x slower                                                            |
| xml_etree_process        | 59.7 ms                                                          | 60.3 ms: 1.01x slower                                                            |
| fannkuch                 | 353 ms                                                           | 357 ms: 1.01x slower                                                             |
| sympy_sum                | 155 ms                                                           | 157 ms: 1.01x slower                                                             |
| sqlglot_normalize        | 120 ms                                                           | 122 ms: 1.01x slower                                                             |
| mako                     | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                            |
| pidigits                 | 254 ms                                                           | 257 ms: 1.01x slower                                                             |
| mdp                      | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                           |
| sqlglot_parse            | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                            |
| docutils                 | 2.98 sec                                                         | 3.02 sec: 1.01x slower                                                           |
| logging_format           | 7.11 us                                                          | 7.21 us: 1.01x slower                                                            |
| meteor_contest           | 128 ms                                                           | 130 ms: 1.01x slower                                                             |
| deepcopy_reduce          | 3.39 us                                                          | 3.44 us: 1.01x slower                                                            |
| async_tree_none          | 365 ms                                                           | 371 ms: 1.02x slower                                                             |
| generators               | 33.5 ms                                                          | 34.1 ms: 1.02x slower                                                            |
| pickle_list              | 4.44 us                                                          | 4.52 us: 1.02x slower                                                            |
| sympy_integrate          | 23.2 ms                                                          | 23.6 ms: 1.02x slower                                                            |
| sqlglot_transpile        | 1.76 ms                                                          | 1.79 ms: 1.02x slower                                                            |
| deepcopy                 | 377 us                                                           | 384 us: 1.02x slower                                                             |
| richards                 | 53.4 ms                                                          | 54.4 ms: 1.02x slower                                                            |
| comprehensions           | 17.0 us                                                          | 17.3 us: 1.02x slower                                                            |
| sympy_str                | 295 ms                                                           | 301 ms: 1.02x slower                                                             |
| crypto_pyaes             | 73.6 ms                                                          | 75.1 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 618 ms: 1.02x slower                                                             |
| nbody                    | 87.8 ms                                                          | 89.9 ms: 1.02x slower                                                            |
| regex_compile            | 144 ms                                                           | 148 ms: 1.02x slower                                                             |
| aiohttp                  | 1.07 ms                                                          | 1.10 ms: 1.02x slower                                                            |
| sympy_expand             | 501 ms                                                           | 513 ms: 1.02x slower                                                             |
| deepcopy_memo            | 37.3 us                                                          | 38.3 us: 1.03x slower                                                            |
| unpickle_list            | 4.70 us                                                          | 4.82 us: 1.03x slower                                                            |
| json_dumps               | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                            |
| logging_simple           | 6.40 us                                                          | 6.59 us: 1.03x slower                                                            |
| json                     | 5.35 ms                                                          | 5.51 ms: 1.03x slower                                                            |
| pickle_pure_python       | 307 us                                                           | 317 us: 1.03x slower                                                             |
| xml_etree_generate       | 85.7 ms                                                          | 88.6 ms: 1.03x slower                                                            |
| typing_runtime_protocols | 171 us                                                           | 179 us: 1.05x slower                                                             |
| chameleon                | 7.40 ms                                                          | 7.86 ms: 1.06x slower                                                            |
| tomli_loads              | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                           |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                     |

Benchmark hidden because not significant (27): async_tree_io_tg, telco, flaskblogging, async_tree_io, scimark_lu, pathlib, pycparser, pprint_pformat, coroutines, genshi_text, sqlglot_optimize, richards_super, html5lib, nqueens, xml_etree_parse, bench_thread_pool, tornado_http, async_tree_none_tg, gunicorn, create_gc_cycles, regex_v8, dask, async_tree_memoization, mypy2, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x