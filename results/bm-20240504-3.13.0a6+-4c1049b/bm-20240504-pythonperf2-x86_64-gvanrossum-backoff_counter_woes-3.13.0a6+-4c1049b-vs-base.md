# Results vs. base

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 97.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                       | 288 ms: 1.00x faster                                                             |
| chameleon      | 7.71 ms                                                                      | 7.86 ms: 1.02x slower                                                            |
| docutils       | 3.00 sec                                                                     | 3.02 sec: 1.01x slower                                                           |
| html5lib       | 73.4 ms                                                                      | 74.9 ms: 1.02x slower                                                            |
| tornado_http   | 119 ms                                                                       | 120 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                       | 257 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                                      | 3.42 ms: 1.02x faster                                                            |
| regex_dna      | 239 ms                                                                       | 235 ms: 1.02x faster                                                             |
| regex_compile  | 146 ms                                                                       | 148 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                                      | 14.8 us: 1.06x faster                                                            |
| unpickle_pure_python | 219 us                                                                       | 215 us: 1.02x faster                                                             |
| xml_etree_process    | 60.0 ms                                                                      | 60.3 ms: 1.01x slower                                                            |
| xml_etree_parse      | 143 ms                                                                       | 144 ms: 1.01x slower                                                             |
| tomli_loads          | 2.55 sec                                                                     | 2.57 sec: 1.01x slower                                                           |
| pickle_list          | 4.47 us                                                                      | 4.52 us: 1.01x slower                                                            |
| pickle_pure_python   | 313 us                                                                       | 317 us: 1.01x slower                                                             |
| json_loads           | 24.3 us                                                                      | 24.8 us: 1.02x slower                                                            |
| xml_etree_generate   | 86.5 ms                                                                      | 88.6 ms: 1.03x slower                                                            |
| json_dumps           | 10.8 ms                                                                      | 11.1 ms: 1.03x slower                                                            |
| unpickle_list        | 4.62 us                                                                      | 4.82 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                     |

