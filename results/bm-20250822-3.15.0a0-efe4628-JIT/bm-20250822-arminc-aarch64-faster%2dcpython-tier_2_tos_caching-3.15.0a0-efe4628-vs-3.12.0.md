# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.032x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                          |
| html5lib       | 65.1 ms                                                               | 61.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                            |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 76.3 ms: 1.21x faster                                                           |
| nbody          | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| pidigits       | 233 ms                                                                | 238 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                           |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                            |
| regex_dna      | 254 ms                                                                | 226 ms: 1.12x faster                                                            |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.24 sec: 1.16x faster                                                          |
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.07x faster                                                            |
| unpickle_pure_python | 260 us                                                                | 249 us: 1.04x faster                                                            |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.04x faster                                                            |
| xml_etree_generate   | 112 ms                                                                | 108 ms: 1.04x faster                                                            |
| xml_etree_process    | 79.0 ms                                                               | 76.3 ms: 1.04x faster                                                           |
| json_dumps           | 12.3 ms                                                               | 11.9 ms: 1.03x faster                                                           |
| pickle_pure_python   | 365 us                                                                | 389 us: 1.06x slower                                                            |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                           |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.6 ms: 1.05x faster                                                           |
| genshi_text     | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                           |
| mako            | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                           |
| genshi_xml      | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.05x faster                                                          |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                            |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 36.8 us: 1.35x faster                                                           |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                            |
| float                      | 92.1 ms                                                               | 76.3 ms: 1.21x faster                                                           |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                           |
| spectral_norm              | 131 ms                                                                | 111 ms: 1.18x faster                                                            |
| richards_super             | 58.5 ms                                                               | 49.9 ms: 1.17x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.24 sec: 1.16x faster                                                          |
| logging_simple             | 7.63 us                                                               | 6.63 us: 1.15x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.1 us: 1.15x faster                                                           |
| richards                   | 50.9 ms                                                               | 44.6 ms: 1.14x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.32 us: 1.14x faster                                                           |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                            |
| regex_dna                  | 254 ms                                                                | 226 ms: 1.12x faster                                                            |
| dulwich_log                | 62.0 ms                                                               | 55.6 ms: 1.11x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.70 us: 1.11x faster                                                           |
| scimark_fft                | 418 ms                                                                | 382 ms: 1.10x faster                                                            |
| pylint                     | 355 ms                                                                | 328 ms: 1.08x faster                                                            |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                                           |
| pyflate                    | 559 ms                                                                | 524 ms: 1.07x faster                                                            |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                            |
| go                         | 157 ms                                                                | 147 ms: 1.07x faster                                                            |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                           |
| html5lib                   | 65.1 ms                                                               | 61.7 ms: 1.06x faster                                                           |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                           |
| django_template            | 40.7 ms                                                               | 38.6 ms: 1.05x faster                                                           |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.4 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 260 us                                                                | 249 us: 1.04x faster                                                            |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                            |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                           |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.04x faster                                                            |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                            |
| xml_etree_process          | 79.0 ms                                                               | 76.3 ms: 1.04x faster                                                           |
| sqlite_synth               | 3.77 us                                                               | 3.65 us: 1.03x faster                                                           |
| json_dumps                 | 12.3 ms                                                               | 11.9 ms: 1.03x faster                                                           |
| genshi_text                | 27.4 ms                                                               | 27.0 ms: 1.02x faster                                                           |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                           |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                                           |
| nbody                      | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                            |
| pidigits                   | 233 ms                                                                | 238 ms: 1.03x slower                                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                           |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                            |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                          |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                           |
| crypto_pyaes               | 86.6 ms                                                               | 90.3 ms: 1.04x slower                                                           |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                            |
| thrift                     | 937 us                                                                | 989 us: 1.06x slower                                                            |
| genshi_xml                 | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 389 us: 1.06x slower                                                            |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                                          |
| coroutines                 | 29.0 ms                                                               | 31.1 ms: 1.07x slower                                                           |
| sympy_expand               | 454 ms                                                                | 486 ms: 1.07x slower                                                            |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                            |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                          |
| pprint_safe_repr           | 916 ms                                                                | 1.13 sec: 1.23x slower                                                          |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.96 ms: 1.58x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.86 ms: 2.01x slower                                                           |
| telco                      | 8.51 ms                                                               | 166 ms: 19.46x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (7): sympy_integrate, sympy_str, 2to3, async_generators, meteor_contest, nqueens, scimark_lu
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x