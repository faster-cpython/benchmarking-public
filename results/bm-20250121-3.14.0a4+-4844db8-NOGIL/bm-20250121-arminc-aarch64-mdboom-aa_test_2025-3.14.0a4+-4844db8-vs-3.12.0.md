# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.138x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 385 ms: 1.25x slower                                             |
| docutils       | 2.98 sec                                                              | 3.40 sec: 1.14x slower                                           |
| html5lib       | 65.1 ms                                                               | 80.0 ms: 1.23x slower                                            |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 923 ms: 1.52x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 959 ms: 1.47x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 530 ms: 1.47x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 505 ms: 1.47x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                             |
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 688 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.25x faster                                             |
| Geometric mean             | (ref)                                                                 | 1.41x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 105 ms: 1.14x slower                                             |
| nbody          | 105 ms                                                                | 184 ms: 1.75x slower                                             |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                            |
| regex_dna      | 254 ms                                                                | 265 ms: 1.04x slower                                             |
| regex_compile  | 137 ms                                                                | 162 ms: 1.18x slower                                             |
| regex_v8       | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                            |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                             |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                             |
| json_loads           | 30.7 us                                                               | 37.6 us: 1.23x slower                                            |
| tomli_loads          | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                           |
| xml_etree_generate   | 112 ms                                                                | 141 ms: 1.26x slower                                             |
| unpickle_pure_python | 260 us                                                                | 345 us: 1.33x slower                                             |
| pickle_pure_python   | 365 us                                                                | 494 us: 1.35x slower                                             |
| json_dumps           | 12.3 ms                                                               | 16.9 ms: 1.38x slower                                            |
| xml_etree_process    | 79.0 ms                                                               | 111 ms: 1.40x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.20x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.45x slower                                            |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                            |
| django_template | 40.7 ms                                                               | 56.2 ms: 1.38x slower                                            |
| genshi_text     | 27.4 ms                                                               | 38.2 ms: 1.39x slower                                            |
| mako            | 12.9 ms                                                               | 22.3 ms: 1.73x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.45x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 923 ms: 1.52x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 959 ms: 1.47x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 530 ms: 1.47x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 505 ms: 1.47x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                             |
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 688 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.25x faster                                             |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                             |
| regex_effbot               | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                            |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                             |
| pathlib                    | 24.5 ms                                                               | 23.4 ms: 1.05x faster                                            |
| regex_dna                  | 254 ms                                                                | 265 ms: 1.04x slower                                             |
| asyncio_websockets         | 658 ms                                                                | 687 ms: 1.04x slower                                             |
| deepcopy_memo              | 49.6 us                                                               | 52.7 us: 1.06x slower                                            |
| pylint                     | 355 ms                                                                | 391 ms: 1.10x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.15 ms: 1.12x slower                                            |
| comprehensions             | 25.4 us                                                               | 28.5 us: 1.12x slower                                            |
| json                       | 5.54 ms                                                               | 6.25 ms: 1.13x slower                                            |
| deepcopy_reduce            | 4.10 us                                                               | 4.63 us: 1.13x slower                                            |
| dulwich_log                | 62.0 ms                                                               | 70.1 ms: 1.13x slower                                            |
| mdp                        | 3.41 sec                                                              | 3.87 sec: 1.13x slower                                           |
| spectral_norm              | 131 ms                                                                | 148 ms: 1.14x slower                                             |
| float                      | 92.1 ms                                                               | 105 ms: 1.14x slower                                             |
| docutils                   | 2.98 sec                                                              | 3.40 sec: 1.14x slower                                           |
| go                         | 157 ms                                                                | 180 ms: 1.15x slower                                             |
| async_generators           | 491 ms                                                                | 566 ms: 1.15x slower                                             |
| coroutines                 | 29.0 ms                                                               | 33.5 ms: 1.16x slower                                            |
| pyflate                    | 559 ms                                                                | 654 ms: 1.17x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                           |
| regex_compile              | 137 ms                                                                | 162 ms: 1.18x slower                                             |
| regex_v8                   | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                            |
| scimark_fft                | 418 ms                                                                | 502 ms: 1.20x slower                                             |
| raytrace                   | 353 ms                                                                | 425 ms: 1.20x slower                                             |
| scimark_sor                | 150 ms                                                                | 181 ms: 1.21x slower                                             |
| gc_traversal               | 4.40 ms                                                               | 5.36 ms: 1.22x slower                                            |
| json_loads                 | 30.7 us                                                               | 37.6 us: 1.23x slower                                            |
| html5lib                   | 65.1 ms                                                               | 80.0 ms: 1.23x slower                                            |
| logging_simple             | 7.63 us                                                               | 9.40 us: 1.23x slower                                            |
| logging_format             | 8.34 us                                                               | 10.3 us: 1.24x slower                                            |
| sympy_sum                  | 154 ms                                                                | 192 ms: 1.24x slower                                             |
| 2to3                       | 308 ms                                                                | 385 ms: 1.25x slower                                             |
| tomli_loads                | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                           |
| xml_etree_generate         | 112 ms                                                                | 141 ms: 1.26x slower                                             |
| logging_silent             | 127 ns                                                                | 160 ns: 1.26x slower                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.85 ms: 1.27x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                           |
| chaos                      | 71.4 ms                                                               | 90.7 ms: 1.27x slower                                            |
| sqlglot_normalize          | 126 ms                                                                | 161 ms: 1.28x slower                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.41 sec: 1.28x slower                                           |
| sqlglot_optimize           | 61.3 ms                                                               | 78.5 ms: 1.28x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 111 ms: 1.28x slower                                             |
| sympy_integrate            | 21.6 ms                                                               | 27.8 ms: 1.29x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                            |
| sympy_str                  | 280 ms                                                                | 369 ms: 1.32x slower                                             |
| scimark_lu                 | 146 ms                                                                | 193 ms: 1.33x slower                                             |
| unpickle_pure_python       | 260 us                                                                | 345 us: 1.33x slower                                             |
| sqlalchemy_declarative     | 157 ms                                                                | 210 ms: 1.33x slower                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 115 ms: 1.35x slower                                             |
| pickle_pure_python         | 365 us                                                                | 494 us: 1.35x slower                                             |
| thrift                     | 937 us                                                                | 1.27 ms: 1.36x slower                                            |
| sqlglot_transpile          | 1.83 ms                                                               | 2.48 ms: 1.36x slower                                            |
| sympy_expand               | 454 ms                                                                | 620 ms: 1.37x slower                                             |
| json_dumps                 | 12.3 ms                                                               | 16.9 ms: 1.38x slower                                            |
| django_template            | 40.7 ms                                                               | 56.2 ms: 1.38x slower                                            |
| hexiom                     | 6.98 ms                                                               | 9.70 ms: 1.39x slower                                            |
| sqlglot_parse              | 1.46 ms                                                               | 2.04 ms: 1.39x slower                                            |
| genshi_text                | 27.4 ms                                                               | 38.2 ms: 1.39x slower                                            |
| nqueens                    | 99.2 ms                                                               | 138 ms: 1.40x slower                                             |
| xml_etree_process          | 79.0 ms                                                               | 111 ms: 1.40x slower                                             |
| meteor_contest             | 112 ms                                                                | 157 ms: 1.41x slower                                             |
| telco                      | 8.51 ms                                                               | 12.2 ms: 1.44x slower                                            |
| bench_thread_pool          | 1.31 ms                                                               | 1.89 ms: 1.44x slower                                            |
| richards                   | 50.9 ms                                                               | 73.4 ms: 1.44x slower                                            |
| sqlalchemy_imperative      | 16.7 ms                                                               | 24.1 ms: 1.44x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.45x slower                                            |
| richards_super             | 58.5 ms                                                               | 87.4 ms: 1.49x slower                                            |
| coverage                   | 87.3 ms                                                               | 132 ms: 1.51x slower                                             |
| fannkuch                   | 443 ms                                                                | 675 ms: 1.52x slower                                             |
| deltablue                  | 4.12 ms                                                               | 6.31 ms: 1.53x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 289 us: 1.60x slower                                             |
| mako                       | 12.9 ms                                                               | 22.3 ms: 1.73x slower                                            |
| nbody                      | 105 ms                                                                | 184 ms: 1.75x slower                                             |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                            |
| bench_mp_pool              | 7.05 ms                                                               | 57.5 ms: 8.15x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.21x slower                                                     |

Benchmark hidden because not significant (4): deepcopy, sqlite_synth, generators, pidigits
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.138x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.25x