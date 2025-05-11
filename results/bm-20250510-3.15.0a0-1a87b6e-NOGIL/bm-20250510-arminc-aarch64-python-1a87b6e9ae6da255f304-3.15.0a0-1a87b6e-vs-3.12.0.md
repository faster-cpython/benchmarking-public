# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.064x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 359 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                  |
| html5lib       | 65.1 ms                                                               | 69.0 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 837 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 869 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 484 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                    |
| async_tree_none            | 624 ms                                                                | 416 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 95.1 ms: 1.03x slower                                                   |
| nbody          | 105 ms                                                                | 168 ms: 1.61x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                   |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| regex_compile  | 137 ms                                                                | 150 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 176 ms: 1.11x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 40.0 us: 1.07x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.72 us: 1.09x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.88 sec: 1.11x slower                                                  |
| unpickle             | 18.5 us                                                               | 20.5 us: 1.11x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 302 us: 1.16x slower                                                    |
| pickle               | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.20 us: 1.17x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 438 us: 1.20x slower                                                    |
| json_loads           | 30.7 us                                                               | 39.0 us: 1.27x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 144 ms: 1.28x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 16.3 ms: 1.33x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.8 ms: 1.30x slower                                                   |
| mako            | 12.9 ms                                                               | 21.4 ms: 1.66x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.36x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.96 sec: 1.74x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 837 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 869 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 484 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.93 ms: 1.50x faster                                                   |
| async_tree_none            | 624 ms                                                                | 416 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                   |
| deepcopy                   | 446 us                                                                | 401 us: 1.11x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.6 ms: 1.10x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.50 us: 1.08x faster                                                   |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 47.7 us: 1.04x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 61.2 ms: 1.01x faster                                                   |
| comprehensions             | 25.4 us                                                               | 25.6 us: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| async_generators           | 491 ms                                                                | 501 ms: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 583 ms: 1.03x slower                                                    |
| float                      | 92.1 ms                                                               | 95.1 ms: 1.03x slower                                                   |
| pylint                     | 355 ms                                                                | 374 ms: 1.05x slower                                                    |
| spectral_norm              | 131 ms                                                                | 138 ms: 1.06x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.6 ms: 1.06x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.34 us: 1.06x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 69.0 ms: 1.06x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 40.0 us: 1.07x slower                                                   |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.08x slower                                                    |
| pyflate                    | 559 ms                                                                | 608 ms: 1.09x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.72 us: 1.09x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                  |
| regex_compile              | 137 ms                                                                | 150 ms: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.11x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.88 sec: 1.11x slower                                                  |
| unpickle                   | 18.5 us                                                               | 20.5 us: 1.11x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.44 sec: 1.12x slower                                                  |
| raytrace                   | 353 ms                                                                | 396 ms: 1.12x slower                                                    |
| scimark_fft                | 418 ms                                                                | 469 ms: 1.12x slower                                                    |
| chaos                      | 71.4 ms                                                               | 80.1 ms: 1.12x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.03 ms: 1.15x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.78 ms: 1.16x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 302 us: 1.16x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 359 ms: 1.17x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.20 us: 1.17x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.07 sec: 1.17x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.20 sec: 1.17x slower                                                  |
| json                       | 5.54 ms                                                               | 6.48 ms: 1.17x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.7 ms: 1.19x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 174 ms: 1.20x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 438 us: 1.20x slower                                                    |
| sympy_str                  | 280 ms                                                                | 338 ms: 1.21x slower                                                    |
| logging_format             | 8.34 us                                                               | 10.1 us: 1.21x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.52 ms: 1.21x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.29 us: 1.22x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 188 ms: 1.22x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 121 ms: 1.22x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 107 ms: 1.26x slower                                                    |
| thrift                     | 937 us                                                                | 1.19 ms: 1.27x slower                                                   |
| json_loads                 | 30.7 us                                                               | 39.0 us: 1.27x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 111 ms: 1.28x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 144 ms: 1.28x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.8 ms: 1.30x slower                                                   |
| sympy_expand               | 454 ms                                                                | 597 ms: 1.32x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.2 ms: 1.32x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 16.3 ms: 1.33x slower                                                   |
| richards_super             | 58.5 ms                                                               | 78.5 ms: 1.34x slower                                                   |
| meteor_contest             | 112 ms                                                                | 150 ms: 1.34x slower                                                    |
| richards                   | 50.9 ms                                                               | 68.5 ms: 1.34x slower                                                   |
| fannkuch                   | 443 ms                                                                | 619 ms: 1.40x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.84 ms: 1.40x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 261 us: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| nbody                      | 105 ms                                                                | 168 ms: 1.61x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.4 ms: 1.66x slower                                                   |
| coverage                   | 87.3 ms                                                               | 150 ms: 1.72x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| logging_silent             | 127 ns                                                                | 763 ns: 6.02x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 61.6 ms: 8.74x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, pidigits, go
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.31x