# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.024x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                                                            | 251 ms: 1.02x faster                                                                                                    |
| docutils       | 2.60 sec                                                                                                          | 2.56 sec: 1.02x faster                                                                                                  |
| html5lib       | 62.8 ms                                                                                                           | 61.7 ms: 1.02x faster                                                                                                   |
| sphinx         | 1.01 sec                                                                                                          | 982 ms: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 23.4 ms                                                                                                           | 22.2 ms: 1.06x faster                                                                                                   |
| async_tree_memoization     | 314 ms                                                                                                            | 305 ms: 1.03x faster                                                                                                    |
| async_tree_none            | 258 ms                                                                                                            | 252 ms: 1.03x faster                                                                                                    |
| async_generators           | 395 ms                                                                                                            | 385 ms: 1.02x faster                                                                                                    |
| async_tree_none_tg         | 249 ms                                                                                                            | 243 ms: 1.02x faster                                                                                                    |
| async_tree_memoization_tg  | 309 ms                                                                                                            | 303 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 613 ms                                                                                                            | 602 ms: 1.02x faster                                                                                                    |
| asyncio_tcp                | 476 ms                                                                                                            | 469 ms: 1.01x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                          | 1.78 sec: 1.00x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                                                            | 481 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 482 ms                                                                                                            | 496 ms: 1.03x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 99.0 ms                                                                                                           | 90.8 ms: 1.09x faster                                                                                                   |
| float          | 71.9 ms                                                                                                           | 69.8 ms: 1.03x faster                                                                                                   |
| pidigits       | 186 ms                                                                                                            | 202 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                                                                            | 186 ms: 1.14x faster                                                                                                    |
| regex_v8       | 23.6 ms                                                                                                           | 22.8 ms: 1.04x faster                                                                                                   |
| regex_effbot   | 3.10 ms                                                                                                           | 3.04 ms: 1.02x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.05x faster                                                                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 5.30 us                                                                                                           | 4.52 us: 1.17x faster                                                                                                   |
| json_loads          | 29.8 us                                                                                                           | 28.8 us: 1.04x faster                                                                                                   |
| tomli_loads         | 1.95 sec                                                                                                          | 1.92 sec: 1.02x faster                                                                                                  |
| xml_etree_process   | 59.1 ms                                                                                                           | 58.3 ms: 1.01x faster                                                                                                   |
| pickle_dict         | 34.3 us                                                                                                           | 33.9 us: 1.01x faster                                                                                                   |
| pickle_pure_python  | 315 us                                                                                                            | 312 us: 1.01x faster                                                                                                    |
| pickle_list         | 5.38 us                                                                                                           | 5.34 us: 1.01x faster                                                                                                   |
| xml_etree_generate  | 85.6 ms                                                                                                           | 86.0 ms: 1.00x slower                                                                                                   |
| xml_etree_iterparse | 98.4 ms                                                                                                           | 101 ms: 1.03x slower                                                                                                    |
| pickle              | 13.0 us                                                                                                           | 13.5 us: 1.04x slower                                                                                                   |
| json_dumps          | 11.5 ms                                                                                                           | 12.2 ms: 1.06x slower                                                                                                   |
| xml_etree_parse     | 141 ms                                                                                                            | 159 ms: 1.13x slower                                                                                                    |
| Geometric mean      | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (2): unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                           | 12.9 ms: 1.01x faster                                                                                                   |
| python_startup_no_site | 8.17 ms                                                                                                           | 8.11 ms: 1.01x faster                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                                                           | 20.6 ms: 1.03x faster                                                                                                   |
| genshi_xml      | 49.0 ms                                                                                                           | 47.8 ms: 1.03x faster                                                                                                   |
| django_template | 31.3 ms                                                                                                           | 30.8 ms: 1.02x faster                                                                                                   |
| mako            | 11.4 ms                                                                                                           | 11.9 ms: 1.04x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.01x faster                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.75 ms                                                                                                           | 3.95 ms: 1.20x faster                                                                                                   |
| scimark_fft                | 352 ms                                                                                                            | 300 ms: 1.17x faster                                                                                                    |
| unpickle_list              | 5.30 us                                                                                                           | 4.52 us: 1.17x faster                                                                                                   |
| regex_dna                  | 212 ms                                                                                                            | 186 ms: 1.14x faster                                                                                                    |
| coverage                   | 91.6 ms                                                                                                           | 80.8 ms: 1.13x faster                                                                                                   |
| pathlib                    | 16.9 ms                                                                                                           | 15.0 ms: 1.13x faster                                                                                                   |
| spectral_norm              | 96.4 ms                                                                                                           | 85.8 ms: 1.12x faster                                                                                                   |
| scimark_lu                 | 116 ms                                                                                                            | 104 ms: 1.12x faster                                                                                                    |
| scimark_monte_carlo        | 67.5 ms                                                                                                           | 61.6 ms: 1.10x faster                                                                                                   |
| nbody                      | 99.0 ms                                                                                                           | 90.8 ms: 1.09x faster                                                                                                   |
| scimark_sor                | 117 ms                                                                                                            | 108 ms: 1.09x faster                                                                                                    |
| pyflate                    | 447 ms                                                                                                            | 415 ms: 1.08x faster                                                                                                    |
| deepcopy                   | 260 us                                                                                                            | 244 us: 1.06x faster                                                                                                    |
| typing_runtime_protocols   | 163 us                                                                                                            | 154 us: 1.06x faster                                                                                                    |
| telco                      | 7.94 ms                                                                                                           | 7.47 ms: 1.06x faster                                                                                                   |
| coroutines                 | 23.4 ms                                                                                                           | 22.2 ms: 1.06x faster                                                                                                   |
| chaos                      | 58.8 ms                                                                                                           | 55.7 ms: 1.05x faster                                                                                                   |
| nqueens                    | 83.6 ms                                                                                                           | 79.4 ms: 1.05x faster                                                                                                   |
| richards                   | 43.9 ms                                                                                                           | 41.7 ms: 1.05x faster                                                                                                   |
| richards_super             | 49.9 ms                                                                                                           | 47.7 ms: 1.05x faster                                                                                                   |
| sqlglot_v2_parse           | 1.28 ms                                                                                                           | 1.22 ms: 1.04x faster                                                                                                   |
| sqlglot_v2_transpile       | 1.59 ms                                                                                                           | 1.52 ms: 1.04x faster                                                                                                   |
| sqlite_synth               | 2.77 us                                                                                                           | 2.67 us: 1.04x faster                                                                                                   |
| deepcopy_reduce            | 2.68 us                                                                                                           | 2.58 us: 1.04x faster                                                                                                   |
| json_loads                 | 29.8 us                                                                                                           | 28.8 us: 1.04x faster                                                                                                   |
| regex_v8                   | 23.6 ms                                                                                                           | 22.8 ms: 1.04x faster                                                                                                   |
| bench_thread_pool          | 869 us                                                                                                            | 839 us: 1.04x faster                                                                                                    |
| sqlglot_v2_normalize       | 107 ms                                                                                                            | 104 ms: 1.04x faster                                                                                                    |
| logging_silent             | 93.7 ns                                                                                                           | 90.4 ns: 1.04x faster                                                                                                   |
| sqlalchemy_imperative      | 16.6 ms                                                                                                           | 16.1 ms: 1.04x faster                                                                                                   |
| hexiom                     | 6.21 ms                                                                                                           | 6.00 ms: 1.03x faster                                                                                                   |
| genshi_text                | 21.3 ms                                                                                                           | 20.6 ms: 1.03x faster                                                                                                   |
| comprehensions             | 16.8 us                                                                                                           | 16.3 us: 1.03x faster                                                                                                   |
| bpe_tokeniser              | 4.62 sec                                                                                                          | 4.48 sec: 1.03x faster                                                                                                  |
| thrift                     | 775 us                                                                                                            | 751 us: 1.03x faster                                                                                                    |
| fannkuch                   | 422 ms                                                                                                            | 410 ms: 1.03x faster                                                                                                    |
| sphinx                     | 1.01 sec                                                                                                          | 982 ms: 1.03x faster                                                                                                    |
| float                      | 71.9 ms                                                                                                           | 69.8 ms: 1.03x faster                                                                                                   |
| sympy_integrate            | 19.4 ms                                                                                                           | 18.9 ms: 1.03x faster                                                                                                   |
| async_tree_memoization     | 314 ms                                                                                                            | 305 ms: 1.03x faster                                                                                                    |
| raytrace                   | 266 ms                                                                                                            | 258 ms: 1.03x faster                                                                                                    |
| sympy_expand               | 457 ms                                                                                                            | 445 ms: 1.03x faster                                                                                                    |
| sqlalchemy_declarative     | 130 ms                                                                                                            | 127 ms: 1.03x faster                                                                                                    |
| async_tree_none            | 258 ms                                                                                                            | 252 ms: 1.03x faster                                                                                                    |
| genshi_xml                 | 49.0 ms                                                                                                           | 47.8 ms: 1.03x faster                                                                                                   |
| many_optionals             | 947 us                                                                                                            | 924 us: 1.02x faster                                                                                                    |
| subparsers                 | 20.9 ms                                                                                                           | 20.4 ms: 1.02x faster                                                                                                   |
| async_generators           | 395 ms                                                                                                            | 385 ms: 1.02x faster                                                                                                    |
| async_tree_none_tg         | 249 ms                                                                                                            | 243 ms: 1.02x faster                                                                                                    |
| logging_format             | 6.18 us                                                                                                           | 6.04 us: 1.02x faster                                                                                                   |
| deepcopy_memo              | 29.6 us                                                                                                           | 28.9 us: 1.02x faster                                                                                                   |
| sympy_sum                  | 148 ms                                                                                                            | 145 ms: 1.02x faster                                                                                                    |
| async_tree_memoization_tg  | 309 ms                                                                                                            | 303 ms: 1.02x faster                                                                                                    |
| 2to3                       | 256 ms                                                                                                            | 251 ms: 1.02x faster                                                                                                    |
| sympy_str                  | 267 ms                                                                                                            | 262 ms: 1.02x faster                                                                                                    |
| crypto_pyaes               | 75.7 ms                                                                                                           | 74.3 ms: 1.02x faster                                                                                                   |
| json                       | 5.37 ms                                                                                                           | 5.26 ms: 1.02x faster                                                                                                   |
| docutils                   | 2.60 sec                                                                                                          | 2.56 sec: 1.02x faster                                                                                                  |
| async_tree_io              | 613 ms                                                                                                            | 602 ms: 1.02x faster                                                                                                    |
| regex_effbot               | 3.10 ms                                                                                                           | 3.04 ms: 1.02x faster                                                                                                   |
| bench_mp_pool              | 82.8 ms                                                                                                           | 81.4 ms: 1.02x faster                                                                                                   |
| html5lib                   | 62.8 ms                                                                                                           | 61.7 ms: 1.02x faster                                                                                                   |
| django_template            | 31.3 ms                                                                                                           | 30.8 ms: 1.02x faster                                                                                                   |
| tomli_loads                | 1.95 sec                                                                                                          | 1.92 sec: 1.02x faster                                                                                                  |
| sqlglot_v2_optimize        | 53.2 ms                                                                                                           | 52.3 ms: 1.02x faster                                                                                                   |
| dulwich_log                | 58.3 ms                                                                                                           | 57.4 ms: 1.02x faster                                                                                                   |
| deltablue                  | 3.09 ms                                                                                                           | 3.04 ms: 1.02x faster                                                                                                   |
| xml_etree_process          | 59.1 ms                                                                                                           | 58.3 ms: 1.01x faster                                                                                                   |
| asyncio_tcp                | 476 ms                                                                                                            | 469 ms: 1.01x faster                                                                                                    |
| python_startup             | 13.1 ms                                                                                                           | 12.9 ms: 1.01x faster                                                                                                   |
| pickle_dict                | 34.3 us                                                                                                           | 33.9 us: 1.01x faster                                                                                                   |
| pickle_pure_python         | 315 us                                                                                                            | 312 us: 1.01x faster                                                                                                    |
| logging_simple             | 5.53 us                                                                                                           | 5.48 us: 1.01x faster                                                                                                   |
| pickle_list                | 5.38 us                                                                                                           | 5.34 us: 1.01x faster                                                                                                   |
| python_startup_no_site     | 8.17 ms                                                                                                           | 8.11 ms: 1.01x faster                                                                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                          | 1.78 sec: 1.00x faster                                                                                                  |
| xml_etree_generate         | 85.6 ms                                                                                                           | 86.0 ms: 1.00x slower                                                                                                   |
| go                         | 113 ms                                                                                                            | 113 ms: 1.00x slower                                                                                                    |
| gc_traversal               | 4.82 ms                                                                                                           | 4.86 ms: 1.01x slower                                                                                                   |
| k_core                     | 2.29 sec                                                                                                          | 2.33 sec: 1.02x slower                                                                                                  |
| meteor_contest             | 108 ms                                                                                                            | 110 ms: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                                                            | 481 ms: 1.03x slower                                                                                                    |
| xml_etree_iterparse        | 98.4 ms                                                                                                           | 101 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 482 ms                                                                                                            | 496 ms: 1.03x slower                                                                                                    |
| create_gc_cycles           | 2.48 ms                                                                                                           | 2.55 ms: 1.03x slower                                                                                                   |
| pprint_pformat             | 1.50 sec                                                                                                          | 1.54 sec: 1.03x slower                                                                                                  |
| pprint_safe_repr           | 730 ms                                                                                                            | 755 ms: 1.03x slower                                                                                                    |
| pickle                     | 13.0 us                                                                                                           | 13.5 us: 1.04x slower                                                                                                   |
| mako                       | 11.4 ms                                                                                                           | 11.9 ms: 1.04x slower                                                                                                   |
| json_dumps                 | 11.5 ms                                                                                                           | 12.2 ms: 1.06x slower                                                                                                   |
| pidigits                   | 186 ms                                                                                                            | 202 ms: 1.08x slower                                                                                                    |
| unpack_sequence            | 50.9 ns                                                                                                           | 57.0 ns: 1.12x slower                                                                                                   |
| xml_etree_parse            | 141 ms                                                                                                            | 159 ms: 1.13x slower                                                                                                    |
| mdp                        | 2.48 sec                                                                                                          | 2.92 sec: 1.17x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (10): pylint, async_tree_io_tg, shortest_path, generators, asyncio_websockets, regex_compile, unpickle, unpickle_pure_python, connected_components, pycparser

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x