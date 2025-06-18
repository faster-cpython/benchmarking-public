# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.165x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 369 ms: 1.20x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 531 ms: 1.46x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 518 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 446 ms: 1.40x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.02 sec: 1.39x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 818 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 813 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 94.8 ms: 1.03x slower                                                   |
| pidigits       | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| nbody          | 105 ms                                                                | 132 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.14x faster                                                   |
| regex_dna      | 254 ms                                                                | 229 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 154 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.72 sec: 1.05x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.72 us: 1.09x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 42.3 us: 1.13x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 173 ms: 1.15x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 229 ms: 1.18x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 308 us: 1.19x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.8 us: 1.23x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 474 us: 1.30x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 103 ms: 1.30x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 150 ms: 1.34x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.18 us: 1.37x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 16.8 ms: 1.37x slower                                                   |
| pickle               | 13.4 us                                                               | 20.1 us: 1.50x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.74 ms: 1.16x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.1 ms: 1.51x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 33.0 ms: 1.20x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 76.5 ms: 1.26x slower                                                   |
| django_template | 40.7 ms                                                               | 53.1 ms: 1.31x slower                                                   |
| mako            | 12.9 ms                                                               | 17.0 ms: 1.31x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.99 sec: 1.72x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 531 ms: 1.46x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 518 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 446 ms: 1.40x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.02 sec: 1.39x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 43.7 us: 1.14x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 818 ms: 1.11x faster                                                    |
| regex_dna                  | 254 ms                                                                | 229 ms: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.7 ms: 1.10x faster                                                   |
| deepcopy                   | 446 us                                                                | 408 us: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 813 ms: 1.09x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| float                      | 92.1 ms                                                               | 94.8 ms: 1.03x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 64.2 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| pyflate                    | 559 ms                                                                | 584 ms: 1.05x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.72 sec: 1.05x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.37 ms: 1.06x slower                                                   |
| pylint                     | 355 ms                                                                | 376 ms: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.7 ms: 1.09x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.72 us: 1.09x slower                                                   |
| go                         | 157 ms                                                                | 172 ms: 1.09x slower                                                    |
| async_generators           | 491 ms                                                                | 540 ms: 1.10x slower                                                    |
| regex_compile              | 137 ms                                                                | 154 ms: 1.12x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.60 us: 1.12x slower                                                   |
| scimark_fft                | 418 ms                                                                | 470 ms: 1.12x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 24.3 ms: 1.13x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 95.8 ms: 1.13x slower                                                   |
| raytrace                   | 353 ms                                                                | 400 ms: 1.13x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 42.3 us: 1.13x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 173 ms: 1.15x slower                                                    |
| scimark_sor                | 150 ms                                                                | 172 ms: 1.15x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.51 ms: 1.15x slower                                                   |
| spectral_norm              | 131 ms                                                                | 151 ms: 1.15x slower                                                    |
| meteor_contest             | 112 ms                                                                | 129 ms: 1.16x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.74 ms: 1.16x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 33.8 ms: 1.16x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 229 ms: 1.18x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 183 ms: 1.18x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 308 us: 1.19x slower                                                    |
| chaos                      | 71.4 ms                                                               | 84.9 ms: 1.19x slower                                                   |
| 2to3                       | 308 ms                                                                | 369 ms: 1.20x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.0 ms: 1.20x slower                                                   |
| pidigits                   | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| logging_simple             | 7.63 us                                                               | 9.27 us: 1.21x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                                  |
| unpickle                   | 18.5 us                                                               | 22.5 us: 1.22x slower                                                   |
| logging_format             | 8.34 us                                                               | 10.2 us: 1.23x slower                                                   |
| json_loads                 | 30.7 us                                                               | 37.8 us: 1.23x slower                                                   |
| sympy_str                  | 280 ms                                                                | 345 ms: 1.23x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 107 ms: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.71 ms: 1.25x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.71 ms: 1.25x slower                                                   |
| json                       | 5.54 ms                                                               | 6.95 ms: 1.25x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 76.5 ms: 1.26x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.76 us: 1.26x slower                                                   |
| nbody                      | 105 ms                                                                | 132 ms: 1.27x slower                                                    |
| fannkuch                   | 443 ms                                                                | 564 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 189 ms: 1.30x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 474 us: 1.30x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 103 ms: 1.30x slower                                                    |
| django_template            | 40.7 ms                                                               | 53.1 ms: 1.31x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.65 sec: 1.31x slower                                                  |
| mako                       | 12.9 ms                                                               | 17.0 ms: 1.31x slower                                                   |
| thrift                     | 937 us                                                                | 1.25 ms: 1.33x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 150 ms: 1.34x slower                                                    |
| pickle_list                | 5.25 us                                                               | 7.18 us: 1.37x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 16.8 ms: 1.37x slower                                                   |
| sympy_expand               | 454 ms                                                                | 624 ms: 1.38x slower                                                    |
| pickle                     | 13.4 us                                                               | 20.1 us: 1.50x slower                                                   |
| python_startup             | 11.4 ms                                                               | 17.1 ms: 1.51x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 275 us: 1.52x slower                                                    |
| coverage                   | 87.3 ms                                                               | 135 ms: 1.54x slower                                                    |
| telco                      | 8.51 ms                                                               | 13.6 ms: 1.59x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.22 ms: 1.64x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.24 sec: 1.72x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.58 sec: 1.73x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 2.00x slower                                                   |
| logging_silent             | 127 ns                                                                | 912 ns: 7.19x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.00 sec: 425.03x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.24x slower                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, richards
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.165x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.12x