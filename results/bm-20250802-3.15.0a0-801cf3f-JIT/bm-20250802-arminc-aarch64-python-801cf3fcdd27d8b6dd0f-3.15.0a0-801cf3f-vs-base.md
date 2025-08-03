# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.014x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                            | 310 ms: 1.03x slower                                                                                                  |
| docutils       | 2.94 sec                                                                                                          | 3.13 sec: 1.06x slower                                                                                                |
| html5lib       | 60.8 ms                                                                                                           | 64.5 ms: 1.06x slower                                                                                                 |
| sphinx         | 1.13 sec                                                                                                          | 1.16 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.18 sec                                                                                                          | 2.21 sec: 1.01x slower                                                                                                |
| async_tree_none            | 383 ms                                                                                                            | 391 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 662 ms: 1.02x slower                                                                                                  |
| async_tree_io              | 879 ms                                                                                                            | 902 ms: 1.03x slower                                                                                                  |
| async_tree_memoization     | 456 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                  |
| async_tree_memoization_tg  | 451 ms                                                                                                            | 472 ms: 1.05x slower                                                                                                  |
| async_tree_none_tg         | 363 ms                                                                                                            | 385 ms: 1.06x slower                                                                                                  |
| async_generators           | 453 ms                                                                                                            | 485 ms: 1.07x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): asyncio_websockets, coroutines, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                                                                           | 82.9 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                                                                            | 218 ms: 1.02x faster                                                                                                  |
| regex_effbot   | 3.86 ms                                                                                                           | 3.79 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|---------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads         | 2.45 sec                                                                                                          | 2.31 sec: 1.06x faster                                                                                                |
| pickle              | 15.7 us                                                                                                           | 15.3 us: 1.03x faster                                                                                                 |
| xml_etree_process   | 78.6 ms                                                                                                           | 77.3 ms: 1.02x faster                                                                                                 |
| xml_etree_iterparse | 141 ms                                                                                                            | 145 ms: 1.03x slower                                                                                                  |
| Geometric mean      | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (10): unpickle_pure_python, json_dumps, unpickle, xml_etree_generate, unpickle_list, pickle_dict, xml_etree_parse, json_loads, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup | 15.1 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                                                           | 12.9 ms: 1.07x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| richards_super             | 63.2 ms                                                                                                           | 50.8 ms: 1.24x faster                                                                                                 |
| richards                   | 53.5 ms                                                                                                           | 44.4 ms: 1.20x faster                                                                                                 |
| mako                       | 13.8 ms                                                                                                           | 12.9 ms: 1.07x faster                                                                                                 |
| tomli_loads                | 2.45 sec                                                                                                          | 2.31 sec: 1.06x faster                                                                                                |
| thrift                     | 980 us                                                                                                            | 935 us: 1.05x faster                                                                                                  |
| scimark_fft                | 422 ms                                                                                                            | 405 ms: 1.04x faster                                                                                                  |
| sqlite_synth               | 3.75 us                                                                                                           | 3.64 us: 1.03x faster                                                                                                 |
| pickle                     | 15.7 us                                                                                                           | 15.3 us: 1.03x faster                                                                                                 |
| float                      | 84.7 ms                                                                                                           | 82.9 ms: 1.02x faster                                                                                                 |
| regex_dna                  | 222 ms                                                                                                            | 218 ms: 1.02x faster                                                                                                  |
| xml_etree_process          | 78.6 ms                                                                                                           | 77.3 ms: 1.02x faster                                                                                                 |
| regex_effbot               | 3.86 ms                                                                                                           | 3.79 ms: 1.02x faster                                                                                                 |
| spectral_norm              | 118 ms                                                                                                            | 117 ms: 1.01x faster                                                                                                  |
| python_startup             | 15.1 ms                                                                                                           | 15.2 ms: 1.01x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.18 sec                                                                                                          | 2.21 sec: 1.01x slower                                                                                                |
| async_tree_none            | 383 ms                                                                                                            | 391 ms: 1.02x slower                                                                                                  |
| sphinx                     | 1.13 sec                                                                                                          | 1.16 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 662 ms: 1.02x slower                                                                                                  |
| async_tree_io              | 879 ms                                                                                                            | 902 ms: 1.03x slower                                                                                                  |
| sympy_sum                  | 142 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| xml_etree_iterparse        | 141 ms                                                                                                            | 145 ms: 1.03x slower                                                                                                  |
| 2to3                       | 301 ms                                                                                                            | 310 ms: 1.03x slower                                                                                                  |
| pathlib                    | 21.7 ms                                                                                                           | 22.4 ms: 1.03x slower                                                                                                 |
| async_tree_memoization     | 456 ms                                                                                                            | 472 ms: 1.03x slower                                                                                                  |
| pyflate                    | 515 ms                                                                                                            | 533 ms: 1.03x slower                                                                                                  |
| shortest_path              | 585 ms                                                                                                            | 606 ms: 1.04x slower                                                                                                  |
| k_core                     | 2.77 sec                                                                                                          | 2.87 sec: 1.04x slower                                                                                                |
| nqueens                    | 98.2 ms                                                                                                           | 102 ms: 1.04x slower                                                                                                  |
| raytrace                   | 323 ms                                                                                                            | 336 ms: 1.04x slower                                                                                                  |
| connected_components       | 553 ms                                                                                                            | 577 ms: 1.04x slower                                                                                                  |
| async_tree_memoization_tg  | 451 ms                                                                                                            | 472 ms: 1.05x slower                                                                                                  |
| scimark_lu                 | 142 ms                                                                                                            | 149 ms: 1.05x slower                                                                                                  |
| sympy_expand               | 463 ms                                                                                                            | 487 ms: 1.05x slower                                                                                                  |
| crypto_pyaes               | 84.1 ms                                                                                                           | 89.0 ms: 1.06x slower                                                                                                 |
| sqlglot_v2_parse           | 1.44 ms                                                                                                           | 1.53 ms: 1.06x slower                                                                                                 |
| html5lib                   | 60.8 ms                                                                                                           | 64.5 ms: 1.06x slower                                                                                                 |
| async_tree_none_tg         | 363 ms                                                                                                            | 385 ms: 1.06x slower                                                                                                  |
| typing_runtime_protocols   | 195 us                                                                                                            | 207 us: 1.06x slower                                                                                                  |
| docutils                   | 2.94 sec                                                                                                          | 3.13 sec: 1.06x slower                                                                                                |
| async_generators           | 453 ms                                                                                                            | 485 ms: 1.07x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                           | 1.87 ms: 1.07x slower                                                                                                 |
| pycparser                  | 1.24 sec                                                                                                          | 1.33 sec: 1.07x slower                                                                                                |
| hexiom                     | 6.92 ms                                                                                                           | 7.58 ms: 1.10x slower                                                                                                 |
| comprehensions             | 19.9 us                                                                                                           | 22.6 us: 1.14x slower                                                                                                 |
| go                         | 128 ms                                                                                                            | 154 ms: 1.20x slower                                                                                                  |
| pprint_pformat             | 1.82 sec                                                                                                          | 2.32 sec: 1.27x slower                                                                                                |
| pprint_safe_repr           | 896 ms                                                                                                            | 1.15 sec: 1.28x slower                                                                                                |
| unpack_sequence            | 49.6 ns                                                                                                           | 71.8 ns: 1.45x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (55): regex_v8, unpickle_pure_python, genshi_text, dulwich_log, scimark_sparse_mat_mult, json_dumps, unpickle, asyncio_websockets, deltablue, sympy_str, xml_etree_generate, bpe_tokeniser, logging_format, coroutines, logging_simple, unpickle_list, chaos, pidigits, pickle_dict, djangocms, xml_etree_parse, coverage, python_startup_no_site, deepcopy, json, django_template, scimark_monte_carlo, json_loads, pickle_pure_python, async_tree_io_tg, deepcopy_memo, sqlglot_v2_optimize, mdp, async_tree_cpu_io_mixed, deepcopy_reduce, subparsers, scimark_sor, create_gc_cycles, fannkuch, bench_thread_pool, pickle_list, telco, gc_traversal, pylint, asyncio_tcp, nbody, sqlglot_v2_normalize, generators, logging_silent, sympy_integrate, meteor_contest, many_optionals, regex_compile, genshi_xml, bench_mp_pool

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x