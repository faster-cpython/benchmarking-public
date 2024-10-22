# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 70.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                  |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| html5lib       | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                 |
| tornado_http   | 91.5 ms                                                | 92.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                  |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                  |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                 |
| nbody          | 85.7 ms                                                | 81.5 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                 |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                 |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| xml_etree_generate  | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                 |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_process   | 60.4 ms                                                | 56.5 ms: 1.07x faster                                                 |
| xml_etree_iterparse | 102 ms                                                 | 99.1 ms: 1.03x faster                                                 |
| json_loads          | 27.0 us                                                | 27.9 us: 1.03x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                 |
| django_template | 34.4 ms                                                | 36.3 ms: 1.06x slower                                                 |
| genshi_text     | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 58.6 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 29.0 us: 1.31x faster                                                 |
| deepcopy                   | 352 us                                                 | 269 us: 1.31x faster                                                  |
| scimark_fft                | 369 ms                                                 | 310 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 392 ms: 1.19x faster                                                  |
| richards                   | 48.1 ms                                                | 40.6 ms: 1.19x faster                                                 |
| richards_super             | 54.4 ms                                                | 46.3 ms: 1.18x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| mako                       | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                 |
| float                      | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 60.0 ms: 1.10x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| pyflate                    | 460 ms                                                 | 430 ms: 1.07x faster                                                  |
| xml_etree_process          | 60.4 ms                                                | 56.5 ms: 1.07x faster                                                 |
| telco                      | 8.45 ms                                                | 7.93 ms: 1.07x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                  |
| nbody                      | 85.7 ms                                                | 81.5 ms: 1.05x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 744 ms                                                 | 712 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.04x faster                                                |
| regex_effbot               | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 532 ms: 1.02x faster                                                  |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                  |
| chaos                      | 58.4 ms                                                | 57.5 ms: 1.02x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.59 us: 1.01x faster                                                 |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                                 |
| gc_traversal               | 3.81 ms                                                | 3.76 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.7 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                 |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                 |
| html5lib                   | 64.5 ms                                                | 65.0 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| regex_v8                   | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                  |
| bench_thread_pool          | 815 us                                                 | 824 us: 1.01x slower                                                  |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                 |
| tornado_http               | 91.5 ms                                                | 92.8 ms: 1.01x slower                                                 |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                  |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.9 us: 1.03x slower                                                 |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                 |
| django_template            | 34.4 ms                                                | 36.3 ms: 1.06x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                  |
| nqueens                    | 80.6 ms                                                | 85.4 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                                  |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                  |
| hexiom                     | 6.13 ms                                                | 6.54 ms: 1.07x slower                                                 |
| async_tree_io              | 843 ms                                                 | 904 ms: 1.07x slower                                                  |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                  |
| coverage                   | 83.7 ms                                                | 90.5 ms: 1.08x slower                                                 |
| sympy_str                  | 274 ms                                                 | 297 ms: 1.08x slower                                                  |
| genshi_text                | 22.9 ms                                                | 24.8 ms: 1.08x slower                                                 |
| scimark_lu                 | 115 ms                                                 | 125 ms: 1.09x slower                                                  |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                                  |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.46 ms: 1.10x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.2 ms: 1.12x slower                                                 |
| pylint                     | 313 ms                                                 | 351 ms: 1.12x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 58.6 ms: 1.16x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (10): json_dumps, pickle_pure_python, bench_mp_pool, go, regex_dna, sqlglot_parse, coroutines, unpickle_pure_python, asyncio_websockets, thrift
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 70.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x