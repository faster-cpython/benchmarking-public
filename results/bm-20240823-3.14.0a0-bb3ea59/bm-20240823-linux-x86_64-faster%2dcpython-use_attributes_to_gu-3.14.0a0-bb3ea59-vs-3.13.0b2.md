# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: bb3ea59
- commit date: 2024-08-23
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 256 ms: 1.07x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                          |
| html5lib       | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 89.6 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                           |
| float          | 78.9 ms                                                    | 78.4 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                            |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 33.5 ms: 1.04x faster                                                           |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.26x faster                                                           |
| go                         | 145 ms                                                     | 118 ms: 1.23x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                            |
| richards                   | 50.9 ms                                                    | 45.4 ms: 1.12x faster                                                           |
| richards_super             | 57.4 ms                                                    | 51.3 ms: 1.12x faster                                                           |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 70.7 ms: 1.10x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.82 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                            |
| scimark_fft                | 392 ms                                                     | 361 ms: 1.09x faster                                                            |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.08x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 21.9 ms: 1.08x faster                                                           |
| thrift                     | 823 us                                                     | 765 us: 1.08x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                            |
| 2to3                       | 274 ms                                                     | 256 ms: 1.07x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                           |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                            |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.07x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                            |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 89.6 ms: 1.06x faster                                                           |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.2 ms: 1.05x faster                                                           |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.04x faster                                                            |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                          |
| sympy_expand               | 473 ms                                                     | 453 ms: 1.04x faster                                                            |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                          |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.4 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                           |
| django_template            | 34.8 ms                                                    | 33.5 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                            |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| xml_etree_generate         | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                           |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| hexiom                     | 6.30 ms                                                    | 6.13 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.5 ms: 1.03x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                            |
| raytrace                   | 267 ms                                                     | 261 ms: 1.02x faster                                                            |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                            |
| nbody                      | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                           |
| telco                      | 8.41 ms                                                    | 8.27 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                                            |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                            |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                           |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                           |
| float                      | 78.9 ms                                                    | 78.4 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                          |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_io, json, fannkuch, regex_effbot, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x