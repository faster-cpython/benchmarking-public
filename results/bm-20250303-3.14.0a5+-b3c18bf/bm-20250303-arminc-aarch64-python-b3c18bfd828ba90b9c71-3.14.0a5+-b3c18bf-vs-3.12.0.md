# Results vs. 3.12.0

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: linux-aarch64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 290 ms: 1.06x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                     |
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 857 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 455 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 878 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 363 ms: 1.59x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.57x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                    |
| nbody          | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| xml_etree_generate   | 112 ms                                                                | 108 ms: 1.04x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 77.5 ms: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 381 us: 1.04x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.5 us: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                    |
| genshi_xml     | 60.6 ms                                                               | 59.1 ms: 1.03x faster                                                    |
| mako           | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                     |
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 857 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 455 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 878 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 363 ms: 1.59x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 653 ms: 1.40x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                     |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.1 ms: 1.24x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                    |
| go                         | 157 ms                                                                | 134 ms: 1.18x faster                                                     |
| pylint                     | 355 ms                                                                | 306 ms: 1.16x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                    |
| raytrace                   | 353 ms                                                                | 307 ms: 1.15x faster                                                     |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| async_generators           | 491 ms                                                                | 431 ms: 1.14x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                    |
| spectral_norm              | 131 ms                                                                | 115 ms: 1.14x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 139 ms: 1.13x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.77 us: 1.13x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.47 us: 1.12x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                                     |
| sympy_str                  | 280 ms                                                                | 255 ms: 1.10x faster                                                     |
| float                      | 92.1 ms                                                               | 84.4 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.78 ms: 1.09x faster                                                    |
| chaos                      | 71.4 ms                                                               | 65.6 ms: 1.09x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.36 ms: 1.08x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 57.4 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.6 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                     |
| 2to3                       | 308 ms                                                                | 290 ms: 1.06x faster                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.29 sec: 1.04x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                     |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.03x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 59.1 ms: 1.03x faster                                                    |
| richards_super             | 58.5 ms                                                               | 57.1 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 895 ms: 1.02x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 77.5 ms: 1.02x faster                                                    |
| richards                   | 50.9 ms                                                               | 50.2 ms: 1.02x faster                                                    |
| pyflate                    | 559 ms                                                                | 554 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                                   |
| hexiom                     | 6.98 ms                                                               | 6.93 ms: 1.01x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.01x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 381 us: 1.04x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 190 us: 1.05x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                    |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.40 ms: 1.11x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.5 us: 1.12x slower                                                    |
| nbody                      | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| python_startup             | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.49 ms: 1.48x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.49 ms: 1.82x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.45 sec: 630.30x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (16): sympy_integrate, django_template, scimark_fft, sqlglot_optimize, crypto_pyaes, scimark_sor, thrift, nqueens, scimark_sparse_mat_mult, sympy_expand, sqlglot_normalize, meteor_contest, bench_thread_pool, asyncio_websockets, pidigits, logging_silent
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250303-3.14.0a5+-b3c18bf/bm-20250303-arminc-aarch64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x