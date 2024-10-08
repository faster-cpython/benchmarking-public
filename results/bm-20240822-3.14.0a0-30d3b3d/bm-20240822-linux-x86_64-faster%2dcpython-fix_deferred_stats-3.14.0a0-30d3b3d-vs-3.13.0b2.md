# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: fix_deferred_stats
- machine: linux-x86_64
- commit hash: 30d3b3d
- commit date: 2024-08-22
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                                          |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                        |
| html5lib       | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                         |
| tornado_http   | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.19x faster                                                          |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 553 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                          |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                                          |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.8 ms: 1.03x faster                                                         |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                          |
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                         |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                                          |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                          |
| tomli_loads          | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                          |
| xml_etree_process    | 61.2 ms                                                    | 59.7 ms: 1.02x faster                                                         |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| xml_etree_generate   | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                         |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                         |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                          |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                         |
| genshi_xml      | 51.6 ms                                                    | 49.9 ms: 1.03x faster                                                         |
| django_template | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                         |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                         |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                          |
| deepcopy_memo              | 39.7 us                                                    | 30.1 us: 1.32x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 391 ms: 1.19x faster                                                          |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                          |
| scimark_fft                | 392 ms                                                     | 352 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 553 ms: 1.11x faster                                                          |
| richards                   | 50.9 ms                                                    | 46.1 ms: 1.11x faster                                                         |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                                          |
| gc_traversal               | 3.98 ms                                                    | 3.64 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                          |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.87 ms: 1.08x faster                                                         |
| thrift                     | 823 us                                                     | 766 us: 1.07x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 72.1 ms: 1.07x faster                                                         |
| generators                 | 29.6 ms                                                    | 27.6 ms: 1.07x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                          |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.07x faster                                                         |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                          |
| bench_thread_pool          | 834 us                                                     | 786 us: 1.06x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                         |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                                         |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                          |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                          |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                          |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                                         |
| tornado_http               | 94.6 ms                                                    | 90.1 ms: 1.05x faster                                                         |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                                          |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                                          |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                         |
| genshi_text                | 23.7 ms                                                    | 22.6 ms: 1.05x faster                                                         |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                                          |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 899 ms: 1.04x faster                                                          |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                                         |
| tomli_loads                | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                         |
| bpe_tokeniser              | 5.02 sec                                                   | 4.85 sec: 1.04x faster                                                        |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                         |
| genshi_xml                 | 51.6 ms                                                    | 49.9 ms: 1.03x faster                                                         |
| django_template            | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.15 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                         |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                          |
| nbody                      | 88.3 ms                                                    | 85.8 ms: 1.03x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                          |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                         |
| xml_etree_process          | 61.2 ms                                                    | 59.7 ms: 1.02x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| nqueens                    | 81.4 ms                                                    | 79.6 ms: 1.02x faster                                                         |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                          |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                        |
| hexiom                     | 6.30 ms                                                    | 6.18 ms: 1.02x faster                                                         |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                         |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                          |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                                          |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.01x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                         |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                         |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 751 ms: 1.01x faster                                                          |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                          |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                                         |
| fannkuch                   | 402 ms                                                     | 399 ms: 1.01x faster                                                          |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                                          |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                         |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                         |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                         |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                         |
| json                       | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                                         |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                                          |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_io, typing_runtime_protocols, float, scimark_sor, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x