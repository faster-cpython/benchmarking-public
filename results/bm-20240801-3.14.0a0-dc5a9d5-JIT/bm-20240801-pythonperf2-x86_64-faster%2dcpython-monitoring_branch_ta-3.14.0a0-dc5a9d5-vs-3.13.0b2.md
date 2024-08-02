# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 88.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                                  |
| docutils       | 2.98 sec                                                         | 3.12 sec: 1.04x slower                                                                |
| html5lib       | 74.7 ms                                                          | 70.5 ms: 1.06x faster                                                                 |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 762 ms: 1.18x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 788 ms: 1.11x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 538 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.05x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 76.1 ms: 1.05x faster                                                                 |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                                  |
| nbody          | 87.8 ms                                                          | 91.2 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 133 ms: 1.08x faster                                                                  |
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.07 sec: 1.16x faster                                                                |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                           | 97.7 ms: 1.05x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                                 |
| xml_etree_process    | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 139 ms: 1.03x faster                                                                  |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.05 ms: 1.15x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 26.3 ms: 1.01x slower                                                                 |
| genshi_xml      | 58.1 ms                                                          | 60.1 ms: 1.03x slower                                                                 |
| django_template | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.5 us: 1.26x faster                                                                 |
| deepcopy                   | 377 us                                                           | 306 us: 1.23x faster                                                                  |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                                 |
| richards                   | 53.4 ms                                                          | 45.2 ms: 1.18x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 762 ms: 1.18x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 52.8 ms: 1.16x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.07 sec: 1.16x faster                                                                |
| mako                       | 10.4 ms                                                          | 9.05 ms: 1.15x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 3.00 us: 1.13x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                                  |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 3.85 ms: 1.11x faster                                                                 |
| async_tree_io              | 873 ms                                                           | 788 ms: 1.11x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| scimark_fft                | 312 ms                                                           | 284 ms: 1.10x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                                  |
| pyflate                    | 482 ms                                                           | 442 ms: 1.09x faster                                                                  |
| regex_compile              | 144 ms                                                           | 133 ms: 1.08x faster                                                                  |
| telco                      | 8.40 ms                                                          | 7.82 ms: 1.07x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 538 ms: 1.06x faster                                                                  |
| regex_dna                  | 249 ms                                                           | 235 ms: 1.06x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 70.5 ms: 1.06x faster                                                                 |
| float                      | 80.2 ms                                                          | 76.1 ms: 1.05x faster                                                                 |
| unpickle_pure_python       | 224 us                                                           | 214 us: 1.05x faster                                                                  |
| coverage                   | 83.5 ms                                                          | 79.5 ms: 1.05x faster                                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.89 sec: 1.05x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                           | 97.7 ms: 1.05x faster                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.05x faster                                                                  |
| crypto_pyaes               | 73.6 ms                                                          | 70.5 ms: 1.04x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.1 ms: 1.04x faster                                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                                 |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.04x faster                                                                 |
| xml_etree_process          | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                                 |
| logging_format             | 7.11 us                                                          | 6.88 us: 1.03x faster                                                                 |
| xml_etree_parse            | 144 ms                                                           | 139 ms: 1.03x faster                                                                  |
| logging_simple             | 6.40 us                                                          | 6.23 us: 1.03x faster                                                                 |
| regex_v8                   | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                                 |
| pathlib                    | 17.1 ms                                                          | 16.7 ms: 1.02x faster                                                                 |
| fannkuch                   | 353 ms                                                           | 345 ms: 1.02x faster                                                                  |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.7 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                                  |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                                  |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                                |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| genshi_text                | 25.9 ms                                                          | 26.3 ms: 1.01x slower                                                                 |
| json                       | 5.35 ms                                                          | 5.43 ms: 1.02x slower                                                                 |
| thrift                     | 880 us                                                           | 894 us: 1.02x slower                                                                  |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| async_generators           | 363 ms                                                           | 372 ms: 1.02x slower                                                                  |
| pprint_pformat             | 1.66 sec                                                         | 1.70 sec: 1.03x slower                                                                |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                                 |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                                  |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                                 |
| genshi_xml                 | 58.1 ms                                                          | 60.1 ms: 1.03x slower                                                                 |
| nbody                      | 87.8 ms                                                          | 91.2 ms: 1.04x slower                                                                 |
| docutils                   | 2.98 sec                                                         | 3.12 sec: 1.04x slower                                                                |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                                |
| 2to3                       | 291 ms                                                           | 306 ms: 1.05x slower                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 62.6 ms: 1.05x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                          | 1.86 ms: 1.05x slower                                                                 |
| django_template            | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                                 |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                                |
| sympy_str                  | 295 ms                                                           | 312 ms: 1.06x slower                                                                  |
| sympy_expand               | 501 ms                                                           | 531 ms: 1.06x slower                                                                  |
| hexiom                     | 6.35 ms                                                          | 6.74 ms: 1.06x slower                                                                 |
| scimark_sor                | 119 ms                                                           | 127 ms: 1.07x slower                                                                  |
| deltablue                  | 3.37 ms                                                          | 3.60 ms: 1.07x slower                                                                 |
| sqlglot_normalize          | 120 ms                                                           | 129 ms: 1.07x slower                                                                  |
| typing_runtime_protocols   | 171 us                                                           | 184 us: 1.08x slower                                                                  |
| logging_silent             | 96.3 ns                                                          | 104 ns: 1.08x slower                                                                  |
| sympy_sum                  | 155 ms                                                           | 168 ms: 1.08x slower                                                                  |
| comprehensions             | 17.0 us                                                          | 18.4 us: 1.09x slower                                                                 |
| generators                 | 33.5 ms                                                          | 36.9 ms: 1.10x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 98.2 ms: 1.11x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 66.5 ms: 1.12x slower                                                                 |
| sympy_integrate            | 23.2 ms                                                          | 26.0 ms: 1.12x slower                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 110 ms: 1.13x slower                                                                  |
| pylint                     | 339 ms                                                           | 386 ms: 1.14x slower                                                                  |
| raytrace                   | 260 ms                                                           | 297 ms: 1.14x slower                                                                  |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (7): bench_mp_pool, bench_thread_pool, asyncio_tcp, go, tornado_http, dask, pprint_safe_repr
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x