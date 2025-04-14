# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.002x slower
- HPT reliability: 76.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 72.9 ms                                                      | 73.7 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                             |
| async_generators           | 364 ms                                                       | 370 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 690 ms: 1.16x slower                                             |
| async_tree_none            | 370 ms                                                       | 429 ms: 1.16x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 542 ms: 1.21x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 556 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 435 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.07 sec: 1.28x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.9 ms: 1.10x faster                                            |
| float          | 81.6 ms                                                      | 80.9 ms: 1.01x faster                                            |
| pidigits       | 252 ms                                                       | 265 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_v8       | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                            |
| regex_effbot   | 3.51 ms                                                      | 3.63 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                           |
| xml_etree_process    | 60.7 ms                                                      | 57.6 ms: 1.05x faster                                            |
| pickle_pure_python   | 322 us                                                       | 308 us: 1.04x faster                                             |
| json_dumps           | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| xml_etree_generate   | 85.2 ms                                                      | 84.0 ms: 1.01x faster                                            |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                            |
| unpickle_pure_python | 216 us                                                       | 225 us: 1.04x slower                                             |
| xml_etree_parse      | 144 ms                                                       | 151 ms: 1.05x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 108 ms: 1.08x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.3 ms: 1.27x slower                                            |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                            |
| genshi_xml     | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                            |
| mako           | 10.3 ms                                                      | 10.1 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.55 ms: 1.71x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 126 us: 1.40x faster                                             |
| python_startup             | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| mypy2                      | 1.02 sec                                                     | 862 ms: 1.19x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 3.94 ms: 1.14x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                           |
| nbody                      | 92.1 ms                                                      | 83.9 ms: 1.10x faster                                            |
| json                       | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                            |
| deepcopy                   | 388 us                                                       | 362 us: 1.07x faster                                             |
| telco                      | 8.77 ms                                                      | 8.17 ms: 1.07x faster                                            |
| thrift                     | 918 us                                                       | 858 us: 1.07x faster                                             |
| coverage                   | 84.5 ms                                                      | 79.1 ms: 1.07x faster                                            |
| deepcopy_reduce            | 3.49 us                                                      | 3.27 us: 1.07x faster                                            |
| genshi_text                | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                            |
| bench_mp_pool              | 4.82 ms                                                      | 4.54 ms: 1.06x faster                                            |
| genshi_xml                 | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.06x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                             |
| xml_etree_process          | 60.7 ms                                                      | 57.6 ms: 1.05x faster                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                           |
| pickle_pure_python         | 322 us                                                       | 308 us: 1.04x faster                                             |
| sympy_expand               | 506 ms                                                       | 488 ms: 1.04x faster                                             |
| comprehensions             | 17.3 us                                                      | 16.6 us: 1.04x faster                                            |
| deepcopy_memo              | 38.9 us                                                      | 37.6 us: 1.03x faster                                            |
| richards_super             | 60.2 ms                                                      | 58.3 ms: 1.03x faster                                            |
| nqueens                    | 92.3 ms                                                      | 89.5 ms: 1.03x faster                                            |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.03x faster                                             |
| json_dumps                 | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                            |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                             |
| fannkuch                   | 384 ms                                                       | 374 ms: 1.03x faster                                             |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                             |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                             |
| crypto_pyaes               | 73.5 ms                                                      | 71.7 ms: 1.03x faster                                            |
| mako                       | 10.3 ms                                                      | 10.1 ms: 1.03x faster                                            |
| sympy_sum                  | 154 ms                                                       | 150 ms: 1.02x faster                                             |
| hexiom                     | 6.47 ms                                                      | 6.35 ms: 1.02x faster                                            |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                            |
| xml_etree_generate         | 85.2 ms                                                      | 84.0 ms: 1.01x faster                                            |
| logging_silent             | 97.5 ns                                                      | 96.5 ns: 1.01x faster                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 58.1 ms: 1.01x faster                                            |
| float                      | 81.6 ms                                                      | 80.9 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                            |
| 2to3                       | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| scimark_fft                | 298 ms                                                       | 301 ms: 1.01x slower                                             |
| generators                 | 33.9 ms                                                      | 34.2 ms: 1.01x slower                                            |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                             |
| html5lib                   | 72.9 ms                                                      | 73.7 ms: 1.01x slower                                            |
| regex_v8                   | 24.9 ms                                                      | 25.2 ms: 1.01x slower                                            |
| scimark_lu                 | 97.4 ms                                                      | 98.6 ms: 1.01x slower                                            |
| raytrace                   | 267 ms                                                       | 271 ms: 1.01x slower                                             |
| async_generators           | 364 ms                                                       | 370 ms: 1.02x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| pycparser                  | 1.28 sec                                                     | 1.31 sec: 1.02x slower                                           |
| dulwich_log                | 65.5 ms                                                      | 66.9 ms: 1.02x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                            |
| chaos                      | 60.6 ms                                                      | 61.9 ms: 1.02x slower                                            |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.02x slower                                           |
| bench_thread_pool          | 929 us                                                       | 951 us: 1.02x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.44 us: 1.03x slower                                            |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| regex_effbot               | 3.51 ms                                                      | 3.63 ms: 1.03x slower                                            |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                            |
| logging_format             | 6.95 us                                                      | 7.20 us: 1.04x slower                                            |
| go                         | 167 ms                                                       | 173 ms: 1.04x slower                                             |
| unpickle_pure_python       | 216 us                                                       | 225 us: 1.04x slower                                             |
| pyflate                    | 493 ms                                                       | 513 ms: 1.04x slower                                             |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.9 ms: 1.04x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 151 ms: 1.05x slower                                             |
| pidigits                   | 252 ms                                                       | 265 ms: 1.05x slower                                             |
| deltablue                  | 3.38 ms                                                      | 3.61 ms: 1.07x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 108 ms: 1.08x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.1 ms: 1.10x slower                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 690 ms: 1.16x slower                                             |
| async_tree_none            | 370 ms                                                       | 429 ms: 1.16x slower                                             |
| scimark_sor                | 125 ms                                                       | 146 ms: 1.17x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 542 ms: 1.21x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 556 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 706 ms: 1.23x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.3 ms: 1.27x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 435 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.07 sec: 1.28x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.08 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (6): richards, chameleon, django_template, tornado_http, regex_compile, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 76.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.86x