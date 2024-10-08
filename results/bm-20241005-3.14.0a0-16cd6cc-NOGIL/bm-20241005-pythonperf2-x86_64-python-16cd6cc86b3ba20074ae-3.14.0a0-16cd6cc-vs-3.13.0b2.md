# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.40x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 421 ms: 1.44x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.38 sec: 1.13x slower                                                      |
| html5lib       | 74.7 ms                                                          | 105 ms: 1.41x slower                                                        |
| tornado_http   | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                            | 1.34x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 882 ms: 1.02x faster                                                        |
| async_tree_io              | 873 ms                                                           | 939 ms: 1.07x slower                                                        |
| async_tree_none_tg         | 340 ms                                                           | 371 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 636 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 681 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 519 ms: 1.13x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 475 ms: 1.13x slower                                                        |
| async_tree_none            | 365 ms                                                           | 422 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.10x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 250 ms: 1.02x faster                                                        |
| float          | 80.2 ms                                                          | 141 ms: 1.76x slower                                                        |
| nbody          | 87.8 ms                                                          | 193 ms: 2.19x slower                                                        |
| Geometric mean | (ref)                                                            | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 246 ms: 1.01x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                       |
| regex_compile  | 144 ms                                                           | 223 ms: 1.54x slower                                                        |
| Geometric mean | (ref)                                                            | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle               | 10.6 us                                                          | 9.98 us: 1.06x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 30.9 us: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| pickle_list          | 4.44 us                                                          | 4.40 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 108 ms: 1.05x slower                                                        |
| unpickle             | 15.7 us                                                          | 17.1 us: 1.09x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 5.22 us: 1.11x slower                                                       |
| json_loads           | 25.0 us                                                          | 29.5 us: 1.18x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 13.7 ms: 1.28x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 111 ms: 1.29x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 3.31 sec: 1.38x slower                                                      |
| xml_etree_process    | 59.7 ms                                                          | 89.3 ms: 1.49x slower                                                       |
| unpickle_pure_python | 224 us                                                           | 399 us: 1.78x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 579 us: 1.88x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 17.4 ms: 1.32x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 81.0 ms: 1.39x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 42.0 ms: 1.62x slower                                                       |
| django_template | 39.0 ms                                                          | 65.4 ms: 1.68x slower                                                       |
| mako            | 10.4 ms                                                          | 21.3 ms: 2.05x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.67x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 3.19 ms: 1.47x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.72 ms: 1.17x faster                                                       |
| pickle                     | 10.6 us                                                          | 9.98 us: 1.06x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 30.9 us: 1.06x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 377 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 882 ms: 1.02x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.02x faster                                                        |
| regex_dna                  | 249 ms                                                           | 246 ms: 1.01x faster                                                        |
| pickle_list                | 4.44 us                                                          | 4.40 us: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 108 ms: 1.05x slower                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.98 us: 1.06x slower                                                       |
| async_tree_io              | 873 ms                                                           | 939 ms: 1.07x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                       |
| async_tree_none_tg         | 340 ms                                                           | 371 ms: 1.09x slower                                                        |
| unpickle                   | 15.7 us                                                          | 17.1 us: 1.09x slower                                                       |
| json                       | 5.35 ms                                                          | 5.94 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 636 ms: 1.11x slower                                                        |
| unpickle_list              | 4.70 us                                                          | 5.22 us: 1.11x slower                                                       |
| deepcopy                   | 377 us                                                           | 423 us: 1.12x slower                                                        |
| pathlib                    | 17.1 ms                                                          | 19.2 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 681 ms: 1.13x slower                                                        |
| async_tree_memoization     | 460 ms                                                           | 519 ms: 1.13x slower                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 475 ms: 1.13x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.38 sec: 1.13x slower                                                      |
| async_tree_none            | 365 ms                                                           | 422 ms: 1.15x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.83 sec: 1.16x slower                                                      |
| json_loads                 | 25.0 us                                                          | 29.5 us: 1.18x slower                                                       |
| asyncio_tcp                | 378 ms                                                           | 455 ms: 1.21x slower                                                        |
| telco                      | 8.40 ms                                                          | 10.2 ms: 1.22x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 26.9 ms: 1.23x slower                                                       |
| scimark_fft                | 312 ms                                                           | 384 ms: 1.23x slower                                                        |
| generators                 | 33.5 ms                                                          | 42.1 ms: 1.26x slower                                                       |
| coverage                   | 83.5 ms                                                          | 105 ms: 1.26x slower                                                        |
| pylint                     | 339 ms                                                           | 430 ms: 1.27x slower                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 6.52 sec: 1.27x slower                                                      |
| json_dumps                 | 10.8 ms                                                          | 13.7 ms: 1.28x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 5.48 ms: 1.28x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 111 ms: 1.29x slower                                                        |
| mdp                        | 2.46 sec                                                         | 3.19 sec: 1.30x slower                                                      |
| deepcopy_memo              | 37.3 us                                                          | 49.0 us: 1.31x slower                                                       |
| python_startup             | 13.2 ms                                                          | 17.4 ms: 1.32x slower                                                       |
| async_generators           | 363 ms                                                           | 479 ms: 1.32x slower                                                        |
| dulwich_log                | 67.3 ms                                                          | 89.2 ms: 1.33x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 11.8 ms: 1.33x slower                                                       |
| meteor_contest             | 128 ms                                                           | 171 ms: 1.33x slower                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 4.55 us: 1.34x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 3.31 sec: 1.38x slower                                                      |
| pycparser                  | 1.22 sec                                                         | 1.70 sec: 1.39x slower                                                      |
| tornado_http               | 119 ms                                                           | 166 ms: 1.39x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 81.0 ms: 1.39x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 32.4 ms: 1.40x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 105 ms: 1.41x slower                                                        |
| 2to3                       | 291 ms                                                           | 421 ms: 1.44x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 128 ms: 1.45x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 179 ms: 1.49x slower                                                        |
| xml_etree_process          | 59.7 ms                                                          | 89.3 ms: 1.49x slower                                                       |
| sympy_str                  | 295 ms                                                           | 445 ms: 1.51x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 90.1 ms: 1.51x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 258 us: 1.51x slower                                                        |
| richards                   | 53.4 ms                                                          | 81.6 ms: 1.53x slower                                                       |
| thrift                     | 880 us                                                           | 1.34 ms: 1.53x slower                                                       |
| regex_compile              | 144 ms                                                           | 223 ms: 1.54x slower                                                        |
| pyflate                    | 482 ms                                                           | 754 ms: 1.57x slower                                                        |
| richards_super             | 61.2 ms                                                          | 97.8 ms: 1.60x slower                                                       |
| sympy_expand               | 501 ms                                                           | 805 ms: 1.61x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 119 ms: 1.62x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 42.0 ms: 1.62x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 1.35 sec: 1.65x slower                                                      |
| spectral_norm              | 97.3 ms                                                          | 161 ms: 1.65x slower                                                        |
| fannkuch                   | 353 ms                                                           | 583 ms: 1.65x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 259 ms: 1.67x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 2.79 sec: 1.68x slower                                                      |
| django_template            | 39.0 ms                                                          | 65.4 ms: 1.68x slower                                                       |
| comprehensions             | 17.0 us                                                          | 29.5 us: 1.74x slower                                                       |
| logging_format             | 7.11 us                                                          | 12.4 us: 1.74x slower                                                       |
| float                      | 80.2 ms                                                          | 141 ms: 1.76x slower                                                        |
| logging_simple             | 6.40 us                                                          | 11.3 us: 1.77x slower                                                       |
| go                         | 165 ms                                                           | 292 ms: 1.77x slower                                                        |
| unpickle_pure_python       | 224 us                                                           | 399 us: 1.78x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 11.4 ms: 1.79x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 1.65 ms: 1.82x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 579 us: 1.88x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 181 ns: 1.88x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 3.34 ms: 1.89x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 130 ms: 1.98x slower                                                        |
| chaos                      | 59.6 ms                                                          | 121 ms: 2.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 2.82 ms: 2.03x slower                                                       |
| mako                       | 10.4 ms                                                          | 21.3 ms: 2.05x slower                                                       |
| scimark_sor                | 119 ms                                                           | 247 ms: 2.08x slower                                                        |
| nbody                      | 87.8 ms                                                          | 193 ms: 2.19x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 216 ms: 2.22x slower                                                        |
| raytrace                   | 260 ms                                                           | 596 ms: 2.29x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 8.13 ms: 2.41x slower                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 34.0 ms: 6.93x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.40x slower                                                                |
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.29x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.16x