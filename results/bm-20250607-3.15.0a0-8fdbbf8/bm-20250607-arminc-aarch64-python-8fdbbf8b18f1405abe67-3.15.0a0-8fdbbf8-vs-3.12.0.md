# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.237x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.44 sec: 1.15x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 509 ms: 1.53x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 979 ms: 1.44x faster                                                    |
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 527 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 418 ms: 1.38x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 805 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 806 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                                   |
| pidigits       | 233 ms                                                                | 281 ms: 1.21x slower                                                    |
| nbody          | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                   |
| regex_dna      | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                                | 152 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.83 us: 1.11x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 168 ms: 1.12x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.3 us: 1.16x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 230 ms: 1.18x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 321 us: 1.24x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.6 us: 1.26x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 471 us: 1.29x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 106 ms: 1.34x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.19 us: 1.37x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 160 ms: 1.42x slower                                                    |
| pickle               | 13.4 us                                                               | 19.7 us: 1.47x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.58 ms: 1.15x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.9 ms: 1.49x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 74.3 ms: 1.23x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 33.9 ms: 1.24x slower                                                   |
| django_template | 40.7 ms                                                               | 52.6 ms: 1.29x slower                                                   |
| mako            | 12.9 ms                                                               | 17.4 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.98 sec: 1.72x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 509 ms: 1.53x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 979 ms: 1.44x faster                                                    |
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 527 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 418 ms: 1.38x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 805 ms: 1.13x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 44.0 us: 1.13x faster                                                   |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.10x faster                                                   |
| deepcopy                   | 446 us                                                                | 405 us: 1.10x faster                                                    |
| regex_dna                  | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 806 ms: 1.10x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.3 ms: 1.08x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 581 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.04x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 584 ms: 1.05x slower                                                    |
| pylint                     | 355 ms                                                                | 373 ms: 1.05x slower                                                    |
| float                      | 92.1 ms                                                               | 97.2 ms: 1.06x slower                                                   |
| async_generators           | 491 ms                                                                | 519 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.6 ms: 1.09x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.50 ms: 1.09x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 23.6 ms: 1.09x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.83 us: 1.11x slower                                                   |
| regex_compile              | 137 ms                                                                | 152 ms: 1.11x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 168 ms: 1.12x slower                                                    |
| raytrace                   | 353 ms                                                                | 400 ms: 1.13x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.49 ms: 1.14x slower                                                   |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.14x slower                                                    |
| 2to3                       | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.58 ms: 1.15x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.70 us: 1.15x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.44 sec: 1.15x slower                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 98.2 ms: 1.15x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 43.3 us: 1.16x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 179 ms: 1.16x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 34.0 ms: 1.17x slower                                                   |
| chaos                      | 71.4 ms                                                               | 83.9 ms: 1.18x slower                                                   |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 230 ms: 1.18x slower                                                    |
| sympy_str                  | 280 ms                                                                | 332 ms: 1.19x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 103 ms: 1.19x slower                                                    |
| spectral_norm              | 131 ms                                                                | 156 ms: 1.19x slower                                                    |
| scimark_fft                | 418 ms                                                                | 501 ms: 1.20x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.40 ms: 1.20x slower                                                   |
| pidigits                   | 233 ms                                                                | 281 ms: 1.21x slower                                                    |
| unpickle                   | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| logging_format             | 8.34 us                                                               | 10.2 us: 1.22x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.33 us: 1.22x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 74.3 ms: 1.23x slower                                                   |
| richards_super             | 58.5 ms                                                               | 71.8 ms: 1.23x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 321 us: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.9 ms: 1.24x slower                                                   |
| richards                   | 50.9 ms                                                               | 63.5 ms: 1.25x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.6 us: 1.26x slower                                                   |
| json                       | 5.54 ms                                                               | 7.02 ms: 1.27x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.88 ms: 1.27x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 471 us: 1.29x slower                                                    |
| sympy_expand               | 454 ms                                                                | 585 ms: 1.29x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 188 ms: 1.29x slower                                                    |
| django_template            | 40.7 ms                                                               | 52.6 ms: 1.29x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.92 us: 1.31x slower                                                   |
| nbody                      | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| fannkuch                   | 443 ms                                                                | 593 ms: 1.34x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 106 ms: 1.34x slower                                                    |
| mako                       | 12.9 ms                                                               | 17.4 ms: 1.35x slower                                                   |
| pickle_list                | 5.25 us                                                               | 7.19 us: 1.37x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.41x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.30 sec: 1.42x slower                                                  |
| xml_etree_generate         | 112 ms                                                                | 160 ms: 1.42x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 259 us: 1.44x slower                                                    |
| pickle                     | 13.4 us                                                               | 19.7 us: 1.47x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.9 ms: 1.49x slower                                                   |
| telco                      | 8.51 ms                                                               | 13.4 ms: 1.57x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.47 ms: 1.70x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 4.05 ms: 2.11x slower                                                   |
| logging_silent             | 127 ns                                                                | 929 ns: 7.33x slower                                                    |
| coverage                   | 87.3 ms                                                               | 695 ms: 7.96x slower                                                    |
| thrift                     | 937 us                                                                | 196 ms: 209.68x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 6.68 sec: 947.59x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.34x slower                                                            |

Benchmark hidden because not significant (1): dulwich_log
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.237x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.10x