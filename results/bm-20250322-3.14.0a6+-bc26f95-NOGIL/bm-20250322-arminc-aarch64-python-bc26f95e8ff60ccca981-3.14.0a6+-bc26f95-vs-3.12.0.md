# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.090x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 363 ms: 1.18x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.25 sec: 1.09x slower                                                   |
| html5lib       | 65.1 ms                                                               | 74.1 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 844 ms: 1.66x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 455 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 499 ms: 1.56x faster                                                     |
| async_tree_none            | 624 ms                                                                | 415 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 679 ms: 1.34x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| nbody          | 105 ms                                                                | 186 ms: 1.78x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.96 ms: 1.17x faster                                                    |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                    |
| regex_compile  | 137 ms                                                                | 161 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.72 us: 1.09x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.3 us: 1.10x slower                                                    |
| pickle               | 13.4 us                                                               | 15.5 us: 1.16x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.30 us: 1.18x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 308 us: 1.19x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.09 sec: 1.19x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 135 ms: 1.20x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 441 us: 1.21x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 98.0 ms: 1.24x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.2 us: 1.25x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 16.0 ms: 1.31x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                               | 19.5 ms: 1.72x slower                                                    |
| python_startup_no_site | 8.37 ms                                                               | 14.4 ms: 1.72x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.72x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 76.7 ms: 1.27x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 36.1 ms: 1.32x slower                                                    |
| django_template | 40.7 ms                                                               | 53.7 ms: 1.32x slower                                                    |
| mako            | 12.9 ms                                                               | 22.1 ms: 1.71x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.39x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 844 ms: 1.66x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 455 ms: 1.63x faster                                                     |
| gc_traversal               | 4.40 ms                                                               | 2.72 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 499 ms: 1.56x faster                                                     |
| async_tree_none            | 624 ms                                                                | 415 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 679 ms: 1.34x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.96 ms: 1.17x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| deepcopy                   | 446 us                                                                | 412 us: 1.08x faster                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.49 us: 1.08x faster                                                    |
| generators                 | 43.5 ms                                                               | 41.2 ms: 1.06x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.7 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| regex_v8                   | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.4 us: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 29.7 ms: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 584 ms: 1.03x slower                                                     |
| pylint                     | 355 ms                                                                | 375 ms: 1.06x slower                                                     |
| comprehensions             | 25.4 us                                                               | 26.9 us: 1.06x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.35 us: 1.06x slower                                                    |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                     |
| async_generators           | 491 ms                                                                | 525 ms: 1.07x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.25 sec: 1.09x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.72 us: 1.09x slower                                                    |
| go                         | 157 ms                                                                | 171 ms: 1.09x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.74 sec: 1.10x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.10 ms: 1.10x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.3 us: 1.10x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.11x slower                                                   |
| float                      | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| pyflate                    | 559 ms                                                                | 622 ms: 1.11x slower                                                     |
| logging_simple             | 7.63 us                                                               | 8.54 us: 1.12x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.46 sec: 1.13x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 74.1 ms: 1.14x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.57 us: 1.15x slower                                                    |
| raytrace                   | 353 ms                                                                | 406 ms: 1.15x slower                                                     |
| scimark_sor                | 150 ms                                                                | 172 ms: 1.15x slower                                                     |
| logging_silent             | 127 ns                                                                | 146 ns: 1.15x slower                                                     |
| scimark_fft                | 418 ms                                                                | 482 ms: 1.15x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.5 us: 1.16x slower                                                    |
| regex_compile              | 137 ms                                                                | 161 ms: 1.17x slower                                                     |
| 2to3                       | 308 ms                                                                | 363 ms: 1.18x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 7.30 us: 1.18x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 308 us: 1.19x slower                                                     |
| json                       | 5.54 ms                                                               | 6.58 ms: 1.19x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.09 sec: 1.19x slower                                                   |
| chaos                      | 71.4 ms                                                               | 85.1 ms: 1.19x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.20x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.26 sec: 1.20x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 135 ms: 1.20x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 441 us: 1.21x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.98 ms: 1.21x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 26.6 ms: 1.23x slower                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 194 ms: 1.23x slower                                                     |
| thrift                     | 937 us                                                                | 1.16 ms: 1.23x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 98.0 ms: 1.24x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.2 us: 1.25x slower                                                    |
| sympy_str                  | 280 ms                                                                | 354 ms: 1.27x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 76.7 ms: 1.27x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 21.2 ms: 1.27x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 111 ms: 1.28x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 187 ms: 1.28x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 129 ms: 1.30x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 110 ms: 1.30x slower                                                     |
| sympy_expand               | 454 ms                                                                | 592 ms: 1.31x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 16.0 ms: 1.31x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.1 ms: 1.32x slower                                                    |
| django_template            | 40.7 ms                                                               | 53.7 ms: 1.32x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.31 ms: 1.33x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.27 ms: 1.33x slower                                                    |
| meteor_contest             | 112 ms                                                                | 151 ms: 1.35x slower                                                     |
| telco                      | 8.51 ms                                                               | 11.7 ms: 1.38x slower                                                    |
| richards                   | 50.9 ms                                                               | 70.6 ms: 1.39x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.84 ms: 1.40x slower                                                    |
| richards_super             | 58.5 ms                                                               | 82.8 ms: 1.42x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 262 us: 1.45x slower                                                     |
| fannkuch                   | 443 ms                                                                | 652 ms: 1.47x slower                                                     |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.62x slower                                                     |
| mako                       | 12.9 ms                                                               | 22.1 ms: 1.71x slower                                                    |
| python_startup             | 11.4 ms                                                               | 19.5 ms: 1.72x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 14.4 ms: 1.72x slower                                                    |
| nbody                      | 105 ms                                                                | 186 ms: 1.78x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 57.7 ms: 8.19x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.090x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.28x