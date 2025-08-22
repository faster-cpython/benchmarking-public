# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.041x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                          |
| html5lib       | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 380 ms: 1.64x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 874 ms: 1.62x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.52x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 661 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 75.9 ms: 1.21x faster                                                           |
| nbody          | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.80 ms: 1.22x faster                                                           |
| regex_dna      | 254 ms                                                                | 218 ms: 1.17x faster                                                            |
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                            |
| regex_v8       | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.22 sec: 1.17x faster                                                          |
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.06x faster                                                            |
| unpickle_pure_python | 260 us                                                                | 247 us: 1.05x faster                                                            |
| xml_etree_process    | 79.0 ms                                                               | 75.8 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                            |
| json_dumps           | 12.3 ms                                                               | 11.9 ms: 1.03x faster                                                           |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                           |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                           |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.63 sec: 2.09x faster                                                          |
| async_tree_none            | 624 ms                                                                | 380 ms: 1.64x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 874 ms: 1.62x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.52x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 661 ms: 1.38x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 36.6 us: 1.36x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                            |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                            |
| richards                   | 50.9 ms                                                               | 41.7 ms: 1.22x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.80 ms: 1.22x faster                                                           |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.22x faster                                                           |
| float                      | 92.1 ms                                                               | 75.9 ms: 1.21x faster                                                           |
| richards_super             | 58.5 ms                                                               | 49.3 ms: 1.19x faster                                                           |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.17x faster                                                            |
| tomli_loads                | 2.59 sec                                                              | 2.22 sec: 1.17x faster                                                          |
| spectral_norm              | 131 ms                                                                | 113 ms: 1.16x faster                                                            |
| logging_format             | 8.34 us                                                               | 7.26 us: 1.15x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.2 us: 1.14x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                           |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                            |
| logging_simple             | 7.63 us                                                               | 6.78 us: 1.13x faster                                                           |
| deltablue                  | 4.12 ms                                                               | 3.68 ms: 1.12x faster                                                           |
| dulwich_log                | 62.0 ms                                                               | 55.4 ms: 1.12x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                           |
| pyflate                    | 559 ms                                                                | 506 ms: 1.11x faster                                                            |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                            |
| pylint                     | 355 ms                                                                | 324 ms: 1.10x faster                                                            |
| scimark_sor                | 150 ms                                                                | 139 ms: 1.08x faster                                                            |
| chaos                      | 71.4 ms                                                               | 66.5 ms: 1.07x faster                                                           |
| scimark_fft                | 418 ms                                                                | 390 ms: 1.07x faster                                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.4 ms: 1.07x faster                                                           |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.06x faster                                                            |
| regex_v8                   | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                                           |
| go                         | 157 ms                                                                | 148 ms: 1.06x faster                                                            |
| html5lib                   | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 260 us                                                                | 247 us: 1.05x faster                                                            |
| xml_etree_process          | 79.0 ms                                                               | 75.8 ms: 1.04x faster                                                           |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                            |
| json_dumps                 | 12.3 ms                                                               | 11.9 ms: 1.03x faster                                                           |
| sympy_str                  | 280 ms                                                                | 272 ms: 1.03x faster                                                            |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.03x faster                                                            |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                           |
| async_generators           | 491 ms                                                                | 481 ms: 1.02x faster                                                            |
| nbody                      | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                            |
| json                       | 5.54 ms                                                               | 5.63 ms: 1.02x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                            |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                          |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                            |
| coroutines                 | 29.0 ms                                                               | 29.9 ms: 1.03x slower                                                           |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                                           |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                            |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                           |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                          |
| sympy_expand               | 454 ms                                                                | 486 ms: 1.07x slower                                                            |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.97 ms: 1.13x slower                                                           |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                            |
| typing_runtime_protocols   | 181 us                                                                | 216 us: 1.19x slower                                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.25 sec: 1.20x slower                                                          |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.21x slower                                                          |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.73 ms: 1.94x slower                                                           |
| telco                      | 8.51 ms                                                               | 165 ms: 19.39x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                                    |

Benchmark hidden because not significant (11): xml_etree_generate, django_template, mako, 2to3, sqlite_synth, genshi_text, meteor_contest, crypto_pyaes, logging_silent, hexiom, thrift
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x