# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.002x slower
- HPT reliability: 63.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| chameleon      | 7.49 ms                                                      | 7.42 ms: 1.01x faster                                            |
| docutils       | 2.81 sec                                                     | 2.84 sec: 1.01x slower                                           |
| html5lib       | 72.9 ms                                                      | 76.0 ms: 1.04x slower                                            |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                             |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_none            | 370 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 699 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 551 ms: 1.20x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 546 ms: 1.22x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 705 ms: 1.23x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 434 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.30x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.8 ms: 1.09x faster                                            |
| float          | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                            |
| pidigits       | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                            |
| regex_compile  | 143 ms                                                       | 142 ms: 1.00x faster                                             |
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_v8       | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process   | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                            |
| json_dumps          | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| tomli_loads         | 2.43 sec                                                     | 2.38 sec: 1.02x faster                                           |
| pickle_pure_python  | 322 us                                                       | 316 us: 1.02x faster                                             |
| json_loads          | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| xml_etree_parse     | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| xml_etree_iterparse | 99.8 ms                                                      | 105 ms: 1.05x slower                                             |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.0 ms: 1.24x slower                                            |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                            |
| genshi_xml      | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                            |
| django_template | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.61 ms: 1.65x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 117 us: 1.50x faster                                             |
| python_startup             | 15.6 ms                                                      | 12.6 ms: 1.24x faster                                            |
| gc_traversal               | 4.48 ms                                                      | 3.76 ms: 1.19x faster                                            |
| mypy2                      | 1.02 sec                                                     | 867 ms: 1.18x faster                                             |
| nbody                      | 92.1 ms                                                      | 84.8 ms: 1.09x faster                                            |
| telco                      | 8.77 ms                                                      | 8.16 ms: 1.07x faster                                            |
| json                       | 5.62 ms                                                      | 5.30 ms: 1.06x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 791 ms: 1.06x faster                                             |
| spectral_norm              | 97.4 ms                                                      | 92.5 ms: 1.05x faster                                            |
| deepcopy                   | 388 us                                                       | 369 us: 1.05x faster                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                           |
| xml_etree_process          | 60.7 ms                                                      | 57.7 ms: 1.05x faster                                            |
| genshi_text                | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                            |
| bench_mp_pool              | 4.82 ms                                                      | 4.58 ms: 1.05x faster                                            |
| thrift                     | 918 us                                                       | 873 us: 1.05x faster                                             |
| deepcopy_memo              | 38.9 us                                                      | 37.2 us: 1.05x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.5 us: 1.05x faster                                            |
| logging_silent             | 97.5 ns                                                      | 93.6 ns: 1.04x faster                                            |
| nqueens                    | 92.3 ms                                                      | 88.8 ms: 1.04x faster                                            |
| genshi_xml                 | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                            |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                             |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.04x faster                                             |
| float                      | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                            |
| json_dumps                 | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| scimark_lu                 | 97.4 ms                                                      | 94.4 ms: 1.03x faster                                            |
| crypto_pyaes               | 73.5 ms                                                      | 71.3 ms: 1.03x faster                                            |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                             |
| deepcopy_reduce            | 3.49 us                                                      | 3.41 us: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.38 sec: 1.02x faster                                           |
| sympy_expand               | 506 ms                                                       | 496 ms: 1.02x faster                                             |
| coverage                   | 84.5 ms                                                      | 82.9 ms: 1.02x faster                                            |
| raytrace                   | 267 ms                                                       | 262 ms: 1.02x faster                                             |
| pickle_pure_python         | 322 us                                                       | 316 us: 1.02x faster                                             |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                             |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                           |
| django_template            | 38.9 ms                                                      | 38.4 ms: 1.01x faster                                            |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                             |
| chameleon                  | 7.49 ms                                                      | 7.42 ms: 1.01x faster                                            |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                            |
| regex_effbot               | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                            |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| hexiom                     | 6.47 ms                                                      | 6.44 ms: 1.01x faster                                            |
| regex_compile              | 143 ms                                                       | 142 ms: 1.00x faster                                             |
| 2to3                       | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| chaos                      | 60.6 ms                                                      | 61.0 ms: 1.01x slower                                            |
| richards_super             | 60.2 ms                                                      | 60.8 ms: 1.01x slower                                            |
| scimark_fft                | 298 ms                                                       | 301 ms: 1.01x slower                                             |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.84 sec: 1.01x slower                                           |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| go                         | 167 ms                                                       | 170 ms: 1.02x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                            |
| fannkuch                   | 384 ms                                                       | 393 ms: 1.02x slower                                             |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.0 ms: 1.03x slower                                            |
| pyflate                    | 493 ms                                                       | 506 ms: 1.03x slower                                             |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| bench_thread_pool          | 929 us                                                       | 958 us: 1.03x slower                                             |
| logging_format             | 6.95 us                                                      | 7.21 us: 1.04x slower                                            |
| richards                   | 52.5 ms                                                      | 54.4 ms: 1.04x slower                                            |
| pidigits                   | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| regex_v8                   | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| html5lib                   | 72.9 ms                                                      | 76.0 ms: 1.04x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 105 ms: 1.05x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 69.0 ms: 1.05x slower                                            |
| logging_simple             | 6.28 us                                                      | 6.63 us: 1.06x slower                                            |
| deltablue                  | 3.38 ms                                                      | 3.59 ms: 1.06x slower                                            |
| pathlib                    | 17.4 ms                                                      | 19.0 ms: 1.09x slower                                            |
| scimark_sor                | 125 ms                                                       | 146 ms: 1.17x slower                                             |
| async_tree_none            | 370 ms                                                       | 434 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 699 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 551 ms: 1.20x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 546 ms: 1.22x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 705 ms: 1.23x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.0 ms: 1.24x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 434 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.08 sec: 1.30x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (7): xml_etree_generate, sqlglot_optimize, pylint, pycparser, unpickle_pure_python, mako, generators
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 63.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.87x