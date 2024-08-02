# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 343 ms: 1.18x slower                                                        |
| chameleon      | 7.40 ms                                                          | 8.74 ms: 1.18x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.45 sec: 1.16x slower                                                      |
| html5lib       | 74.7 ms                                                          | 87.5 ms: 1.17x slower                                                       |
| tornado_http   | 119 ms                                                           | 130 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                            | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 932 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 603 ms: 1.05x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 363 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 645 ms: 1.07x slower                                                        |
| async_tree_io              | 873 ms                                                           | 935 ms: 1.07x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 496 ms: 1.08x slower                                                        |
| async_tree_none            | 365 ms                                                           | 396 ms: 1.08x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 459 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.07x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 97.3 ms: 1.21x slower                                                       |
| nbody          | 87.8 ms                                                          | 124 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                            | 1.20x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.4 ms: 1.02x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                           | 215 ms: 1.49x slower                                                        |
| Geometric mean | (ref)                                                            | 1.11x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.8 us: 1.06x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.6 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| pickle_list          | 4.44 us                                                          | 4.65 us: 1.05x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 11.3 ms: 1.05x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 113 ms: 1.11x slower                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 98.3 ms: 1.15x slower                                                       |
| xml_etree_process    | 59.7 ms                                                          | 68.8 ms: 1.15x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.95 sec: 1.23x slower                                                      |
| unpickle_pure_python | 224 us                                                           | 311 us: 1.38x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 437 us: 1.42x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.10x slower                                                                |

Benchmark hidden because not significant (3): json_loads, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 67.9 ms: 1.17x slower                                                       |
| django_template | 39.0 ms                                                          | 45.9 ms: 1.18x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 33.4 ms: 1.29x slower                                                       |
| mako            | 10.4 ms                                                          | 14.0 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.24x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict                | 32.8 us                                                          | 30.8 us: 1.06x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.51 ms: 1.04x faster                                                       |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.03x faster                                                        |
| coverage                   | 83.5 ms                                                          | 82.4 ms: 1.01x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.6 us: 1.01x faster                                                       |
| python_startup             | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 17.2 ms: 1.00x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                                       |
| generators                 | 33.5 ms                                                          | 33.9 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                      |
| regex_v8                   | 26.0 ms                                                          | 26.4 ms: 1.02x slower                                                       |
| json                       | 5.35 ms                                                          | 5.46 ms: 1.02x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 386 ms: 1.02x slower                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 2.05 ms: 1.02x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 900 ms                                                           | 932 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.90 us: 1.04x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 22.9 ms: 1.04x slower                                                       |
| pickle_list                | 4.44 us                                                          | 4.65 us: 1.05x slower                                                       |
| flaskblogging              | 4.68 ms                                                          | 4.92 ms: 1.05x slower                                                       |
| thrift                     | 880 us                                                           | 925 us: 1.05x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.48 us: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 603 ms: 1.05x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 11.3 ms: 1.05x slower                                                       |
| async_tree_none_tg         | 340 ms                                                           | 363 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 645 ms: 1.07x slower                                                        |
| async_tree_io              | 873 ms                                                           | 935 ms: 1.07x slower                                                        |
| richards_super             | 61.2 ms                                                          | 65.9 ms: 1.08x slower                                                       |
| dask                       | 391 ms                                                           | 422 ms: 1.08x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 496 ms: 1.08x slower                                                        |
| async_tree_none            | 365 ms                                                           | 396 ms: 1.08x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.94 us: 1.08x slower                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 459 ms: 1.09x slower                                                        |
| tornado_http               | 119 ms                                                           | 130 ms: 1.09x slower                                                        |
| telco                      | 8.40 ms                                                          | 9.20 ms: 1.10x slower                                                       |
| richards                   | 53.4 ms                                                          | 58.9 ms: 1.10x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 113 ms: 1.11x slower                                                        |
| async_generators           | 363 ms                                                           | 404 ms: 1.12x slower                                                        |
| meteor_contest             | 128 ms                                                           | 144 ms: 1.12x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 1.02 ms: 1.13x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.81 sec: 1.14x slower                                                      |
| xml_etree_generate         | 85.7 ms                                                          | 98.3 ms: 1.15x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 68.8 ms: 1.15x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.45 sec: 1.16x slower                                                      |
| dulwich_log                | 67.3 ms                                                          | 78.0 ms: 1.16x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 140 ms: 1.17x slower                                                        |
| pylint                     | 339 ms                                                           | 396 ms: 1.17x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 67.9 ms: 1.17x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 87.5 ms: 1.17x slower                                                       |
| 2to3                       | 291 ms                                                           | 343 ms: 1.18x slower                                                        |
| django_template            | 39.0 ms                                                          | 45.9 ms: 1.18x slower                                                       |
| chameleon                  | 7.40 ms                                                          | 8.74 ms: 1.18x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 70.6 ms: 1.19x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.45 sec: 1.19x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 204 us: 1.20x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.08 us: 1.20x slower                                                       |
| float                      | 80.2 ms                                                          | 97.3 ms: 1.21x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 28.2 ms: 1.22x slower                                                       |
| go                         | 165 ms                                                           | 202 ms: 1.22x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.95 sec: 1.23x slower                                                      |
| sympy_sum                  | 155 ms                                                           | 190 ms: 1.23x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 2.18 ms: 1.23x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.73 ms: 1.24x slower                                                       |
| raytrace                   | 260 ms                                                           | 323 ms: 1.24x slower                                                        |
| pprint_safe_repr           | 818 ms                                                           | 1.02 sec: 1.24x slower                                                      |
| pprint_pformat             | 1.66 sec                                                         | 2.08 sec: 1.25x slower                                                      |
| deepcopy                   | 377 us                                                           | 473 us: 1.25x slower                                                        |
| sympy_str                  | 295 ms                                                           | 372 ms: 1.26x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 93.4 ms: 1.27x slower                                                       |
| sympy_expand               | 501 ms                                                           | 636 ms: 1.27x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 33.4 ms: 1.29x slower                                                       |
| scimark_sor                | 119 ms                                                           | 159 ms: 1.34x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 118 ms: 1.34x slower                                                        |
| fannkuch                   | 353 ms                                                           | 473 ms: 1.34x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 4.53 ms: 1.34x slower                                                       |
| mako                       | 10.4 ms                                                          | 14.0 ms: 1.35x slower                                                       |
| pyflate                    | 482 ms                                                           | 651 ms: 1.35x slower                                                        |
| chaos                      | 59.6 ms                                                          | 80.9 ms: 1.36x slower                                                       |
| scimark_fft                | 312 ms                                                           | 428 ms: 1.37x slower                                                        |
| unpickle_pure_python       | 224 us                                                           | 311 us: 1.38x slower                                                        |
| nbody                      | 87.8 ms                                                          | 124 ms: 1.41x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 437 us: 1.42x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 142 ms: 1.45x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 97.8 ms: 1.49x slower                                                       |
| regex_compile              | 144 ms                                                           | 215 ms: 1.49x slower                                                        |
| spectral_norm              | 97.3 ms                                                          | 148 ms: 1.52x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.49 ms: 1.52x slower                                                       |
| deepcopy_memo              | 37.3 us                                                          | 57.8 us: 1.55x slower                                                       |
| comprehensions             | 17.0 us                                                          | 27.4 us: 1.61x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 10.4 ms: 1.64x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 165 ns: 1.71x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.17x slower                                                                |

Benchmark hidden because not significant (6): asyncio_websockets, json_loads, bench_mp_pool, unpickle_list, pidigits, pickle
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.01x