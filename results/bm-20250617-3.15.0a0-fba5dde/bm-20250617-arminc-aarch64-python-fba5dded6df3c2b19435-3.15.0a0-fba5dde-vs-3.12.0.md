# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.175x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 357 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.44 sec: 1.15x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.40x faster                                                  |
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.04 sec: 1.35x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 434 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 823 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 814 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 96.7 ms: 1.05x slower                                                   |
| pidigits       | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| nbody          | 105 ms                                                                | 141 ms: 1.35x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| regex_dna      | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 155 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.17 us                                                               | 6.80 us: 1.10x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                  |
| xml_etree_iterparse  | 150 ms                                                                | 170 ms: 1.13x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.4 us: 1.16x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 227 ms: 1.16x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.6 us: 1.22x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.5 us: 1.25x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 329 us: 1.27x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 468 us: 1.28x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 110 ms: 1.39x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| pickle               | 13.4 us                                                               | 20.5 us: 1.53x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.27x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.73 ms: 1.16x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.1 ms: 1.50x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 33.3 ms: 1.21x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 75.1 ms: 1.24x slower                                                   |
| django_template | 40.7 ms                                                               | 53.6 ms: 1.32x slower                                                   |
| mako            | 12.9 ms                                                               | 17.0 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.97 sec: 1.74x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.40x faster                                                  |
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.04 sec: 1.35x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 434 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 43.3 us: 1.15x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| regex_dna                  | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 823 ms: 1.11x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                   |
| deepcopy                   | 446 us                                                                | 406 us: 1.10x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.7 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 814 ms: 1.09x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                    |
| async_generators           | 491 ms                                                                | 515 ms: 1.05x slower                                                    |
| float                      | 92.1 ms                                                               | 96.7 ms: 1.05x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 66.0 ms: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 23.5 ms: 1.09x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.8 ms: 1.09x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.54 ms: 1.10x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.80 us: 1.10x slower                                                   |
| raytrace                   | 353 ms                                                                | 390 ms: 1.10x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.59 us: 1.12x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 95.9 ms: 1.13x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 170 ms: 1.13x slower                                                    |
| scimark_sor                | 150 ms                                                                | 169 ms: 1.13x slower                                                    |
| regex_compile              | 137 ms                                                                | 155 ms: 1.13x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 33.0 ms: 1.14x slower                                                   |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.14x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.44 sec: 1.15x slower                                                  |
| chaos                      | 71.4 ms                                                               | 82.7 ms: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 357 ms: 1.16x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 43.4 us: 1.16x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 227 ms: 1.16x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.52 ms: 1.16x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 9.73 ms: 1.16x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 180 ms: 1.17x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.23 ms: 1.18x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                                  |
| scimark_fft                | 418 ms                                                                | 498 ms: 1.19x slower                                                    |
| spectral_norm              | 131 ms                                                                | 156 ms: 1.20x slower                                                    |
| sympy_str                  | 280 ms                                                                | 339 ms: 1.21x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 105 ms: 1.21x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.3 ms: 1.21x slower                                                   |
| pidigits                   | 233 ms                                                                | 282 ms: 1.21x slower                                                    |
| unpickle                   | 18.5 us                                                               | 22.6 us: 1.22x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.40 us: 1.23x slower                                                   |
| logging_format             | 8.34 us                                                               | 10.3 us: 1.23x slower                                                   |
| richards_super             | 58.5 ms                                                               | 72.2 ms: 1.24x slower                                                   |
| json                       | 5.54 ms                                                               | 6.86 ms: 1.24x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 75.1 ms: 1.24x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.76 ms: 1.25x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.5 us: 1.25x slower                                                   |
| richards                   | 50.9 ms                                                               | 64.0 ms: 1.26x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 329 us: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 186 ms: 1.28x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.82 us: 1.28x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 468 us: 1.28x slower                                                    |
| django_template            | 40.7 ms                                                               | 53.6 ms: 1.32x slower                                                   |
| mako                       | 12.9 ms                                                               | 17.0 ms: 1.32x slower                                                   |
| fannkuch                   | 443 ms                                                                | 590 ms: 1.33x slower                                                    |
| thrift                     | 937 us                                                                | 1.25 ms: 1.34x slower                                                   |
| sympy_expand               | 454 ms                                                                | 606 ms: 1.34x slower                                                    |
| pickle_list                | 5.25 us                                                               | 7.08 us: 1.35x slower                                                   |
| nbody                      | 105 ms                                                                | 141 ms: 1.35x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 110 ms: 1.39x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.70 sec: 1.43x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 259 us: 1.43x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.34 sec: 1.46x slower                                                  |
| python_startup             | 11.4 ms                                                               | 17.1 ms: 1.50x slower                                                   |
| pickle                     | 13.4 us                                                               | 20.5 us: 1.53x slower                                                   |
| telco                      | 8.51 ms                                                               | 13.6 ms: 1.60x slower                                                   |
| coverage                   | 87.3 ms                                                               | 141 ms: 1.61x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.30 ms: 1.66x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.86 ms: 2.01x slower                                                   |
| logging_silent             | 127 ns                                                                | 946 ns: 7.46x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.40 sec: 766.09x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.25x slower                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.175x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.12x