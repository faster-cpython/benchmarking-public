# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.014x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                              | 290 ms: 1.02x faster                                                                                                      |
| html5lib       | 65.1 ms                                                                                                             | 59.3 ms: 1.10x faster                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x faster                                                                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 449 ms                                                                                                              | 416 ms: 1.08x faster                                                                                                      |
| coroutines                 | 29.8 ms                                                                                                             | 28.2 ms: 1.06x faster                                                                                                     |
| async_tree_none_tg         | 368 ms                                                                                                              | 362 ms: 1.02x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 647 ms                                                                                                              | 707 ms: 1.09x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                              | 728 ms: 1.10x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (8): async_tree_none, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_io, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 87.7 ms                                                                                                             | 85.6 ms: 1.02x faster                                                                                                     |
| pidigits       | 237 ms                                                                                                              | 293 ms: 1.24x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.95 ms                                                                                                             | 4.12 ms: 1.04x slower                                                                                                     |
| regex_v8       | 27.9 ms                                                                                                             | 30.6 ms: 1.10x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.60 us                                                                                                             | 5.77 us: 1.14x faster                                                                                                     |
| xml_etree_generate   | 115 ms                                                                                                              | 104 ms: 1.11x faster                                                                                                      |
| pickle_dict          | 38.7 us                                                                                                             | 35.5 us: 1.09x faster                                                                                                     |
| xml_etree_process    | 80.1 ms                                                                                                             | 74.7 ms: 1.07x faster                                                                                                     |
| pickle_list          | 5.74 us                                                                                                             | 5.35 us: 1.07x faster                                                                                                     |
| pickle_pure_python   | 397 us                                                                                                              | 374 us: 1.06x faster                                                                                                      |
| unpickle_pure_python | 273 us                                                                                                              | 259 us: 1.05x faster                                                                                                      |
| tomli_loads          | 2.46 sec                                                                                                            | 2.35 sec: 1.05x faster                                                                                                    |
| unpickle             | 17.9 us                                                                                                             | 17.3 us: 1.04x faster                                                                                                     |
| json_loads           | 34.3 us                                                                                                             | 33.2 us: 1.03x faster                                                                                                     |
| xml_etree_iterparse  | 141 ms                                                                                                              | 150 ms: 1.07x slower                                                                                                      |
| xml_etree_parse      | 174 ms                                                                                                              | 204 ms: 1.17x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (2): pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 16.3 ms                                                                                                             | 16.1 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| django_template | 40.4 ms                                                                                                             | 38.4 ms: 1.05x faster                                                                                                     |
| genshi_xml      | 60.2 ms                                                                                                             | 58.6 ms: 1.03x faster                                                                                                     |
| mako            | 14.2 ms                                                                                                             | 14.0 ms: 1.01x faster                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.60 us                                                                                                             | 5.77 us: 1.14x faster                                                                                                     |
| logging_silent             | 129 ns                                                                                                              | 116 ns: 1.11x faster                                                                                                      |
| xml_etree_generate         | 115 ms                                                                                                              | 104 ms: 1.11x faster                                                                                                      |
| deepcopy_memo              | 39.3 us                                                                                                             | 35.5 us: 1.11x faster                                                                                                     |
| deepcopy                   | 342 us                                                                                                              | 310 us: 1.10x faster                                                                                                      |
| html5lib                   | 65.1 ms                                                                                                             | 59.3 ms: 1.10x faster                                                                                                     |
| richards                   | 54.0 ms                                                                                                             | 49.5 ms: 1.09x faster                                                                                                     |
| scimark_monte_carlo        | 84.1 ms                                                                                                             | 77.2 ms: 1.09x faster                                                                                                     |
| pickle_dict                | 38.7 us                                                                                                             | 35.5 us: 1.09x faster                                                                                                     |
| scimark_fft                | 429 ms                                                                                                              | 395 ms: 1.09x faster                                                                                                      |
| scimark_sparse_mat_mult    | 6.85 ms                                                                                                             | 6.31 ms: 1.08x faster                                                                                                     |
| async_generators           | 449 ms                                                                                                              | 416 ms: 1.08x faster                                                                                                      |
| pyflate                    | 572 ms                                                                                                              | 530 ms: 1.08x faster                                                                                                      |
| deepcopy_reduce            | 3.59 us                                                                                                             | 3.34 us: 1.08x faster                                                                                                     |
| xml_etree_process          | 80.1 ms                                                                                                             | 74.7 ms: 1.07x faster                                                                                                     |
| pickle_list                | 5.74 us                                                                                                             | 5.35 us: 1.07x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.81 ms                                                                                                             | 1.70 ms: 1.07x faster                                                                                                     |
| pathlib                    | 22.7 ms                                                                                                             | 21.3 ms: 1.07x faster                                                                                                     |
| thrift                     | 967 us                                                                                                              | 910 us: 1.06x faster                                                                                                      |
| pprint_safe_repr           | 965 ms                                                                                                              | 908 ms: 1.06x faster                                                                                                      |
| pickle_pure_python         | 397 us                                                                                                              | 374 us: 1.06x faster                                                                                                      |
| richards_super             | 59.4 ms                                                                                                             | 56.0 ms: 1.06x faster                                                                                                     |
| pprint_pformat             | 1.97 sec                                                                                                            | 1.86 sec: 1.06x faster                                                                                                    |
| coroutines                 | 29.8 ms                                                                                                             | 28.2 ms: 1.06x faster                                                                                                     |
| django_template            | 40.4 ms                                                                                                             | 38.4 ms: 1.05x faster                                                                                                     |
| unpickle_pure_python       | 273 us                                                                                                              | 259 us: 1.05x faster                                                                                                      |
| pylint                     | 317 ms                                                                                                              | 301 ms: 1.05x faster                                                                                                      |
| bpe_tokeniser              | 5.64 sec                                                                                                            | 5.37 sec: 1.05x faster                                                                                                    |
| bench_thread_pool          | 1.35 ms                                                                                                             | 1.29 ms: 1.05x faster                                                                                                     |
| tomli_loads                | 2.46 sec                                                                                                            | 2.35 sec: 1.05x faster                                                                                                    |
| sqlglot_v2_parse           | 1.44 ms                                                                                                             | 1.38 ms: 1.04x faster                                                                                                     |
| mdp                        | 3.32 sec                                                                                                            | 3.19 sec: 1.04x faster                                                                                                    |
| unpickle                   | 17.9 us                                                                                                             | 17.3 us: 1.04x faster                                                                                                     |
| create_gc_cycles           | 3.82 ms                                                                                                             | 3.68 ms: 1.04x faster                                                                                                     |
| logging_format             | 7.75 us                                                                                                             | 7.50 us: 1.03x faster                                                                                                     |
| json_loads                 | 34.3 us                                                                                                             | 33.2 us: 1.03x faster                                                                                                     |
| sphinx                     | 1.16 sec                                                                                                            | 1.12 sec: 1.03x faster                                                                                                    |
| coverage                   | 98.6 ms                                                                                                             | 95.7 ms: 1.03x faster                                                                                                     |
| nqueens                    | 102 ms                                                                                                              | 99.2 ms: 1.03x faster                                                                                                     |
| genshi_xml                 | 60.2 ms                                                                                                             | 58.6 ms: 1.03x faster                                                                                                     |
| gc_traversal               | 6.68 ms                                                                                                             | 6.51 ms: 1.03x faster                                                                                                     |
| float                      | 87.7 ms                                                                                                             | 85.6 ms: 1.02x faster                                                                                                     |
| dulwich_log                | 51.8 ms                                                                                                             | 50.6 ms: 1.02x faster                                                                                                     |
| pycparser                  | 1.28 sec                                                                                                            | 1.25 sec: 1.02x faster                                                                                                    |
| logging_simple             | 7.05 us                                                                                                             | 6.89 us: 1.02x faster                                                                                                     |
| 2to3                       | 296 ms                                                                                                              | 290 ms: 1.02x faster                                                                                                      |
| async_tree_none_tg         | 368 ms                                                                                                              | 362 ms: 1.02x faster                                                                                                      |
| python_startup             | 16.3 ms                                                                                                             | 16.1 ms: 1.01x faster                                                                                                     |
| mako                       | 14.2 ms                                                                                                             | 14.0 ms: 1.01x faster                                                                                                     |
| sqlite_synth               | 3.76 us                                                                                                             | 3.91 us: 1.04x slower                                                                                                     |
| regex_effbot               | 3.95 ms                                                                                                             | 4.12 ms: 1.04x slower                                                                                                     |
| xml_etree_iterparse        | 141 ms                                                                                                              | 150 ms: 1.07x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 647 ms                                                                                                              | 707 ms: 1.09x slower                                                                                                      |
| regex_v8                   | 27.9 ms                                                                                                             | 30.6 ms: 1.10x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                              | 728 ms: 1.10x slower                                                                                                      |
| unpack_sequence            | 60.7 ns                                                                                                             | 69.7 ns: 1.15x slower                                                                                                     |
| xml_etree_parse            | 174 ms                                                                                                              | 204 ms: 1.17x slower                                                                                                      |
| pidigits                   | 237 ms                                                                                                              | 293 ms: 1.24x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (46): sympy_sum, sqlglot_v2_optimize, scimark_sor, many_optionals, genshi_text, comprehensions, regex_compile, chaos, spectral_norm, pickle, typing_runtime_protocols, regex_dna, scimark_lu, sqlglot_v2_normalize, generators, hexiom, nbody, raytrace, sympy_integrate, crypto_pyaes, sympy_expand, k_core, go, fannkuch, subparsers, async_tree_none, async_tree_io_tg, telco, async_tree_memoization_tg, asyncio_websockets, sqlalchemy_declarative, python_startup_no_site, docutils, shortest_path, async_tree_memoization, async_tree_io, asyncio_tcp_ssl, json, connected_components, deltablue, sympy_str, sqlalchemy_imperative, asyncio_tcp, json_dumps, meteor_contest, bench_mp_pool

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x