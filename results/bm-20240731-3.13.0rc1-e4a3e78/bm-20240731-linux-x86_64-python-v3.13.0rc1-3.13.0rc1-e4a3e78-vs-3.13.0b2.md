# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 266 ms: 1.03x faster                                         |
| chameleon      | 7.22 ms                                                    | 6.88 ms: 1.05x faster                                        |
| docutils       | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                       |
| html5lib       | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                        |
| tornado_http   | 94.6 ms                                                    | 91.0 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                      | 1.03x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                         |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                         |
| async_tree_none            | 378 ms                                                     | 367 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 572 ms: 1.03x faster                                         |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                 |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.6 ms: 1.03x faster                                        |
| float          | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                        |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                      | 1.03x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                         |
| regex_v8       | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                        |
| regex_effbot   | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                        |
| regex_dna      | 221 ms                                                     | 237 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                      | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                        |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                         |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                         |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                         |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                         |
| xml_etree_process    | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                        |
| xml_etree_generate   | 87.4 ms                                                    | 88.0 ms: 1.01x slower                                        |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                        |
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.6 ms: 1.04x faster                                        |
| genshi_text     | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                        |
| genshi_xml      | 51.6 ms                                                    | 50.4 ms: 1.02x faster                                        |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| coverage                   | 93.1 ms                                                    | 83.9 ms: 1.11x faster                                        |
| richards                   | 50.9 ms                                                    | 47.5 ms: 1.07x faster                                        |
| scimark_fft                | 392 ms                                                     | 367 ms: 1.07x faster                                         |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                        |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                        |
| dulwich_log                | 67.2 ms                                                    | 63.2 ms: 1.06x faster                                        |
| richards_super             | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                        |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                         |
| deepcopy_reduce            | 3.35 us                                                    | 3.16 us: 1.06x faster                                        |
| crypto_pyaes               | 77.5 ms                                                    | 73.3 ms: 1.06x faster                                        |
| logging_silent             | 105 ns                                                     | 99.5 ns: 1.05x faster                                        |
| json                       | 5.31 ms                                                    | 5.04 ms: 1.05x faster                                        |
| coroutines                 | 23.2 ms                                                    | 22.0 ms: 1.05x faster                                        |
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                         |
| chameleon                  | 7.22 ms                                                    | 6.88 ms: 1.05x faster                                        |
| mdp                        | 2.79 sec                                                   | 2.66 sec: 1.05x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 484 ms: 1.05x faster                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.03 ms: 1.05x faster                                        |
| async_tree_io_tg           | 936 ms                                                     | 895 ms: 1.05x faster                                         |
| hexiom                     | 6.30 ms                                                    | 6.02 ms: 1.05x faster                                        |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                         |
| tornado_http               | 94.6 ms                                                    | 91.0 ms: 1.04x faster                                        |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                        |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                         |
| mypy2                      | 742 ms                                                     | 714 ms: 1.04x faster                                         |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                        |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                         |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                        |
| django_template            | 34.8 ms                                                    | 33.6 ms: 1.04x faster                                        |
| deepcopy                   | 367 us                                                     | 354 us: 1.04x faster                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                       |
| generators                 | 29.6 ms                                                    | 28.6 ms: 1.04x faster                                        |
| pprint_safe_repr           | 758 ms                                                     | 734 ms: 1.03x faster                                         |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                         |
| genshi_text                | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                        |
| async_tree_none            | 378 ms                                                     | 367 ms: 1.03x faster                                         |
| nbody                      | 88.3 ms                                                    | 85.6 ms: 1.03x faster                                        |
| deepcopy_memo              | 39.7 us                                                    | 38.5 us: 1.03x faster                                        |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                        |
| 2to3                       | 274 ms                                                     | 266 ms: 1.03x faster                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                         |
| float                      | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 54.0 ms: 1.03x faster                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 572 ms: 1.03x faster                                         |
| bench_thread_pool          | 834 us                                                     | 812 us: 1.03x faster                                         |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.03x faster                                        |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                         |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.02x faster                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                       |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.02x faster                                        |
| pathlib                    | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                        |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                         |
| genshi_xml                 | 51.6 ms                                                    | 50.4 ms: 1.02x faster                                        |
| sympy_str                  | 282 ms                                                     | 276 ms: 1.02x faster                                         |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                         |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                         |
| telco                      | 8.41 ms                                                    | 8.23 ms: 1.02x faster                                        |
| docutils                   | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.91 sec: 1.02x faster                                       |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                         |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                         |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                        |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                         |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                        |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                        |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                        |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.1 ms: 1.02x faster                                        |
| pyflate                    | 484 ms                                                     | 477 ms: 1.02x faster                                         |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                         |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                         |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                         |
| xml_etree_process          | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                        |
| html5lib                   | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                        |
| async_generators           | 442 ms                                                     | 439 ms: 1.01x faster                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                        |
| xml_etree_generate         | 87.4 ms                                                    | 88.0 ms: 1.01x slower                                        |
| fannkuch                   | 402 ms                                                     | 411 ms: 1.02x slower                                         |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                       |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.04x slower                                         |
| regex_v8                   | 25.1 ms                                                    | 26.3 ms: 1.05x slower                                        |
| regex_effbot               | 3.67 ms                                                    | 3.85 ms: 1.05x slower                                        |
| regex_dna                  | 221 ms                                                     | 237 ms: 1.07x slower                                         |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                 |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_memoization_tg, tomli_loads, nqueens, async_tree_none_tg, pylint
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x