# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.082x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 359 ms: 1.16x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.31 sec: 1.11x slower                                                   |
| html5lib       | 65.1 ms                                                               | 74.7 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 861 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 457 ms: 1.62x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 418 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 640 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 683 ms: 1.34x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 101 ms: 1.09x slower                                                     |
| nbody          | 105 ms                                                                | 182 ms: 1.74x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.5 ms: 1.03x faster                                                    |
| regex_dna      | 254 ms                                                                | 253 ms: 1.00x faster                                                     |
| regex_compile  | 137 ms                                                                | 160 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.15x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 39.3 us: 1.05x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.67 us: 1.08x slower                                                    |
| pickle               | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 303 us: 1.17x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 7.21 us: 1.17x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.05 sec: 1.18x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 448 us: 1.23x slower                                                     |
| xml_etree_generate   | 112 ms                                                                | 139 ms: 1.24x slower                                                     |
| json_loads           | 30.7 us                                                               | 38.4 us: 1.25x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 100 ms: 1.27x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 16.6 ms: 1.35x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 14.0 ms: 1.67x slower                                                    |
| python_startup         | 11.4 ms                                                               | 19.6 ms: 1.72x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.70x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 74.0 ms: 1.22x slower                                                    |
| django_template | 40.7 ms                                                               | 53.9 ms: 1.33x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 36.5 ms: 1.33x slower                                                    |
| mako            | 12.9 ms                                                               | 22.3 ms: 1.73x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.39x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.99 sec: 1.72x faster                                                   |
| gc_traversal               | 4.40 ms                                                               | 2.69 ms: 1.63x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 861 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 457 ms: 1.62x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 418 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 640 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 683 ms: 1.34x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.15x faster                                                     |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                    |
| deepcopy                   | 446 us                                                                | 401 us: 1.11x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.59 us: 1.05x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.5 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 253 ms: 1.00x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 50.7 us: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 579 ms: 1.02x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.3 us: 1.05x slower                                                    |
| pylint                     | 355 ms                                                                | 374 ms: 1.05x slower                                                     |
| comprehensions             | 25.4 us                                                               | 26.8 us: 1.06x slower                                                    |
| async_generators           | 491 ms                                                                | 519 ms: 1.06x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.9 ms: 1.06x slower                                                    |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.42 us: 1.08x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.67 us: 1.08x slower                                                    |
| go                         | 157 ms                                                                | 171 ms: 1.09x slower                                                     |
| float                      | 92.1 ms                                                               | 101 ms: 1.09x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.12 ms: 1.10x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.10x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.31 sec: 1.11x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.44 sec: 1.11x slower                                                   |
| pyflate                    | 559 ms                                                                | 627 ms: 1.12x slower                                                     |
| scimark_sor                | 150 ms                                                                | 170 ms: 1.14x slower                                                     |
| scimark_fft                | 418 ms                                                                | 480 ms: 1.15x slower                                                     |
| raytrace                   | 353 ms                                                                | 405 ms: 1.15x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 74.7 ms: 1.15x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.80 us: 1.15x slower                                                    |
| logging_silent             | 127 ns                                                                | 148 ns: 1.16x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.16x slower                                                    |
| 2to3                       | 308 ms                                                                | 359 ms: 1.16x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 303 us: 1.17x slower                                                     |
| json                       | 5.54 ms                                                               | 6.47 ms: 1.17x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.75 us: 1.17x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.21 us: 1.17x slower                                                    |
| regex_compile              | 137 ms                                                                | 160 ms: 1.17x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.05 sec: 1.18x slower                                                   |
| chaos                      | 71.4 ms                                                               | 85.1 ms: 1.19x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.21x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.29 sec: 1.21x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 5.01 ms: 1.22x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 121 ms: 1.22x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 74.0 ms: 1.22x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 448 us: 1.23x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 8.61 ms: 1.23x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 191 ms: 1.24x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 139 ms: 1.24x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 196 ms: 1.24x slower                                                     |
| json_loads                 | 30.7 us                                                               | 38.4 us: 1.25x slower                                                    |
| sympy_str                  | 280 ms                                                                | 353 ms: 1.26x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 100 ms: 1.27x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 27.4 ms: 1.27x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 21.2 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 186 ms: 1.27x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 113 ms: 1.31x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.11 ms: 1.31x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 113 ms: 1.32x slower                                                     |
| django_template            | 40.7 ms                                                               | 53.9 ms: 1.33x slower                                                    |
| sympy_expand               | 454 ms                                                                | 603 ms: 1.33x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 36.5 ms: 1.33x slower                                                    |
| meteor_contest             | 112 ms                                                                | 150 ms: 1.34x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 16.6 ms: 1.35x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.5 ms: 1.36x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.82 ms: 1.39x slower                                                    |
| fannkuch                   | 443 ms                                                                | 625 ms: 1.41x slower                                                     |
| richards_super             | 58.5 ms                                                               | 83.8 ms: 1.43x slower                                                    |
| richards                   | 50.9 ms                                                               | 73.9 ms: 1.45x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 265 us: 1.47x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 14.0 ms: 1.67x slower                                                    |
| coverage                   | 87.3 ms                                                               | 149 ms: 1.70x slower                                                     |
| python_startup             | 11.4 ms                                                               | 19.6 ms: 1.72x slower                                                    |
| mako                       | 12.9 ms                                                               | 22.3 ms: 1.73x slower                                                    |
| nbody                      | 105 ms                                                                | 182 ms: 1.74x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 57.2 ms: 8.11x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.29x