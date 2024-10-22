# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 69.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 306 ms: 1.05x slower                                                                  |
| docutils       | 2.81 sec                                                     | 3.12 sec: 1.11x slower                                                                |
| html5lib       | 71.9 ms                                                      | 70.5 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 762 ms: 1.08x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 788 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 538 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                                |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| async_generators           | 359 ms                                                       | 372 ms: 1.03x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 76.1 ms: 1.08x faster                                                                 |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                                  |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 25.3 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.07 sec: 1.16x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 139 ms: 1.04x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 82.3 ms: 1.04x faster                                                                 |
| xml_etree_iterparse  | 100 ms                                                       | 97.7 ms: 1.02x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 214 us: 1.00x faster                                                                  |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.05 ms: 1.15x faster                                                                 |
| genshi_text     | 26.6 ms                                                      | 26.3 ms: 1.01x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 60.1 ms: 1.05x slower                                                                 |
| django_template | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.5 us: 1.34x faster                                                                 |
| deepcopy                   | 397 us                                                       | 306 us: 1.30x faster                                                                  |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                                 |
| richards                   | 52.7 ms                                                      | 45.2 ms: 1.17x faster                                                                 |
| tomli_loads                | 2.41 sec                                                     | 2.07 sec: 1.16x faster                                                                |
| mako                       | 10.4 ms                                                      | 9.05 ms: 1.15x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 52.8 ms: 1.13x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 3.85 ms: 1.11x faster                                                                 |
| pyflate                    | 492 ms                                                       | 442 ms: 1.11x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                                  |
| scimark_fft                | 314 ms                                                       | 284 ms: 1.10x faster                                                                  |
| telco                      | 8.58 ms                                                      | 7.82 ms: 1.10x faster                                                                 |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| float                      | 81.9 ms                                                      | 76.1 ms: 1.08x faster                                                                 |
| async_tree_io_tg           | 819 ms                                                       | 762 ms: 1.08x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 788 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 538 ms: 1.07x faster                                                                  |
| xml_etree_process          | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                                 |
| fannkuch                   | 365 ms                                                       | 345 ms: 1.06x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.89 sec: 1.04x faster                                                                |
| pathlib                    | 17.4 ms                                                      | 16.7 ms: 1.04x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 139 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                                  |
| xml_etree_generate         | 85.3 ms                                                      | 82.3 ms: 1.04x faster                                                                 |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                                  |
| regex_v8                   | 26.2 ms                                                      | 25.3 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 72.8 ms                                                      | 70.5 ms: 1.03x faster                                                                 |
| logging_format             | 7.07 us                                                      | 6.88 us: 1.03x faster                                                                 |
| logging_simple             | 6.40 us                                                      | 6.23 us: 1.03x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                                 |
| xml_etree_iterparse        | 100 ms                                                       | 97.7 ms: 1.02x faster                                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                                 |
| coverage                   | 81.1 ms                                                      | 79.5 ms: 1.02x faster                                                                 |
| html5lib                   | 71.9 ms                                                      | 70.5 ms: 1.02x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 26.3 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                                  |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                                  |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.7 ms: 1.00x faster                                                                 |
| unpickle_pure_python       | 214 us                                                       | 214 us: 1.00x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                                                |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| scimark_sor                | 126 ms                                                       | 127 ms: 1.01x slower                                                                  |
| pprint_safe_repr           | 812 ms                                                       | 819 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                                                |
| thrift                     | 877 us                                                       | 894 us: 1.02x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| raytrace                   | 289 ms                                                       | 297 ms: 1.03x slower                                                                  |
| go                         | 160 ms                                                       | 165 ms: 1.03x slower                                                                  |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                                |
| dask                       | 379 ms                                                       | 391 ms: 1.03x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| bench_mp_pool              | 4.65 ms                                                      | 4.81 ms: 1.03x slower                                                                 |
| async_generators           | 359 ms                                                       | 372 ms: 1.03x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.43 ms: 1.04x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.86 ms: 1.04x slower                                                                 |
| genshi_xml                 | 57.3 ms                                                      | 60.1 ms: 1.05x slower                                                                 |
| sqlglot_optimize           | 59.7 ms                                                      | 62.6 ms: 1.05x slower                                                                 |
| sympy_expand               | 505 ms                                                       | 531 ms: 1.05x slower                                                                  |
| 2to3                       | 291 ms                                                       | 306 ms: 1.05x slower                                                                  |
| deltablue                  | 3.41 ms                                                      | 3.60 ms: 1.06x slower                                                                 |
| sympy_str                  | 296 ms                                                       | 312 ms: 1.06x slower                                                                  |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.06x slower                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 184 us: 1.06x slower                                                                  |
| django_template            | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                                 |
| logging_silent             | 97.7 ns                                                      | 104 ns: 1.06x slower                                                                  |
| hexiom                     | 6.33 ms                                                      | 6.74 ms: 1.06x slower                                                                 |
| comprehensions             | 17.3 us                                                      | 18.4 us: 1.07x slower                                                                 |
| chaos                      | 61.7 ms                                                      | 66.5 ms: 1.08x slower                                                                 |
| sqlglot_normalize          | 118 ms                                                       | 129 ms: 1.09x slower                                                                  |
| gc_traversal               | 4.11 ms                                                      | 4.47 ms: 1.09x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 168 ms: 1.09x slower                                                                  |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                                 |
| generators                 | 33.5 ms                                                      | 36.9 ms: 1.10x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 3.12 sec: 1.11x slower                                                                |
| nqueens                    | 88.2 ms                                                      | 98.2 ms: 1.11x slower                                                                 |
| pylint                     | 346 ms                                                       | 386 ms: 1.11x slower                                                                  |
| sympy_integrate            | 23.3 ms                                                      | 26.0 ms: 1.12x slower                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 110 ms: 1.12x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (3): pickle_pure_python, tornado_http, bench_thread_pool
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 69.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x