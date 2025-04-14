# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 310 ms: 1.05x slower                                                                                                    |
| docutils       | 2.96 sec                                                                                                            | 3.17 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization | 465 ms                                                                                                              | 471 ms: 1.01x slower                                                                                                    |
| async_tree_io_tg       | 907 ms                                                                                                              | 919 ms: 1.01x slower                                                                                                    |
| async_generators       | 449 ms                                                                                                              | 478 ms: 1.06x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (10): coroutines, async_tree_io, asyncio_websockets, asyncio_tcp_ssl, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 87.7 ms                                                                                                             | 85.3 ms: 1.03x faster                                                                                                   |
| nbody          | 121 ms                                                                                                              | 129 ms: 1.07x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 245 ms                                                                                                              | 238 ms: 1.03x faster                                                                                                    |
| regex_v8       | 27.9 ms                                                                                                             | 28.1 ms: 1.01x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 115 ms                                                                                                              | 110 ms: 1.05x faster                                                                                                    |
| unpickle             | 17.9 us                                                                                                             | 17.4 us: 1.03x faster                                                                                                   |
| xml_etree_process    | 80.1 ms                                                                                                             | 78.5 ms: 1.02x faster                                                                                                   |
| json_loads           | 34.3 us                                                                                                             | 34.0 us: 1.01x faster                                                                                                   |
| unpickle_pure_python | 273 us                                                                                                              | 288 us: 1.06x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (9): pickle_list, pickle, unpickle_list, tomli_loads, pickle_dict, json_dumps, xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako           | 14.2 ms                                                                                                             | 13.7 ms: 1.03x faster                                                                                                   |
| genshi_xml     | 60.2 ms                                                                                                             | 62.8 ms: 1.04x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.00x slower                                                                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 2.75 sec                                                                                                            | 814 ms: 3.37x faster                                                                                                    |
| richards_super           | 59.4 ms                                                                                                             | 55.3 ms: 1.07x faster                                                                                                   |
| xml_etree_generate       | 115 ms                                                                                                              | 110 ms: 1.05x faster                                                                                                    |
| deepcopy_memo            | 39.3 us                                                                                                             | 37.4 us: 1.05x faster                                                                                                   |
| create_gc_cycles         | 3.82 ms                                                                                                             | 3.65 ms: 1.04x faster                                                                                                   |
| mako                     | 14.2 ms                                                                                                             | 13.7 ms: 1.03x faster                                                                                                   |
| regex_dna                | 245 ms                                                                                                              | 238 ms: 1.03x faster                                                                                                    |
| float                    | 87.7 ms                                                                                                             | 85.3 ms: 1.03x faster                                                                                                   |
| thrift                   | 967 us                                                                                                              | 941 us: 1.03x faster                                                                                                    |
| unpickle                 | 17.9 us                                                                                                             | 17.4 us: 1.03x faster                                                                                                   |
| xml_etree_process        | 80.1 ms                                                                                                             | 78.5 ms: 1.02x faster                                                                                                   |
| logging_format           | 7.75 us                                                                                                             | 7.60 us: 1.02x faster                                                                                                   |
| logging_simple           | 7.05 us                                                                                                             | 6.92 us: 1.02x faster                                                                                                   |
| gc_traversal             | 6.68 ms                                                                                                             | 6.58 ms: 1.01x faster                                                                                                   |
| json_loads               | 34.3 us                                                                                                             | 34.0 us: 1.01x faster                                                                                                   |
| regex_v8                 | 27.9 ms                                                                                                             | 28.1 ms: 1.01x slower                                                                                                   |
| shortest_path            | 582 ms                                                                                                              | 587 ms: 1.01x slower                                                                                                    |
| async_tree_memoization   | 465 ms                                                                                                              | 471 ms: 1.01x slower                                                                                                    |
| async_tree_io_tg         | 907 ms                                                                                                              | 919 ms: 1.01x slower                                                                                                    |
| bpe_tokeniser            | 5.64 sec                                                                                                            | 5.73 sec: 1.02x slower                                                                                                  |
| k_core                   | 2.81 sec                                                                                                            | 2.88 sec: 1.02x slower                                                                                                  |
| deltablue                | 3.90 ms                                                                                                             | 4.01 ms: 1.03x slower                                                                                                   |
| pyflate                  | 572 ms                                                                                                              | 594 ms: 1.04x slower                                                                                                    |
| scimark_monte_carlo      | 84.1 ms                                                                                                             | 87.6 ms: 1.04x slower                                                                                                   |
| sqlalchemy_declarative   | 145 ms                                                                                                              | 151 ms: 1.04x slower                                                                                                    |
| genshi_xml               | 60.2 ms                                                                                                             | 62.8 ms: 1.04x slower                                                                                                   |
| 2to3                     | 296 ms                                                                                                              | 310 ms: 1.05x slower                                                                                                    |
| unpickle_pure_python     | 273 us                                                                                                              | 288 us: 1.06x slower                                                                                                    |
| sympy_integrate          | 20.8 ms                                                                                                             | 22.0 ms: 1.06x slower                                                                                                   |
| sympy_str                | 266 ms                                                                                                              | 283 ms: 1.06x slower                                                                                                    |
| async_generators         | 449 ms                                                                                                              | 478 ms: 1.06x slower                                                                                                    |
| deepcopy_reduce          | 3.59 us                                                                                                             | 3.83 us: 1.07x slower                                                                                                   |
| sympy_expand             | 467 ms                                                                                                              | 498 ms: 1.07x slower                                                                                                    |
| nbody                    | 121 ms                                                                                                              | 129 ms: 1.07x slower                                                                                                    |
| sqlalchemy_imperative    | 15.5 ms                                                                                                             | 16.7 ms: 1.07x slower                                                                                                   |
| sqlglot_v2_transpile     | 1.81 ms                                                                                                             | 1.95 ms: 1.07x slower                                                                                                   |
| docutils                 | 2.96 sec                                                                                                            | 3.17 sec: 1.07x slower                                                                                                  |
| fannkuch                 | 507 ms                                                                                                              | 551 ms: 1.09x slower                                                                                                    |
| nqueens                  | 102 ms                                                                                                              | 112 ms: 1.10x slower                                                                                                    |
| dulwich_log              | 51.8 ms                                                                                                             | 57.1 ms: 1.10x slower                                                                                                   |
| meteor_contest           | 113 ms                                                                                                              | 124 ms: 1.10x slower                                                                                                    |
| spectral_norm            | 121 ms                                                                                                              | 134 ms: 1.11x slower                                                                                                    |
| pycparser                | 1.28 sec                                                                                                            | 1.43 sec: 1.12x slower                                                                                                  |
| crypto_pyaes             | 90.0 ms                                                                                                             | 102 ms: 1.13x slower                                                                                                    |
| typing_runtime_protocols | 195 us                                                                                                              | 222 us: 1.14x slower                                                                                                    |
| sqlglot_v2_parse         | 1.44 ms                                                                                                             | 1.65 ms: 1.14x slower                                                                                                   |
| hexiom                   | 7.41 ms                                                                                                             | 8.57 ms: 1.16x slower                                                                                                   |
| comprehensions           | 21.2 us                                                                                                             | 26.0 us: 1.23x slower                                                                                                   |
| pprint_safe_repr         | 965 ms                                                                                                              | 1.25 sec: 1.29x slower                                                                                                  |
| pprint_pformat           | 1.97 sec                                                                                                            | 2.58 sec: 1.31x slower                                                                                                  |
| go                       | 137 ms                                                                                                              | 180 ms: 1.31x slower                                                                                                    |
| unpack_sequence          | 60.7 ns                                                                                                             | 85.7 ns: 1.41x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (52): richards, coroutines, html5lib, pickle_list, scimark_sor, pickle, bench_thread_pool, regex_effbot, pathlib, unpickle_list, django_template, sqlite_synth, coverage, python_startup, async_tree_io, tomli_loads, sympy_sum, asyncio_websockets, connected_components, python_startup_no_site, regex_compile, asyncio_tcp_ssl, async_tree_none, pidigits, genshi_text, pickle_dict, mdp, json_dumps, async_tree_cpu_io_mixed, async_tree_memoization_tg, xml_etree_iterparse, async_tree_none_tg, sqlglot_v2_optimize, chaos, sphinx, generators, scimark_lu, scimark_fft, json, async_tree_cpu_io_mixed_tg, xml_etree_parse, scimark_sparse_mat_mult, asyncio_tcp, deepcopy, pickle_pure_python, sqlglot_v2_normalize, logging_silent, many_optionals, raytrace, pylint, subparsers, telco

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x