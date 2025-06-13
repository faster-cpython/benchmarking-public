# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-aarch64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.026x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                           |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                         |
| html5lib       | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                           |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                           |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.7 ms: 1.08x faster                                                          |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                           |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                          |
| regex_dna      | 254 ms                                                                | 220 ms: 1.16x faster                                                           |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.09x faster                                                           |
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                         |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                           |
| pickle_pure_python  | 365 us                                                                | 379 us: 1.04x slower                                                           |
| json_loads          | 30.7 us                                                               | 32.9 us: 1.07x slower                                                          |
| json_dumps          | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                          |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                          |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.62 sec: 2.10x faster                                                         |
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                           |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                           |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                           |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                          |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                          |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.23x faster                                                          |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                          |
| dulwich_log                | 62.0 ms                                                               | 53.2 ms: 1.17x faster                                                          |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.16x faster                                                           |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                           |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                                          |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                          |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                           |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                           |
| async_generators           | 491 ms                                                                | 452 ms: 1.08x faster                                                           |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                           |
| float                      | 92.1 ms                                                               | 85.7 ms: 1.08x faster                                                          |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                         |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                           |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                          |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                                           |
| pyflate                    | 559 ms                                                                | 535 ms: 1.04x faster                                                           |
| html5lib                   | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                                          |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                                          |
| logging_format             | 8.34 us                                                               | 8.10 us: 1.03x faster                                                          |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                           |
| meteor_contest             | 112 ms                                                                | 109 ms: 1.03x faster                                                           |
| logging_simple             | 7.63 us                                                               | 7.45 us: 1.02x faster                                                          |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                         |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                         |
| richards_super             | 58.5 ms                                                               | 58.2 ms: 1.01x faster                                                          |
| scimark_lu                 | 146 ms                                                                | 147 ms: 1.01x slower                                                           |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                           |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                           |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                          |
| sympy_expand               | 454 ms                                                                | 469 ms: 1.03x slower                                                           |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.04x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 379 us: 1.04x slower                                                           |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.04x slower                                                          |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 2.02 sec: 1.07x slower                                                         |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                          |
| pprint_safe_repr           | 916 ms                                                                | 983 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.08x slower                                                           |
| fannkuch                   | 443 ms                                                                | 483 ms: 1.09x slower                                                           |
| telco                      | 8.51 ms                                                               | 9.32 ms: 1.10x slower                                                          |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.92 ms: 1.12x slower                                                          |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                           |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                          |
| gc_traversal               | 4.40 ms                                                               | 7.02 ms: 1.60x slower                                                          |
| create_gc_cycles           | 1.92 ms                                                               | 3.97 ms: 2.07x slower                                                          |
| logging_silent             | 127 ns                                                                | 634 ns: 5.00x slower                                                           |
| coverage                   | 87.3 ms                                                               | 544 ms: 6.23x slower                                                           |
| thrift                     | 937 us                                                                | 193 ms: 206.54x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                   |

Benchmark hidden because not significant (15): crypto_pyaes, django_template, regex_v8, scimark_sor, nqueens, deltablue, hexiom, xml_etree_generate, genshi_xml, sqlite_synth, xml_etree_process, genshi_text, unpickle_pure_python, coroutines, richards
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x