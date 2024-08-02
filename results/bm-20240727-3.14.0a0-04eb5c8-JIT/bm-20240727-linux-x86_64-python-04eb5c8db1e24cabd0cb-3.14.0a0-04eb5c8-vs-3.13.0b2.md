# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| html5lib       | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                                  |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 81.5 ms: 1.08x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.01x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 56.5 ms: 1.08x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                 |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                                 |
| deepcopy                   | 367 us                                                     | 269 us: 1.36x faster                                                  |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.26x faster                                                  |
| richards                   | 50.9 ms                                                    | 40.6 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                 |
| richards_super             | 57.4 ms                                                    | 46.3 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.22x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.0 ms: 1.15x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                  |
| pyflate                    | 484 ms                                                     | 430 ms: 1.13x faster                                                  |
| float                      | 78.9 ms                                                    | 70.6 ms: 1.12x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.10x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.08x faster                                                  |
| nbody                      | 88.3 ms                                                    | 81.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 56.5 ms: 1.08x faster                                                 |
| chaos                      | 61.3 ms                                                    | 57.5 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.07x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.93 ms: 1.06x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                 |
| async_tree_io              | 939 ms                                                     | 904 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                 |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.0 ms: 1.03x faster                                                 |
| generators                 | 29.6 ms                                                    | 28.7 ms: 1.03x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| coverage                   | 93.1 ms                                                    | 90.5 ms: 1.03x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.59 us: 1.03x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                 |
| thrift                     | 823 us                                                     | 801 us: 1.03x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                 |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                  |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| tornado_http               | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                  |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                  |
| dask                       | 369 ms                                                     | 365 ms: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 824 us: 1.01x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                  |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.00x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                 |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 56.4 ms: 1.02x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                  |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.03x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.54 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 85.4 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                  |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.46 ms: 1.06x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                  |
| pylint                     | 317 ms                                                     | 351 ms: 1.11x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x