Benchmark hidden because not significant (3): pickle, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.82 ms                                                                      | 8.80 ms: 1.00x faster                                                            |
| python_startup         | 12.9 ms                                                                      | 12.8 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 10.4 ms                                                                      | 10.5 ms: 1.01x slower                                                            |
| genshi_xml     | 54.6 ms                                                                      | 56.7 ms: 1.04x slower                                                            |
| genshi_text    | 24.8 ms                                                                      | 26.0 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle                 | 15.7 us                                                                      | 14.8 us: 1.06x faster                                                            |
| pycparser                | 1.28 sec                                                                     | 1.22 sec: 1.05x faster                                                           |
| pyflate                  | 491 ms                                                                       | 470 ms: 1.05x faster                                                             |
| scimark_sor              | 116 ms                                                                       | 113 ms: 1.03x faster                                                             |
| regex_effbot             | 3.50 ms                                                                      | 3.42 ms: 1.02x faster                                                            |
| async_generators         | 369 ms                                                                       | 360 ms: 1.02x faster                                                             |
| scimark_monte_carlo      | 66.9 ms                                                                      | 65.4 ms: 1.02x faster                                                            |
| raytrace                 | 268 ms                                                                       | 262 ms: 1.02x faster                                                             |
| create_gc_cycles         | 2.06 ms                                                                      | 2.02 ms: 1.02x faster                                                            |
| generators               | 34.7 ms                                                                      | 34.1 ms: 1.02x faster                                                            |
| flaskblogging            | 4.73 ms                                                                      | 4.64 ms: 1.02x faster                                                            |
| unpickle_pure_python     | 219 us                                                                       | 215 us: 1.02x faster                                                             |
| regex_dna                | 239 ms                                                                       | 235 ms: 1.02x faster                                                             |
| sqlite_synth             | 2.82 us                                                                      | 2.79 us: 1.01x faster                                                            |
| deltablue                | 3.39 ms                                                                      | 3.35 ms: 1.01x faster                                                            |
| logging_silent           | 97.8 ns                                                                      | 97.1 ns: 1.01x faster                                                            |
| pathlib                  | 17.2 ms                                                                      | 17.1 ms: 1.01x faster                                                            |
| fannkuch                 | 359 ms                                                                       | 357 ms: 1.01x faster                                                             |
| scimark_lu               | 97.6 ms                                                                      | 97.1 ms: 1.01x faster                                                            |
| mdp                      | 2.51 sec                                                                     | 2.49 sec: 1.01x faster                                                           |
| nqueens                  | 89.0 ms                                                                      | 88.6 ms: 1.00x faster                                                            |
| 2to3                     | 289 ms                                                                       | 288 ms: 1.00x faster                                                             |
| telco                    | 8.34 ms                                                                      | 8.30 ms: 1.00x faster                                                            |
| dulwich_log              | 66.8 ms                                                                      | 66.5 ms: 1.00x faster                                                            |
| sqlglot_transpile        | 1.80 ms                                                                      | 1.79 ms: 1.00x faster                                                            |
| python_startup_no_site   | 8.82 ms                                                                      | 8.80 ms: 1.00x faster                                                            |
| python_startup           | 12.9 ms                                                                      | 12.8 ms: 1.00x faster                                                            |
| scimark_fft              | 296 ms                                                                       | 297 ms: 1.00x slower                                                             |
| xml_etree_process        | 60.0 ms                                                                      | 60.3 ms: 1.01x slower                                                            |
| hexiom                   | 6.25 ms                                                                      | 6.29 ms: 1.01x slower                                                            |
| deepcopy_memo            | 38.0 us                                                                      | 38.3 us: 1.01x slower                                                            |
| coroutines               | 21.9 ms                                                                      | 22.0 ms: 1.01x slower                                                            |
| meteor_contest           | 129 ms                                                                       | 130 ms: 1.01x slower                                                             |
| richards_super           | 60.9 ms                                                                      | 61.4 ms: 1.01x slower                                                            |
| sqlglot_optimize         | 59.2 ms                                                                      | 59.7 ms: 1.01x slower                                                            |
| xml_etree_parse          | 143 ms                                                                       | 144 ms: 1.01x slower                                                             |
| sqlglot_normalize        | 121 ms                                                                       | 122 ms: 1.01x slower                                                             |
| docutils                 | 3.00 sec                                                                     | 3.02 sec: 1.01x slower                                                           |
| richards                 | 53.9 ms                                                                      | 54.4 ms: 1.01x slower                                                            |
| tomli_loads              | 2.55 sec                                                                     | 2.57 sec: 1.01x slower                                                           |
| mako                     | 10.4 ms                                                                      | 10.5 ms: 1.01x slower                                                            |
| pickle_list              | 4.47 us                                                                      | 4.52 us: 1.01x slower                                                            |
| logging_simple           | 6.51 us                                                                      | 6.59 us: 1.01x slower                                                            |
| pidigits                 | 254 ms                                                                       | 257 ms: 1.01x slower                                                             |
| tornado_http             | 119 ms                                                                       | 120 ms: 1.01x slower                                                             |
| crypto_pyaes             | 74.3 ms                                                                      | 75.1 ms: 1.01x slower                                                            |
| spectral_norm            | 93.6 ms                                                                      | 94.7 ms: 1.01x slower                                                            |
| pickle_pure_python       | 313 us                                                                       | 317 us: 1.01x slower                                                             |
| regex_compile            | 146 ms                                                                       | 148 ms: 1.01x slower                                                             |
| dask                     | 389 ms                                                                       | 395 ms: 1.02x slower                                                             |
| json                     | 5.42 ms                                                                      | 5.51 ms: 1.02x slower                                                            |
| bench_thread_pool        | 896 us                                                                       | 912 us: 1.02x slower                                                             |
| json_loads               | 24.3 us                                                                      | 24.8 us: 1.02x slower                                                            |
| html5lib                 | 73.4 ms                                                                      | 74.9 ms: 1.02x slower                                                            |
| chameleon                | 7.71 ms                                                                      | 7.86 ms: 1.02x slower                                                            |
| aiohttp                  | 1.08 ms                                                                      | 1.10 ms: 1.02x slower                                                            |
| xml_etree_generate       | 86.5 ms                                                                      | 88.6 ms: 1.03x slower                                                            |
| json_dumps               | 10.8 ms                                                                      | 11.1 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult  | 4.17 ms                                                                      | 4.30 ms: 1.03x slower                                                            |
| go                       | 158 ms                                                                       | 163 ms: 1.03x slower                                                             |
| typing_runtime_protocols | 174 us                                                                       | 179 us: 1.03x slower                                                             |
| gc_traversal             | 4.50 ms                                                                      | 4.67 ms: 1.04x slower                                                            |
| genshi_xml               | 54.6 ms                                                                      | 56.7 ms: 1.04x slower                                                            |
| unpickle_list            | 4.62 us                                                                      | 4.82 us: 1.04x slower                                                            |
| genshi_text              | 24.8 ms                                                                      | 26.0 ms: 1.05x slower                                                            |
| coverage                 | 79.1 ms                                                                      | 83.2 ms: 1.05x slower                                                            |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (35): mypy2, async_tree_memoization_tg, django_template, pickle, nbody, chaos, asyncio_websockets, sympy_sum, bench_mp_pool, xml_etree_iterparse, comprehensions, asyncio_tcp_ssl, regex_v8, thrift, sympy_str, deepcopy, logging_format, gunicorn, pickle_dict, pprint_safe_repr, float, sympy_integrate, pprint_pformat, deepcopy_reduce, sympy_expand, pylint, asyncio_tcp, sqlglot_parse, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization

# HPT report

- Reliability score: 97.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x