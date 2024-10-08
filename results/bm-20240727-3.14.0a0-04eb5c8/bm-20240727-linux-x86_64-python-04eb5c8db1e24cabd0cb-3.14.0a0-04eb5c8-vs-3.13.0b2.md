# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 264 ms: 1.04x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.9 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| nbody          | 88.3 ms                                                    | 89.0 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.03 sec: 1.04x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 60.2 ms: 1.02x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 52.4 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.4 us: 1.35x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.22x faster                                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.62 ms: 1.14x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                  |
| scimark_fft                | 392 ms                                                     | 351 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.8 ms: 1.11x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.10x faster                                                |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                 |
| thrift                     | 823 us                                                     | 777 us: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 73.6 ms: 1.05x faster                                                 |
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                 |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.03 sec: 1.04x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.9 ms: 1.04x faster                                                 |
| dask                       | 369 ms                                                     | 355 ms: 1.04x faster                                                  |
| generators                 | 29.6 ms                                                    | 28.5 ms: 1.04x faster                                                 |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                     | 264 ms: 1.04x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.10 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                                 |
| chaos                      | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                                |
| docutils                   | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                 |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.02x faster                                                  |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.02x faster                                                |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 79.8 ms: 1.02x faster                                                 |
| raytrace                   | 267 ms                                                     | 261 ms: 1.02x faster                                                  |
| sympy_expand               | 473 ms                                                     | 464 ms: 1.02x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 60.2 ms: 1.02x faster                                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 748 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                |
| hexiom                     | 6.30 ms                                                    | 6.22 ms: 1.01x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                  |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                                  |
| float                      | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.6 ms: 1.01x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 87.0 ms: 1.00x faster                                                 |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| fannkuch                   | 402 ms                                                     | 405 ms: 1.01x slower                                                  |
| nbody                      | 88.3 ms                                                    | 89.0 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 166 us: 1.01x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 52.4 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (6): deltablue, comprehensions, regex_effbot, pylint, pickle_pure_python, genshi_text
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x