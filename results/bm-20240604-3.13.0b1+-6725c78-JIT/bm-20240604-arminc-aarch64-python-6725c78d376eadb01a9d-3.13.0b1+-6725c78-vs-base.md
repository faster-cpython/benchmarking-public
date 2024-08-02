# Results vs. base

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                              | 365 ms: 1.20x slower                                                                                                    |
| chameleon      | 8.99 ms                                                                                                             | 9.29 ms: 1.03x slower                                                                                                   |
| docutils       | 3.07 sec                                                                                                            | 3.62 sec: 1.18x slower                                                                                                  |
| html5lib       | 66.1 ms                                                                                                             | 71.7 ms: 1.08x slower                                                                                                   |
| tornado_http   | 127 ms                                                                                                              | 150 ms: 1.18x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.26 sec                                                                                                            | 1.23 sec: 1.03x faster                                                                                                  |
| async_tree_none            | 487 ms                                                                                                              | 504 ms: 1.04x slower                                                                                                    |
| async_tree_none_tg         | 473 ms                                                                                                              | 489 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 781 ms                                                                                                              | 817 ms: 1.05x slower                                                                                                    |
| async_tree_io              | 1.19 sec                                                                                                            | 1.25 sec: 1.05x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                                                                              | 801 ms: 1.05x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 91.1 ms                                                                                                             | 89.2 ms: 1.02x faster                                                                                                   |
| nbody          | 112 ms                                                                                                              | 114 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.7 ms                                                                                                             | 30.3 ms: 1.01x faster                                                                                                   |
| regex_effbot   | 4.89 ms                                                                                                             | 4.94 ms: 1.01x slower                                                                                                   |
| regex_dna      | 249 ms                                                                                                              | 260 ms: 1.04x slower                                                                                                    |
| regex_compile  | 129 ms                                                                                                              | 176 ms: 1.36x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                                                             | 13.2 ms: 1.01x faster                                                                                                   |
| json_loads           | 32.2 us                                                                                                             | 32.0 us: 1.01x faster                                                                                                   |
| unpickle             | 19.7 us                                                                                                             | 20.0 us: 1.02x slower                                                                                                   |
| tomli_loads          | 2.56 sec                                                                                                            | 2.62 sec: 1.02x slower                                                                                                  |
| unpickle_list        | 6.48 us                                                                                                             | 6.63 us: 1.02x slower                                                                                                   |
| xml_etree_generate   | 114 ms                                                                                                              | 117 ms: 1.02x slower                                                                                                    |
| unpickle_pure_python | 253 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| pickle_pure_python   | 360 us                                                                                                              | 396 us: 1.10x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (6): pickle_list, xml_etree_parse, pickle, pickle_dict, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                             | 15.9 ms: 1.20x slower                                                                                                   |
| python_startup_no_site | 8.55 ms                                                                                                             | 11.2 ms: 1.31x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                               | 1.25x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                                                                             | 12.9 ms: 1.04x faster                                                                                                   |
| django_template | 41.8 ms                                                                                                             | 49.8 ms: 1.19x slower                                                                                                   |
| genshi_text     | 28.0 ms                                                                                                             | 34.3 ms: 1.22x slower                                                                                                   |
| genshi_xml      | 60.8 ms                                                                                                             | 83.0 ms: 1.36x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.18x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json | results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako                       | 13.4 ms                                                                                                             | 12.9 ms: 1.04x faster                                                                                                   |
| async_tree_io_tg           | 1.26 sec                                                                                                            | 1.23 sec: 1.03x faster                                                                                                  |
| deepcopy_memo              | 50.8 us                                                                                                             | 49.4 us: 1.03x faster                                                                                                   |
| float                      | 91.1 ms                                                                                                             | 89.2 ms: 1.02x faster                                                                                                   |
| json_dumps                 | 13.4 ms                                                                                                             | 13.2 ms: 1.01x faster                                                                                                   |
| sqlite_synth               | 3.91 us                                                                                                             | 3.87 us: 1.01x faster                                                                                                   |
| regex_v8                   | 30.7 ms                                                                                                             | 30.3 ms: 1.01x faster                                                                                                   |
| json_loads                 | 32.2 us                                                                                                             | 32.0 us: 1.01x faster                                                                                                   |
| richards                   | 55.9 ms                                                                                                             | 56.5 ms: 1.01x slower                                                                                                   |
| regex_effbot               | 4.89 ms                                                                                                             | 4.94 ms: 1.01x slower                                                                                                   |
| richards_super             | 62.3 ms                                                                                                             | 63.0 ms: 1.01x slower                                                                                                   |
| nbody                      | 112 ms                                                                                                              | 114 ms: 1.02x slower                                                                                                    |
| unpickle                   | 19.7 us                                                                                                             | 20.0 us: 1.02x slower                                                                                                   |
| json                       | 5.60 ms                                                                                                             | 5.71 ms: 1.02x slower                                                                                                   |
| thrift                     | 951 us                                                                                                              | 971 us: 1.02x slower                                                                                                    |
| tomli_loads                | 2.56 sec                                                                                                            | 2.62 sec: 1.02x slower                                                                                                  |
| unpickle_list              | 6.48 us                                                                                                             | 6.63 us: 1.02x slower                                                                                                   |
| xml_etree_generate         | 114 ms                                                                                                              | 117 ms: 1.02x slower                                                                                                    |
| logging_silent             | 135 ns                                                                                                              | 138 ns: 1.03x slower                                                                                                    |
| mdp                        | 3.34 sec                                                                                                            | 3.44 sec: 1.03x slower                                                                                                  |
| chameleon                  | 8.99 ms                                                                                                             | 9.29 ms: 1.03x slower                                                                                                   |
| async_generators           | 493 ms                                                                                                              | 509 ms: 1.03x slower                                                                                                    |
| spectral_norm              | 141 ms                                                                                                              | 146 ms: 1.03x slower                                                                                                    |
| async_tree_none            | 487 ms                                                                                                              | 504 ms: 1.04x slower                                                                                                    |
| async_tree_none_tg         | 473 ms                                                                                                              | 489 ms: 1.04x slower                                                                                                    |
| scimark_fft                | 444 ms                                                                                                              | 460 ms: 1.04x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                              | 117 ms: 1.04x slower                                                                                                    |
| logging_format             | 7.73 us                                                                                                             | 8.02 us: 1.04x slower                                                                                                   |
| logging_simple             | 7.01 us                                                                                                             | 7.27 us: 1.04x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                            | 2.28 sec: 1.04x slower                                                                                                  |
| fannkuch                   | 451 ms                                                                                                              | 469 ms: 1.04x slower                                                                                                    |
| telco                      | 9.87 ms                                                                                                             | 10.3 ms: 1.04x slower                                                                                                   |
| regex_dna                  | 249 ms                                                                                                              | 260 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 781 ms                                                                                                              | 817 ms: 1.05x slower                                                                                                    |
| async_tree_io              | 1.19 sec                                                                                                            | 1.25 sec: 1.05x slower                                                                                                  |
| create_gc_cycles           | 2.31 ms                                                                                                             | 2.42 ms: 1.05x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                                                                              | 801 ms: 1.05x slower                                                                                                    |
| scimark_sparse_mat_mult    | 6.56 ms                                                                                                             | 6.95 ms: 1.06x slower                                                                                                   |
| crypto_pyaes               | 82.0 ms                                                                                                             | 87.1 ms: 1.06x slower                                                                                                   |
| generators                 | 37.1 ms                                                                                                             | 39.5 ms: 1.06x slower                                                                                                   |
| scimark_monte_carlo        | 82.5 ms                                                                                                             | 88.1 ms: 1.07x slower                                                                                                   |
| raytrace                   | 298 ms                                                                                                              | 318 ms: 1.07x slower                                                                                                    |
| typing_runtime_protocols   | 194 us                                                                                                              | 207 us: 1.07x slower                                                                                                    |
| bench_thread_pool          | 1.26 ms                                                                                                             | 1.35 ms: 1.07x slower                                                                                                   |
| pyflate                    | 559 ms                                                                                                              | 599 ms: 1.07x slower                                                                                                    |
| html5lib                   | 66.1 ms                                                                                                             | 71.7 ms: 1.08x slower                                                                                                   |
| flaskblogging              | 4.83 ms                                                                                                             | 5.25 ms: 1.09x slower                                                                                                   |
| dask                       | 369 ms                                                                                                              | 403 ms: 1.09x slower                                                                                                    |
| scimark_sor                | 158 ms                                                                                                              | 173 ms: 1.10x slower                                                                                                    |
| unpickle_pure_python       | 253 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| pickle_pure_python         | 360 us                                                                                                              | 396 us: 1.10x slower                                                                                                    |
| gunicorn                   | 1.24 ms                                                                                                             | 1.37 ms: 1.10x slower                                                                                                   |
| sqlglot_optimize           | 62.7 ms                                                                                                             | 69.3 ms: 1.11x slower                                                                                                   |
| pycparser                  | 1.21 sec                                                                                                            | 1.34 sec: 1.11x slower                                                                                                  |
| deepcopy                   | 448 us                                                                                                              | 497 us: 1.11x slower                                                                                                    |
| sqlglot_normalize          | 127 ms                                                                                                              | 142 ms: 1.12x slower                                                                                                    |
| asyncio_tcp                | 574 ms                                                                                                              | 645 ms: 1.12x slower                                                                                                    |
| go                         | 160 ms                                                                                                              | 180 ms: 1.13x slower                                                                                                    |
| comprehensions             | 20.4 us                                                                                                             | 23.1 us: 1.13x slower                                                                                                   |
| deepcopy_reduce            | 4.06 us                                                                                                             | 4.64 us: 1.14x slower                                                                                                   |
| aiohttp                    | 1.18 ms                                                                                                             | 1.35 ms: 1.14x slower                                                                                                   |
| sqlglot_parse              | 1.39 ms                                                                                                             | 1.60 ms: 1.15x slower                                                                                                   |
| sqlglot_transpile          | 1.74 ms                                                                                                             | 2.00 ms: 1.15x slower                                                                                                   |
| nqueens                    | 98.8 ms                                                                                                             | 116 ms: 1.17x slower                                                                                                    |
| tornado_http               | 127 ms                                                                                                              | 150 ms: 1.18x slower                                                                                                    |
| docutils                   | 3.07 sec                                                                                                            | 3.62 sec: 1.18x slower                                                                                                  |
| deltablue                  | 3.85 ms                                                                                                             | 4.58 ms: 1.19x slower                                                                                                   |
| django_template            | 41.8 ms                                                                                                             | 49.8 ms: 1.19x slower                                                                                                   |
| pprint_safe_repr           | 926 ms                                                                                                              | 1.10 sec: 1.19x slower                                                                                                  |
| 2to3                       | 304 ms                                                                                                              | 365 ms: 1.20x slower                                                                                                    |
| python_startup             | 13.2 ms                                                                                                             | 15.9 ms: 1.20x slower                                                                                                   |
| bench_mp_pool              | 7.04 ms                                                                                                             | 8.50 ms: 1.21x slower                                                                                                   |
| sympy_expand               | 461 ms                                                                                                              | 561 ms: 1.22x slower                                                                                                    |
| pprint_pformat             | 1.90 sec                                                                                                            | 2.32 sec: 1.22x slower                                                                                                  |
| genshi_text                | 28.0 ms                                                                                                             | 34.3 ms: 1.22x slower                                                                                                   |
| mypy2                      | 764 ms                                                                                                              | 938 ms: 1.23x slower                                                                                                    |
| pylint                     | 338 ms                                                                                                              | 417 ms: 1.23x slower                                                                                                    |
| sympy_str                  | 266 ms                                                                                                              | 332 ms: 1.25x slower                                                                                                    |
| chaos                      | 68.7 ms                                                                                                             | 86.1 ms: 1.25x slower                                                                                                   |
| hexiom                     | 7.10 ms                                                                                                             | 8.91 ms: 1.26x slower                                                                                                   |
| sympy_integrate            | 21.1 ms                                                                                                             | 26.7 ms: 1.27x slower                                                                                                   |
| dulwich_log                | 59.7 ms                                                                                                             | 77.4 ms: 1.30x slower                                                                                                   |
| scimark_lu                 | 140 ms                                                                                                              | 183 ms: 1.30x slower                                                                                                    |
| python_startup_no_site     | 8.55 ms                                                                                                             | 11.2 ms: 1.31x slower                                                                                                   |
| sympy_sum                  | 145 ms                                                                                                              | 191 ms: 1.31x slower                                                                                                    |
| regex_compile              | 129 ms                                                                                                              | 176 ms: 1.36x slower                                                                                                    |
| genshi_xml                 | 60.8 ms                                                                                                             | 83.0 ms: 1.36x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                               | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (14): pidigits, gc_traversal, pickle_list, xml_etree_parse, coroutines, pickle, asyncio_websockets, coverage, pickle_dict, pathlib, xml_etree_iterparse, xml_etree_process, async_tree_memoization, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.09x