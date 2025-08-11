# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.087x slower
- HPT reliability: 99.73%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                  |
| html5lib       | 65.1 ms                                                               | 69.9 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 843 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 448 ms: 1.65x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 867 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 637 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.37x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 95.0 ms: 1.03x slower                                                   |
| nbody          | 105 ms                                                                | 181 ms: 1.73x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.22x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                   |
| regex_dna      | 254 ms                                                                | 241 ms: 1.05x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| regex_compile  | 137 ms                                                                | 148 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 131 ms: 1.15x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.06x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.7 us: 1.04x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.74 us: 1.09x slower                                                   |
| unpickle             | 18.5 us                                                               | 20.2 us: 1.10x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.87 sec: 1.11x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.91 us: 1.12x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 299 us: 1.15x slower                                                    |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| json_loads           | 30.7 us                                                               | 36.4 us: 1.19x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 437 us: 1.20x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 142 ms: 1.26x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| python_startup         | 11.4 ms                                                               | 19.9 ms: 1.75x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.58x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 76.4 ms: 1.26x slower                                                   |
| django_template | 40.7 ms                                                               | 51.5 ms: 1.27x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.8 ms: 1.31x slower                                                   |
| mako            | 12.9 ms                                                               | 21.0 ms: 1.63x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.36x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.94 sec: 1.76x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 843 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 448 ms: 1.65x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 867 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.85 ms: 1.54x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 637 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.37x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                   |
| deepcopy                   | 446 us                                                                | 386 us: 1.16x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 131 ms: 1.15x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 45.5 us: 1.09x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.52 us: 1.07x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.06x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.9 ms: 1.06x faster                                                   |
| regex_dna                  | 254 ms                                                                | 241 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.2 us: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.7 ms: 1.04x faster                                                   |
| go                         | 157 ms                                                                | 153 ms: 1.03x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.21 us: 1.03x slower                                                   |
| float                      | 92.1 ms                                                               | 95.0 ms: 1.03x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.7 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 515 ms: 1.05x slower                                                    |
| pyflate                    | 559 ms                                                                | 595 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.17 us: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                  |
| pylint                     | 355 ms                                                                | 381 ms: 1.07x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 69.9 ms: 1.07x slower                                                   |
| regex_compile              | 137 ms                                                                | 148 ms: 1.08x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 31.4 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.74 us: 1.09x slower                                                   |
| logging_format             | 8.34 us                                                               | 9.14 us: 1.10x slower                                                   |
| unpickle                   | 18.5 us                                                               | 20.2 us: 1.10x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.41 sec: 1.10x slower                                                  |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.87 sec: 1.11x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.91 us: 1.12x slower                                                   |
| raytrace                   | 353 ms                                                                | 396 ms: 1.12x slower                                                    |
| chaos                      | 71.4 ms                                                               | 80.0 ms: 1.12x slower                                                   |
| scimark_fft                | 418 ms                                                                | 471 ms: 1.13x slower                                                    |
| json                       | 5.54 ms                                                               | 6.30 ms: 1.14x slower                                                   |
| 2to3                       | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.98 ms: 1.14x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.16 sec: 1.15x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.05 sec: 1.15x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 299 us: 1.15x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.85 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.27 ms: 1.18x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.19x slower                                                   |
| json_loads                 | 30.7 us                                                               | 36.4 us: 1.19x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 437 us: 1.20x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 104 ms: 1.22x slower                                                    |
| sympy_str                  | 280 ms                                                                | 342 ms: 1.22x slower                                                    |
| meteor_contest             | 112 ms                                                                | 140 ms: 1.25x slower                                                    |
| thrift                     | 937 us                                                                | 1.18 ms: 1.26x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 76.4 ms: 1.26x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 109 ms: 1.26x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 142 ms: 1.26x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.5 ms: 1.27x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.91 ms: 1.28x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 188 ms: 1.29x slower                                                    |
| sympy_expand               | 454 ms                                                                | 591 ms: 1.30x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.8 ms: 1.31x slower                                                   |
| fannkuch                   | 443 ms                                                                | 593 ms: 1.34x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 250 us: 1.38x slower                                                    |
| richards                   | 50.9 ms                                                               | 70.6 ms: 1.39x slower                                                   |
| richards_super             | 58.5 ms                                                               | 81.2 ms: 1.39x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.86 ms: 1.42x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| mako                       | 12.9 ms                                                               | 21.0 ms: 1.63x slower                                                   |
| coverage                   | 87.3 ms                                                               | 144 ms: 1.65x slower                                                    |
| nbody                      | 105 ms                                                                | 181 ms: 1.73x slower                                                    |
| python_startup             | 11.4 ms                                                               | 19.9 ms: 1.75x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 66.8 ms: 9.47x slower                                                   |
| telco                      | 8.51 ms                                                               | 187 ms: 21.99x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_websockets, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.087x slower

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.33x