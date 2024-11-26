# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.001x faster
- HPT reliability: 69.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| chameleon      | 7.49 ms                                                      | 7.28 ms: 1.03x faster                                            |
| docutils       | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| html5lib       | 72.9 ms                                                      | 76.2 ms: 1.05x slower                                            |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                             |
| async_generators           | 364 ms                                                       | 366 ms: 1.01x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_none            | 370 ms                                                       | 433 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 697 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 546 ms: 1.19x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 543 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 703 ms: 1.22x slower                                             |
| async_tree_none_tg         | 342 ms                                                       | 434 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.07 sec: 1.29x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                            |
| pidigits       | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 237 ms: 1.01x faster                                             |
| regex_effbot   | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                            |
| regex_v8       | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.29 sec: 1.06x faster                                           |
| pickle_pure_python   | 322 us                                                       | 305 us: 1.05x faster                                             |
| json_dumps           | 10.8 ms                                                      | 10.3 ms: 1.05x faster                                            |
| unpickle_pure_python | 216 us                                                       | 211 us: 1.02x faster                                             |
| json_loads           | 24.7 us                                                      | 24.5 us: 1.01x faster                                            |
| xml_etree_process    | 60.7 ms                                                      | 60.2 ms: 1.01x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| xml_etree_generate   | 85.2 ms                                                      | 87.7 ms: 1.03x slower                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 105 ms: 1.05x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.7 ms: 1.23x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.1 ms: 1.24x slower                                            |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                            |
| genshi_xml      | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                            |
| django_template | 38.9 ms                                                      | 37.7 ms: 1.03x faster                                            |
| mako            | 10.3 ms                                                      | 10.1 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.61 ms: 1.65x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 116 us: 1.52x faster                                             |
| gc_traversal               | 4.48 ms                                                      | 3.55 ms: 1.26x faster                                            |
| python_startup             | 15.6 ms                                                      | 12.7 ms: 1.23x faster                                            |
| mypy2                      | 1.02 sec                                                     | 864 ms: 1.19x faster                                             |
| telco                      | 8.77 ms                                                      | 8.09 ms: 1.08x faster                                            |
| coverage                   | 84.5 ms                                                      | 78.5 ms: 1.08x faster                                            |
| bench_mp_pool              | 4.82 ms                                                      | 4.49 ms: 1.07x faster                                            |
| tomli_loads                | 2.43 sec                                                     | 2.29 sec: 1.06x faster                                           |
| deepcopy_reduce            | 3.49 us                                                      | 3.29 us: 1.06x faster                                            |
| genshi_text                | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                            |
| genshi_xml                 | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                            |
| raytrace                   | 267 ms                                                       | 253 ms: 1.06x faster                                             |
| thrift                     | 918 us                                                       | 870 us: 1.05x faster                                             |
| spectral_norm              | 97.4 ms                                                      | 92.4 ms: 1.05x faster                                            |
| pickle_pure_python         | 322 us                                                       | 305 us: 1.05x faster                                             |
| json                       | 5.62 ms                                                      | 5.34 ms: 1.05x faster                                            |
| deepcopy_memo              | 38.9 us                                                      | 37.0 us: 1.05x faster                                            |
| json_dumps                 | 10.8 ms                                                      | 10.3 ms: 1.05x faster                                            |
| richards_super             | 60.2 ms                                                      | 57.5 ms: 1.05x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 800 ms: 1.04x faster                                             |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                           |
| deepcopy                   | 388 us                                                       | 373 us: 1.04x faster                                             |
| nqueens                    | 92.3 ms                                                      | 88.7 ms: 1.04x faster                                            |
| comprehensions             | 17.3 us                                                      | 16.7 us: 1.04x faster                                            |
| float                      | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                            |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                             |
| django_template            | 38.9 ms                                                      | 37.7 ms: 1.03x faster                                            |
| scimark_lu                 | 97.4 ms                                                      | 94.6 ms: 1.03x faster                                            |
| chameleon                  | 7.49 ms                                                      | 7.28 ms: 1.03x faster                                            |
| hexiom                     | 6.47 ms                                                      | 6.32 ms: 1.02x faster                                            |
| richards                   | 52.5 ms                                                      | 51.2 ms: 1.02x faster                                            |
| generators                 | 33.9 ms                                                      | 33.1 ms: 1.02x faster                                            |
| unpickle_pure_python       | 216 us                                                       | 211 us: 1.02x faster                                             |
| logging_silent             | 97.5 ns                                                      | 95.3 ns: 1.02x faster                                            |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                             |
| mako                       | 10.3 ms                                                      | 10.1 ms: 1.02x faster                                            |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.01x faster                                           |
| crypto_pyaes               | 73.5 ms                                                      | 72.5 ms: 1.01x faster                                            |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                             |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                             |
| json_loads                 | 24.7 us                                                      | 24.5 us: 1.01x faster                                            |
| xml_etree_process          | 60.7 ms                                                      | 60.2 ms: 1.01x faster                                            |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                             |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                            |
| regex_dna                  | 238 ms                                                       | 237 ms: 1.01x faster                                             |
| sympy_expand               | 506 ms                                                       | 504 ms: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.20 ms: 1.00x faster                                            |
| 2to3                       | 293 ms                                                       | 292 ms: 1.00x faster                                             |
| async_generators           | 364 ms                                                       | 366 ms: 1.01x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.83 sec: 1.01x slower                                           |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 59.1 ms: 1.01x slower                                            |
| chaos                      | 60.6 ms                                                      | 61.1 ms: 1.01x slower                                            |
| regex_effbot               | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                            |
| sqlglot_parse              | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                            |
| logging_format             | 6.95 us                                                      | 7.11 us: 1.02x slower                                            |
| pycparser                  | 1.28 sec                                                     | 1.31 sec: 1.02x slower                                           |
| logging_simple             | 6.28 us                                                      | 6.44 us: 1.03x slower                                            |
| xml_etree_generate         | 85.2 ms                                                      | 87.7 ms: 1.03x slower                                            |
| scimark_fft                | 298 ms                                                       | 307 ms: 1.03x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                             |
| pyflate                    | 493 ms                                                       | 509 ms: 1.03x slower                                             |
| pidigits                   | 252 ms                                                       | 262 ms: 1.04x slower                                             |
| regex_v8                   | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| html5lib                   | 72.9 ms                                                      | 76.2 ms: 1.05x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 68.8 ms: 1.05x slower                                            |
| deltablue                  | 3.38 ms                                                      | 3.56 ms: 1.05x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 105 ms: 1.05x slower                                             |
| bench_thread_pool          | 929 us                                                       | 979 us: 1.05x slower                                             |
| fannkuch                   | 384 ms                                                       | 406 ms: 1.06x slower                                             |
| scimark_monte_carlo        | 65.2 ms                                                      | 70.6 ms: 1.08x slower                                            |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.08x slower                                            |
| scimark_sor                | 125 ms                                                       | 143 ms: 1.14x slower                                             |
| async_tree_none            | 370 ms                                                       | 433 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 697 ms: 1.17x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 546 ms: 1.19x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 543 ms: 1.21x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 703 ms: 1.22x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.1 ms: 1.24x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 434 ms: 1.27x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.07 sec: 1.29x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 1.07 sec: 1.31x slower                                           |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (4): nbody, pylint, go, regex_compile
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 69.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.88x