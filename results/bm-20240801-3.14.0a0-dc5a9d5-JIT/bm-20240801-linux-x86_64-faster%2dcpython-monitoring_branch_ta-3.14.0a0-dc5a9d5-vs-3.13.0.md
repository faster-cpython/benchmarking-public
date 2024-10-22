# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 78.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                          |
| html5lib       | 64.5 ms                                                | 64.2 ms: 1.00x faster                                                           |
| tornado_http   | 91.5 ms                                                | 92.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                            |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                           |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                            |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                            |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                           |
| nbody          | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                           |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                            |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                          |
| xml_etree_generate   | 87.0 ms                                                | 79.2 ms: 1.10x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 99.2 ms: 1.03x faster                                                           |
| pickle_pure_python   | 300 us                                                 | 295 us: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| django_template | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                           |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 53.9 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-linux-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.8 us: 1.32x faster                                                           |
| deepcopy                   | 352 us                                                 | 273 us: 1.29x faster                                                            |
| scimark_fft                | 369 ms                                                 | 308 ms: 1.20x faster                                                            |
| richards                   | 48.1 ms                                                | 40.4 ms: 1.19x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                            |
| richards_super             | 54.4 ms                                                | 46.5 ms: 1.17x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.39 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.77 us: 1.14x faster                                                           |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                            |
| mako                       | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| float                      | 78.5 ms                                                | 70.4 ms: 1.11x faster                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 59.9 ms: 1.11x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                          |
| xml_etree_generate         | 87.0 ms                                                | 79.2 ms: 1.10x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                           |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                            |
| nbody                      | 85.7 ms                                                | 79.4 ms: 1.08x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                            |
| pyflate                    | 460 ms                                                 | 427 ms: 1.08x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 67.9 ms: 1.08x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.07x faster                                                          |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                                           |
| telco                      | 8.45 ms                                                | 8.07 ms: 1.05x faster                                                           |
| fannkuch                   | 381 ms                                                 | 364 ms: 1.05x faster                                                            |
| logging_format             | 6.25 us                                                | 6.00 us: 1.04x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                          |
| logging_simple             | 5.66 us                                                | 5.47 us: 1.04x faster                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 99.2 ms: 1.03x faster                                                           |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                            |
| pickle_pure_python         | 300 us                                                 | 295 us: 1.02x faster                                                            |
| regex_v8                   | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                           |
| comprehensions             | 16.4 us                                                | 16.1 us: 1.02x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 733 ms: 1.01x faster                                                            |
| chaos                      | 58.4 ms                                                | 57.6 ms: 1.01x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| html5lib                   | 64.5 ms                                                | 64.2 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                            |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| gc_traversal               | 3.81 ms                                                | 3.81 ms: 1.00x slower                                                           |
| tornado_http               | 91.5 ms                                                | 92.1 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                          |
| bench_thread_pool          | 815 us                                                 | 821 us: 1.01x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                            |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                            |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.03x slower                                                           |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                           |
| 2to3                       | 265 ms                                                 | 273 ms: 1.03x slower                                                            |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                            |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 55.9 ms: 1.04x slower                                                           |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 860 ms: 1.04x slower                                                            |
| django_template            | 34.4 ms                                                | 35.9 ms: 1.04x slower                                                           |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                                            |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                            |
| nqueens                    | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                           |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.07x slower                                                            |
| genshi_xml                 | 50.3 ms                                                | 53.9 ms: 1.07x slower                                                           |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                            |
| dask                       | 338 ms                                                 | 365 ms: 1.08x slower                                                            |
| scimark_lu                 | 115 ms                                                 | 125 ms: 1.08x slower                                                            |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.67 ms: 1.09x slower                                                           |
| sympy_expand               | 462 ms                                                 | 503 ms: 1.09x slower                                                            |
| coverage                   | 83.7 ms                                                | 91.7 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.52 ms: 1.12x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.90 sec: 1.12x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                            |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.13x slower                                                           |
| pylint                     | 313 ms                                                 | 355 ms: 1.14x slower                                                            |
| generators                 | 28.8 ms                                                | 33.3 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (6): pprint_pformat, thrift, bench_mp_pool, go, asyncio_websockets, json
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 78.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x