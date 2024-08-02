# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.00x slower
- HPT reliability: 88.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 290 ms: 1.01x faster                                             |
| chameleon      | 7.40 ms                                                          | 7.20 ms: 1.03x faster                                            |
| html5lib       | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 604 ms                                                           | 614 ms: 1.02x slower                                             |
| Geometric mean          | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| regex_dna      | 249 ms                                                           | 251 ms: 1.01x slower                                             |
| regex_effbot   | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                             |
| json_loads           | 25.0 us                                                          | 25.0 us: 1.00x faster                                            |
| xml_etree_generate   | 85.7 ms                                                          | 86.9 ms: 1.01x slower                                            |
| tomli_loads          | 2.40 sec                                                         | 2.44 sec: 1.01x slower                                           |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.02x slower                                            |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                             |
| xml_etree_process    | 59.7 ms                                                          | 61.5 ms: 1.03x slower                                            |
| xml_etree_parse      | 144 ms                                                           | 149 ms: 1.04x slower                                             |
| xml_etree_iterparse  | 103 ms                                                           | 106 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                            |
| python_startup_no_site | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 56.8 ms: 1.02x faster                                            |
| genshi_text    | 25.9 ms                                                          | 26.2 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| bench_mp_pool            | 4.91 ms                                                          | 4.64 ms: 1.06x faster                                            |
| unpickle_pure_python     | 224 us                                                           | 214 us: 1.05x faster                                             |
| coverage                 | 83.5 ms                                                          | 79.6 ms: 1.05x faster                                            |
| regex_v8                 | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                            |
| richards_super           | 61.2 ms                                                          | 59.0 ms: 1.04x faster                                            |
| scimark_fft              | 312 ms                                                           | 302 ms: 1.03x faster                                             |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.16 ms: 1.03x faster                                            |
| chameleon                | 7.40 ms                                                          | 7.20 ms: 1.03x faster                                            |
| genshi_xml               | 58.1 ms                                                          | 56.8 ms: 1.02x faster                                            |
| scimark_sor              | 119 ms                                                           | 116 ms: 1.02x faster                                             |
| asyncio_websockets       | 395 ms                                                           | 387 ms: 1.02x faster                                             |
| gc_traversal             | 4.69 ms                                                          | 4.60 ms: 1.02x faster                                            |
| dulwich_log              | 67.3 ms                                                          | 66.3 ms: 1.02x faster                                            |
| logging_format           | 7.11 us                                                          | 7.01 us: 1.01x faster                                            |
| meteor_contest           | 128 ms                                                           | 126 ms: 1.01x faster                                             |
| scimark_lu               | 97.5 ms                                                          | 96.2 ms: 1.01x faster                                            |
| sympy_sum                | 155 ms                                                           | 153 ms: 1.01x faster                                             |
| sqlglot_optimize         | 59.5 ms                                                          | 58.9 ms: 1.01x faster                                            |
| go                       | 165 ms                                                           | 163 ms: 1.01x faster                                             |
| sqlglot_normalize        | 120 ms                                                           | 119 ms: 1.01x faster                                             |
| richards                 | 53.4 ms                                                          | 53.0 ms: 1.01x faster                                            |
| html5lib                 | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                            |
| json                     | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                            |
| regex_compile            | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| asyncio_tcp              | 378 ms                                                           | 375 ms: 1.01x faster                                             |
| 2to3                     | 291 ms                                                           | 290 ms: 1.01x faster                                             |
| pprint_safe_repr         | 818 ms                                                           | 814 ms: 1.00x faster                                             |
| json_loads               | 25.0 us                                                          | 25.0 us: 1.00x faster                                            |
| pathlib                  | 17.1 ms                                                          | 17.1 ms: 1.00x faster                                            |
| async_generators         | 363 ms                                                           | 362 ms: 1.00x faster                                             |
| generators               | 33.5 ms                                                          | 33.4 ms: 1.00x faster                                            |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                           |
| bpe_tokeniser            | 5.14 sec                                                         | 5.13 sec: 1.00x faster                                           |
| nqueens                  | 88.4 ms                                                          | 88.6 ms: 1.00x slower                                            |
| spectral_norm            | 97.3 ms                                                          | 97.6 ms: 1.00x slower                                            |
| hexiom                   | 6.35 ms                                                          | 6.38 ms: 1.00x slower                                            |
| sqlglot_transpile        | 1.76 ms                                                          | 1.77 ms: 1.00x slower                                            |
| deepcopy_memo            | 37.3 us                                                          | 37.5 us: 1.01x slower                                            |
| regex_dna                | 249 ms                                                           | 251 ms: 1.01x slower                                             |
| sympy_integrate          | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                            |
| typing_runtime_protocols | 171 us                                                           | 172 us: 1.01x slower                                             |
| sqlglot_parse            | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                            |
| coroutines               | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                            |
| scimark_monte_carlo      | 65.5 ms                                                          | 66.1 ms: 1.01x slower                                            |
| genshi_text              | 25.9 ms                                                          | 26.2 ms: 1.01x slower                                            |
| logging_simple           | 6.40 us                                                          | 6.47 us: 1.01x slower                                            |
| raytrace                 | 260 ms                                                           | 263 ms: 1.01x slower                                             |
| python_startup           | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                            |
| crypto_pyaes             | 73.6 ms                                                          | 74.6 ms: 1.01x slower                                            |
| deepcopy_reduce          | 3.39 us                                                          | 3.44 us: 1.01x slower                                            |
| xml_etree_generate       | 85.7 ms                                                          | 86.9 ms: 1.01x slower                                            |
| tomli_loads              | 2.40 sec                                                         | 2.44 sec: 1.01x slower                                           |
| json_dumps               | 10.8 ms                                                          | 10.9 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 614 ms: 1.02x slower                                             |
| python_startup_no_site   | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                            |
| pyflate                  | 482 ms                                                           | 492 ms: 1.02x slower                                             |
| chaos                    | 59.6 ms                                                          | 60.9 ms: 1.02x slower                                            |
| pickle_pure_python       | 307 us                                                           | 315 us: 1.02x slower                                             |
| thrift                   | 880 us                                                           | 903 us: 1.03x slower                                             |
| xml_etree_process        | 59.7 ms                                                          | 61.5 ms: 1.03x slower                                            |
| mdp                      | 2.46 sec                                                         | 2.54 sec: 1.03x slower                                           |
| fannkuch                 | 353 ms                                                           | 365 ms: 1.03x slower                                             |
| xml_etree_parse          | 144 ms                                                           | 149 ms: 1.04x slower                                             |
| xml_etree_iterparse      | 103 ms                                                           | 106 ms: 1.04x slower                                             |
| regex_effbot             | 3.40 ms                                                          | 3.54 ms: 1.04x slower                                            |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                     |

Benchmark hidden because not significant (28): telco, bench_thread_pool, logging_silent, mako, tornado_http, float, deepcopy, sympy_expand, pidigits, pprint_pformat, sympy_str, comprehensions, docutils, deltablue, async_tree_io, pylint, django_template, pycparser, async_tree_none, mypy2, async_tree_io_tg, dask, nbody, create_gc_cycles, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x