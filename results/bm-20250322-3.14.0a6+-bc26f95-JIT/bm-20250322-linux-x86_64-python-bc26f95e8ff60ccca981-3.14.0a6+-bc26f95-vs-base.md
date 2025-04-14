# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.003x slower
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                                                            | 264 ms: 1.03x slower                                                                                                  |
| docutils       | 2.60 sec                                                                                                          | 2.70 sec: 1.04x slower                                                                                                |
| html5lib       | 62.8 ms                                                                                                           | 62.0 ms: 1.01x faster                                                                                                 |
| sphinx         | 1.01 sec                                                                                                          | 1.03 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 476 ms                                                                                                            | 477 ms: 1.00x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                          | 1.80 sec: 1.01x slower                                                                                                |
| coroutines                 | 23.4 ms                                                                                                           | 23.7 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 482 ms                                                                                                            | 489 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                                                            | 476 ms: 1.02x slower                                                                                                  |
| async_generators           | 395 ms                                                                                                            | 418 ms: 1.06x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 99.0 ms                                                                                                           | 88.1 ms: 1.12x faster                                                                                                 |
| float          | 71.9 ms                                                                                                           | 65.1 ms: 1.10x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                                                            | 127 ms: 1.01x slower                                                                                                  |
| regex_v8       | 23.6 ms                                                                                                           | 24.2 ms: 1.02x slower                                                                                                 |
| regex_dna      | 212 ms                                                                                                            | 227 ms: 1.07x slower                                                                                                  |
| regex_effbot   | 3.10 ms                                                                                                           | 3.55 ms: 1.15x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 85.6 ms                                                                                                           | 79.9 ms: 1.07x faster                                                                                                 |
| xml_etree_process    | 59.1 ms                                                                                                           | 56.6 ms: 1.04x faster                                                                                                 |
| tomli_loads          | 1.95 sec                                                                                                          | 1.88 sec: 1.03x faster                                                                                                |
| pickle_list          | 5.38 us                                                                                                           | 5.24 us: 1.03x faster                                                                                                 |
| unpickle_pure_python | 218 us                                                                                                            | 214 us: 1.02x faster                                                                                                  |
| xml_etree_parse      | 141 ms                                                                                                            | 140 ms: 1.01x faster                                                                                                  |
| xml_etree_iterparse  | 98.4 ms                                                                                                           | 97.3 ms: 1.01x faster                                                                                                 |
| json_loads           | 29.8 us                                                                                                           | 29.7 us: 1.00x faster                                                                                                 |
| pickle_pure_python   | 315 us                                                                                                            | 320 us: 1.02x slower                                                                                                  |
| unpickle             | 14.4 us                                                                                                           | 14.6 us: 1.02x slower                                                                                                 |
| pickle_dict          | 34.3 us                                                                                                           | 35.9 us: 1.05x slower                                                                                                 |
| unpickle_list        | 5.30 us                                                                                                           | 5.56 us: 1.05x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                           | 13.0 ms: 1.00x faster                                                                                                 |
| python_startup_no_site | 8.17 ms                                                                                                           | 8.15 ms: 1.00x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.4 ms                                                                                                           | 11.0 ms: 1.04x faster                                                                                                 |
| genshi_text     | 21.3 ms                                                                                                           | 21.2 ms: 1.01x faster                                                                                                 |
| genshi_xml      | 49.0 ms                                                                                                           | 49.7 ms: 1.01x slower                                                                                                 |
| django_template | 31.3 ms                                                                                                           | 32.2 ms: 1.03x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.00x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards_super             | 49.9 ms                                                                                                           | 41.3 ms: 1.21x faster                                                                                                 |
| richards                   | 43.9 ms                                                                                                           | 36.4 ms: 1.20x faster                                                                                                 |
| nbody                      | 99.0 ms                                                                                                           | 88.1 ms: 1.12x faster                                                                                                 |
| scimark_fft                | 352 ms                                                                                                            | 317 ms: 1.11x faster                                                                                                  |
| float                      | 71.9 ms                                                                                                           | 65.1 ms: 1.10x faster                                                                                                 |
| xml_etree_generate         | 85.6 ms                                                                                                           | 79.9 ms: 1.07x faster                                                                                                 |
| coverage                   | 91.6 ms                                                                                                           | 87.0 ms: 1.05x faster                                                                                                 |
| xml_etree_process          | 59.1 ms                                                                                                           | 56.6 ms: 1.04x faster                                                                                                 |
| gc_traversal               | 4.82 ms                                                                                                           | 4.64 ms: 1.04x faster                                                                                                 |
| mako                       | 11.4 ms                                                                                                           | 11.0 ms: 1.04x faster                                                                                                 |
| tomli_loads                | 1.95 sec                                                                                                          | 1.88 sec: 1.03x faster                                                                                                |
| pyflate                    | 447 ms                                                                                                            | 434 ms: 1.03x faster                                                                                                  |
| sqlite_synth               | 2.77 us                                                                                                           | 2.70 us: 1.03x faster                                                                                                 |
| pickle_list                | 5.38 us                                                                                                           | 5.24 us: 1.03x faster                                                                                                 |
| connected_components       | 464 ms                                                                                                            | 453 ms: 1.03x faster                                                                                                  |
| pathlib                    | 16.9 ms                                                                                                           | 16.5 ms: 1.02x faster                                                                                                 |
| unpickle_pure_python       | 218 us                                                                                                            | 214 us: 1.02x faster                                                                                                  |
| deepcopy_memo              | 29.6 us                                                                                                           | 28.9 us: 1.02x faster                                                                                                 |
| generators                 | 28.7 ms                                                                                                           | 28.2 ms: 1.02x faster                                                                                                 |
| json                       | 5.37 ms                                                                                                           | 5.27 ms: 1.02x faster                                                                                                 |
| shortest_path              | 503 ms                                                                                                            | 494 ms: 1.02x faster                                                                                                  |
| fannkuch                   | 422 ms                                                                                                            | 415 ms: 1.02x faster                                                                                                  |
| html5lib                   | 62.8 ms                                                                                                           | 62.0 ms: 1.01x faster                                                                                                 |
| deltablue                  | 3.09 ms                                                                                                           | 3.05 ms: 1.01x faster                                                                                                 |
| xml_etree_parse            | 141 ms                                                                                                            | 140 ms: 1.01x faster                                                                                                  |
| xml_etree_iterparse        | 98.4 ms                                                                                                           | 97.3 ms: 1.01x faster                                                                                                 |
| mdp                        | 2.48 sec                                                                                                          | 2.46 sec: 1.01x faster                                                                                                |
| genshi_text                | 21.3 ms                                                                                                           | 21.2 ms: 1.01x faster                                                                                                 |
| logging_format             | 6.18 us                                                                                                           | 6.14 us: 1.01x faster                                                                                                 |
| bpe_tokeniser              | 4.62 sec                                                                                                          | 4.60 sec: 1.01x faster                                                                                                |
| python_startup             | 13.1 ms                                                                                                           | 13.0 ms: 1.00x faster                                                                                                 |
| bench_mp_pool              | 82.8 ms                                                                                                           | 82.5 ms: 1.00x faster                                                                                                 |
| json_loads                 | 29.8 us                                                                                                           | 29.7 us: 1.00x faster                                                                                                 |
| python_startup_no_site     | 8.17 ms                                                                                                           | 8.15 ms: 1.00x faster                                                                                                 |
| create_gc_cycles           | 2.48 ms                                                                                                           | 2.48 ms: 1.00x slower                                                                                                 |
| asyncio_tcp                | 476 ms                                                                                                            | 477 ms: 1.00x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                          | 1.80 sec: 1.01x slower                                                                                                |
| logging_simple             | 5.53 us                                                                                                           | 5.56 us: 1.01x slower                                                                                                 |
| deepcopy                   | 260 us                                                                                                            | 261 us: 1.01x slower                                                                                                  |
| nqueens                    | 83.6 ms                                                                                                           | 84.1 ms: 1.01x slower                                                                                                 |
| scimark_lu                 | 116 ms                                                                                                            | 117 ms: 1.01x slower                                                                                                  |
| raytrace                   | 266 ms                                                                                                            | 268 ms: 1.01x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.59 ms                                                                                                           | 1.61 ms: 1.01x slower                                                                                                 |
| regex_compile              | 126 ms                                                                                                            | 127 ms: 1.01x slower                                                                                                  |
| bench_thread_pool          | 869 us                                                                                                            | 880 us: 1.01x slower                                                                                                  |
| thrift                     | 775 us                                                                                                            | 786 us: 1.01x slower                                                                                                  |
| coroutines                 | 23.4 ms                                                                                                           | 23.7 ms: 1.01x slower                                                                                                 |
| genshi_xml                 | 49.0 ms                                                                                                           | 49.7 ms: 1.01x slower                                                                                                 |
| pickle_pure_python         | 315 us                                                                                                            | 320 us: 1.02x slower                                                                                                  |
| telco                      | 7.94 ms                                                                                                           | 8.06 ms: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 482 ms                                                                                                            | 489 ms: 1.02x slower                                                                                                  |
| unpickle                   | 14.4 us                                                                                                           | 14.6 us: 1.02x slower                                                                                                 |
| subparsers                 | 20.9 ms                                                                                                           | 21.2 ms: 1.02x slower                                                                                                 |
| meteor_contest             | 108 ms                                                                                                            | 110 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                                                            | 476 ms: 1.02x slower                                                                                                  |
| deepcopy_reduce            | 2.68 us                                                                                                           | 2.73 us: 1.02x slower                                                                                                 |
| sqlglot_v2_parse           | 1.28 ms                                                                                                           | 1.30 ms: 1.02x slower                                                                                                 |
| sqlglot_v2_normalize       | 107 ms                                                                                                            | 109 ms: 1.02x slower                                                                                                  |
| sphinx                     | 1.01 sec                                                                                                          | 1.03 sec: 1.02x slower                                                                                                |
| scimark_monte_carlo        | 67.5 ms                                                                                                           | 68.9 ms: 1.02x slower                                                                                                 |
| sqlalchemy_declarative     | 130 ms                                                                                                            | 133 ms: 1.02x slower                                                                                                  |
| regex_v8                   | 23.6 ms                                                                                                           | 24.2 ms: 1.02x slower                                                                                                 |
| sympy_sum                  | 148 ms                                                                                                            | 151 ms: 1.02x slower                                                                                                  |
| sqlglot_v2_optimize        | 53.2 ms                                                                                                           | 54.4 ms: 1.02x slower                                                                                                 |
| spectral_norm              | 96.4 ms                                                                                                           | 98.8 ms: 1.02x slower                                                                                                 |
| sqlalchemy_imperative      | 16.6 ms                                                                                                           | 17.1 ms: 1.02x slower                                                                                                 |
| chaos                      | 58.8 ms                                                                                                           | 60.3 ms: 1.03x slower                                                                                                 |
| django_template            | 31.3 ms                                                                                                           | 32.2 ms: 1.03x slower                                                                                                 |
| dulwich_log                | 58.3 ms                                                                                                           | 59.9 ms: 1.03x slower                                                                                                 |
| 2to3                       | 256 ms                                                                                                            | 264 ms: 1.03x slower                                                                                                  |
| sympy_str                  | 267 ms                                                                                                            | 275 ms: 1.03x slower                                                                                                  |
| many_optionals             | 947 us                                                                                                            | 977 us: 1.03x slower                                                                                                  |
| sympy_integrate            | 19.4 ms                                                                                                           | 20.1 ms: 1.03x slower                                                                                                 |
| pprint_pformat             | 1.50 sec                                                                                                          | 1.55 sec: 1.03x slower                                                                                                |
| scimark_sor                | 117 ms                                                                                                            | 121 ms: 1.04x slower                                                                                                  |
| logging_silent             | 93.7 ns                                                                                                           | 97.0 ns: 1.04x slower                                                                                                 |
| docutils                   | 2.60 sec                                                                                                          | 2.70 sec: 1.04x slower                                                                                                |
| typing_runtime_protocols   | 163 us                                                                                                            | 169 us: 1.04x slower                                                                                                  |
| sympy_expand               | 457 ms                                                                                                            | 475 ms: 1.04x slower                                                                                                  |
| pickle_dict                | 34.3 us                                                                                                           | 35.9 us: 1.05x slower                                                                                                 |
| pprint_safe_repr           | 730 ms                                                                                                            | 764 ms: 1.05x slower                                                                                                  |
| unpickle_list              | 5.30 us                                                                                                           | 5.56 us: 1.05x slower                                                                                                 |
| pycparser                  | 1.13 sec                                                                                                          | 1.19 sec: 1.05x slower                                                                                                |
| crypto_pyaes               | 75.7 ms                                                                                                           | 79.9 ms: 1.06x slower                                                                                                 |
| async_generators           | 395 ms                                                                                                            | 418 ms: 1.06x slower                                                                                                  |
| regex_dna                  | 212 ms                                                                                                            | 227 ms: 1.07x slower                                                                                                  |
| hexiom                     | 6.21 ms                                                                                                           | 6.90 ms: 1.11x slower                                                                                                 |
| comprehensions             | 16.8 us                                                                                                           | 19.0 us: 1.13x slower                                                                                                 |
| regex_effbot               | 3.10 ms                                                                                                           | 3.55 ms: 1.15x slower                                                                                                 |
| go                         | 113 ms                                                                                                            | 129 ms: 1.15x slower                                                                                                  |
| unpack_sequence            | 50.9 ns                                                                                                           | 73.4 ns: 1.44x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (13): scimark_sparse_mat_mult, async_tree_memoization, json_dumps, pickle, pidigits, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_none, k_core, async_tree_io_tg, async_tree_memoization_tg, pylint

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x