# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: remove_build_const_k
- machine: linux-x86_64
- commit hash: bcb5b37
- commit date: 2024-07-23
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 260 ms: 1.05x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| html5lib       | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 89.7 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 373 ms: 1.19x faster                                                            |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 291 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                            |
| async_tree_io              | 939 ms                                                     | 835 ms: 1.12x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 843 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.3 ms: 1.02x faster                                                           |
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                           |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                                           |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                           |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 209 us: 1.04x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 84.5 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| pickle_pure_python   | 305 us                                                     | 296 us: 1.03x faster                                                            |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| json_loads           | 28.9 us                                                    | 28.1 us: 1.03x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                           |
| mako            | 11.2 ms                                                    | 10.8 ms: 1.05x faster                                                           |
| django_template | 34.8 ms                                                    | 33.6 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                      | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.35 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 373 ms: 1.19x faster                                                            |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 291 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                            |
| async_tree_io              | 939 ms                                                     | 835 ms: 1.12x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.54 ms: 1.12x faster                                                           |
| richards                   | 50.9 ms                                                    | 45.6 ms: 1.12x faster                                                           |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 843 ms: 1.11x faster                                                            |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                            |
| scimark_fft                | 392 ms                                                     | 356 ms: 1.10x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 70.5 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                                           |
| logging_silent             | 105 ns                                                     | 98.1 ns: 1.07x faster                                                           |
| chaos                      | 61.3 ms                                                    | 57.6 ms: 1.07x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.40 us: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 785 us: 1.06x faster                                                            |
| dulwich_log                | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                           |
| thrift                     | 823 us                                                     | 777 us: 1.06x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                                           |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.06x faster                                                            |
| raytrace                   | 267 ms                                                     | 253 ms: 1.05x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 89.7 ms: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                     | 260 ms: 1.05x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 58.1 ms: 1.05x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 22.5 ms: 1.05x faster                                                           |
| scimark_sor                | 127 ms                                                     | 121 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.25 ms: 1.05x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 52.8 ms: 1.05x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 49.1 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 722 ms: 1.05x faster                                                            |
| sqlglot_normalize          | 110 ms                                                     | 105 ms: 1.05x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| dask                       | 369 ms                                                     | 352 ms: 1.05x faster                                                            |
| json                       | 5.31 ms                                                    | 5.06 ms: 1.05x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| mako                       | 11.2 ms                                                    | 10.8 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.56 ms: 1.04x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.2 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 209 us: 1.04x faster                                                            |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                           |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                            |
| hexiom                     | 6.30 ms                                                    | 6.06 ms: 1.04x faster                                                           |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                                            |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.6 ms: 1.04x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 490 ms: 1.04x faster                                                            |
| django_template            | 34.8 ms                                                    | 33.6 ms: 1.04x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 84.5 ms: 1.03x faster                                                           |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.03x faster                                                            |
| async_generators           | 442 ms                                                     | 427 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| telco                      | 8.41 ms                                                    | 8.15 ms: 1.03x faster                                                           |
| pickle_pure_python         | 305 us                                                     | 296 us: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                          |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                           |
| json_loads                 | 28.9 us                                                    | 28.1 us: 1.03x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.16 ms: 1.03x faster                                                           |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                                           |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                            |
| float                      | 78.9 ms                                                    | 77.3 ms: 1.02x faster                                                           |
| nbody                      | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                            |
| fannkuch                   | 402 ms                                                     | 395 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 80.5 ms: 1.01x faster                                                           |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                           |
| pyflate                    | 484 ms                                                     | 482 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                           |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                           |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                          |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): pylint, typing_runtime_protocols
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.00x