# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 367 ms: 1.20x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.67 sec: 1.18x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 139 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 696 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 744 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 117 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 275 us: 1.10x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 396 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| genshi_text     | 27.4 ms                                                      | 32.9 ms: 1.20x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 72.7 ms: 1.20x slower                                                   |
| django_template | 42.3 ms                                                      | 52.1 ms: 1.23x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.4 us: 1.32x faster                                                   |
| deepcopy                   | 448 us                                                       | 376 us: 1.19x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_none            | 492 ms                                                       | 435 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 696 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 744 ms: 1.06x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.91 ms: 1.05x faster                                                   |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.04x faster                                                  |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 22.2 ms: 1.03x faster                                                   |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| richards                   | 55.9 ms                                                      | 54.9 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| thrift                     | 962 us                                                       | 979 us: 1.02x slower                                                    |
| spectral_norm              | 141 ms                                                       | 144 ms: 1.02x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.35 us: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| logging_format             | 7.82 us                                                      | 8.00 us: 1.02x slower                                                   |
| nbody                      | 114 ms                                                       | 117 ms: 1.02x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                  |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.04x slower                                                   |
| async_generators           | 488 ms                                                       | 506 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.22 us: 1.05x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 148 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.90 ms: 1.05x slower                                                   |
| dask                       | 370 ms                                                       | 391 ms: 1.06x slower                                                    |
| meteor_contest             | 113 ms                                                       | 120 ms: 1.06x slower                                                    |
| fannkuch                   | 451 ms                                                       | 481 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 70.6 ms: 1.07x slower                                                   |
| scimark_fft                | 445 ms                                                       | 476 ms: 1.07x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.1 ms: 1.08x slower                                                   |
| tornado_http               | 128 ms                                                       | 139 ms: 1.09x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 275 us: 1.10x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 641 ms: 1.10x slower                                                    |
| pyflate                    | 557 ms                                                       | 612 ms: 1.10x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.2 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 213 us: 1.10x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 396 us: 1.10x slower                                                    |
| raytrace                   | 297 ms                                                       | 332 ms: 1.12x slower                                                    |
| go                         | 161 ms                                                       | 182 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 147 ms: 1.14x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.44 ms: 1.14x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 72.5 ms: 1.16x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.65 ms: 1.16x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.23 ms: 1.17x slower                                                   |
| comprehensions             | 20.5 us                                                      | 24.1 us: 1.17x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.67 sec: 1.18x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 32.9 ms: 1.20x slower                                                   |
| 2to3                       | 305 ms                                                       | 367 ms: 1.20x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.47 sec: 1.20x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 72.7 ms: 1.20x slower                                                   |
| django_template            | 42.3 ms                                                      | 52.1 ms: 1.23x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.11 ms: 1.23x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.16 sec: 1.24x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.39 sec: 1.24x slower                                                  |
| nqueens                    | 98.9 ms                                                      | 123 ms: 1.24x slower                                                    |
| pylint                     | 337 ms                                                       | 429 ms: 1.27x slower                                                    |
| chaos                      | 68.3 ms                                                      | 87.7 ms: 1.28x slower                                                   |
| sympy_expand               | 457 ms                                                       | 589 ms: 1.29x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 9.24 ms: 1.31x slower                                                   |
| sympy_str                  | 265 ms                                                       | 350 ms: 1.32x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 27.5 ms: 1.32x slower                                                   |
| regex_compile              | 128 ms                                                       | 174 ms: 1.36x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 201 ms: 1.40x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.3 ms: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (13): xml_etree_parse, xml_etree_process, regex_v8, richards_super, float, coverage, pidigits, xml_etree_generate, bpe_tokeniser, logging_silent, asyncio_websockets, create_gc_cycles, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x