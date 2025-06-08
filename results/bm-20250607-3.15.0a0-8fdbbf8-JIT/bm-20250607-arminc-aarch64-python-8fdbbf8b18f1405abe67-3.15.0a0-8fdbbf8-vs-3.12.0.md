# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.245x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 369 ms: 1.20x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                    |
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.02 sec: 1.39x faster                                                  |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.04 sec: 1.35x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 823 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 812 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 279 ms: 1.20x slower                                                    |
| nbody          | 105 ms                                                                | 143 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                   |
| regex_dna      | 254 ms                                                                | 227 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 157 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.72 sec: 1.05x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.72 us: 1.09x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 170 ms: 1.13x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.2 us: 1.16x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 227 ms: 1.16x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 307 us: 1.18x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.9 us: 1.24x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 478 us: 1.31x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 104 ms: 1.32x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.11 us: 1.36x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 154 ms: 1.38x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.2 ms: 1.40x slower                                                   |
| pickle               | 13.4 us                                                               | 20.1 us: 1.50x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.71 ms: 1.16x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.0 ms: 1.50x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| mako            | 12.9 ms                                                               | 16.5 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 79.4 ms: 1.31x slower                                                   |
| django_template | 40.7 ms                                                               | 53.8 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.99 sec: 1.71x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                    |
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.02 sec: 1.39x faster                                                  |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.04 sec: 1.35x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.01 ms: 1.16x faster                                                   |
| regex_dna                  | 254 ms                                                                | 227 ms: 1.12x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 44.8 us: 1.11x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 823 ms: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.6 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 812 ms: 1.09x faster                                                    |
| deepcopy                   | 446 us                                                                | 410 us: 1.09x faster                                                    |
| richards                   | 50.9 ms                                                               | 51.7 ms: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| richards_super             | 58.5 ms                                                               | 60.8 ms: 1.04x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.72 sec: 1.05x slower                                                  |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                    |
| pylint                     | 355 ms                                                                | 380 ms: 1.07x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                   |
| go                         | 157 ms                                                                | 170 ms: 1.08x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 67.4 ms: 1.09x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.72 us: 1.09x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| async_generators           | 491 ms                                                                | 540 ms: 1.10x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.55 us: 1.11x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 24.2 ms: 1.12x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 170 ms: 1.13x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 27.8 ms: 1.13x slower                                                   |
| raytrace                   | 353 ms                                                                | 401 ms: 1.14x slower                                                    |
| regex_compile              | 137 ms                                                                | 157 ms: 1.14x slower                                                    |
| scimark_fft                | 418 ms                                                                | 482 ms: 1.15x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 43.2 us: 1.16x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 98.5 ms: 1.16x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.52 ms: 1.16x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 9.71 ms: 1.16x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 227 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 34.0 ms: 1.17x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 181 ms: 1.17x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 307 us: 1.18x slower                                                    |
| meteor_contest             | 112 ms                                                                | 134 ms: 1.19x slower                                                    |
| 2to3                       | 308 ms                                                                | 369 ms: 1.20x slower                                                    |
| pidigits                   | 233 ms                                                                | 279 ms: 1.20x slower                                                    |
| spectral_norm              | 131 ms                                                                | 157 ms: 1.21x slower                                                    |
| chaos                      | 71.4 ms                                                               | 86.2 ms: 1.21x slower                                                   |
| unpickle                   | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| json_loads                 | 30.7 us                                                               | 37.9 us: 1.24x slower                                                   |
| sympy_str                  | 280 ms                                                                | 348 ms: 1.24x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.70 us: 1.25x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 108 ms: 1.25x slower                                                    |
| logging_format             | 8.34 us                                                               | 10.4 us: 1.25x slower                                                   |
| json                       | 5.54 ms                                                               | 6.93 ms: 1.25x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.74 ms: 1.25x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.57 us: 1.25x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.77 ms: 1.26x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 186 ms: 1.28x slower                                                    |
| mako                       | 12.9 ms                                                               | 16.5 ms: 1.28x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.61 sec: 1.28x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 478 us: 1.31x slower                                                    |
| fannkuch                   | 443 ms                                                                | 581 ms: 1.31x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 79.4 ms: 1.31x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 104 ms: 1.32x slower                                                    |
| django_template            | 40.7 ms                                                               | 53.8 ms: 1.32x slower                                                   |
| pickle_list                | 5.25 us                                                               | 7.11 us: 1.36x slower                                                   |
| nbody                      | 105 ms                                                                | 143 ms: 1.37x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 136 ms: 1.37x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 154 ms: 1.38x slower                                                    |
| sympy_expand               | 454 ms                                                                | 628 ms: 1.38x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.2 ms: 1.40x slower                                                   |
| pickle                     | 13.4 us                                                               | 20.1 us: 1.50x slower                                                   |
| python_startup             | 11.4 ms                                                               | 17.0 ms: 1.50x slower                                                   |
| telco                      | 8.51 ms                                                               | 13.2 ms: 1.55x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 280 us: 1.55x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.39 ms: 1.68x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.26 sec: 1.73x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.59 sec: 1.74x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 4.04 ms: 2.11x slower                                                   |
| logging_silent             | 127 ns                                                                | 948 ns: 7.47x slower                                                    |
| coverage                   | 87.3 ms                                                               | 720 ms: 8.25x slower                                                    |
| thrift                     | 937 us                                                                | 197 ms: 210.63x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 3.45 sec: 488.72x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.35x slower                                                            |

Benchmark hidden because not significant (3): comprehensions, asyncio_tcp, float
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.245x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.13x