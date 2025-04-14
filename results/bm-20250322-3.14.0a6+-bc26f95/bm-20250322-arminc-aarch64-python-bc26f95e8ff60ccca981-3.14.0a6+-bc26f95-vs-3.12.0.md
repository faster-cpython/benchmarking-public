# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.045x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 907 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.7 ms: 1.05x faster                                                    |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.9 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 174 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                   |
| unpickle             | 18.5 us                                                               | 17.9 us: 1.03x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.1 ms: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 38.7 us: 1.04x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 273 us: 1.05x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.60 us: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 397 us: 1.09x slower                                                     |
| pickle_list          | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| json_loads           | 30.7 us                                                               | 34.3 us: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| pickle               | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 386 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 461 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 882 ms: 1.60x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 907 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 647 ms: 1.37x faster                                                     |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 51.8 ms: 1.20x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.95 ms: 1.17x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                    |
| go                         | 157 ms                                                                | 137 ms: 1.15x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                    |
| pylint                     | 355 ms                                                                | 317 ms: 1.12x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 174 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 318 ms: 1.11x faster                                                     |
| async_generators           | 491 ms                                                                | 449 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.05 us: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                    |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                     |
| float                      | 92.1 ms                                                               | 87.7 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                    |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 546 ms: 1.04x faster                                                     |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| unpickle                   | 18.5 us                                                               | 17.9 us: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 27.9 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.96 sec: 1.01x faster                                                   |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 80.1 ms: 1.01x slower                                                    |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                                   |
| pyflate                    | 559 ms                                                                | 572 ms: 1.02x slower                                                     |
| scimark_fft                | 418 ms                                                                | 429 ms: 1.03x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                     |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 38.7 us: 1.04x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 273 us: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 965 ms: 1.05x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.41 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.60 us: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.3 us: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.6 ms: 1.13x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| fannkuch                   | 443 ms                                                                | 507 ms: 1.14x slower                                                     |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.1 us: 1.20x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.68 ms: 1.52x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.75 sec: 389.29x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (16): scimark_lu, scimark_monte_carlo, genshi_xml, sympy_sum, django_template, chaos, sqlite_synth, html5lib, scimark_sor, genshi_text, richards_super, pidigits, coroutines, xml_etree_generate, crypto_pyaes, richards
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x