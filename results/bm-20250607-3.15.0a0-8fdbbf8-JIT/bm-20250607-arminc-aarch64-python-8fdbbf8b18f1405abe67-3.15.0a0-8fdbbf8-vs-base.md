# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.001x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                                                                            | 369 ms: 1.05x slower                                                                                                  |
| docutils       | 3.44 sec                                                                                                          | 3.67 sec: 1.07x slower                                                                                                |
| html5lib       | 67.4 ms                                                                                                           | 70.5 ms: 1.05x slower                                                                                                 |
| sphinx         | 1.34 sec                                                                                                          | 1.39 sec: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.05x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.02 sec                                                                                                          | 1.04 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed | 805 ms                                                                                                            | 823 ms: 1.02x slower                                                                                                  |
| async_tree_none         | 433 ms                                                                                                            | 445 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg      | 418 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                  |
| async_tree_io           | 979 ms                                                                                                            | 1.02 sec: 1.04x slower                                                                                                |
| async_generators        | 519 ms                                                                                                            | 540 ms: 1.04x slower                                                                                                  |
| async_tree_memoization  | 509 ms                                                                                                            | 532 ms: 1.05x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (6): asyncio_tcp, asyncio_tcp_ssl, coroutines, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 97.2 ms                                                                                                           | 92.8 ms: 1.05x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                                                            | 227 ms: 1.02x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.86 sec                                                                                                          | 2.72 sec: 1.05x faster                                                                                                |
| unpickle_pure_python | 321 us                                                                                                            | 307 us: 1.05x faster                                                                                                  |
| xml_etree_process    | 106 ms                                                                                                            | 104 ms: 1.02x faster                                                                                                  |
| json_dumps           | 17.4 ms                                                                                                           | 17.2 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse  | 168 ms                                                                                                            | 170 ms: 1.01x slower                                                                                                  |
| pickle_pure_python   | 471 us                                                                                                            | 478 us: 1.01x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (8): xml_etree_generate, json_loads, unpickle_list, xml_etree_parse, pickle_list, pickle_dict, unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.9 ms                                                                                                           | 17.0 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 9.58 ms                                                                                                           | 9.71 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 17.4 ms                                                                                                           | 16.5 ms: 1.05x faster                                                                                                 |
| django_template | 52.6 ms                                                                                                           | 53.8 ms: 1.02x slower                                                                                                 |
| genshi_xml      | 74.3 ms                                                                                                           | 79.4 ms: 1.07x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 6.68 sec                                                                                                          | 3.45 sec: 1.94x faster                                                                                                |
| richards                 | 63.5 ms                                                                                                           | 51.7 ms: 1.23x faster                                                                                                 |
| richards_super           | 71.8 ms                                                                                                           | 60.8 ms: 1.18x faster                                                                                                 |
| mako                     | 17.4 ms                                                                                                           | 16.5 ms: 1.05x faster                                                                                                 |
| tomli_loads              | 2.86 sec                                                                                                          | 2.72 sec: 1.05x faster                                                                                                |
| sqlite_synth             | 4.92 us                                                                                                           | 4.70 us: 1.05x faster                                                                                                 |
| float                    | 97.2 ms                                                                                                           | 92.8 ms: 1.05x faster                                                                                                 |
| unpickle_pure_python     | 321 us                                                                                                            | 307 us: 1.05x faster                                                                                                  |
| scimark_fft              | 501 ms                                                                                                            | 482 ms: 1.04x faster                                                                                                  |
| bpe_tokeniser            | 6.75 sec                                                                                                          | 6.56 sec: 1.03x faster                                                                                                |
| regex_dna                | 231 ms                                                                                                            | 227 ms: 1.02x faster                                                                                                  |
| xml_etree_process        | 106 ms                                                                                                            | 104 ms: 1.02x faster                                                                                                  |
| telco                    | 13.4 ms                                                                                                           | 13.2 ms: 1.01x faster                                                                                                 |
| json                     | 7.02 ms                                                                                                           | 6.93 ms: 1.01x faster                                                                                                 |
| shortest_path            | 612 ms                                                                                                            | 606 ms: 1.01x faster                                                                                                  |
| json_dumps               | 17.4 ms                                                                                                           | 17.2 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse      | 168 ms                                                                                                            | 170 ms: 1.01x slower                                                                                                  |
| python_startup           | 16.9 ms                                                                                                           | 17.0 ms: 1.01x slower                                                                                                 |
| unpack_sequence          | 61.9 ns                                                                                                           | 62.6 ns: 1.01x slower                                                                                                 |
| pyflate                  | 584 ms                                                                                                            | 592 ms: 1.01x slower                                                                                                  |
| python_startup_no_site   | 9.58 ms                                                                                                           | 9.71 ms: 1.01x slower                                                                                                 |
| deepcopy                 | 405 us                                                                                                            | 410 us: 1.01x slower                                                                                                  |
| pickle_pure_python       | 471 us                                                                                                            | 478 us: 1.01x slower                                                                                                  |
| async_tree_io_tg         | 1.02 sec                                                                                                          | 1.04 sec: 1.02x slower                                                                                                |
| django_template          | 52.6 ms                                                                                                           | 53.8 ms: 1.02x slower                                                                                                 |
| async_tree_cpu_io_mixed  | 805 ms                                                                                                            | 823 ms: 1.02x slower                                                                                                  |
| sqlglot_v2_optimize      | 76.2 ms                                                                                                           | 78.1 ms: 1.02x slower                                                                                                 |
| logging_format           | 10.2 us                                                                                                           | 10.4 us: 1.03x slower                                                                                                 |
| logging_simple           | 9.33 us                                                                                                           | 9.57 us: 1.03x slower                                                                                                 |
| async_tree_none          | 433 ms                                                                                                            | 445 ms: 1.03x slower                                                                                                  |
| async_tree_none_tg       | 418 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                  |
| sqlglot_v2_parse         | 1.74 ms                                                                                                           | 1.80 ms: 1.04x slower                                                                                                 |
| coverage                 | 695 ms                                                                                                            | 720 ms: 1.04x slower                                                                                                  |
| sphinx                   | 1.34 sec                                                                                                          | 1.39 sec: 1.04x slower                                                                                                |
| async_tree_io            | 979 ms                                                                                                            | 1.02 sec: 1.04x slower                                                                                                |
| async_generators         | 519 ms                                                                                                            | 540 ms: 1.04x slower                                                                                                  |
| async_tree_memoization   | 509 ms                                                                                                            | 532 ms: 1.05x slower                                                                                                  |
| html5lib                 | 67.4 ms                                                                                                           | 70.5 ms: 1.05x slower                                                                                                 |
| 2to3                     | 352 ms                                                                                                            | 369 ms: 1.05x slower                                                                                                  |
| sympy_str                | 332 ms                                                                                                            | 348 ms: 1.05x slower                                                                                                  |
| crypto_pyaes             | 103 ms                                                                                                            | 108 ms: 1.05x slower                                                                                                  |
| docutils                 | 3.44 sec                                                                                                          | 3.67 sec: 1.07x slower                                                                                                |
| genshi_xml               | 74.3 ms                                                                                                           | 79.4 ms: 1.07x slower                                                                                                 |
| sympy_expand             | 585 ms                                                                                                            | 628 ms: 1.07x slower                                                                                                  |
| typing_runtime_protocols | 259 us                                                                                                            | 280 us: 1.08x slower                                                                                                  |
| dulwich_log              | 62.0 ms                                                                                                           | 67.4 ms: 1.09x slower                                                                                                 |
| nqueens                  | 125 ms                                                                                                            | 136 ms: 1.09x slower                                                                                                  |
| comprehensions           | 23.0 us                                                                                                           | 25.2 us: 1.10x slower                                                                                                 |
| pycparser                | 1.46 sec                                                                                                          | 1.61 sec: 1.10x slower                                                                                                |
| go                       | 141 ms                                                                                                            | 170 ms: 1.21x slower                                                                                                  |
| pprint_safe_repr         | 1.30 sec                                                                                                          | 1.59 sec: 1.22x slower                                                                                                |
| pprint_pformat           | 2.64 sec                                                                                                          | 3.26 sec: 1.23x slower                                                                                                |
| Geometric mean           | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (50): xml_etree_generate, deepcopy_reduce, fannkuch, asyncio_tcp, json_loads, unpickle_list, generators, deltablue, xml_etree_parse, scimark_sparse_mat_mult, pickle_list, gc_traversal, k_core, scimark_lu, scimark_sor, pidigits, connected_components, regex_effbot, genshi_text, asyncio_tcp_ssl, create_gc_cycles, pickle_dict, unpickle, coroutines, subparsers, raytrace, scimark_monte_carlo, thrift, asyncio_websockets, mdp, async_tree_cpu_io_mixed_tg, sympy_sum, spectral_norm, async_tree_memoization_tg, deepcopy_memo, pickle, pylint, bench_thread_pool, logging_silent, sympy_integrate, sqlglot_v2_transpile, many_optionals, regex_v8, chaos, regex_compile, nbody, hexiom, sqlglot_v2_normalize, pathlib, meteor_contest

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x