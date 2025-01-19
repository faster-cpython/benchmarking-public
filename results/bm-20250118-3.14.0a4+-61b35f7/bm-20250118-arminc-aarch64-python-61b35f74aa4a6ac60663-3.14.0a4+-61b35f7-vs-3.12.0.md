# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.044x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 897 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 678 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.33x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.7 ms: 1.06x faster                                                    |
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 33.2 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse    | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| pickle_dict        | 37.3 us                                                               | 39.6 us: 1.06x slower                                                    |
| pickle_pure_python | 365 us                                                                | 393 us: 1.08x slower                                                     |
| unpickle_list      | 6.17 us                                                               | 6.65 us: 1.08x slower                                                    |
| json_loads         | 30.7 us                                                               | 33.8 us: 1.10x slower                                                    |
| pickle_list        | 5.25 us                                                               | 6.01 us: 1.14x slower                                                    |
| pickle             | 13.4 us                                                               | 16.0 us: 1.19x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 15.4 ms: 1.25x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (6): unpickle, xml_etree_iterparse, tomli_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.15 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| mako            | 12.9 ms                                                               | 14.6 ms: 1.13x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 385 ms: 1.62x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 897 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 678 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.33x faster                                                     |
| deepcopy                   | 446 us                                                                | 349 us: 1.28x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.0 us: 1.21x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.1 ms: 1.21x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.0 us: 1.15x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.55 us: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.12x faster                                                    |
| go                         | 157 ms                                                                | 140 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                     |
| pylint                     | 355 ms                                                                | 318 ms: 1.12x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.99 us: 1.09x faster                                                    |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                     |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| float                      | 92.1 ms                                                               | 86.7 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                     |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 84.4 ms: 1.03x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 99.7 ms: 1.00x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                   |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 947 ms: 1.03x slower                                                     |
| sympy_expand               | 454 ms                                                                | 471 ms: 1.04x slower                                                     |
| json                       | 5.54 ms                                                               | 5.80 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.7 ms: 1.05x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 39.6 us: 1.06x slower                                                    |
| thrift                     | 937 us                                                                | 1.00 ms: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.65 us: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.55 ms: 1.08x slower                                                    |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                                     |
| fannkuch                   | 443 ms                                                                | 484 ms: 1.09x slower                                                     |
| logging_silent             | 127 ns                                                                | 139 ns: 1.09x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.15 ms: 1.09x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.13 us: 1.10x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.8 us: 1.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.53 ms: 1.12x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.6 ms: 1.13x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.14x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.01 us: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.2 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.0 us: 1.19x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 15.4 ms: 1.25x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.96 ms: 1.58x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.61 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.08 sec: 1003.94x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (28): sympy_str, unpickle, xml_etree_iterparse, genshi_text, dulwich_log, tomli_loads, sqlglot_parse, 2to3, scimark_fft, scimark_monte_carlo, mdp, sympy_integrate, scimark_sor, asyncio_tcp, docutils, regex_dna, pyflate, coroutines, genshi_xml, richards, sqlglot_transpile, bench_thread_pool, xml_etree_generate, unpickle_pure_python, sqlglot_optimize, sqlglot_normalize, xml_etree_process, scimark_sparse_mat_mult
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x