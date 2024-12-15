# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.047x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| docutils       | 3.05 sec                                                                                                            | 3.18 sec: 1.04x slower                                                                                                  |
| html5lib       | 64.6 ms                                                                                                             | 71.4 ms: 1.11x slower                                                                                                   |
| sphinx         | 1.19 sec                                                                                                            | 1.26 sec: 1.06x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators | 501 ms                                                                                                              | 540 ms: 1.08x slower                                                                                                    |
| Geometric mean   | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (10): asyncio_websockets, coroutines, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                                                              | 145 ms: 1.10x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads    | 2.70 sec                                                                                                            | 2.52 sec: 1.07x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (8): json_dumps, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, unpickle_pure_python, json_loads, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 42.7 ms                                                                                                             | 49.1 ms: 1.15x slower                                                                                                   |
| genshi_text     | 28.1 ms                                                                                                             | 34.5 ms: 1.23x slower                                                                                                   |
| genshi_xml      | 62.2 ms                                                                                                             | 80.3 ms: 1.29x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.16x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool           | 6.14 sec                                                                                                            | 1.51 sec: 4.06x faster                                                                                                  |
| tomli_loads             | 2.70 sec                                                                                                            | 2.52 sec: 1.07x faster                                                                                                  |
| deepcopy_memo           | 42.7 us                                                                                                             | 40.1 us: 1.07x faster                                                                                                   |
| bpe_tokeniser           | 5.74 sec                                                                                                            | 5.80 sec: 1.01x slower                                                                                                  |
| k_core                  | 2.86 sec                                                                                                            | 2.94 sec: 1.03x slower                                                                                                  |
| subparsers              | 25.8 ms                                                                                                             | 26.6 ms: 1.03x slower                                                                                                   |
| mypy2                   | 1.05 sec                                                                                                            | 1.08 sec: 1.03x slower                                                                                                  |
| docutils                | 3.05 sec                                                                                                            | 3.18 sec: 1.04x slower                                                                                                  |
| json                    | 5.61 ms                                                                                                             | 5.86 ms: 1.05x slower                                                                                                   |
| connected_components    | 536 ms                                                                                                              | 564 ms: 1.05x slower                                                                                                    |
| mdp                     | 3.38 sec                                                                                                            | 3.58 sec: 1.06x slower                                                                                                  |
| sphinx                  | 1.19 sec                                                                                                            | 1.26 sec: 1.06x slower                                                                                                  |
| meteor_contest          | 118 ms                                                                                                              | 125 ms: 1.06x slower                                                                                                    |
| sympy_expand            | 484 ms                                                                                                              | 517 ms: 1.07x slower                                                                                                    |
| scimark_lu              | 139 ms                                                                                                              | 149 ms: 1.07x slower                                                                                                    |
| deltablue               | 4.01 ms                                                                                                             | 4.30 ms: 1.07x slower                                                                                                   |
| pyflate                 | 561 ms                                                                                                              | 603 ms: 1.07x slower                                                                                                    |
| async_generators        | 501 ms                                                                                                              | 540 ms: 1.08x slower                                                                                                    |
| sympy_str               | 278 ms                                                                                                              | 300 ms: 1.08x slower                                                                                                    |
| deepcopy                | 353 us                                                                                                              | 383 us: 1.09x slower                                                                                                    |
| crypto_pyaes            | 85.2 ms                                                                                                             | 92.9 ms: 1.09x slower                                                                                                   |
| fannkuch                | 477 ms                                                                                                              | 522 ms: 1.10x slower                                                                                                    |
| sympy_sum               | 145 ms                                                                                                              | 159 ms: 1.10x slower                                                                                                    |
| logging_format          | 8.02 us                                                                                                             | 8.79 us: 1.10x slower                                                                                                   |
| regex_compile           | 131 ms                                                                                                              | 145 ms: 1.10x slower                                                                                                    |
| html5lib                | 64.6 ms                                                                                                             | 71.4 ms: 1.11x slower                                                                                                   |
| pathlib                 | 21.8 ms                                                                                                             | 24.1 ms: 1.11x slower                                                                                                   |
| scimark_sparse_mat_mult | 6.28 ms                                                                                                             | 6.95 ms: 1.11x slower                                                                                                   |
| deepcopy_reduce         | 3.65 us                                                                                                             | 4.05 us: 1.11x slower                                                                                                   |
| sqlalchemy_imperative   | 15.5 ms                                                                                                             | 17.4 ms: 1.12x slower                                                                                                   |
| raytrace                | 324 ms                                                                                                              | 363 ms: 1.12x slower                                                                                                    |
| dulwich_log             | 62.3 ms                                                                                                             | 70.0 ms: 1.12x slower                                                                                                   |
| spectral_norm           | 130 ms                                                                                                              | 146 ms: 1.12x slower                                                                                                    |
| pycparser               | 1.26 sec                                                                                                            | 1.44 sec: 1.14x slower                                                                                                  |
| chaos                   | 73.7 ms                                                                                                             | 84.6 ms: 1.15x slower                                                                                                   |
| django_template         | 42.7 ms                                                                                                             | 49.1 ms: 1.15x slower                                                                                                   |
| many_optionals          | 715 us                                                                                                              | 841 us: 1.18x slower                                                                                                    |
| go                      | 144 ms                                                                                                              | 172 ms: 1.19x slower                                                                                                    |
| pylint                  | 306 ms                                                                                                              | 365 ms: 1.19x slower                                                                                                    |
| comprehensions          | 21.2 us                                                                                                             | 25.5 us: 1.20x slower                                                                                                   |
| genshi_text             | 28.1 ms                                                                                                             | 34.5 ms: 1.23x slower                                                                                                   |
| hexiom                  | 7.45 ms                                                                                                             | 9.28 ms: 1.24x slower                                                                                                   |
| nqueens                 | 103 ms                                                                                                              | 131 ms: 1.27x slower                                                                                                    |
| genshi_xml              | 62.2 ms                                                                                                             | 80.3 ms: 1.29x slower                                                                                                   |
| pprint_safe_repr        | 997 ms                                                                                                              | 1.31 sec: 1.31x slower                                                                                                  |
| pprint_pformat          | 2.05 sec                                                                                                            | 2.69 sec: 1.31x slower                                                                                                  |
| generators              | 36.6 ms                                                                                                             | 49.7 ms: 1.36x slower                                                                                                   |
| Geometric mean          | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (51): create_gc_cycles, nbody, json_dumps, gc_traversal, regex_effbot, float, sqlite_synth, mako, scimark_monte_carlo, xml_etree_generate, djangocms, xml_etree_iterparse, richards, scimark_sor, xml_etree_parse, python_startup, python_startup_no_site, unpickle_pure_python, regex_dna, json_loads, pidigits, asyncio_websockets, telco, sqlalchemy_declarative, xml_etree_process, coroutines, async_tree_none_tg, async_tree_io, async_tree_none, scimark_fft, regex_v8, shortest_path, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, coverage, logging_silent, async_tree_memoization_tg, bench_thread_pool, logging_simple, sympy_integrate, pickle_pure_python, 2to3, richards_super, thrift, sqlglot_parse, sqlglot_normalize, typing_runtime_protocols, sqlglot_transpile, sqlglot_optimize

- Geometric mean (including insignificant results): 1.047x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.02x