# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 6b9055c
- commit date: 2024-08-14
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 353 ms: 1.21x slower                                                                |
| docutils       | 2.98 sec                                                         | 3.54 sec: 1.19x slower                                                              |
| html5lib       | 74.7 ms                                                          | 85.2 ms: 1.14x slower                                                               |
| tornado_http   | 119 ms                                                           | 127 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                            | 1.15x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 811 ms: 1.11x faster                                                                |
| async_tree_none_tg         | 340 ms                                                           | 320 ms: 1.06x faster                                                                |
| async_tree_none            | 365 ms                                                           | 348 ms: 1.05x faster                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 404 ms: 1.04x faster                                                                |
| async_tree_memoization     | 460 ms                                                           | 443 ms: 1.04x faster                                                                |
| async_tree_io              | 873 ms                                                           | 853 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                                |
| Geometric mean             | (ref)                                                            | 1.04x faster                                                                        |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 255 ms: 1.01x slower                                                                |
| float          | 80.2 ms                                                          | 93.8 ms: 1.17x slower                                                               |
| nbody          | 87.8 ms                                                          | 128 ms: 1.46x slower                                                                |
| Geometric mean | (ref)                                                            | 1.20x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                                |
| regex_v8       | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                               |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                               |
| regex_compile  | 144 ms                                                           | 208 ms: 1.45x slower                                                                |
| Geometric mean | (ref)                                                            | 1.11x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_loads           | 25.0 us                                                          | 25.6 us: 1.02x slower                                                               |
| json_dumps           | 10.8 ms                                                          | 11.9 ms: 1.10x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                           | 116 ms: 1.13x slower                                                                |
| xml_etree_process    | 59.7 ms                                                          | 70.0 ms: 1.17x slower                                                               |
| xml_etree_generate   | 85.7 ms                                                          | 101 ms: 1.17x slower                                                                |
| tomli_loads          | 2.40 sec                                                         | 2.87 sec: 1.19x slower                                                              |
| unpickle_pure_python | 224 us                                                           | 272 us: 1.21x slower                                                                |
| pickle_pure_python   | 307 us                                                           | 410 us: 1.33x slower                                                                |
| Geometric mean       | (ref)                                                            | 1.14x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                               |
| python_startup_no_site | 8.85 ms                                                          | 9.12 ms: 1.03x slower                                                               |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 65.7 ms: 1.13x slower                                                               |
| django_template | 39.0 ms                                                          | 44.4 ms: 1.14x slower                                                               |
| genshi_text     | 25.9 ms                                                          | 30.8 ms: 1.19x slower                                                               |
| mako            | 10.4 ms                                                          | 14.6 ms: 1.41x slower                                                               |
| Geometric mean  | (ref)                                                            | 1.21x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 811 ms: 1.11x faster                                                                |
| async_tree_none_tg         | 340 ms                                                           | 320 ms: 1.06x faster                                                                |
| deepcopy                   | 377 us                                                           | 355 us: 1.06x faster                                                                |
| deepcopy_reduce            | 3.39 us                                                          | 3.23 us: 1.05x faster                                                               |
| async_tree_none            | 365 ms                                                           | 348 ms: 1.05x faster                                                                |
| coverage                   | 83.5 ms                                                          | 80.0 ms: 1.04x faster                                                               |
| async_tree_memoization_tg  | 421 ms                                                           | 404 ms: 1.04x faster                                                                |
| async_tree_memoization     | 460 ms                                                           | 443 ms: 1.04x faster                                                                |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                                |
| async_tree_io              | 873 ms                                                           | 853 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                                |
| pathlib                    | 17.1 ms                                                          | 16.8 ms: 1.02x faster                                                               |
| pidigits                   | 254 ms                                                           | 255 ms: 1.01x slower                                                                |
| asyncio_websockets         | 395 ms                                                           | 398 ms: 1.01x slower                                                                |
| thrift                     | 880 us                                                           | 886 us: 1.01x slower                                                                |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                               |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.60 sec: 1.01x slower                                                              |
| gc_traversal               | 4.69 ms                                                          | 4.76 ms: 1.02x slower                                                               |
| create_gc_cycles           | 2.00 ms                                                          | 2.04 ms: 1.02x slower                                                               |
| json_loads                 | 25.0 us                                                          | 25.6 us: 1.02x slower                                                               |
| coroutines                 | 22.0 ms                                                          | 22.5 ms: 1.02x slower                                                               |
| logging_format             | 7.11 us                                                          | 7.27 us: 1.02x slower                                                               |
| asyncio_tcp                | 378 ms                                                           | 388 ms: 1.03x slower                                                                |
| python_startup_no_site     | 8.85 ms                                                          | 9.12 ms: 1.03x slower                                                               |
| regex_v8                   | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                               |
| logging_simple             | 6.40 us                                                          | 6.67 us: 1.04x slower                                                               |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                               |
| tornado_http               | 119 ms                                                           | 127 ms: 1.06x slower                                                                |
| async_generators           | 363 ms                                                           | 385 ms: 1.06x slower                                                                |
| telco                      | 8.40 ms                                                          | 8.95 ms: 1.07x slower                                                               |
| json                       | 5.35 ms                                                          | 5.78 ms: 1.08x slower                                                               |
| bench_thread_pool          | 908 us                                                           | 982 us: 1.08x slower                                                                |
| json_dumps                 | 10.8 ms                                                          | 11.9 ms: 1.10x slower                                                               |
| bpe_tokeniser              | 5.14 sec                                                         | 5.77 sec: 1.12x slower                                                              |
| xml_etree_iterparse        | 103 ms                                                           | 116 ms: 1.13x slower                                                                |
| meteor_contest             | 128 ms                                                           | 145 ms: 1.13x slower                                                                |
| genshi_xml                 | 58.1 ms                                                          | 65.7 ms: 1.13x slower                                                               |
| mdp                        | 2.46 sec                                                         | 2.80 sec: 1.14x slower                                                              |
| django_template            | 39.0 ms                                                          | 44.4 ms: 1.14x slower                                                               |
| html5lib                   | 74.7 ms                                                          | 85.2 ms: 1.14x slower                                                               |
| richards_super             | 61.2 ms                                                          | 71.2 ms: 1.16x slower                                                               |
| float                      | 80.2 ms                                                          | 93.8 ms: 1.17x slower                                                               |
| xml_etree_process          | 59.7 ms                                                          | 70.0 ms: 1.17x slower                                                               |
| typing_runtime_protocols   | 171 us                                                           | 200 us: 1.17x slower                                                                |
| xml_etree_generate         | 85.7 ms                                                          | 101 ms: 1.17x slower                                                                |
| sqlglot_normalize          | 120 ms                                                           | 142 ms: 1.18x slower                                                                |
| docutils                   | 2.98 sec                                                         | 3.54 sec: 1.19x slower                                                              |
| genshi_text                | 25.9 ms                                                          | 30.8 ms: 1.19x slower                                                               |
| richards                   | 53.4 ms                                                          | 63.6 ms: 1.19x slower                                                               |
| tomli_loads                | 2.40 sec                                                         | 2.87 sec: 1.19x slower                                                              |
| go                         | 165 ms                                                           | 199 ms: 1.21x slower                                                                |
| 2to3                       | 291 ms                                                           | 353 ms: 1.21x slower                                                                |
| unpickle_pure_python       | 224 us                                                           | 272 us: 1.21x slower                                                                |
| pylint                     | 339 ms                                                           | 411 ms: 1.21x slower                                                                |
| sqlglot_optimize           | 59.5 ms                                                          | 72.5 ms: 1.22x slower                                                               |
| sympy_integrate            | 23.2 ms                                                          | 28.5 ms: 1.23x slower                                                               |
| sympy_sum                  | 155 ms                                                           | 192 ms: 1.24x slower                                                                |
| sqlglot_parse              | 1.39 ms                                                          | 1.73 ms: 1.24x slower                                                               |
| raytrace                   | 260 ms                                                           | 325 ms: 1.25x slower                                                                |
| sympy_expand               | 501 ms                                                           | 626 ms: 1.25x slower                                                                |
| sqlglot_transpile          | 1.76 ms                                                          | 2.21 ms: 1.25x slower                                                               |
| pprint_safe_repr           | 818 ms                                                           | 1.03 sec: 1.26x slower                                                              |
| pycparser                  | 1.22 sec                                                         | 1.54 sec: 1.26x slower                                                              |
| sympy_str                  | 295 ms                                                           | 373 ms: 1.26x slower                                                                |
| pprint_pformat             | 1.66 sec                                                         | 2.11 sec: 1.27x slower                                                              |
| pyflate                    | 482 ms                                                           | 613 ms: 1.27x slower                                                                |
| deepcopy_memo              | 37.3 us                                                          | 47.5 us: 1.27x slower                                                               |
| crypto_pyaes               | 73.6 ms                                                          | 95.2 ms: 1.29x slower                                                               |
| scimark_lu                 | 97.5 ms                                                          | 127 ms: 1.30x slower                                                                |
| nqueens                    | 88.4 ms                                                          | 116 ms: 1.32x slower                                                                |
| pickle_pure_python         | 307 us                                                           | 410 us: 1.33x slower                                                                |
| chaos                      | 59.6 ms                                                          | 80.0 ms: 1.34x slower                                                               |
| generators                 | 33.5 ms                                                          | 45.3 ms: 1.35x slower                                                               |
| scimark_fft                | 312 ms                                                           | 426 ms: 1.37x slower                                                                |
| fannkuch                   | 353 ms                                                           | 496 ms: 1.41x slower                                                                |
| mako                       | 10.4 ms                                                          | 14.6 ms: 1.41x slower                                                               |
| scimark_monte_carlo        | 65.5 ms                                                          | 93.7 ms: 1.43x slower                                                               |
| regex_compile              | 144 ms                                                           | 208 ms: 1.45x slower                                                                |
| nbody                      | 87.8 ms                                                          | 128 ms: 1.46x slower                                                                |
| scimark_sor                | 119 ms                                                           | 181 ms: 1.52x slower                                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.62 ms: 1.55x slower                                                               |
| deltablue                  | 3.37 ms                                                          | 5.24 ms: 1.55x slower                                                               |
| spectral_norm              | 97.3 ms                                                          | 155 ms: 1.59x slower                                                                |
| logging_silent             | 96.3 ns                                                          | 154 ns: 1.60x slower                                                                |
| comprehensions             | 17.0 us                                                          | 27.2 us: 1.60x slower                                                               |
| hexiom                     | 6.35 ms                                                          | 10.4 ms: 1.64x slower                                                               |
| Geometric mean             | (ref)                                                            | 1.16x slower                                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, async_tree_cpu_io_mixed, bench_mp_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.02x