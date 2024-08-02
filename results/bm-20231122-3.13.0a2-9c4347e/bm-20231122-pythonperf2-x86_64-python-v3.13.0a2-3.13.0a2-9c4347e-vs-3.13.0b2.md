# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x slower
- HPT reliability: 50.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.47 ms: 1.01x slower                                            |
| docutils       | 2.98 sec                                                         | 2.83 sec: 1.05x faster                                           |
| html5lib       | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 690 ms: 1.14x slower                                             |
| async_tree_none            | 365 ms                                                           | 429 ms: 1.17x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 542 ms: 1.18x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.07 sec: 1.22x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 706 ms: 1.23x slower                                             |
| async_tree_none_tg         | 340 ms                                                           | 435 ms: 1.28x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 556 ms: 1.32x slower                                             |
| Geometric mean             | (ref)                                                            | 1.22x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 83.9 ms: 1.05x faster                                            |
| float          | 80.2 ms                                                          | 80.9 ms: 1.01x slower                                            |
| pidigits       | 254 ms                                                           | 265 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                            | 1.00x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.04x faster                                             |
| regex_v8       | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                            |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| regex_effbot   | 3.40 ms                                                          | 3.63 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|---------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads         | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                           |
| pickle              | 10.6 us                                                          | 10.0 us: 1.06x faster                                            |
| unpickle            | 15.7 us                                                          | 15.1 us: 1.04x faster                                            |
| xml_etree_process   | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                            |
| json_dumps          | 10.8 ms                                                          | 10.5 ms: 1.02x faster                                            |
| pickle_list         | 4.44 us                                                          | 4.34 us: 1.02x faster                                            |
| xml_etree_generate  | 85.7 ms                                                          | 84.0 ms: 1.02x faster                                            |
| unpickle_list       | 4.70 us                                                          | 4.62 us: 1.02x faster                                            |
| pickle_dict         | 32.8 us                                                          | 32.6 us: 1.01x faster                                            |
| pickle_pure_python  | 307 us                                                           | 308 us: 1.00x slower                                             |
| json_loads          | 25.0 us                                                          | 25.5 us: 1.02x slower                                            |
| xml_etree_parse     | 144 ms                                                           | 151 ms: 1.05x slower                                             |
| xml_etree_iterparse | 103 ms                                                           | 108 ms: 1.05x slower                                             |
| Geometric mean      | (ref)                                                            | 1.02x faster                                                     |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.9 ms: 1.03x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.3 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                            | 1.12x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                            |
| mako           | 10.4 ms                                                          | 10.1 ms: 1.03x faster                                            |
| genshi_text    | 25.9 ms                                                          | 25.6 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                            | 1.03x faster                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 126 us: 1.36x faster                                             |
| create_gc_cycles           | 2.00 ms                                                          | 1.55 ms: 1.29x faster                                            |
| gc_traversal               | 4.69 ms                                                          | 3.94 ms: 1.19x faster                                            |
| tomli_loads                | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                           |
| bench_mp_pool              | 4.91 ms                                                          | 4.54 ms: 1.08x faster                                            |
| pickle                     | 10.6 us                                                          | 10.0 us: 1.06x faster                                            |
| genshi_xml                 | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                            |
| coverage                   | 83.5 ms                                                          | 79.1 ms: 1.06x faster                                            |
| spectral_norm              | 97.3 ms                                                          | 92.3 ms: 1.05x faster                                            |
| docutils                   | 2.98 sec                                                         | 2.83 sec: 1.05x faster                                           |
| richards_super             | 61.2 ms                                                          | 58.3 ms: 1.05x faster                                            |
| nbody                      | 87.8 ms                                                          | 83.9 ms: 1.05x faster                                            |
| deepcopy                   | 377 us                                                           | 362 us: 1.04x faster                                             |
| sqlglot_normalize          | 120 ms                                                           | 115 ms: 1.04x faster                                             |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                            |
| xml_etree_process          | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                            |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 3.27 us: 1.04x faster                                            |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.04x faster                                             |
| pprint_safe_repr           | 818 ms                                                           | 792 ms: 1.03x faster                                             |
| regex_v8                   | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                            |
| mako                       | 10.4 ms                                                          | 10.1 ms: 1.03x faster                                            |
| sympy_sum                  | 155 ms                                                           | 150 ms: 1.03x faster                                             |
| json                       | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 384 ms: 1.03x faster                                             |
| telco                      | 8.40 ms                                                          | 8.17 ms: 1.03x faster                                            |
| sympy_expand               | 501 ms                                                           | 488 ms: 1.03x faster                                             |
| crypto_pyaes               | 73.6 ms                                                          | 71.7 ms: 1.03x faster                                            |
| asyncio_tcp                | 378 ms                                                           | 368 ms: 1.03x faster                                             |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.03x faster                                           |
| thrift                     | 880 us                                                           | 858 us: 1.03x faster                                             |
| python_startup             | 13.2 ms                                                          | 12.9 ms: 1.03x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.02x faster                                            |
| richards                   | 53.4 ms                                                          | 52.1 ms: 1.02x faster                                            |
| sqlglot_optimize           | 59.5 ms                                                          | 58.1 ms: 1.02x faster                                            |
| pickle_list                | 4.44 us                                                          | 4.34 us: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                            |
| sqlite_synth               | 2.80 us                                                          | 2.74 us: 1.02x faster                                            |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                             |
| xml_etree_generate         | 85.7 ms                                                          | 84.0 ms: 1.02x faster                                            |
| comprehensions             | 17.0 us                                                          | 16.6 us: 1.02x faster                                            |
| unpickle_list              | 4.70 us                                                          | 4.62 us: 1.02x faster                                            |
| genshi_text                | 25.9 ms                                                          | 25.6 ms: 1.01x faster                                            |
| html5lib                   | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                            |
| flaskblogging              | 4.68 ms                                                          | 4.63 ms: 1.01x faster                                            |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                             |
| regex_compile              | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| aiohttp                    | 1.07 ms                                                          | 1.06 ms: 1.01x faster                                            |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                            |
| pickle_dict                | 32.8 us                                                          | 32.6 us: 1.01x faster                                            |
| dulwich_log                | 67.3 ms                                                          | 66.9 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                           |
| 2to3                       | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| pickle_pure_python         | 307 us                                                           | 308 us: 1.00x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.44 us: 1.01x slower                                            |
| deepcopy_memo              | 37.3 us                                                          | 37.6 us: 1.01x slower                                            |
| float                      | 80.2 ms                                                          | 80.9 ms: 1.01x slower                                            |
| chameleon                  | 7.40 ms                                                          | 7.47 ms: 1.01x slower                                            |
| coroutines                 | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                            |
| scimark_lu                 | 97.5 ms                                                          | 98.6 ms: 1.01x slower                                            |
| logging_format             | 7.11 us                                                          | 7.20 us: 1.01x slower                                            |
| nqueens                    | 88.4 ms                                                          | 89.5 ms: 1.01x slower                                            |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                            |
| async_generators           | 363 ms                                                           | 370 ms: 1.02x slower                                             |
| generators                 | 33.5 ms                                                          | 34.2 ms: 1.02x slower                                            |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.9 ms: 1.04x slower                                            |
| chaos                      | 59.6 ms                                                          | 61.9 ms: 1.04x slower                                            |
| raytrace                   | 260 ms                                                           | 271 ms: 1.04x slower                                             |
| pidigits                   | 254 ms                                                           | 265 ms: 1.04x slower                                             |
| bench_thread_pool          | 908 us                                                           | 951 us: 1.05x slower                                             |
| go                         | 165 ms                                                           | 173 ms: 1.05x slower                                             |
| xml_etree_parse            | 144 ms                                                           | 151 ms: 1.05x slower                                             |
| xml_etree_iterparse        | 103 ms                                                           | 108 ms: 1.05x slower                                             |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                           |
| fannkuch                   | 353 ms                                                           | 374 ms: 1.06x slower                                             |
| pyflate                    | 482 ms                                                           | 513 ms: 1.07x slower                                             |
| regex_effbot               | 3.40 ms                                                          | 3.63 ms: 1.07x slower                                            |
| deltablue                  | 3.37 ms                                                          | 3.61 ms: 1.07x slower                                            |
| pycparser                  | 1.22 sec                                                         | 1.31 sec: 1.07x slower                                           |
| pathlib                    | 17.1 ms                                                          | 19.1 ms: 1.11x slower                                            |
| mypy2                      | 764 ms                                                           | 862 ms: 1.13x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 690 ms: 1.14x slower                                             |
| async_tree_none            | 365 ms                                                           | 429 ms: 1.17x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 542 ms: 1.18x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.07 sec: 1.22x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 706 ms: 1.23x slower                                             |
| scimark_sor                | 119 ms                                                           | 146 ms: 1.23x slower                                             |
| async_tree_none_tg         | 340 ms                                                           | 435 ms: 1.28x slower                                             |
| python_startup_no_site     | 8.85 ms                                                          | 11.3 ms: 1.28x slower                                            |
| async_tree_memoization_tg  | 421 ms                                                           | 556 ms: 1.32x slower                                             |
| Geometric mean             | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (8): tornado_http, django_template, hexiom, unpickle_pure_python, sqlglot_parse, logging_silent, gunicorn, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 50.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x