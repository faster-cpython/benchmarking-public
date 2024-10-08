# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 386 ms: 1.27x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.04 sec: 1.30x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 140 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 542 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 580 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 751 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.3 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.81 ms: 1.04x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 188 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| xml_etree_process    | 80.8 ms                                                      | 79.7 ms: 1.01x faster                                                   |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 268 us: 1.07x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 391 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.3 ms: 1.25x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 36.8 us: 1.38x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                    |
| deepcopy                   | 448 us                                                       | 397 us: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 542 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 580 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                                    |
| scimark_sor                | 159 ms                                                       | 150 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 3.81 us: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 751 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| float                      | 91.4 ms                                                      | 88.3 ms: 1.04x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.04x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.81 ms: 1.04x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.08 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 79.7 ms: 1.01x faster                                                   |
| coverage                   | 98.4 ms                                                      | 97.7 ms: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| scimark_fft                | 445 ms                                                       | 454 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| thrift                     | 962 us                                                       | 992 us: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.44 us: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 6.02 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.80 ms: 1.04x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.16 us: 1.04x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                  |
| async_generators           | 488 ms                                                       | 511 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 614 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 268 us: 1.07x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.56 ms: 1.08x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 88.2 ms: 1.08x slower                                                   |
| meteor_contest             | 113 ms                                                       | 122 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 210 us: 1.09x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 391 us: 1.09x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.24 ms: 1.09x slower                                                   |
| tornado_http               | 128 ms                                                       | 140 ms: 1.10x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.8 ms: 1.10x slower                                                   |
| raytrace                   | 297 ms                                                       | 328 ms: 1.11x slower                                                    |
| fannkuch                   | 451 ms                                                       | 502 ms: 1.11x slower                                                    |
| pyflate                    | 557 ms                                                       | 643 ms: 1.15x slower                                                    |
| go                         | 161 ms                                                       | 186 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 150 ms: 1.16x slower                                                    |
| comprehensions             | 20.5 us                                                      | 24.2 us: 1.18x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.69 ms: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| richards_super             | 62.3 ms                                                      | 75.0 ms: 1.20x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.49 sec: 1.22x slower                                                  |
| richards                   | 55.9 ms                                                      | 68.4 ms: 1.22x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 123 ms: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.3 ms: 1.25x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 78.4 ms: 1.25x slower                                                   |
| 2to3                       | 305 ms                                                       | 386 ms: 1.27x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.22 ms: 1.30x slower                                                   |
| chaos                      | 68.3 ms                                                      | 88.9 ms: 1.30x slower                                                   |
| docutils                   | 3.10 sec                                                     | 4.04 sec: 1.30x slower                                                  |
| sympy_expand               | 457 ms                                                       | 604 ms: 1.32x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 28.9 ms: 1.38x slower                                                   |
| sympy_str                  | 265 ms                                                       | 370 ms: 1.39x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.0 ms: 1.41x slower                                                   |
| pylint                     | 337 ms                                                       | 477 ms: 1.42x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.35 sec: 1.44x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.79 sec: 1.45x slower                                                  |
| regex_compile              | 128 ms                                                       | 188 ms: 1.47x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 218 ms: 1.51x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.2 ms: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (10): xml_etree_parse, create_gc_cycles, mako, pidigits, coroutines, logging_silent, asyncio_websockets, python_startup, nbody, json
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x