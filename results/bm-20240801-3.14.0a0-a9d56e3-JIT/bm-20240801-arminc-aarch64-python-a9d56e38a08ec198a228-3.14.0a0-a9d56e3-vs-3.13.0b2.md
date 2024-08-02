# Results vs. 3.13.0b2

- fork: python
- ref: a9d56e38a08ec198a228
- machine: linux-aarch64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 372 ms: 1.22x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.74 sec: 1.21x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 140 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 440 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 756 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 187 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.00x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 401 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.91 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| genshi_text     | 27.4 ms                                                      | 32.9 ms: 1.20x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 73.3 ms: 1.21x slower                                                   |
| django_template | 42.3 ms                                                      | 51.4 ms: 1.22x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 39.0 us: 1.30x faster                                                   |
| deepcopy                   | 448 us                                                       | 388 us: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 440 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 756 ms: 1.05x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.01 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.4 ms: 1.02x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| coverage                   | 98.4 ms                                                      | 97.8 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.00x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                  |
| nbody                      | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                  |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| spectral_norm              | 141 ms                                                       | 145 ms: 1.03x slower                                                    |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                    |
| async_generators           | 488 ms                                                       | 504 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.91 ms: 1.04x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.47 us: 1.04x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| json                       | 5.64 ms                                                      | 5.87 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.31 ms: 1.04x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.16 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.85 ms: 1.05x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.25 us: 1.05x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.6 ms: 1.06x slower                                                   |
| meteor_contest             | 113 ms                                                       | 121 ms: 1.07x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 624 ms: 1.07x slower                                                    |
| pyflate                    | 557 ms                                                       | 597 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                   |
| fannkuch                   | 451 ms                                                       | 488 ms: 1.08x slower                                                    |
| dask                       | 370 ms                                                       | 401 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 212 us: 1.09x slower                                                    |
| tornado_http               | 128 ms                                                       | 140 ms: 1.10x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.1 ms: 1.10x slower                                                   |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                    |
| raytrace                   | 297 ms                                                       | 329 ms: 1.11x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 401 us: 1.12x slower                                                    |
| go                         | 161 ms                                                       | 183 ms: 1.14x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.42 ms: 1.14x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 148 ms: 1.15x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 72.8 ms: 1.16x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.66 ms: 1.17x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.28 ms: 1.18x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.44 sec: 1.18x slower                                                  |
| comprehensions             | 20.5 us                                                      | 24.3 us: 1.18x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 32.9 ms: 1.20x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.74 sec: 1.21x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.34 sec: 1.21x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 73.3 ms: 1.21x slower                                                   |
| django_template            | 42.3 ms                                                      | 51.4 ms: 1.22x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.14 sec: 1.22x slower                                                  |
| 2to3                       | 305 ms                                                       | 372 ms: 1.22x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.11 ms: 1.23x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 123 ms: 1.24x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 180 ms: 1.27x slower                                                    |
| chaos                      | 68.3 ms                                                      | 87.2 ms: 1.28x slower                                                   |
| sympy_expand               | 457 ms                                                       | 593 ms: 1.30x slower                                                    |
| pylint                     | 337 ms                                                       | 438 ms: 1.30x slower                                                    |
| sympy_str                  | 265 ms                                                       | 348 ms: 1.31x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 27.7 ms: 1.33x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.75 ms: 1.38x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 200 ms: 1.40x slower                                                    |
| regex_compile              | 128 ms                                                       | 187 ms: 1.46x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.3 ms: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_parse, richards, regex_effbot, richards_super, create_gc_cycles, float, xml_etree_process, pidigits, regex_dna, xml_etree_iterparse, thrift
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x