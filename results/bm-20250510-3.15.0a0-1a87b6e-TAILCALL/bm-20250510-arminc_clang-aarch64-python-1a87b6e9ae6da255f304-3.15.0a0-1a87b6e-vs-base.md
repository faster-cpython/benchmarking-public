# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.002x slower
- HPT reliability: 94.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                                                                          | 3.02 sec: 1.02x slower                                                                                                  |
| html5lib       | 62.0 ms                                                                                                           | 60.2 ms: 1.03x faster                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators           | 460 ms                                                                                                            | 432 ms: 1.06x faster                                                                                                    |
| coroutines                 | 30.2 ms                                                                                                           | 28.8 ms: 1.05x faster                                                                                                   |
| async_tree_none_tg         | 373 ms                                                                                                            | 360 ms: 1.03x faster                                                                                                    |
| async_tree_memoization_tg  | 463 ms                                                                                                            | 449 ms: 1.03x faster                                                                                                    |
| async_tree_io              | 887 ms                                                                                                            | 863 ms: 1.03x faster                                                                                                    |
| async_tree_memoization     | 465 ms                                                                                                            | 455 ms: 1.02x faster                                                                                                    |
| asyncio_tcp_ssl            | 2.17 sec                                                                                                          | 2.21 sec: 1.01x slower                                                                                                  |
| asyncio_tcp                | 534 ms                                                                                                            | 558 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                                                            | 711 ms: 1.08x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 651 ms                                                                                                            | 721 ms: 1.11x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (3): async_tree_none, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 122 ms                                                                                                            | 129 ms: 1.06x slower                                                                                                    |
| pidigits       | 235 ms                                                                                                            | 292 ms: 1.24x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                                                            | 247 ms: 1.03x slower                                                                                                    |
| regex_v8       | 28.5 ms                                                                                                           | 30.6 ms: 1.07x slower                                                                                                   |
| regex_effbot   | 3.84 ms                                                                                                           | 4.64 ms: 1.21x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.07x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list       | 6.80 us                                                                                                           | 5.79 us: 1.17x faster                                                                                                   |
| unpickle            | 18.8 us                                                                                                           | 17.0 us: 1.10x faster                                                                                                   |
| pickle_dict         | 39.0 us                                                                                                           | 36.5 us: 1.07x faster                                                                                                   |
| json_loads          | 36.4 us                                                                                                           | 34.2 us: 1.07x faster                                                                                                   |
| xml_etree_process   | 79.6 ms                                                                                                           | 76.1 ms: 1.05x faster                                                                                                   |
| xml_etree_iterparse | 143 ms                                                                                                            | 148 ms: 1.04x slower                                                                                                    |
| xml_etree_parse     | 180 ms                                                                                                            | 205 ms: 1.14x slower                                                                                                    |
| Geometric mean      | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (7): unpickle_pure_python, pickle, pickle_pure_python, pickle_list, xml_etree_generate, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 15.2 ms: 1.00x slower                                                                                                   |
| python_startup_no_site | 8.66 ms                                                                                                           | 8.74 ms: 1.01x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                                                                           | 14.1 ms: 1.01x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| unpickle_list              | 6.80 us                                                                                                           | 5.79 us: 1.17x faster                                                                                                   |
| unpickle                   | 18.8 us                                                                                                           | 17.0 us: 1.10x faster                                                                                                   |
| scimark_fft                | 445 ms                                                                                                            | 407 ms: 1.09x faster                                                                                                    |
| spectral_norm              | 130 ms                                                                                                            | 121 ms: 1.07x faster                                                                                                    |
| pickle_dict                | 39.0 us                                                                                                           | 36.5 us: 1.07x faster                                                                                                   |
| json_loads                 | 36.4 us                                                                                                           | 34.2 us: 1.07x faster                                                                                                   |
| deepcopy_memo              | 38.1 us                                                                                                           | 35.7 us: 1.07x faster                                                                                                   |
| async_generators           | 460 ms                                                                                                            | 432 ms: 1.06x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.82 ms                                                                                                           | 1.71 ms: 1.06x faster                                                                                                   |
| deepcopy_reduce            | 3.57 us                                                                                                           | 3.36 us: 1.06x faster                                                                                                   |
| deepcopy                   | 335 us                                                                                                            | 318 us: 1.05x faster                                                                                                    |
| richards                   | 51.6 ms                                                                                                           | 49.0 ms: 1.05x faster                                                                                                   |
| pathlib                    | 22.7 ms                                                                                                           | 21.6 ms: 1.05x faster                                                                                                   |
| coroutines                 | 30.2 ms                                                                                                           | 28.8 ms: 1.05x faster                                                                                                   |
| generators                 | 36.9 ms                                                                                                           | 35.2 ms: 1.05x faster                                                                                                   |
| xml_etree_process          | 79.6 ms                                                                                                           | 76.1 ms: 1.05x faster                                                                                                   |
| bpe_tokeniser              | 5.50 sec                                                                                                          | 5.26 sec: 1.04x faster                                                                                                  |
| scimark_lu                 | 142 ms                                                                                                            | 137 ms: 1.04x faster                                                                                                    |
| json                       | 6.11 ms                                                                                                           | 5.88 ms: 1.04x faster                                                                                                   |
| logging_format             | 8.39 us                                                                                                           | 8.10 us: 1.04x faster                                                                                                   |
| gc_traversal               | 6.97 ms                                                                                                           | 6.73 ms: 1.03x faster                                                                                                   |
| async_tree_none_tg         | 373 ms                                                                                                            | 360 ms: 1.03x faster                                                                                                    |
| html5lib                   | 62.0 ms                                                                                                           | 60.2 ms: 1.03x faster                                                                                                   |
| async_tree_memoization_tg  | 463 ms                                                                                                            | 449 ms: 1.03x faster                                                                                                    |
| bench_thread_pool          | 1.36 ms                                                                                                           | 1.32 ms: 1.03x faster                                                                                                   |
| async_tree_io              | 887 ms                                                                                                            | 863 ms: 1.03x faster                                                                                                    |
| scimark_monte_carlo        | 80.6 ms                                                                                                           | 78.7 ms: 1.02x faster                                                                                                   |
| async_tree_memoization     | 465 ms                                                                                                            | 455 ms: 1.02x faster                                                                                                    |
| coverage                   | 545 ms                                                                                                            | 534 ms: 1.02x faster                                                                                                    |
| thrift                     | 194 ms                                                                                                            | 192 ms: 1.01x faster                                                                                                    |
| crypto_pyaes               | 85.1 ms                                                                                                           | 84.2 ms: 1.01x faster                                                                                                   |
| python_startup             | 15.1 ms                                                                                                           | 15.2 ms: 1.00x slower                                                                                                   |
| python_startup_no_site     | 8.66 ms                                                                                                           | 8.74 ms: 1.01x slower                                                                                                   |
| mako                       | 14.0 ms                                                                                                           | 14.1 ms: 1.01x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.17 sec                                                                                                          | 2.21 sec: 1.01x slower                                                                                                  |
| pprint_pformat             | 1.84 sec                                                                                                          | 1.88 sec: 1.02x slower                                                                                                  |
| docutils                   | 2.95 sec                                                                                                          | 3.02 sec: 1.02x slower                                                                                                  |
| regex_dna                  | 240 ms                                                                                                            | 247 ms: 1.03x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                            | 116 ms: 1.03x slower                                                                                                    |
| xml_etree_iterparse        | 143 ms                                                                                                            | 148 ms: 1.04x slower                                                                                                    |
| pprint_safe_repr           | 891 ms                                                                                                            | 926 ms: 1.04x slower                                                                                                    |
| create_gc_cycles           | 3.70 ms                                                                                                           | 3.85 ms: 1.04x slower                                                                                                   |
| logging_silent             | 605 ns                                                                                                            | 631 ns: 1.04x slower                                                                                                    |
| asyncio_tcp                | 534 ms                                                                                                            | 558 ms: 1.04x slower                                                                                                    |
| nbody                      | 122 ms                                                                                                            | 129 ms: 1.06x slower                                                                                                    |
| regex_v8                   | 28.5 ms                                                                                                           | 30.6 ms: 1.07x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                                                            | 711 ms: 1.08x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 651 ms                                                                                                            | 721 ms: 1.11x slower                                                                                                    |
| xml_etree_parse            | 180 ms                                                                                                            | 205 ms: 1.14x slower                                                                                                    |
| regex_effbot               | 3.84 ms                                                                                                           | 4.64 ms: 1.21x slower                                                                                                   |
| pidigits                   | 235 ms                                                                                                            | 292 ms: 1.24x slower                                                                                                    |
| unpack_sequence            | 53.3 ns                                                                                                           | 70.7 ns: 1.33x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (50): bench_mp_pool, richards_super, unpickle_pure_python, comprehensions, scimark_sor, telco, pickle, genshi_text, chaos, sympy_str, pickle_pure_python, typing_runtime_protocols, sqlglot_v2_parse, subparsers, pickle_list, logging_simple, regex_compile, 2to3, scimark_sparse_mat_mult, sqlglot_v2_normalize, xml_etree_generate, dulwich_log, sympy_expand, raytrace, async_tree_none, sqlglot_v2_optimize, mdp, genshi_xml, pycparser, async_tree_io_tg, sympy_integrate, many_optionals, k_core, deltablue, tomli_loads, sphinx, asyncio_websockets, hexiom, float, pylint, shortest_path, pyflate, nqueens, go, connected_components, django_template, json_dumps, sympy_sum, fannkuch, sqlite_synth

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 94.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x