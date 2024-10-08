# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.06x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 359 ms: 1.18x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.61 sec: 1.16x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.0 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 140 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_none            | 492 ms                                                       | 434 ms: 1.14x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 570 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 546 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 700 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 738 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 90.9 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 180 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 146 ms: 1.00x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 272 us: 1.08x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 396 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.92 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.8 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                      | 50.7 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 82.9 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.7 us: 1.31x faster                                                   |
| deepcopy                   | 448 us                                                       | 380 us: 1.18x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_none            | 492 ms                                                       | 434 ms: 1.14x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 570 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 546 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 700 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 738 ms: 1.07x faster                                                    |
| generators                 | 37.1 ms                                                      | 35.6 ms: 1.04x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.8 ms: 1.04x faster                                                   |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.04 ms: 1.03x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.8 ms: 1.02x faster                                                   |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| richards_super             | 62.3 ms                                                      | 61.4 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| float                      | 91.4 ms                                                      | 90.9 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 146 ms: 1.00x faster                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| logging_silent             | 133 ns                                                       | 135 ns: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.02x slower                                                   |
| logging_format             | 7.82 us                                                      | 7.96 us: 1.02x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.95 sec: 1.02x slower                                                  |
| thrift                     | 962 us                                                       | 981 us: 1.02x slower                                                    |
| spectral_norm              | 141 ms                                                       | 144 ms: 1.02x slower                                                    |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                    |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.44 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.77 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.03x slower                                                   |
| async_generators           | 488 ms                                                       | 505 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.92 ms: 1.04x slower                                                   |
| json                       | 5.64 ms                                                      | 5.86 ms: 1.04x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.20 us: 1.04x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 617 ms: 1.06x slower                                                    |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                    |
| fannkuch                   | 451 ms                                                       | 479 ms: 1.06x slower                                                    |
| pyflate                    | 557 ms                                                       | 593 ms: 1.07x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.7 ms: 1.07x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.0 ms: 1.07x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 88.4 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 272 us: 1.08x slower                                                    |
| tornado_http               | 128 ms                                                       | 140 ms: 1.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.10x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 396 us: 1.10x slower                                                    |
| raytrace                   | 297 ms                                                       | 329 ms: 1.11x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.32 ms: 1.11x slower                                                   |
| go                         | 161 ms                                                       | 180 ms: 1.12x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.12x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 145 ms: 1.12x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 71.2 ms: 1.14x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.5 us: 1.15x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.41 sec: 1.16x slower                                                  |
| docutils                   | 3.10 sec                                                     | 3.61 sec: 1.16x slower                                                  |
| 2to3                       | 305 ms                                                       | 359 ms: 1.18x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.03 ms: 1.19x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.38 ms: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                      | 50.7 ms: 1.20x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.15 sec: 1.23x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.38 sec: 1.23x slower                                                  |
| sympy_expand               | 457 ms                                                       | 571 ms: 1.25x slower                                                    |
| pylint                     | 337 ms                                                       | 428 ms: 1.27x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 35.0 ms: 1.28x slower                                                   |
| sympy_str                  | 265 ms                                                       | 339 ms: 1.28x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 181 ms: 1.28x slower                                                    |
| chaos                      | 68.3 ms                                                      | 87.5 ms: 1.28x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.16 ms: 1.29x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 27.1 ms: 1.30x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 82.9 ms: 1.37x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 199 ms: 1.38x slower                                                    |
| regex_compile              | 128 ms                                                       | 180 ms: 1.40x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_parse, coverage, create_gc_cycles, pidigits, asyncio_websockets, logging_simple, pathlib, xml_etree_process
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x