# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.050x faster
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                            |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                          |
| html5lib       | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                            |
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 910 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 77.3 ms: 1.19x faster                                                           |
| nbody          | 105 ms                                                                | 105 ms: 1.01x slower                                                            |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                           |
| regex_dna      | 254 ms                                                                | 216 ms: 1.17x faster                                                            |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                            |
| regex_v8       | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.29 sec: 1.13x faster                                                          |
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                            |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                            |
| xml_etree_process   | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                                           |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                           |
| pickle_pure_python  | 365 us                                                                | 391 us: 1.07x slower                                                            |
| json_dumps          | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.58 ms: 1.03x slower                                                           |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.3 ms: 1.00x faster                                                           |
| mako           | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                           |
| genshi_xml     | 60.6 ms                                                               | 64.3 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                            |
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 910 ms: 1.55x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 479 ms: 1.55x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                            |
| deepcopy                   | 446 us                                                                | 339 us: 1.32x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                           |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.23x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                           |
| float                      | 92.1 ms                                                               | 77.3 ms: 1.19x faster                                                           |
| regex_dna                  | 254 ms                                                                | 216 ms: 1.17x faster                                                            |
| dulwich_log                | 62.0 ms                                                               | 53.9 ms: 1.15x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.3 us: 1.14x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.29 sec: 1.13x faster                                                          |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                            |
| richards                   | 50.9 ms                                                               | 45.6 ms: 1.12x faster                                                           |
| richards_super             | 58.5 ms                                                               | 52.4 ms: 1.12x faster                                                           |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.69 us: 1.11x faster                                                           |
| deltablue                  | 4.12 ms                                                               | 3.73 ms: 1.10x faster                                                           |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                            |
| pylint                     | 355 ms                                                                | 325 ms: 1.09x faster                                                            |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                           |
| pyflate                    | 559 ms                                                                | 522 ms: 1.07x faster                                                            |
| scimark_fft                | 418 ms                                                                | 391 ms: 1.07x faster                                                            |
| raytrace                   | 353 ms                                                                | 332 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                            |
| scimark_sor                | 150 ms                                                                | 141 ms: 1.06x faster                                                            |
| regex_v8                   | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                           |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                           |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                                            |
| xml_etree_process          | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                                           |
| html5lib                   | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                           |
| genshi_text                | 27.4 ms                                                               | 27.3 ms: 1.00x faster                                                           |
| nqueens                    | 99.2 ms                                                               | 99.8 ms: 1.01x slower                                                           |
| nbody                      | 105 ms                                                                | 105 ms: 1.01x slower                                                            |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                            |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                            |
| json                       | 5.54 ms                                                               | 5.63 ms: 1.02x slower                                                           |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.58 ms: 1.03x slower                                                           |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                            |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                           |
| logging_simple             | 7.63 us                                                               | 7.85 us: 1.03x slower                                                           |
| logging_format             | 8.34 us                                                               | 8.59 us: 1.03x slower                                                           |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 90.0 ms: 1.04x slower                                                           |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                           |
| hexiom                     | 6.98 ms                                                               | 7.40 ms: 1.06x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 64.3 ms: 1.06x slower                                                           |
| thrift                     | 937 us                                                                | 1.00 ms: 1.07x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 391 us: 1.07x slower                                                            |
| scimark_lu                 | 146 ms                                                                | 156 ms: 1.07x slower                                                            |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                            |
| sympy_expand               | 454 ms                                                                | 493 ms: 1.09x slower                                                            |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                          |
| telco                      | 8.51 ms                                                               | 9.58 ms: 1.13x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.02 ms: 1.13x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                            |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                            |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                           |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.38x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 2.60 sec: 1.38x slower                                                          |
| gc_traversal               | 4.40 ms                                                               | 6.98 ms: 1.59x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.69 ms: 1.92x slower                                                           |
| logging_silent             | 127 ns                                                                | 630 ns: 4.96x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (9): sympy_sum, unpickle_pure_python, xml_etree_generate, chaos, sympy_str, sqlite_synth, go, django_template, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.59% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x