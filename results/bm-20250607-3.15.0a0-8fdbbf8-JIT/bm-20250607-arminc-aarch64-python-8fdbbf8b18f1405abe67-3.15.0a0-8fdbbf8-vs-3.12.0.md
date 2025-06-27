# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.040x faster
- HPT reliability: 98.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 62.7 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 901 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 669 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 663 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.6 ms: 1.10x faster                                                   |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| regex_dna      | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| json_loads          | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 393 us: 1.08x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| genshi_xml     | 60.6 ms                                                               | 63.1 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 479 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 901 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 669 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 663 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.4 ms: 1.16x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.3 us: 1.14x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.4 ms: 1.14x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 55.3 ms: 1.12x faster                                                   |
| pylint                     | 355 ms                                                                | 318 ms: 1.11x faster                                                    |
| richards                   | 50.9 ms                                                               | 45.8 ms: 1.11x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                  |
| float                      | 92.1 ms                                                               | 83.6 ms: 1.10x faster                                                   |
| regex_dna                  | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                    |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.4 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.7 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 69.2 ms: 1.03x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.55 us: 1.01x faster                                                   |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.01x slower                                                   |
| logging_format             | 8.34 us                                                               | 8.49 us: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| spectral_norm              | 131 ms                                                                | 134 ms: 1.03x slower                                                    |
| go                         | 157 ms                                                                | 162 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.0 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 63.1 ms: 1.04x slower                                                   |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 104 ms: 1.05x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 91.8 ms: 1.06x slower                                                   |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| sympy_expand               | 454 ms                                                                | 490 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.60 ms: 1.09x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| fannkuch                   | 443 ms                                                                | 488 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.98 ms: 1.13x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 120 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.56 sec: 1.36x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.37x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.84 ms: 2.00x slower                                                   |
| logging_silent             | 127 ns                                                                | 625 ns: 4.92x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (12): sympy_sum, unpickle_pure_python, scimark_sor, regex_v8, django_template, async_generators, xml_etree_generate, sympy_str, genshi_text, xml_etree_process, scimark_fft, scimark_lu
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 98.06% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x