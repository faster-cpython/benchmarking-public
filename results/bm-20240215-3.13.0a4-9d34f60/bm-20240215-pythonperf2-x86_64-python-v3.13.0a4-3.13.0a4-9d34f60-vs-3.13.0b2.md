# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x slower
- HPT reliability: 52.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                            |
| docutils       | 2.98 sec                                                         | 2.84 sec: 1.05x faster                                           |
| html5lib       | 74.7 ms                                                          | 76.0 ms: 1.02x slower                                            |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 699 ms: 1.16x slower                                             |
| async_tree_none            | 365 ms                                                           | 434 ms: 1.19x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 546 ms: 1.19x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 705 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.24x slower                                           |
| async_tree_none_tg         | 340 ms                                                           | 434 ms: 1.27x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 551 ms: 1.31x slower                                             |
| Geometric mean             | (ref)                                                            | 1.22x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.8 ms: 1.04x faster                                            |
| float          | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                            |
| pidigits       | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.03x faster                                             |
| regex_compile  | 144 ms                                                           | 142 ms: 1.01x faster                                             |
| regex_v8       | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                            |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.3 us: 1.08x faster                                            |
| xml_etree_process    | 59.7 ms                                                          | 57.7 ms: 1.03x faster                                            |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                             |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                            |
| pickle_list          | 4.44 us                                                          | 4.33 us: 1.03x faster                                            |
| unpickle             | 15.7 us                                                          | 15.3 us: 1.03x faster                                            |
| tomli_loads          | 2.40 sec                                                         | 2.38 sec: 1.01x faster                                           |
| xml_etree_generate   | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                            |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| xml_etree_iterparse  | 103 ms                                                           | 105 ms: 1.02x slower                                             |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                             |
| xml_etree_parse      | 144 ms                                                           | 148 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.6 ms: 1.05x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.0 ms: 1.25x slower                                            |
| Geometric mean         | (ref)                                                            | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.8 ms: 1.04x faster                                            |
| django_template | 39.0 ms                                                          | 38.4 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 117 us: 1.46x faster                                             |
| create_gc_cycles           | 2.00 ms                                                          | 1.61 ms: 1.25x faster                                            |
| gc_traversal               | 4.69 ms                                                          | 3.76 ms: 1.25x faster                                            |
| pickle_dict                | 32.8 us                                                          | 30.3 us: 1.08x faster                                            |
| bench_mp_pool              | 4.91 ms                                                          | 4.58 ms: 1.07x faster                                            |
| spectral_norm              | 97.3 ms                                                          | 92.5 ms: 1.05x faster                                            |
| sqlglot_normalize          | 120 ms                                                           | 115 ms: 1.05x faster                                             |
| docutils                   | 2.98 sec                                                         | 2.84 sec: 1.05x faster                                           |
| python_startup             | 13.2 ms                                                          | 12.6 ms: 1.05x faster                                            |
| genshi_xml                 | 58.1 ms                                                          | 55.8 ms: 1.04x faster                                            |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                            |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                             |
| nbody                      | 87.8 ms                                                          | 84.8 ms: 1.04x faster                                            |
| xml_etree_process          | 59.7 ms                                                          | 57.7 ms: 1.03x faster                                            |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.03x faster                                             |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                             |
| pprint_safe_repr           | 818 ms                                                           | 791 ms: 1.03x faster                                             |
| scimark_lu                 | 97.5 ms                                                          | 94.4 ms: 1.03x faster                                            |
| crypto_pyaes               | 73.6 ms                                                          | 71.3 ms: 1.03x faster                                            |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                            |
| telco                      | 8.40 ms                                                          | 8.16 ms: 1.03x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                            |
| logging_silent             | 96.3 ns                                                          | 93.6 ns: 1.03x faster                                            |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.03x faster                                           |
| comprehensions             | 17.0 us                                                          | 16.5 us: 1.03x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.03x faster                                             |
| pickle_list                | 4.44 us                                                          | 4.33 us: 1.03x faster                                            |
| unpickle                   | 15.7 us                                                          | 15.3 us: 1.03x faster                                            |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.02x faster                                            |
| deepcopy                   | 377 us                                                           | 369 us: 1.02x faster                                             |
| flaskblogging              | 4.68 ms                                                          | 4.58 ms: 1.02x faster                                            |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                             |
| float                      | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                            |
| sqlglot_optimize           | 59.5 ms                                                          | 58.6 ms: 1.02x faster                                            |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.02x faster                                             |
| django_template            | 39.0 ms                                                          | 38.4 ms: 1.02x faster                                            |
| regex_compile              | 144 ms                                                           | 142 ms: 1.01x faster                                             |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                             |
| sympy_expand               | 501 ms                                                           | 496 ms: 1.01x faster                                             |
| json                       | 5.35 ms                                                          | 5.30 ms: 1.01x faster                                            |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                             |
| async_generators           | 363 ms                                                           | 359 ms: 1.01x faster                                             |
| tomli_loads                | 2.40 sec                                                         | 2.38 sec: 1.01x faster                                           |
| aiohttp                    | 1.07 ms                                                          | 1.06 ms: 1.01x faster                                            |
| xml_etree_generate         | 85.7 ms                                                          | 85.1 ms: 1.01x faster                                            |
| coverage                   | 83.5 ms                                                          | 82.9 ms: 1.01x faster                                            |
| thrift                     | 880 us                                                           | 873 us: 1.01x faster                                             |
| richards_super             | 61.2 ms                                                          | 60.8 ms: 1.01x faster                                            |
| deepcopy_memo              | 37.3 us                                                          | 37.2 us: 1.00x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                           |
| regex_v8                   | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                            |
| 2to3                       | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| chameleon                  | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                            |
| nqueens                    | 88.4 ms                                                          | 88.8 ms: 1.00x slower                                            |
| deepcopy_reduce            | 3.39 us                                                          | 3.41 us: 1.01x slower                                            |
| raytrace                   | 260 ms                                                           | 262 ms: 1.01x slower                                             |
| coroutines                 | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                            |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| hexiom                     | 6.35 ms                                                          | 6.44 ms: 1.01x slower                                            |
| logging_format             | 7.11 us                                                          | 7.21 us: 1.01x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.01x slower                                           |
| html5lib                   | 74.7 ms                                                          | 76.0 ms: 1.02x slower                                            |
| richards                   | 53.4 ms                                                          | 54.4 ms: 1.02x slower                                            |
| generators                 | 33.5 ms                                                          | 34.1 ms: 1.02x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                            |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.0 ms: 1.02x slower                                            |
| chaos                      | 59.6 ms                                                          | 61.0 ms: 1.02x slower                                            |
| xml_etree_iterparse        | 103 ms                                                           | 105 ms: 1.02x slower                                             |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                             |
| dulwich_log                | 67.3 ms                                                          | 69.0 ms: 1.02x slower                                            |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                            |
| pickle_pure_python         | 307 us                                                           | 316 us: 1.03x slower                                             |
| xml_etree_parse            | 144 ms                                                           | 148 ms: 1.03x slower                                             |
| go                         | 165 ms                                                           | 170 ms: 1.03x slower                                             |
| pidigits                   | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.63 us: 1.03x slower                                            |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                           |
| pyflate                    | 482 ms                                                           | 506 ms: 1.05x slower                                             |
| bench_thread_pool          | 908 us                                                           | 958 us: 1.06x slower                                             |
| deltablue                  | 3.37 ms                                                          | 3.59 ms: 1.06x slower                                            |
| pathlib                    | 17.1 ms                                                          | 19.0 ms: 1.11x slower                                            |
| fannkuch                   | 353 ms                                                           | 393 ms: 1.12x slower                                             |
| mypy2                      | 764 ms                                                           | 867 ms: 1.13x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 699 ms: 1.16x slower                                             |
| async_tree_none            | 365 ms                                                           | 434 ms: 1.19x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 546 ms: 1.19x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.08 sec: 1.20x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 705 ms: 1.23x slower                                             |
| scimark_sor                | 119 ms                                                           | 146 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.08 sec: 1.24x slower                                           |
| python_startup_no_site     | 8.85 ms                                                          | 11.0 ms: 1.25x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 434 ms: 1.27x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 551 ms: 1.31x slower                                             |
| Geometric mean             | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (7): unpickle_list, gunicorn, sqlglot_parse, genshi_text, mako, sympy_integrate, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 52.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x