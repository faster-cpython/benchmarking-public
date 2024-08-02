# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| chameleon      | 7.40 ms                                                          | 8.59 ms: 1.16x slower                                                               |
| tornado_http   | 119 ms                                                           | 141 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                            | 1.17x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 920 ms: 1.02x slower                                                                |
| async_tree_none_tg         | 340 ms                                                           | 360 ms: 1.06x slower                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 644 ms: 1.07x slower                                                                |
| async_tree_none            | 365 ms                                                           | 391 ms: 1.07x slower                                                                |
| async_tree_io              | 873 ms                                                           | 937 ms: 1.07x slower                                                                |
| async_tree_memoization     | 460 ms                                                           | 496 ms: 1.08x slower                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 458 ms: 1.09x slower                                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 629 ms: 1.10x slower                                                                |
| Geometric mean             | (ref)                                                            | 1.07x slower                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 259 ms: 1.02x slower                                                                |
| float          | 80.2 ms                                                          | 98.7 ms: 1.23x slower                                                               |
| nbody          | 87.8 ms                                                          | 130 ms: 1.48x slower                                                                |
| Geometric mean | (ref)                                                            | 1.23x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 246 ms: 1.01x faster                                                                |
| regex_v8       | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                               |
| regex_effbot   | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                               |
| regex_compile  | 144 ms                                                           | 231 ms: 1.61x slower                                                                |
| Geometric mean | (ref)                                                            | 1.15x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                               |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                               |
| pickle_dict          | 32.8 us                                                          | 32.9 us: 1.00x slower                                                               |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                                               |
| xml_etree_parse      | 144 ms                                                           | 147 ms: 1.03x slower                                                                |
| json_dumps           | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                           | 116 ms: 1.13x slower                                                                |
| xml_etree_process    | 59.7 ms                                                          | 68.1 ms: 1.14x slower                                                               |
| xml_etree_generate   | 85.7 ms                                                          | 99.2 ms: 1.16x slower                                                               |
| tomli_loads          | 2.40 sec                                                         | 3.36 sec: 1.40x slower                                                              |
| unpickle_pure_python | 224 us                                                           | 338 us: 1.51x slower                                                                |
| pickle_pure_python   | 307 us                                                           | 471 us: 1.53x slower                                                                |
| Geometric mean       | (ref)                                                            | 1.12x slower                                                                        |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.0 ms: 1.01x faster                                                               |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                               |
| Geometric mean         | (ref)                                                            | 1.00x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 39.0 ms                                                          | 47.5 ms: 1.22x slower                                                               |
| mako            | 10.4 ms                                                          | 14.3 ms: 1.38x slower                                                               |
| Geometric mean  | (ref)                                                            | 1.30x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| coverage                   | 83.5 ms                                                          | 78.1 ms: 1.07x faster                                                               |
| unpickle                   | 15.7 us                                                          | 14.8 us: 1.06x faster                                                               |
| gc_traversal               | 4.69 ms                                                          | 4.52 ms: 1.04x faster                                                               |
| json_loads                 | 25.0 us                                                          | 24.5 us: 1.02x faster                                                               |
| regex_dna                  | 249 ms                                                           | 246 ms: 1.01x faster                                                                |
| python_startup             | 13.2 ms                                                          | 13.0 ms: 1.01x faster                                                               |
| pickle_dict                | 32.8 us                                                          | 32.9 us: 1.00x slower                                                               |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.01x slower                                                               |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                               |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                              |
| async_tree_io_tg           | 900 ms                                                           | 920 ms: 1.02x slower                                                                |
| pidigits                   | 254 ms                                                           | 259 ms: 1.02x slower                                                                |
| xml_etree_parse            | 144 ms                                                           | 147 ms: 1.03x slower                                                                |
| json                       | 5.35 ms                                                          | 5.50 ms: 1.03x slower                                                               |
| create_gc_cycles           | 2.00 ms                                                          | 2.06 ms: 1.03x slower                                                               |
| regex_v8                   | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                               |
| thrift                     | 880 us                                                           | 914 us: 1.04x slower                                                                |
| json_dumps                 | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                                               |
| asyncio_tcp                | 378 ms                                                           | 395 ms: 1.05x slower                                                                |
| sqlite_synth               | 2.80 us                                                          | 2.93 us: 1.05x slower                                                               |
| regex_effbot               | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                               |
| async_tree_none_tg         | 340 ms                                                           | 360 ms: 1.06x slower                                                                |
| generators                 | 33.5 ms                                                          | 35.6 ms: 1.06x slower                                                               |
| coroutines                 | 22.0 ms                                                          | 23.4 ms: 1.06x slower                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 644 ms: 1.07x slower                                                                |
| async_tree_none            | 365 ms                                                           | 391 ms: 1.07x slower                                                                |
| async_tree_io              | 873 ms                                                           | 937 ms: 1.07x slower                                                                |
| async_tree_memoization     | 460 ms                                                           | 496 ms: 1.08x slower                                                                |
| pathlib                    | 17.1 ms                                                          | 18.5 ms: 1.08x slower                                                               |
| logging_format             | 7.11 us                                                          | 7.69 us: 1.08x slower                                                               |
| async_tree_memoization_tg  | 421 ms                                                           | 458 ms: 1.09x slower                                                                |
| telco                      | 8.40 ms                                                          | 9.15 ms: 1.09x slower                                                               |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 629 ms: 1.10x slower                                                                |
| mdp                        | 2.46 sec                                                         | 2.73 sec: 1.11x slower                                                              |
| logging_simple             | 6.40 us                                                          | 7.09 us: 1.11x slower                                                               |
| flaskblogging              | 4.68 ms                                                          | 5.19 ms: 1.11x slower                                                               |
| async_generators           | 363 ms                                                           | 403 ms: 1.11x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                           | 116 ms: 1.13x slower                                                                |
| dask                       | 391 ms                                                           | 441 ms: 1.13x slower                                                                |
| xml_etree_process          | 59.7 ms                                                          | 68.1 ms: 1.14x slower                                                               |
| xml_etree_generate         | 85.7 ms                                                          | 99.2 ms: 1.16x slower                                                               |
| bench_thread_pool          | 908 us                                                           | 1.05 ms: 1.16x slower                                                               |
| chameleon                  | 7.40 ms                                                          | 8.59 ms: 1.16x slower                                                               |
| meteor_contest             | 128 ms                                                           | 149 ms: 1.16x slower                                                                |
| tornado_http               | 119 ms                                                           | 141 ms: 1.18x slower                                                                |
| typing_runtime_protocols   | 171 us                                                           | 204 us: 1.19x slower                                                                |
| gunicorn                   | 1.04 ms                                                          | 1.26 ms: 1.21x slower                                                               |
| django_template            | 39.0 ms                                                          | 47.5 ms: 1.22x slower                                                               |
| aiohttp                    | 1.07 ms                                                          | 1.31 ms: 1.22x slower                                                               |
| deepcopy_reduce            | 3.39 us                                                          | 4.14 us: 1.22x slower                                                               |
| float                      | 80.2 ms                                                          | 98.7 ms: 1.23x slower                                                               |
| sqlglot_optimize           | 59.5 ms                                                          | 74.6 ms: 1.25x slower                                                               |
| pycparser                  | 1.22 sec                                                         | 1.55 sec: 1.27x slower                                                              |
| sqlglot_parse              | 1.39 ms                                                          | 1.77 ms: 1.27x slower                                                               |
| sqlglot_transpile          | 1.76 ms                                                          | 2.26 ms: 1.28x slower                                                               |
| deepcopy                   | 377 us                                                           | 485 us: 1.29x slower                                                                |
| sqlglot_normalize          | 120 ms                                                           | 155 ms: 1.29x slower                                                                |
| crypto_pyaes               | 73.6 ms                                                          | 94.8 ms: 1.29x slower                                                               |
| richards_super             | 61.2 ms                                                          | 79.8 ms: 1.30x slower                                                               |
| pyflate                    | 482 ms                                                           | 632 ms: 1.31x slower                                                                |
| go                         | 165 ms                                                           | 217 ms: 1.32x slower                                                                |
| sympy_integrate            | 23.2 ms                                                          | 30.6 ms: 1.32x slower                                                               |
| mypy2                      | 764 ms                                                           | 1.01 sec: 1.32x slower                                                              |
| pprint_safe_repr           | 818 ms                                                           | 1.10 sec: 1.34x slower                                                              |
| pylint                     | 339 ms                                                           | 457 ms: 1.35x slower                                                                |
| richards                   | 53.4 ms                                                          | 72.0 ms: 1.35x slower                                                               |
| pprint_pformat             | 1.66 sec                                                         | 2.24 sec: 1.35x slower                                                              |
| dulwich_log                | 67.3 ms                                                          | 91.1 ms: 1.35x slower                                                               |
| sympy_sum                  | 155 ms                                                           | 211 ms: 1.36x slower                                                                |
| scimark_fft                | 312 ms                                                           | 428 ms: 1.37x slower                                                                |
| chaos                      | 59.6 ms                                                          | 81.9 ms: 1.37x slower                                                               |
| mako                       | 10.4 ms                                                          | 14.3 ms: 1.38x slower                                                               |
| raytrace                   | 260 ms                                                           | 360 ms: 1.38x slower                                                                |
| nqueens                    | 88.4 ms                                                          | 122 ms: 1.38x slower                                                                |
| scimark_sor                | 119 ms                                                           | 165 ms: 1.39x slower                                                                |
| sympy_expand               | 501 ms                                                           | 698 ms: 1.39x slower                                                                |
| tomli_loads                | 2.40 sec                                                         | 3.36 sec: 1.40x slower                                                              |
| fannkuch                   | 353 ms                                                           | 497 ms: 1.41x slower                                                                |
| sympy_str                  | 295 ms                                                           | 417 ms: 1.42x slower                                                                |
| nbody                      | 87.8 ms                                                          | 130 ms: 1.48x slower                                                                |
| unpickle_pure_python       | 224 us                                                           | 338 us: 1.51x slower                                                                |
| spectral_norm              | 97.3 ms                                                          | 147 ms: 1.51x slower                                                                |
| pickle_pure_python         | 307 us                                                           | 471 us: 1.53x slower                                                                |
| scimark_lu                 | 97.5 ms                                                          | 151 ms: 1.55x slower                                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.82 ms: 1.59x slower                                                               |
| regex_compile              | 144 ms                                                           | 231 ms: 1.61x slower                                                                |
| comprehensions             | 17.0 us                                                          | 27.7 us: 1.63x slower                                                               |
| deepcopy_memo              | 37.3 us                                                          | 61.3 us: 1.65x slower                                                               |
| scimark_monte_carlo        | 65.5 ms                                                          | 109 ms: 1.67x slower                                                                |
| hexiom                     | 6.35 ms                                                          | 10.9 ms: 1.71x slower                                                               |
| deltablue                  | 3.37 ms                                                          | 6.15 ms: 1.82x slower                                                               |
| logging_silent             | 96.3 ns                                                          | 185 ns: 1.92x slower                                                                |
| Geometric mean             | (ref)                                                            | 1.21x slower                                                                        |

Benchmark hidden because not significant (4): pickle_list, bench_mp_pool, asyncio_websockets, unpickle_list
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: 2to3, bpe_tokeniser, docutils, genshi_text, genshi_xml, html5lib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.00x