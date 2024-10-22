# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_deferred_stats
- machine: linux-x86_64
- commit hash: 30d3b3d
- commit date: 2024-08-22
- overall geometric mean: 1.01x faster
- HPT reliability: 87.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                                          |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                        |
| html5lib       | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                         |
| tornado_http   | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 401 ms: 1.16x faster                                                          |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                          |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 553 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                                          |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                        |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                          |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                                          |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 899 ms: 1.09x slower                                                          |
| async_tree_io              | 843 ms                                                 | 931 ms: 1.11x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                          |
| float          | 78.5 ms                                                | 79.1 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                         |
| regex_effbot   | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                         |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                          |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.02x faster                                                          |
| xml_etree_process    | 60.4 ms                                                | 59.7 ms: 1.01x faster                                                         |
| xml_etree_generate   | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                          |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                          |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                          |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                         |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                         |
| genshi_text     | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                         |
| genshi_xml      | 50.3 ms                                                | 49.9 ms: 1.01x faster                                                         |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                          |
| deepcopy_memo              | 38.0 us                                                | 30.1 us: 1.26x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                                         |
| async_tree_memoization_tg  | 465 ms                                                 | 401 ms: 1.16x faster                                                          |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                          |
| async_tree_none            | 354 ms                                                 | 323 ms: 1.10x faster                                                          |
| regex_v8                   | 25.3 ms                                                | 23.7 ms: 1.07x faster                                                         |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                         |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                                        |
| scimark_fft                | 369 ms                                                 | 352 ms: 1.05x faster                                                          |
| gc_traversal               | 3.81 ms                                                | 3.64 ms: 1.05x faster                                                         |
| richards_super             | 54.4 ms                                                | 52.0 ms: 1.05x faster                                                         |
| richards                   | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                         |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                         |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                          |
| thrift                     | 796 us                                                 | 766 us: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 553 ms: 1.04x faster                                                          |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                          |
| telco                      | 8.45 ms                                                | 8.15 ms: 1.04x faster                                                         |
| bench_thread_pool          | 815 us                                                 | 786 us: 1.04x faster                                                          |
| tomli_loads                | 2.11 sec                                               | 2.04 sec: 1.03x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.76 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                                         |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                         |
| logging_format             | 6.25 us                                                | 6.10 us: 1.03x faster                                                         |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.02x faster                                                          |
| django_template            | 34.4 ms                                                | 33.7 ms: 1.02x faster                                                         |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                                          |
| tornado_http               | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                         |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.02x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                         |
| nqueens                    | 80.6 ms                                                | 79.6 ms: 1.01x faster                                                         |
| sympy_expand               | 462 ms                                                 | 456 ms: 1.01x faster                                                          |
| crypto_pyaes               | 73.0 ms                                                | 72.1 ms: 1.01x faster                                                         |
| xml_etree_process          | 60.4 ms                                                | 59.7 ms: 1.01x faster                                                         |
| genshi_text                | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                         |
| html5lib                   | 64.5 ms                                                | 63.9 ms: 1.01x faster                                                         |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                          |
| xml_etree_generate         | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                         |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                                          |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                                          |
| genshi_xml                 | 50.3 ms                                                | 49.9 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                         |
| mdp                        | 2.74 sec                                               | 2.73 sec: 1.00x faster                                                        |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                                          |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                          |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                          |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                         |
| float                      | 78.5 ms                                                | 79.1 ms: 1.01x slower                                                         |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                         |
| hexiom                     | 6.13 ms                                                | 6.18 ms: 1.01x slower                                                         |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 744 ms                                                 | 751 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                          |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                                          |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                         |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| go                         | 142 ms                                                 | 143 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.02x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                         |
| coverage                   | 83.7 ms                                                | 85.2 ms: 1.02x slower                                                         |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                                          |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                         |
| pyflate                    | 460 ms                                                 | 474 ms: 1.03x slower                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.85 sec: 1.03x slower                                                        |
| json                       | 5.20 ms                                                | 5.39 ms: 1.04x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                        |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                          |
| fannkuch                   | 381 ms                                                 | 399 ms: 1.05x slower                                                          |
| json_loads                 | 27.0 us                                                | 28.5 us: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 899 ms: 1.09x slower                                                          |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                         |
| async_tree_io              | 843 ms                                                 | 931 ms: 1.11x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): bench_mp_pool, nbody, logging_silent, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 87.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x