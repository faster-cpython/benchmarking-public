# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.263x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 446 ms: 1.45x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 84.1 ms: 1.29x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.35x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 977 ms: 1.44x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 518 ms: 1.43x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.03 sec: 1.38x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 425 ms: 1.36x faster                                                    |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 859 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| pidigits       | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| nbody          | 105 ms                                                                | 191 ms: 1.82x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.36x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                   |
| regex_dna      | 254 ms                                                                | 235 ms: 1.08x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 201 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.4 us: 1.16x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 239 ms: 1.23x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.58 us: 1.23x slower                                                   |
| pickle_list          | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.61 sec: 1.39x slower                                                  |
| unpickle             | 18.5 us                                                               | 26.4 us: 1.43x slower                                                   |
| json_loads           | 30.7 us                                                               | 44.6 us: 1.45x slower                                                   |
| pickle               | 13.4 us                                                               | 20.0 us: 1.49x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 418 us: 1.61x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 19.7 ms: 1.61x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 593 us: 1.62x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 128 ms: 1.63x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 189 ms: 1.68x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.41x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 13.8 ms: 1.64x slower                                                   |
| python_startup         | 11.4 ms                                                               | 23.3 ms: 2.05x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.83x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 98.2 ms: 1.62x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 46.5 ms: 1.69x slower                                                   |
| mako            | 12.9 ms                                                               | 23.8 ms: 1.84x slower                                                   |
| django_template | 40.7 ms                                                               | 75.2 ms: 1.85x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.75x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 977 ms: 1.44x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 518 ms: 1.43x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.03 sec: 1.38x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 425 ms: 1.36x faster                                                    |
| mdp                        | 3.41 sec                                                              | 2.52 sec: 1.35x faster                                                  |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 3.70 ms: 1.19x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                    |
| regex_dna                  | 254 ms                                                                | 235 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 859 ms: 1.06x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| generators                 | 43.5 ms                                                               | 47.0 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 639 ms: 1.13x slower                                                    |
| go                         | 157 ms                                                                | 178 ms: 1.14x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 56.7 us: 1.14x slower                                                   |
| float                      | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.54 sec: 1.16x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 43.4 us: 1.16x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.43 us: 1.17x slower                                                   |
| pyflate                    | 559 ms                                                                | 664 ms: 1.19x slower                                                    |
| deepcopy                   | 446 us                                                                | 534 us: 1.20x slower                                                    |
| pidigits                   | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| comprehensions             | 25.4 us                                                               | 30.8 us: 1.21x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 239 ms: 1.23x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.58 us: 1.23x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 30.2 ms: 1.23x slower                                                   |
| async_generators           | 491 ms                                                                | 613 ms: 1.25x slower                                                    |
| pylint                     | 355 ms                                                                | 457 ms: 1.29x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 84.1 ms: 1.29x slower                                                   |
| scimark_sor                | 150 ms                                                                | 194 ms: 1.30x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.53 ms: 1.32x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 38.5 ms: 1.33x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 83.3 ms: 1.34x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 5.55 ms: 1.35x slower                                                   |
| pickle_list                | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| scimark_fft                | 418 ms                                                                | 580 ms: 1.38x slower                                                    |
| meteor_contest             | 112 ms                                                                | 156 ms: 1.39x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.61 sec: 1.39x slower                                                  |
| chaos                      | 71.4 ms                                                               | 99.4 ms: 1.39x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.76 sec: 1.40x slower                                                  |
| raytrace                   | 353 ms                                                                | 498 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.96 ms: 1.43x slower                                                   |
| unpickle                   | 18.5 us                                                               | 26.4 us: 1.43x slower                                                   |
| json                       | 5.54 ms                                                               | 7.96 ms: 1.44x slower                                                   |
| 2to3                       | 308 ms                                                                | 446 ms: 1.45x slower                                                    |
| spectral_norm              | 131 ms                                                                | 190 ms: 1.45x slower                                                    |
| json_loads                 | 30.7 us                                                               | 44.6 us: 1.45x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.05 ms: 1.46x slower                                                   |
| regex_compile              | 137 ms                                                                | 201 ms: 1.46x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 32.0 ms: 1.48x slower                                                   |
| pickle                     | 13.4 us                                                               | 20.0 us: 1.49x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.96 ms: 1.50x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.22 us: 1.52x slower                                                   |
| logging_simple             | 7.63 us                                                               | 11.8 us: 1.54x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 239 ms: 1.54x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 153 ms: 1.54x slower                                                    |
| fannkuch                   | 443 ms                                                                | 693 ms: 1.56x slower                                                    |
| logging_format             | 8.34 us                                                               | 13.1 us: 1.56x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 232 ms: 1.59x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 418 us: 1.61x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 19.7 ms: 1.61x slower                                                   |
| sympy_str                  | 280 ms                                                                | 450 ms: 1.61x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 98.2 ms: 1.62x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 593 us: 1.62x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 128 ms: 1.63x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 139 ms: 1.64x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 13.8 ms: 1.64x slower                                                   |
| richards                   | 50.9 ms                                                               | 84.8 ms: 1.66x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 189 ms: 1.68x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 46.5 ms: 1.69x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 148 ms: 1.70x slower                                                    |
| richards_super             | 58.5 ms                                                               | 101 ms: 1.73x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 3.27 sec: 1.74x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.60 sec: 1.75x slower                                                  |
| sympy_expand               | 454 ms                                                                | 807 ms: 1.78x slower                                                    |
| thrift                     | 937 us                                                                | 1.69 ms: 1.81x slower                                                   |
| nbody                      | 105 ms                                                                | 191 ms: 1.82x slower                                                    |
| mako                       | 12.9 ms                                                               | 23.8 ms: 1.84x slower                                                   |
| django_template            | 40.7 ms                                                               | 75.2 ms: 1.85x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 358 us: 1.99x slower                                                    |
| coverage                   | 87.3 ms                                                               | 177 ms: 2.03x slower                                                    |
| python_startup             | 11.4 ms                                                               | 23.3 ms: 2.05x slower                                                   |
| telco                      | 8.51 ms                                                               | 17.8 ms: 2.09x slower                                                   |
| logging_silent             | 127 ns                                                                | 1.13 us: 8.95x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 72.7 ms: 10.30x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.39x slower                                                            |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.263x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.29x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.37x