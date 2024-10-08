# Results vs. 3.13.0b2

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 379 ms: 1.24x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| html5lib       | 66.1 ms                                                      | 72.5 ms: 1.10x slower                                                   |
| tornado_http   | 128 ms                                                       | 149 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                        | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 425 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.10x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 714 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 742 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.4 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 190 ms: 1.49x slower                                                    |
| Geometric mean | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 266 us: 1.06x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 382 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.3 us: 1.36x faster                                                   |
| deepcopy                   | 448 us                                                       | 396 us: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 425 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.10x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 714 ms: 1.07x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.78 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 742 ms: 1.07x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.93 ms: 1.05x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                   |
| float                      | 91.4 ms                                                      | 88.4 ms: 1.03x faster                                                   |
| scimark_sor                | 159 ms                                                       | 154 ms: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                  |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                    |
| json                       | 5.64 ms                                                      | 5.78 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.97 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 459 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.76 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.29 sec: 1.04x slower                                                  |
| logging_simple             | 7.21 us                                                      | 7.47 us: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.04x slower                                                  |
| async_generators           | 488 ms                                                       | 511 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.24 us: 1.05x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 266 us: 1.06x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 382 us: 1.06x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.7 ms: 1.06x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.56 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 209 us: 1.08x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 89.0 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 638 ms: 1.09x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 72.5 ms: 1.10x slower                                                   |
| fannkuch                   | 451 ms                                                       | 502 ms: 1.11x slower                                                    |
| pyflate                    | 557 ms                                                       | 622 ms: 1.12x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.34 ms: 1.12x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.1 ms: 1.12x slower                                                   |
| tornado_http               | 128 ms                                                       | 149 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 152 ms: 1.17x slower                                                    |
| raytrace                   | 297 ms                                                       | 353 ms: 1.19x slower                                                    |
| comprehensions             | 20.5 us                                                      | 24.6 us: 1.20x slower                                                   |
| django_template            | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                   |
| richards                   | 55.9 ms                                                      | 67.5 ms: 1.21x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.76 ms: 1.24x slower                                                   |
| richards_super             | 62.3 ms                                                      | 77.3 ms: 1.24x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 77.7 ms: 1.24x slower                                                   |
| 2to3                       | 305 ms                                                       | 379 ms: 1.24x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.53 sec: 1.25x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 124 ms: 1.26x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.19 ms: 1.28x slower                                                   |
| sympy_expand               | 457 ms                                                       | 603 ms: 1.32x slower                                                    |
| docutils                   | 3.10 sec                                                     | 4.10 sec: 1.32x slower                                                  |
| chaos                      | 68.3 ms                                                      | 90.9 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                   |
| sympy_str                  | 265 ms                                                       | 361 ms: 1.36x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.28 sec: 1.37x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.65 sec: 1.37x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 29.0 ms: 1.39x slower                                                   |
| go                         | 161 ms                                                       | 226 ms: 1.40x slower                                                    |
| pylint                     | 337 ms                                                       | 480 ms: 1.42x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.2 ms: 1.45x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 211 ms: 1.47x slower                                                    |
| regex_compile              | 128 ms                                                       | 190 ms: 1.49x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.6 ms: 1.55x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (10): regex_dna, xml_etree_parse, thrift, create_gc_cycles, pidigits, mako, xml_etree_process, xml_etree_iterparse, nbody, coverage
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x