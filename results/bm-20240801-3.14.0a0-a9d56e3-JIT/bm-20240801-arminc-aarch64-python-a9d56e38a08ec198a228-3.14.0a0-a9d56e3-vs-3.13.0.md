# Results vs. 3.13.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: linux-aarch64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 372 ms: 1.22x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.74 sec: 1.29x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.1 ms: 1.11x slower                                                   |
| tornado_http   | 131 ms                                                   | 140 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| async_tree_none            | 493 ms                                                   | 440 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 582 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| async_generators           | 496 ms                                                   | 504 ms: 1.02x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 624 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.4 ms: 1.03x faster                                                   |
| nbody          | 114 ms                                                   | 116 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 260 ms: 1.06x slower                                                    |
| regex_compile  | 128 ms                                                   | 187 ms: 1.45x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.67 sec: 1.06x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 277 us: 1.09x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 401 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.91 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| genshi_text     | 27.7 ms                                                  | 32.9 ms: 1.19x slower                                                   |
| django_template | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 73.3 ms: 1.22x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.14x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 39.0 us: 1.31x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| deepcopy                   | 451 us                                                   | 388 us: 1.16x faster                                                    |
| async_tree_none            | 493 ms                                                   | 440 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 582 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| float                      | 94.4 ms                                                  | 91.4 ms: 1.03x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| coverage                   | 98.5 ms                                                  | 97.8 ms: 1.01x faster                                                   |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| async_generators           | 496 ms                                                   | 504 ms: 1.02x slower                                                    |
| regex_effbot               | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                   |
| nbody                      | 114 ms                                                   | 116 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 8.91 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 1.31 ms: 1.03x slower                                                   |
| richards_super             | 60.3 ms                                                  | 62.0 ms: 1.03x slower                                                   |
| scimark_fft                | 447 ms                                                   | 460 ms: 1.03x slower                                                    |
| thrift                     | 946 us                                                   | 974 us: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                   | 145 ms: 1.03x slower                                                    |
| richards                   | 53.5 ms                                                  | 55.4 ms: 1.03x slower                                                   |
| mdp                        | 3.36 sec                                                 | 3.49 sec: 1.04x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.85 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| logging_format             | 7.83 us                                                  | 8.16 us: 1.04x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 4.25 us: 1.04x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 87.6 ms: 1.04x slower                                                   |
| json                       | 5.61 ms                                                  | 5.87 ms: 1.05x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| regex_dna                  | 246 ms                                                   | 260 ms: 1.06x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.67 sec: 1.06x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.06x slower                                                   |
| logging_simple             | 7.04 us                                                  | 7.47 us: 1.06x slower                                                   |
| meteor_contest             | 113 ms                                                   | 121 ms: 1.06x slower                                                    |
| tornado_http               | 131 ms                                                   | 140 ms: 1.07x slower                                                    |
| pyflate                    | 556 ms                                                   | 597 ms: 1.07x slower                                                    |
| fannkuch                   | 452 ms                                                   | 488 ms: 1.08x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 277 us: 1.09x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 90.1 ms: 1.09x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 624 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 212 us: 1.10x slower                                                    |
| scimark_sor                | 159 ms                                                   | 175 ms: 1.10x slower                                                    |
| raytrace                   | 298 ms                                                   | 329 ms: 1.10x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 5.01 ms: 1.10x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 71.1 ms: 1.11x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 401 us: 1.12x slower                                                    |
| go                         | 163 ms                                                   | 183 ms: 1.12x slower                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 8.28 ms: 1.13x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 1.44 sec: 1.14x slower                                                  |
| dask                       | 350 ms                                                   | 401 ms: 1.14x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.42 ms: 1.15x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 148 ms: 1.16x slower                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 72.8 ms: 1.17x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 32.9 ms: 1.19x slower                                                   |
| comprehensions             | 20.4 us                                                  | 24.3 us: 1.19x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.66 ms: 1.20x slower                                                   |
| 2to3                       | 306 ms                                                   | 372 ms: 1.22x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.11 ms: 1.22x slower                                                   |
| django_template            | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 73.3 ms: 1.22x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.14 sec: 1.23x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 2.34 sec: 1.23x slower                                                  |
| nqueens                    | 98.7 ms                                                  | 123 ms: 1.24x slower                                                    |
| chaos                      | 68.8 ms                                                  | 87.2 ms: 1.27x slower                                                   |
| pylint                     | 343 ms                                                   | 438 ms: 1.27x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.74 sec: 1.29x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 180 ms: 1.29x slower                                                    |
| sympy_expand               | 455 ms                                                   | 593 ms: 1.30x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 27.7 ms: 1.32x slower                                                   |
| sympy_str                  | 264 ms                                                   | 348 ms: 1.32x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 9.75 ms: 1.37x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 200 ms: 1.40x slower                                                    |
| regex_compile              | 128 ms                                                   | 187 ms: 1.45x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.3 ms: 1.51x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (11): json_dumps, async_tree_cpu_io_mixed, coroutines, pathlib, xml_etree_generate, xml_etree_parse, pidigits, bpe_tokeniser, logging_silent, xml_etree_process, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x