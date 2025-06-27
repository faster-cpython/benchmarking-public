# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.344x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                            | 312 ms: 1.02x slower                                                                                                  |
| docutils       | 2.97 sec                                                                                                          | 3.11 sec: 1.05x slower                                                                                                |
| sphinx         | 1.14 sec                                                                                                          | 1.16 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 905 ms                                                                                                            | 914 ms: 1.01x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 665 ms                                                                                                            | 678 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                            | 666 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg         | 372 ms                                                                                                            | 381 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg  | 464 ms                                                                                                            | 481 ms: 1.04x slower                                                                                                  |
| async_tree_io              | 870 ms                                                                                                            | 914 ms: 1.05x slower                                                                                                  |
| async_generators           | 458 ms                                                                                                            | 484 ms: 1.06x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (4): coroutines, asyncio_websockets, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                                                            | 233 ms: 1.03x slower                                                                                                  |
| regex_v8       | 26.8 ms                                                                                                           | 27.7 ms: 1.03x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.47 sec                                                                                                          | 2.35 sec: 1.05x faster                                                                                                |
| json_dumps          | 13.6 ms                                                                                                           | 13.3 ms: 1.03x faster                                                                                                 |
| xml_etree_process   | 79.9 ms                                                                                                           | 78.0 ms: 1.03x faster                                                                                                 |
| json_loads          | 32.5 us                                                                                                           | 32.0 us: 1.02x faster                                                                                                 |
| pickle_pure_python  | 384 us                                                                                                            | 390 us: 1.01x slower                                                                                                  |
| xml_etree_parse     | 182 ms                                                                                                            | 186 ms: 1.02x slower                                                                                                  |
| xml_etree_iterparse | 143 ms                                                                                                            | 148 ms: 1.04x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.71 ms                                                                                                           | 8.56 ms: 1.02x faster                                                                                                 |
| python_startup         | 15.2 ms                                                                                                           | 15.0 ms: 1.01x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                                                           | 13.1 ms: 1.06x faster                                                                                                 |
| genshi_xml     | 60.3 ms                                                                                                           | 64.0 ms: 1.06x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pprint_pformat             | 2.04 sec                                                                                                          | 1.91 us: 1070100.14x faster                                                                                           |
| pprint_safe_repr           | 1.01 sec                                                                                                          | 1.05 us: 956809.91x faster                                                                                            |
| richards                   | 53.1 ms                                                                                                           | 45.4 ms: 1.17x faster                                                                                                 |
| richards_super             | 58.3 ms                                                                                                           | 52.5 ms: 1.11x faster                                                                                                 |
| telco                      | 9.74 ms                                                                                                           | 9.15 ms: 1.06x faster                                                                                                 |
| mako                       | 13.9 ms                                                                                                           | 13.1 ms: 1.06x faster                                                                                                 |
| tomli_loads                | 2.47 sec                                                                                                          | 2.35 sec: 1.05x faster                                                                                                |
| deltablue                  | 4.00 ms                                                                                                           | 3.86 ms: 1.04x faster                                                                                                 |
| bpe_tokeniser              | 5.55 sec                                                                                                          | 5.40 sec: 1.03x faster                                                                                                |
| json_dumps                 | 13.6 ms                                                                                                           | 13.3 ms: 1.03x faster                                                                                                 |
| xml_etree_process          | 79.9 ms                                                                                                           | 78.0 ms: 1.03x faster                                                                                                 |
| logging_silent             | 623 ns                                                                                                            | 610 ns: 1.02x faster                                                                                                  |
| json_loads                 | 32.5 us                                                                                                           | 32.0 us: 1.02x faster                                                                                                 |
| python_startup_no_site     | 8.71 ms                                                                                                           | 8.56 ms: 1.02x faster                                                                                                 |
| logging_format             | 8.39 us                                                                                                           | 8.26 us: 1.02x faster                                                                                                 |
| python_startup             | 15.2 ms                                                                                                           | 15.0 ms: 1.01x faster                                                                                                 |
| async_tree_io_tg           | 905 ms                                                                                                            | 914 ms: 1.01x slower                                                                                                  |
| pickle_pure_python         | 384 us                                                                                                            | 390 us: 1.01x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 665 ms                                                                                                            | 678 ms: 1.02x slower                                                                                                  |
| sphinx                     | 1.14 sec                                                                                                          | 1.16 sec: 1.02x slower                                                                                                |
| k_core                     | 2.80 sec                                                                                                          | 2.87 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 650 ms                                                                                                            | 666 ms: 1.02x slower                                                                                                  |
| 2to3                       | 304 ms                                                                                                            | 312 ms: 1.02x slower                                                                                                  |
| xml_etree_parse            | 182 ms                                                                                                            | 186 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg         | 372 ms                                                                                                            | 381 ms: 1.02x slower                                                                                                  |
| regex_dna                  | 227 ms                                                                                                            | 233 ms: 1.03x slower                                                                                                  |
| sqlglot_v2_normalize       | 125 ms                                                                                                            | 128 ms: 1.03x slower                                                                                                  |
| regex_v8                   | 26.8 ms                                                                                                           | 27.7 ms: 1.03x slower                                                                                                 |
| scimark_monte_carlo        | 79.7 ms                                                                                                           | 82.3 ms: 1.03x slower                                                                                                 |
| async_tree_memoization_tg  | 464 ms                                                                                                            | 481 ms: 1.04x slower                                                                                                  |
| xml_etree_iterparse        | 143 ms                                                                                                            | 148 ms: 1.04x slower                                                                                                  |
| docutils                   | 2.97 sec                                                                                                          | 3.11 sec: 1.05x slower                                                                                                |
| async_tree_io              | 870 ms                                                                                                            | 914 ms: 1.05x slower                                                                                                  |
| async_generators           | 458 ms                                                                                                            | 484 ms: 1.06x slower                                                                                                  |
| fannkuch                   | 466 ms                                                                                                            | 493 ms: 1.06x slower                                                                                                  |
| many_optionals             | 874 us                                                                                                            | 925 us: 1.06x slower                                                                                                  |
| typing_runtime_protocols   | 194 us                                                                                                            | 206 us: 1.06x slower                                                                                                  |
| genshi_xml                 | 60.3 ms                                                                                                           | 64.0 ms: 1.06x slower                                                                                                 |
| sqlglot_v2_transpile       | 1.76 ms                                                                                                           | 1.88 ms: 1.06x slower                                                                                                 |
| sympy_expand               | 463 ms                                                                                                            | 494 ms: 1.07x slower                                                                                                  |
| nqueens                    | 100 ms                                                                                                            | 107 ms: 1.07x slower                                                                                                  |
| sympy_str                  | 267 ms                                                                                                            | 285 ms: 1.07x slower                                                                                                  |
| meteor_contest             | 116 ms                                                                                                            | 125 ms: 1.08x slower                                                                                                  |
| comprehensions             | 20.7 us                                                                                                           | 22.5 us: 1.09x slower                                                                                                 |
| crypto_pyaes               | 84.3 ms                                                                                                           | 91.9 ms: 1.09x slower                                                                                                 |
| sqlglot_v2_parse           | 1.43 ms                                                                                                           | 1.56 ms: 1.09x slower                                                                                                 |
| pycparser                  | 1.25 sec                                                                                                          | 1.39 sec: 1.11x slower                                                                                                |
| go                         | 130 ms                                                                                                            | 159 ms: 1.22x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.33x faster                                                                                                          |

Benchmark hidden because not significant (44): unpickle_pure_python, xml_etree_generate, scimark_lu, scimark_fft, json, deepcopy, generators, coroutines, dulwich_log, deepcopy_memo, thrift, nbody, sqlite_synth, gc_traversal, create_gc_cycles, connected_components, scimark_sor, html5lib, pidigits, float, pyflate, shortest_path, genshi_text, spectral_norm, mdp, djangocms, asyncio_websockets, async_tree_none, async_tree_memoization, raytrace, django_template, logging_simple, pylint, chaos, coverage, pathlib, subparsers, deepcopy_reduce, regex_effbot, scimark_sparse_mat_mult, sqlglot_v2_optimize, sympy_sum, sympy_integrate, hexiom
Ignored benchmarks (1) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: regex_compile

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x