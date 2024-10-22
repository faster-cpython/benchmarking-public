# Results vs. 3.13.0

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: d4df441
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 81.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                          |
| html5lib       | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                           |
| tornado_http   | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 566 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                           |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                            |
| async_generators          | 433 ms                                                 | 463 ms: 1.07x slower                                                            |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                           |
| nbody          | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 25.2 ms: 1.00x faster                                                           |
| regex_compile  | 131 ms                                                 | 133 ms: 1.01x slower                                                            |
| regex_dna      | 220 ms                                                 | 230 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                          |
| xml_etree_generate  | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                           |
| xml_etree_process   | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| xml_etree_iterparse | 102 ms                                                 | 99.3 ms: 1.03x faster                                                           |
| json_dumps          | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| json_loads          | 27.0 us                                                | 28.0 us: 1.04x slower                                                           |
| Geometric mean      | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| django_template | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 52.7 ms: 1.05x slower                                                           |
| genshi_text     | 22.9 ms                                                | 24.1 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 28.5 us: 1.33x faster                                                           |
| deepcopy                  | 352 us                                                 | 271 us: 1.30x faster                                                            |
| richards                  | 48.1 ms                                                | 39.9 ms: 1.21x faster                                                           |
| scimark_fft               | 369 ms                                                 | 306 ms: 1.20x faster                                                            |
| async_tree_memoization_tg | 465 ms                                                 | 393 ms: 1.18x faster                                                            |
| richards_super            | 54.4 ms                                                | 46.9 ms: 1.16x faster                                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.73 us: 1.16x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.38 ms: 1.15x faster                                                           |
| float                     | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                           |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                            |
| mako                      | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                                          |
| scimark_monte_carlo       | 66.3 ms                                                | 60.1 ms: 1.10x faster                                                           |
| xml_etree_generate        | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                           |
| async_tree_none           | 354 ms                                                 | 327 ms: 1.08x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                           |
| nbody                     | 85.7 ms                                                | 79.6 ms: 1.08x faster                                                           |
| scimark_sor               | 122 ms                                                 | 114 ms: 1.07x faster                                                            |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| telco                     | 8.45 ms                                                | 7.97 ms: 1.06x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 302 ms: 1.06x faster                                                            |
| pyflate                   | 460 ms                                                 | 435 ms: 1.06x faster                                                            |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                           |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.05x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                            |
| bpe_tokeniser             | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                          |
| pprint_safe_repr          | 744 ms                                                 | 717 ms: 1.04x faster                                                            |
| logging_simple            | 5.66 us                                                | 5.46 us: 1.04x faster                                                           |
| gc_traversal              | 3.81 ms                                                | 3.68 ms: 1.03x faster                                                           |
| logging_format            | 6.25 us                                                | 6.06 us: 1.03x faster                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 99.3 ms: 1.03x faster                                                           |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                            |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| chaos                     | 58.4 ms                                                | 57.4 ms: 1.02x faster                                                           |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| mdp                       | 2.74 sec                                               | 2.70 sec: 1.01x faster                                                          |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 566 ms: 1.01x faster                                                            |
| html5lib                  | 64.5 ms                                                | 63.8 ms: 1.01x faster                                                           |
| thrift                    | 796 us                                                 | 788 us: 1.01x faster                                                            |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                            |
| comprehensions            | 16.4 us                                                | 16.3 us: 1.01x faster                                                           |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                            |
| regex_v8                  | 25.3 ms                                                | 25.2 ms: 1.00x faster                                                           |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| tornado_http              | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                           |
| regex_compile             | 131 ms                                                 | 133 ms: 1.01x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| json                      | 5.20 ms                                                | 5.31 ms: 1.02x slower                                                           |
| asyncio_tcp               | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| sqlglot_optimize          | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                           |
| 2to3                      | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| sqlglot_transpile         | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                           |
| go                        | 142 ms                                                 | 146 ms: 1.03x slower                                                            |
| django_template           | 34.4 ms                                                | 35.6 ms: 1.03x slower                                                           |
| json_loads                | 27.0 us                                                | 28.0 us: 1.04x slower                                                           |
| regex_dna                 | 220 ms                                                 | 230 ms: 1.05x slower                                                            |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                                            |
| genshi_xml                | 50.3 ms                                                | 52.7 ms: 1.05x slower                                                           |
| nqueens                   | 80.6 ms                                                | 84.6 ms: 1.05x slower                                                           |
| genshi_text               | 22.9 ms                                                | 24.1 ms: 1.06x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                            |
| async_generators          | 433 ms                                                 | 463 ms: 1.07x slower                                                            |
| dask                      | 338 ms                                                 | 363 ms: 1.08x slower                                                            |
| async_tree_io             | 843 ms                                                 | 908 ms: 1.08x slower                                                            |
| typing_runtime_protocols  | 159 us                                                 | 172 us: 1.08x slower                                                            |
| coverage                  | 83.7 ms                                                | 90.9 ms: 1.09x slower                                                           |
| sympy_expand              | 462 ms                                                 | 503 ms: 1.09x slower                                                            |
| sympy_str                 | 274 ms                                                 | 299 ms: 1.09x slower                                                            |
| hexiom                    | 6.13 ms                                                | 6.70 ms: 1.09x slower                                                           |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                           |
| deltablue                 | 3.15 ms                                                | 3.49 ms: 1.11x slower                                                           |
| docutils                  | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                          |
| sympy_integrate           | 19.9 ms                                                | 22.4 ms: 1.13x slower                                                           |
| pylint                    | 313 ms                                                 | 354 ms: 1.13x slower                                                            |
| sympy_sum                 | 150 ms                                                 | 170 ms: 1.14x slower                                                            |
| generators                | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, unpickle_pure_python, pickle_pure_python, raytrace, bench_mp_pool, asyncio_websockets, bench_thread_pool, regex_effbot
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 81.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x