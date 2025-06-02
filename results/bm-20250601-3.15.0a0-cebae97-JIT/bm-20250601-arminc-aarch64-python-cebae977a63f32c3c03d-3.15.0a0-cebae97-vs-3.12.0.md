# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.074x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 366 ms: 1.19x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                                  |
| html5lib       | 65.1 ms                                                               | 69.6 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 527 ms: 1.41x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.03 sec: 1.36x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 825 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 818 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 276 ms: 1.19x slower                                                    |
| nbody          | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| regex_dna      | 254 ms                                                                | 226 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.69 sec: 1.04x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.92 us: 1.12x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 171 ms: 1.13x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.5 us: 1.16x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 227 ms: 1.17x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 311 us: 1.20x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.7 us: 1.23x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.0 us: 1.24x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 149 ms: 1.33x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 105 ms: 1.33x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 488 us: 1.34x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 16.7 ms: 1.36x slower                                                   |
| pickle               | 13.4 us                                                               | 19.9 us: 1.48x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.68 ms: 1.16x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.0 ms: 1.50x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 75.9 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 53.4 ms: 1.31x slower                                                   |
| mako            | 12.9 ms                                                               | 17.5 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat             | 1.88 sec                                                              | 2.43 us: 774073.72x faster                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.50 us: 609810.44x faster                                              |
| mdp                        | 3.41 sec                                                              | 1.98 sec: 1.72x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 527 ms: 1.41x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.03 sec: 1.36x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 43.1 us: 1.15x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| regex_dna                  | 254 ms                                                                | 226 ms: 1.12x faster                                                    |
| deepcopy                   | 446 us                                                                | 400 us: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 825 ms: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.0 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 818 ms: 1.08x faster                                                    |
| richards                   | 50.9 ms                                                               | 51.6 ms: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.69 sec: 1.04x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.28 ms: 1.04x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                   |
| pylint                     | 355 ms                                                                | 375 ms: 1.06x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 69.6 ms: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 598 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| go                         | 157 ms                                                                | 172 ms: 1.09x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.51 us: 1.10x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 68.2 ms: 1.10x slower                                                   |
| async_generators           | 491 ms                                                                | 542 ms: 1.10x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 27.3 ms: 1.11x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 24.2 ms: 1.12x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.92 us: 1.12x slower                                                   |
| raytrace                   | 353 ms                                                                | 399 ms: 1.13x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 171 ms: 1.13x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 97.3 ms: 1.14x slower                                                   |
| spectral_norm              | 131 ms                                                                | 150 ms: 1.15x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.68 ms: 1.16x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 180 ms: 1.16x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 43.5 us: 1.16x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 227 ms: 1.17x slower                                                    |
| meteor_contest             | 112 ms                                                                | 130 ms: 1.17x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 33.9 ms: 1.17x slower                                                   |
| scimark_fft                | 418 ms                                                                | 489 ms: 1.17x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.53 ms: 1.17x slower                                                   |
| chaos                      | 71.4 ms                                                               | 83.9 ms: 1.18x slower                                                   |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                    |
| pidigits                   | 233 ms                                                                | 276 ms: 1.19x slower                                                    |
| 2to3                       | 308 ms                                                                | 366 ms: 1.19x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 311 us: 1.20x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.61 sec: 1.21x slower                                                  |
| sympy_str                  | 280 ms                                                                | 340 ms: 1.22x slower                                                    |
| unpickle                   | 18.5 us                                                               | 22.7 us: 1.23x slower                                                   |
| logging_format             | 8.34 us                                                               | 10.2 us: 1.23x slower                                                   |
| json                       | 5.54 ms                                                               | 6.84 ms: 1.23x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.0 us: 1.24x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.46 us: 1.24x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 108 ms: 1.25x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 75.9 ms: 1.25x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.76 ms: 1.26x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.81 us: 1.28x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 187 ms: 1.29x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.98 ms: 1.29x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.63 sec: 1.30x slower                                                  |
| django_template            | 40.7 ms                                                               | 53.4 ms: 1.31x slower                                                   |
| nbody                      | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| fannkuch                   | 443 ms                                                                | 588 ms: 1.33x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 149 ms: 1.33x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 105 ms: 1.33x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 488 us: 1.34x slower                                                    |
| pickle_list                | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| mako                       | 12.9 ms                                                               | 17.5 ms: 1.36x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 135 ms: 1.36x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 16.7 ms: 1.36x slower                                                   |
| sympy_expand               | 454 ms                                                                | 622 ms: 1.37x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 262 us: 1.45x slower                                                    |
| pickle                     | 13.4 us                                                               | 19.9 us: 1.48x slower                                                   |
| python_startup             | 11.4 ms                                                               | 17.0 ms: 1.50x slower                                                   |
| telco                      | 8.51 ms                                                               | 13.5 ms: 1.59x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.50 ms: 1.71x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.88 ms: 2.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 898 ns: 7.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 729 ms: 8.35x slower                                                    |
| thrift                     | 937 us                                                                | 200 ms: 213.56x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 2.87 sec: 406.47x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (3): float, asyncio_tcp, comprehensions
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.11x