# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.02x faster
- HPT reliability: 98.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                            |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                          |
| html5lib       | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                           |
| tornado_http   | 94.6 ms                                                    | 91.9 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.00x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                            |
| async_tree_io_tg           | 936 ms                                                     | 859 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                            |
| async_tree_io              | 939 ms                                                     | 909 ms: 1.03x faster                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                            |
| nbody          | 88.3 ms                                                    | 92.2 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                           |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                            |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                           |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                      | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                           |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                           |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                           |
| xml_etree_generate   | 87.4 ms                                                    | 86.9 ms: 1.01x faster                                           |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.00x faster                                            |
| xml_etree_iterparse  | 107 ms                                                     | 108 ms: 1.01x slower                                            |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                            |
| tomli_loads          | 2.12 sec                                                   | 2.24 sec: 1.05x slower                                          |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                           |
| mako            | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                           |
| genshi_text     | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                           |
| genshi_xml      | 51.6 ms                                                    | 57.1 ms: 1.11x slower                                           |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                            |
| deepcopy_memo              | 39.7 us                                                    | 31.1 us: 1.28x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 383 ms: 1.16x faster                                            |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                            |
| async_tree_io_tg           | 936 ms                                                     | 859 ms: 1.09x faster                                            |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                           |
| richards                   | 50.9 ms                                                    | 47.0 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                            |
| richards_super             | 57.4 ms                                                    | 53.5 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                            |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                           |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                           |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                            |
| crypto_pyaes               | 77.5 ms                                                    | 72.9 ms: 1.06x faster                                           |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                            |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                           |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                           |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                           |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                            |
| asyncio_tcp                | 508 ms                                                     | 490 ms: 1.04x faster                                            |
| dulwich_log                | 67.2 ms                                                    | 64.9 ms: 1.03x faster                                           |
| async_tree_io              | 939 ms                                                     | 909 ms: 1.03x faster                                            |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.87 sec: 1.03x faster                                          |
| tornado_http               | 94.6 ms                                                    | 91.9 ms: 1.03x faster                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                            |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                            |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                          |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                          |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                            |
| chaos                      | 61.3 ms                                                    | 60.2 ms: 1.02x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 159 ms: 1.02x faster                                            |
| json                       | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                           |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                            |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                            |
| pprint_safe_repr           | 758 ms                                                     | 747 ms: 1.02x faster                                            |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                            |
| telco                      | 8.41 ms                                                    | 8.30 ms: 1.01x faster                                           |
| sympy_expand               | 473 ms                                                     | 466 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.20 ms: 1.01x faster                                           |
| 2to3                       | 274 ms                                                     | 270 ms: 1.01x faster                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 60.6 ms: 1.01x faster                                           |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                           |
| sympy_str                  | 282 ms                                                     | 280 ms: 1.01x faster                                            |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                          |
| xml_etree_generate         | 87.4 ms                                                    | 86.9 ms: 1.01x faster                                           |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                           |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                           |
| xml_etree_iterparse        | 107 ms                                                     | 108 ms: 1.01x slower                                            |
| unpickle_pure_python       | 218 us                                                     | 220 us: 1.01x slower                                            |
| sympy_sum                  | 156 ms                                                     | 157 ms: 1.01x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                           |
| html5lib                   | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                           |
| meteor_contest             | 110 ms                                                     | 111 ms: 1.01x slower                                            |
| sympy_integrate            | 20.5 ms                                                    | 20.8 ms: 1.01x slower                                           |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                          |
| mako                       | 11.2 ms                                                    | 11.5 ms: 1.02x slower                                           |
| fannkuch                   | 402 ms                                                     | 414 ms: 1.03x slower                                            |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                            |
| coroutines                 | 23.2 ms                                                    | 24.0 ms: 1.03x slower                                           |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                            |
| nbody                      | 88.3 ms                                                    | 92.2 ms: 1.04x slower                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 58.0 ms: 1.04x slower                                           |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                          |
| tomli_loads                | 2.12 sec                                                   | 2.24 sec: 1.05x slower                                          |
| comprehensions             | 16.6 us                                                    | 18.0 us: 1.09x slower                                           |
| genshi_text                | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                           |
| pylint                     | 317 ms                                                     | 347 ms: 1.09x slower                                            |
| genshi_xml                 | 51.6 ms                                                    | 57.1 ms: 1.11x slower                                           |
| nqueens                    | 81.4 ms                                                    | 90.6 ms: 1.11x slower                                           |
| hexiom                     | 6.30 ms                                                    | 7.05 ms: 1.12x slower                                           |
| generators                 | 29.6 ms                                                    | 45.8 ms: 1.55x slower                                           |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                    |

Benchmark hidden because not significant (8): coverage, float, go, sqlglot_normalize, typing_runtime_protocols, pyflate, scimark_monte_carlo, logging_silent
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x