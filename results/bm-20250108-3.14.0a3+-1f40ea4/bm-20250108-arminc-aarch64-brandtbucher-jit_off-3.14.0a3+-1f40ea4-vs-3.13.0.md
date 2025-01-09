# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_off
- machine: linux-aarch64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                              |
| async_tree_memoization     | 664 ms                                                   | 492 ms: 1.35x faster                                              |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                              |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                              |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.9 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                             |
| regex_dna      | 263 ms                                                   | 244 ms: 1.08x faster                                              |
| regex_compile  | 134 ms                                                   | 126 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                    | 1.11x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                              |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                              |
| tomli_loads         | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                            |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                      |

Benchmark hidden because not significant (6): json_loads, unpickle_pure_python, xml_etree_generate, xml_etree_process, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.07 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 27.3 ms: 1.04x faster                                             |
| django_template | 39.4 ms                                                  | 42.2 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                      |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                              |
| async_tree_memoization     | 664 ms                                                   | 492 ms: 1.35x faster                                              |
| deepcopy                   | 479 us                                                   | 355 us: 1.35x faster                                              |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                              |
| regex_effbot               | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                              |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                              |
| deepcopy_memo              | 53.0 us                                                  | 41.7 us: 1.27x faster                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                              |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.72 us: 1.14x faster                                             |
| go                         | 164 ms                                                   | 147 ms: 1.12x faster                                              |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                              |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.10x faster                                             |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.10x faster                                              |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                              |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                              |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                             |
| json                       | 5.94 ms                                                  | 5.51 ms: 1.08x faster                                             |
| regex_dna                  | 263 ms                                                   | 244 ms: 1.08x faster                                              |
| thrift                     | 1.01 ms                                                  | 940 us: 1.08x faster                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.24 ms: 1.07x faster                                             |
| float                      | 95.8 ms                                                  | 89.9 ms: 1.06x faster                                             |
| telco                      | 10.5 ms                                                  | 9.82 ms: 1.06x faster                                             |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                            |
| regex_compile              | 134 ms                                                   | 126 ms: 1.06x faster                                              |
| scimark_sor                | 164 ms                                                   | 156 ms: 1.05x faster                                              |
| genshi_text                | 28.6 ms                                                  | 27.3 ms: 1.04x faster                                             |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.04x faster                                            |
| tomli_loads                | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.84 sec: 1.03x faster                                            |
| pyflate                    | 582 ms                                                   | 566 ms: 1.03x faster                                              |
| python_startup_no_site     | 8.79 ms                                                  | 9.07 ms: 1.03x slower                                             |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.62 ms: 1.07x slower                                             |
| django_template            | 39.4 ms                                                  | 42.2 ms: 1.07x slower                                             |
| sympy_str                  | 265 ms                                                   | 287 ms: 1.08x slower                                              |
| many_optionals             | 626 us                                                   | 729 us: 1.16x slower                                              |
| gc_traversal               | 5.92 ms                                                  | 6.96 ms: 1.17x slower                                             |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                             |
| bench_mp_pool              | 8.07 ms                                                  | 5.05 sec: 626.04x slower                                          |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                      |

Benchmark hidden because not significant (52): scimark_lu, sqlglot_transpile, sympy_sum, html5lib, sqlglot_optimize, scimark_monte_carlo, richards, sqlalchemy_declarative, json_loads, crypto_pyaes, 2to3, richards_super, sphinx, regex_v8, sqlglot_normalize, mdp, asyncio_websockets, pprint_safe_repr, unpickle_pure_python, shortest_path, bench_thread_pool, xml_etree_generate, pprint_pformat, connected_components, sqlite_synth, coverage, deltablue, nqueens, comprehensions, docutils, xml_etree_process, async_generators, pidigits, meteor_contest, coroutines, mako, logging_format, logging_simple, logging_silent, fannkuch, hexiom, sqlglot_parse, python_startup, sympy_integrate, sqlalchemy_imperative, sympy_expand, genshi_xml, json_dumps, nbody, chaos, raytrace, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: dulwich_log

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x