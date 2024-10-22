# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-aarch64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 370 ms: 1.21x slower                                                              |
| docutils       | 2.91 sec                                                 | 3.74 sec: 1.29x slower                                                            |
| html5lib       | 64.3 ms                                                  | 70.9 ms: 1.10x slower                                                             |
| tornado_http   | 131 ms                                                   | 139 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                    | 1.16x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                              |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 423 ms: 1.10x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 588 ms: 1.06x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                              |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                              |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                            |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                            |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                            |
| asyncio_tcp                | 568 ms                                                   | 653 ms: 1.15x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.7 ms: 1.03x faster                                                             |
| nbody          | 114 ms                                                   | 116 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                             |
| regex_effbot   | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                             |
| regex_dna      | 246 ms                                                   | 258 ms: 1.05x slower                                                              |
| regex_compile  | 128 ms                                                   | 182 ms: 1.42x slower                                                              |
| Geometric mean | (ref)                                                    | 1.09x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                             |
| json_loads           | 31.4 us                                                  | 32.9 us: 1.05x slower                                                             |
| tomli_loads          | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                            |
| unpickle_pure_python | 254 us                                                   | 277 us: 1.09x slower                                                              |
| pickle_pure_python   | 359 us                                                   | 398 us: 1.11x slower                                                              |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                             |
| python_startup_no_site | 8.75 ms                                                  | 8.88 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                    | 1.00x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                             |
| django_template | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                             |
| genshi_text     | 27.7 ms                                                  | 33.2 ms: 1.20x slower                                                             |
| genshi_xml      | 60.2 ms                                                  | 75.3 ms: 1.25x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.15x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.9 us: 1.31x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                              |
| deepcopy                   | 451 us                                                   | 382 us: 1.18x faster                                                              |
| async_tree_none            | 493 ms                                                   | 443 ms: 1.11x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 423 ms: 1.10x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 588 ms: 1.06x faster                                                              |
| regex_v8                   | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                              |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                             |
| float                      | 94.4 ms                                                  | 91.7 ms: 1.03x faster                                                             |
| json_dumps                 | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                             |
| pathlib                    | 22.4 ms                                                  | 22.0 ms: 1.02x faster                                                             |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                             |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                              |
| python_startup_no_site     | 8.75 ms                                                  | 8.88 ms: 1.02x slower                                                             |
| regex_effbot               | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                             |
| thrift                     | 946 us                                                   | 964 us: 1.02x slower                                                              |
| nbody                      | 114 ms                                                   | 116 ms: 1.02x slower                                                              |
| spectral_norm              | 141 ms                                                   | 144 ms: 1.02x slower                                                              |
| richards_super             | 60.3 ms                                                  | 61.6 ms: 1.02x slower                                                             |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                            |
| coverage                   | 98.5 ms                                                  | 101 ms: 1.03x slower                                                              |
| richards                   | 53.5 ms                                                  | 55.0 ms: 1.03x slower                                                             |
| logging_format             | 7.83 us                                                  | 8.05 us: 1.03x slower                                                             |
| json                       | 5.61 ms                                                  | 5.77 ms: 1.03x slower                                                             |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                              |
| scimark_fft                | 447 ms                                                   | 462 ms: 1.03x slower                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 4.22 us: 1.04x slower                                                             |
| mdp                        | 3.36 sec                                                 | 3.49 sec: 1.04x slower                                                            |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.87 ms: 1.04x slower                                                             |
| bench_thread_pool          | 1.28 ms                                                  | 1.33 ms: 1.04x slower                                                             |
| meteor_contest             | 113 ms                                                   | 119 ms: 1.05x slower                                                              |
| regex_dna                  | 246 ms                                                   | 258 ms: 1.05x slower                                                              |
| json_loads                 | 31.4 us                                                  | 32.9 us: 1.05x slower                                                             |
| logging_simple             | 7.04 us                                                  | 7.37 us: 1.05x slower                                                             |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                            |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                            |
| tomli_loads                | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                            |
| fannkuch                   | 452 ms                                                   | 477 ms: 1.06x slower                                                              |
| tornado_http               | 131 ms                                                   | 139 ms: 1.06x slower                                                              |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.8 ms: 1.07x slower                                                             |
| bench_mp_pool              | 7.30 ms                                                  | 7.89 ms: 1.08x slower                                                             |
| unpickle_pure_python       | 254 us                                                   | 277 us: 1.09x slower                                                              |
| scimark_sor                | 159 ms                                                   | 173 ms: 1.09x slower                                                              |
| crypto_pyaes               | 82.7 ms                                                  | 90.3 ms: 1.09x slower                                                             |
| telco                      | 9.73 ms                                                  | 10.7 ms: 1.09x slower                                                             |
| html5lib                   | 64.3 ms                                                  | 70.9 ms: 1.10x slower                                                             |
| typing_runtime_protocols   | 192 us                                                   | 212 us: 1.10x slower                                                              |
| pyflate                    | 556 ms                                                   | 616 ms: 1.11x slower                                                              |
| pickle_pure_python         | 359 us                                                   | 398 us: 1.11x slower                                                              |
| raytrace                   | 298 ms                                                   | 332 ms: 1.11x slower                                                              |
| dask                       | 350 ms                                                   | 391 ms: 1.12x slower                                                              |
| go                         | 163 ms                                                   | 182 ms: 1.12x slower                                                              |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                                             |
| create_gc_cycles           | 2.12 ms                                                  | 2.39 ms: 1.12x slower                                                             |
| asyncio_tcp                | 568 ms                                                   | 653 ms: 1.15x slower                                                              |
| pycparser                  | 1.26 sec                                                 | 1.45 sec: 1.15x slower                                                            |
| deltablue                  | 3.85 ms                                                  | 4.44 ms: 1.15x slower                                                             |
| sqlglot_optimize           | 62.4 ms                                                  | 72.0 ms: 1.16x slower                                                             |
| sqlglot_normalize          | 128 ms                                                   | 149 ms: 1.16x slower                                                              |
| comprehensions             | 20.4 us                                                  | 24.1 us: 1.18x slower                                                             |
| django_template            | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                             |
| genshi_text                | 27.7 ms                                                  | 33.2 ms: 1.20x slower                                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.67 ms: 1.21x slower                                                             |
| 2to3                       | 306 ms                                                   | 370 ms: 1.21x slower                                                              |
| sqlglot_transpile          | 1.73 ms                                                  | 2.13 ms: 1.23x slower                                                             |
| genshi_xml                 | 60.2 ms                                                  | 75.3 ms: 1.25x slower                                                             |
| nqueens                    | 98.7 ms                                                  | 124 ms: 1.26x slower                                                              |
| pprint_safe_repr           | 926 ms                                                   | 1.18 sec: 1.27x slower                                                            |
| chaos                      | 68.8 ms                                                  | 87.7 ms: 1.27x slower                                                             |
| pprint_pformat             | 1.90 sec                                                 | 2.43 sec: 1.28x slower                                                            |
| docutils                   | 2.91 sec                                                 | 3.74 sec: 1.29x slower                                                            |
| pylint                     | 343 ms                                                   | 442 ms: 1.29x slower                                                              |
| scimark_lu                 | 139 ms                                                   | 180 ms: 1.29x slower                                                              |
| sympy_expand               | 455 ms                                                   | 595 ms: 1.31x slower                                                              |
| sympy_integrate            | 21.0 ms                                                  | 27.7 ms: 1.32x slower                                                             |
| sympy_str                  | 264 ms                                                   | 350 ms: 1.33x slower                                                              |
| hexiom                     | 7.13 ms                                                  | 9.78 ms: 1.37x slower                                                             |
| sympy_sum                  | 143 ms                                                   | 203 ms: 1.41x slower                                                              |
| regex_compile              | 128 ms                                                   | 182 ms: 1.42x slower                                                              |
| generators                 | 37.8 ms                                                  | 57.4 ms: 1.52x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                                      |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, xml_etree_parse, xml_etree_process, logging_silent, coroutines, pidigits, bpe_tokeniser, xml_etree_iterparse, xml_etree_generate
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x