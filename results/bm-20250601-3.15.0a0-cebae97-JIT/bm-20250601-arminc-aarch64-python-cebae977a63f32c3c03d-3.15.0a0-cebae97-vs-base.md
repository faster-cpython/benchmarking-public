# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.365x faster
- HPT reliability: 85.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 356 ms                                                                                                            | 366 ms: 1.03x slower                                                                                                  |
| docutils       | 3.45 sec                                                                                                          | 3.61 sec: 1.05x slower                                                                                                |
| sphinx         | 1.36 sec                                                                                                          | 1.38 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl         | 2.25 sec                                                                                                          | 2.26 sec: 1.00x slower                                                                                                |
| asyncio_tcp             | 556 ms                                                                                                            | 566 ms: 1.02x slower                                                                                                  |
| async_tree_none         | 441 ms                                                                                                            | 449 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed | 808 ms                                                                                                            | 825 ms: 1.02x slower                                                                                                  |
| async_tree_io           | 987 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                |
| async_generators        | 521 ms                                                                                                            | 542 ms: 1.04x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 96.5 ms                                                                                                           | 91.6 ms: 1.05x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.93 sec                                                                                                          | 2.69 sec: 1.09x faster                                                                                                |
| xml_etree_generate   | 161 ms                                                                                                            | 149 ms: 1.08x faster                                                                                                  |
| unpickle_pure_python | 328 us                                                                                                            | 311 us: 1.06x faster                                                                                                  |
| json_dumps           | 17.2 ms                                                                                                           | 16.7 ms: 1.03x faster                                                                                                 |
| xml_etree_parse      | 229 ms                                                                                                            | 227 ms: 1.01x faster                                                                                                  |
| pickle               | 19.7 us                                                                                                           | 19.9 us: 1.01x slower                                                                                                 |
| xml_etree_iterparse  | 167 ms                                                                                                            | 171 ms: 1.02x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (7): xml_etree_process, json_loads, unpickle_list, unpickle, pickle_list, pickle_dict, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 17.2 ms                                                                                                           | 17.0 ms: 1.01x faster                                                                                                 |
| python_startup_no_site | 9.71 ms                                                                                                           | 9.68 ms: 1.00x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 17.9 ms                                                                                                           | 17.5 ms: 1.02x faster                                                                                                 |
| django_template | 52.5 ms                                                                                                           | 53.4 ms: 1.02x slower                                                                                                 |
| genshi_xml      | 74.7 ms                                                                                                           | 75.9 ms: 1.02x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat          | 2.76 sec                                                                                                          | 2.43 us: 1134431.02x faster                                                                                           |
| pprint_safe_repr        | 1.35 sec                                                                                                          | 1.50 us: 898902.65x faster                                                                                            |
| bench_mp_pool           | 5.59 sec                                                                                                          | 2.87 sec: 1.95x faster                                                                                                |
| richards                | 62.9 ms                                                                                                           | 51.6 ms: 1.22x faster                                                                                                 |
| richards_super          | 71.2 ms                                                                                                           | 61.4 ms: 1.16x faster                                                                                                 |
| tomli_loads             | 2.93 sec                                                                                                          | 2.69 sec: 1.09x faster                                                                                                |
| xml_etree_generate      | 161 ms                                                                                                            | 149 ms: 1.08x faster                                                                                                  |
| deltablue               | 4.54 ms                                                                                                           | 4.28 ms: 1.06x faster                                                                                                 |
| unpickle_pure_python    | 328 us                                                                                                            | 311 us: 1.06x faster                                                                                                  |
| float                   | 96.5 ms                                                                                                           | 91.6 ms: 1.05x faster                                                                                                 |
| json_dumps              | 17.2 ms                                                                                                           | 16.7 ms: 1.03x faster                                                                                                 |
| bpe_tokeniser           | 6.64 sec                                                                                                          | 6.48 sec: 1.02x faster                                                                                                |
| deepcopy_reduce         | 4.61 us                                                                                                           | 4.51 us: 1.02x faster                                                                                                 |
| mako                    | 17.9 ms                                                                                                           | 17.5 ms: 1.02x faster                                                                                                 |
| scimark_fft             | 500 ms                                                                                                            | 489 ms: 1.02x faster                                                                                                  |
| logging_silent          | 914 ns                                                                                                            | 898 ns: 1.02x faster                                                                                                  |
| json                    | 6.95 ms                                                                                                           | 6.84 ms: 1.02x faster                                                                                                 |
| mdp                     | 2.01 sec                                                                                                          | 1.98 sec: 1.02x faster                                                                                                |
| python_startup          | 17.2 ms                                                                                                           | 17.0 ms: 1.01x faster                                                                                                 |
| shortest_path           | 599 ms                                                                                                            | 594 ms: 1.01x faster                                                                                                  |
| xml_etree_parse         | 229 ms                                                                                                            | 227 ms: 1.01x faster                                                                                                  |
| python_startup_no_site  | 9.71 ms                                                                                                           | 9.68 ms: 1.00x faster                                                                                                 |
| asyncio_tcp_ssl         | 2.25 sec                                                                                                          | 2.26 sec: 1.00x slower                                                                                                |
| pickle                  | 19.7 us                                                                                                           | 19.9 us: 1.01x slower                                                                                                 |
| pyflate                 | 590 ms                                                                                                            | 598 ms: 1.01x slower                                                                                                  |
| sphinx                  | 1.36 sec                                                                                                          | 1.38 sec: 1.02x slower                                                                                                |
| django_template         | 52.5 ms                                                                                                           | 53.4 ms: 1.02x slower                                                                                                 |
| genshi_xml              | 74.7 ms                                                                                                           | 75.9 ms: 1.02x slower                                                                                                 |
| asyncio_tcp             | 556 ms                                                                                                            | 566 ms: 1.02x slower                                                                                                  |
| async_tree_none         | 441 ms                                                                                                            | 449 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed | 808 ms                                                                                                            | 825 ms: 1.02x slower                                                                                                  |
| xml_etree_iterparse     | 167 ms                                                                                                            | 171 ms: 1.02x slower                                                                                                  |
| raytrace                | 390 ms                                                                                                            | 399 ms: 1.02x slower                                                                                                  |
| telco                   | 13.2 ms                                                                                                           | 13.5 ms: 1.03x slower                                                                                                 |
| meteor_contest          | 127 ms                                                                                                            | 130 ms: 1.03x slower                                                                                                  |
| async_tree_io           | 987 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                |
| 2to3                    | 356 ms                                                                                                            | 366 ms: 1.03x slower                                                                                                  |
| sqlglot_v2_optimize     | 75.7 ms                                                                                                           | 78.1 ms: 1.03x slower                                                                                                 |
| many_optionals          | 1.10 ms                                                                                                           | 1.13 ms: 1.03x slower                                                                                                 |
| bench_thread_pool       | 1.48 ms                                                                                                           | 1.53 ms: 1.04x slower                                                                                                 |
| sympy_expand            | 599 ms                                                                                                            | 622 ms: 1.04x slower                                                                                                  |
| dulwich_log             | 65.6 ms                                                                                                           | 68.2 ms: 1.04x slower                                                                                                 |
| async_generators        | 521 ms                                                                                                            | 542 ms: 1.04x slower                                                                                                  |
| sqlglot_v2_parse        | 1.73 ms                                                                                                           | 1.81 ms: 1.04x slower                                                                                                 |
| hexiom                  | 8.37 ms                                                                                                           | 8.76 ms: 1.05x slower                                                                                                 |
| docutils                | 3.45 sec                                                                                                          | 3.61 sec: 1.05x slower                                                                                                |
| sqlglot_v2_transpile    | 2.14 ms                                                                                                           | 2.24 ms: 1.05x slower                                                                                                 |
| nqueens                 | 125 ms                                                                                                            | 135 ms: 1.07x slower                                                                                                  |
| pycparser               | 1.49 sec                                                                                                          | 1.63 sec: 1.09x slower                                                                                                |
| comprehensions          | 23.1 us                                                                                                           | 26.5 us: 1.15x slower                                                                                                 |
| unpack_sequence         | 56.4 ns                                                                                                           | 65.8 ns: 1.17x slower                                                                                                 |
| go                      | 141 ms                                                                                                            | 172 ms: 1.22x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.32x faster                                                                                                          |

Benchmark hidden because not significant (49): genshi_text, nbody, xml_etree_process, gc_traversal, create_gc_cycles, coverage, deepcopy_memo, fannkuch, logging_format, async_tree_cpu_io_mixed_tg, spectral_norm, asyncio_websockets, connected_components, regex_effbot, deepcopy, pidigits, async_tree_none_tg, regex_dna, sqlite_synth, json_loads, unpickle_list, unpickle, chaos, pylint, sqlglot_v2_normalize, pickle_list, sympy_str, async_tree_memoization, thrift, async_tree_memoization_tg, typing_runtime_protocols, async_tree_io_tg, generators, sympy_sum, sympy_integrate, subparsers, pathlib, k_core, logging_simple, regex_v8, scimark_lu, scimark_sor, pickle_dict, coroutines, scimark_monte_carlo, scimark_sparse_mat_mult, crypto_pyaes, pickle_pure_python, html5lib
Ignored benchmarks (1) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: regex_compile

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 85.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x