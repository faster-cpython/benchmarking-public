# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 346 ms: 1.19x slower                                                         |
| chameleon      | 7.40 ms                                                          | 8.73 ms: 1.18x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.48 sec: 1.17x slower                                                       |
| html5lib       | 74.7 ms                                                          | 89.0 ms: 1.19x slower                                                        |
| tornado_http   | 119 ms                                                           | 130 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                            | 1.16x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 881 ms: 1.02x faster                                                         |
| async_tree_memoization     | 460 ms                                                           | 480 ms: 1.04x slower                                                         |
| async_tree_io              | 873 ms                                                           | 921 ms: 1.05x slower                                                         |
| async_tree_none_tg         | 340 ms                                                           | 367 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 619 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 656 ms: 1.08x slower                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 461 ms: 1.10x slower                                                         |
| async_tree_none            | 365 ms                                                           | 402 ms: 1.10x slower                                                         |
| Geometric mean             | (ref)                                                            | 1.06x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                         |
| float          | 80.2 ms                                                          | 97.4 ms: 1.21x slower                                                        |
| nbody          | 87.8 ms                                                          | 125 ms: 1.42x slower                                                         |
| Geometric mean | (ref)                                                            | 1.20x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 247 ms: 1.01x faster                                                         |
| regex_v8       | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.63 ms: 1.07x slower                                                        |
| regex_compile  | 144 ms                                                           | 216 ms: 1.50x slower                                                         |
| Geometric mean | (ref)                                                            | 1.13x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 15.0 us: 1.04x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.4 us: 1.02x faster                                                        |
| pickle_list          | 4.44 us                                                          | 4.49 us: 1.01x slower                                                        |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                        |
| unpickle_list        | 4.70 us                                                          | 4.81 us: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 148 ms: 1.03x slower                                                         |
| json_dumps           | 10.8 ms                                                          | 11.4 ms: 1.05x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 115 ms: 1.13x slower                                                         |
| xml_etree_generate   | 85.7 ms                                                          | 96.7 ms: 1.13x slower                                                        |
| xml_etree_process    | 59.7 ms                                                          | 69.0 ms: 1.16x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.94 sec: 1.23x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 305 us: 1.36x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 434 us: 1.41x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.10x slower                                                                 |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 8.92 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 39.0 ms                                                          | 46.4 ms: 1.19x slower                                                        |
| genshi_xml      | 58.1 ms                                                          | 70.3 ms: 1.21x slower                                                        |
| genshi_text     | 25.9 ms                                                          | 33.3 ms: 1.29x slower                                                        |
| mako            | 10.4 ms                                                          | 14.5 ms: 1.40x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.27x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coverage                   | 83.5 ms                                                          | 79.5 ms: 1.05x faster                                                        |
| unpickle                   | 15.7 us                                                          | 15.0 us: 1.04x faster                                                        |
| json_loads                 | 25.0 us                                                          | 24.4 us: 1.02x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 881 ms: 1.02x faster                                                         |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                         |
| regex_dna                  | 249 ms                                                           | 247 ms: 1.01x faster                                                         |
| pidigits                   | 254 ms                                                           | 254 ms: 1.00x slower                                                         |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 8.92 ms: 1.01x slower                                                        |
| pickle_list                | 4.44 us                                                          | 4.49 us: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                        |
| pickle                     | 10.6 us                                                          | 10.8 us: 1.02x slower                                                        |
| generators                 | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                                        |
| unpickle_list              | 4.70 us                                                          | 4.81 us: 1.02x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.87 us: 1.03x slower                                                        |
| asyncio_tcp                | 378 ms                                                           | 389 ms: 1.03x slower                                                         |
| thrift                     | 880 us                                                           | 907 us: 1.03x slower                                                         |
| create_gc_cycles           | 2.00 ms                                                          | 2.07 ms: 1.03x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 148 ms: 1.03x slower                                                         |
| json                       | 5.35 ms                                                          | 5.57 ms: 1.04x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 480 ms: 1.04x slower                                                         |
| coroutines                 | 22.0 ms                                                          | 23.0 ms: 1.04x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.48 us: 1.05x slower                                                        |
| async_tree_io              | 873 ms                                                           | 921 ms: 1.05x slower                                                         |
| json_dumps                 | 10.8 ms                                                          | 11.4 ms: 1.05x slower                                                        |
| flaskblogging              | 4.68 ms                                                          | 4.97 ms: 1.06x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.84 us: 1.07x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.63 ms: 1.07x slower                                                        |
| pathlib                    | 17.1 ms                                                          | 18.4 ms: 1.08x slower                                                        |
| async_generators           | 363 ms                                                           | 391 ms: 1.08x slower                                                         |
| async_tree_none_tg         | 340 ms                                                           | 367 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 619 ms: 1.08x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 656 ms: 1.08x slower                                                         |
| dask                       | 391 ms                                                           | 426 ms: 1.09x slower                                                         |
| tornado_http               | 119 ms                                                           | 130 ms: 1.09x slower                                                         |
| telco                      | 8.40 ms                                                          | 9.17 ms: 1.09x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 461 ms: 1.10x slower                                                         |
| async_tree_none            | 365 ms                                                           | 402 ms: 1.10x slower                                                         |
| aiohttp                    | 1.07 ms                                                          | 1.19 ms: 1.11x slower                                                        |
| gunicorn                   | 1.04 ms                                                          | 1.16 ms: 1.11x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.01 ms: 1.11x slower                                                        |
| meteor_contest             | 128 ms                                                           | 144 ms: 1.12x slower                                                         |
| xml_etree_iterparse        | 103 ms                                                           | 115 ms: 1.13x slower                                                         |
| mdp                        | 2.46 sec                                                         | 2.77 sec: 1.13x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 96.7 ms: 1.13x slower                                                        |
| richards_super             | 61.2 ms                                                          | 70.1 ms: 1.15x slower                                                        |
| xml_etree_process          | 59.7 ms                                                          | 69.0 ms: 1.16x slower                                                        |
| richards                   | 53.4 ms                                                          | 62.3 ms: 1.17x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 199 us: 1.17x slower                                                         |
| docutils                   | 2.98 sec                                                         | 3.48 sec: 1.17x slower                                                       |
| pylint                     | 339 ms                                                           | 396 ms: 1.17x slower                                                         |
| chameleon                  | 7.40 ms                                                          | 8.73 ms: 1.18x slower                                                        |
| 2to3                       | 291 ms                                                           | 346 ms: 1.19x slower                                                         |
| mypy2                      | 764 ms                                                           | 908 ms: 1.19x slower                                                         |
| django_template            | 39.0 ms                                                          | 46.4 ms: 1.19x slower                                                        |
| dulwich_log                | 67.3 ms                                                          | 80.2 ms: 1.19x slower                                                        |
| html5lib                   | 74.7 ms                                                          | 89.0 ms: 1.19x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.46 sec: 1.20x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 144 ms: 1.20x slower                                                         |
| sqlglot_optimize           | 59.5 ms                                                          | 71.5 ms: 1.20x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.10 us: 1.21x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 70.3 ms: 1.21x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 28.1 ms: 1.21x slower                                                        |
| float                      | 80.2 ms                                                          | 97.4 ms: 1.21x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 189 ms: 1.22x slower                                                         |
| tomli_loads                | 2.40 sec                                                         | 2.94 sec: 1.23x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 2.19 ms: 1.24x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.73 ms: 1.25x slower                                                        |
| sympy_expand               | 501 ms                                                           | 625 ms: 1.25x slower                                                         |
| go                         | 165 ms                                                           | 206 ms: 1.25x slower                                                         |
| crypto_pyaes               | 73.6 ms                                                          | 92.6 ms: 1.26x slower                                                        |
| sympy_str                  | 295 ms                                                           | 372 ms: 1.26x slower                                                         |
| pprint_safe_repr           | 818 ms                                                           | 1.03 sec: 1.26x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 2.12 sec: 1.27x slower                                                       |
| raytrace                   | 260 ms                                                           | 333 ms: 1.28x slower                                                         |
| deepcopy                   | 377 us                                                           | 483 us: 1.28x slower                                                         |
| genshi_text                | 25.9 ms                                                          | 33.3 ms: 1.29x slower                                                        |
| pyflate                    | 482 ms                                                           | 654 ms: 1.36x slower                                                         |
| unpickle_pure_python       | 224 us                                                           | 305 us: 1.36x slower                                                         |
| chaos                      | 59.6 ms                                                          | 81.1 ms: 1.36x slower                                                        |
| scimark_fft                | 312 ms                                                           | 425 ms: 1.36x slower                                                         |
| nqueens                    | 88.4 ms                                                          | 120 ms: 1.36x slower                                                         |
| deltablue                  | 3.37 ms                                                          | 4.60 ms: 1.36x slower                                                        |
| scimark_sor                | 119 ms                                                           | 165 ms: 1.39x slower                                                         |
| fannkuch                   | 353 ms                                                           | 490 ms: 1.39x slower                                                         |
| mako                       | 10.4 ms                                                          | 14.5 ms: 1.40x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 434 us: 1.41x slower                                                         |
| nbody                      | 87.8 ms                                                          | 125 ms: 1.42x slower                                                         |
| regex_compile              | 144 ms                                                           | 216 ms: 1.50x slower                                                         |
| scimark_monte_carlo        | 65.5 ms                                                          | 99.5 ms: 1.52x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 149 ms: 1.53x slower                                                         |
| scimark_lu                 | 97.5 ms                                                          | 149 ms: 1.53x slower                                                         |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.60 ms: 1.54x slower                                                        |
| deepcopy_memo              | 37.3 us                                                          | 58.6 us: 1.57x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 155 ns: 1.61x slower                                                         |
| comprehensions             | 17.0 us                                                          | 27.8 us: 1.64x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 10.7 ms: 1.69x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.17x slower                                                                 |

Benchmark hidden because not significant (3): gc_traversal, pickle_dict, bench_mp_pool
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.01x