# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-aarch64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.004x slower
- HPT reliability: 69.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                         |
| Geometric mean | (ref)                                                    | 1.02x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 512 ms: 1.29x faster                                                           |
| async_tree_memoization     | 664 ms                                                   | 518 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 1.16 sec                                                 | 947 ms: 1.23x faster                                                           |
| async_tree_none            | 504 ms                                                   | 414 ms: 1.22x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 958 ms: 1.19x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 409 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                           |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                                   |

Benchmark hidden because not significant (3): async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                                          |
| nbody          | 118 ms                                                   | 132 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                          |
| regex_dna      | 263 ms                                                   | 252 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                    | 1.09x faster                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 159 ms                                                   | 148 ms: 1.07x faster                                                           |
| tomli_loads          | 2.67 sec                                                 | 2.55 sec: 1.04x faster                                                         |
| unpickle_pure_python | 265 us                                                   | 284 us: 1.07x slower                                                           |
| json_loads           | 32.8 us                                                  | 35.9 us: 1.09x slower                                                          |
| pickle_pure_python   | 374 us                                                   | 411 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.6 ms: 1.04x slower                                                          |
| python_startup_no_site | 8.79 ms                                                  | 9.15 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 41.9 ms: 1.06x slower                                                          |
| genshi_xml      | 61.6 ms                                                  | 65.9 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 339 us: 1.41x faster                                                           |
| deepcopy_memo              | 53.0 us                                                  | 40.0 us: 1.33x faster                                                          |
| async_tree_memoization_tg  | 663 ms                                                   | 512 ms: 1.29x faster                                                           |
| async_tree_memoization     | 664 ms                                                   | 518 ms: 1.28x faster                                                           |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                          |
| async_tree_io_tg           | 1.16 sec                                                 | 947 ms: 1.23x faster                                                           |
| async_tree_none            | 504 ms                                                   | 414 ms: 1.22x faster                                                           |
| async_tree_io              | 1.14 sec                                                 | 958 ms: 1.19x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 409 ms: 1.18x faster                                                           |
| spectral_norm              | 143 ms                                                   | 123 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 4.24 us                                                  | 3.64 us: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                           |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                           |
| float                      | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                           |
| thrift                     | 1.01 ms                                                  | 919 us: 1.10x faster                                                           |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                          |
| scimark_fft                | 463 ms                                                   | 429 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                           |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 6.02 sec                                                 | 5.76 sec: 1.04x faster                                                         |
| regex_dna                  | 263 ms                                                   | 252 ms: 1.04x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.55 sec: 1.04x faster                                                         |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                           |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                                           |
| mdp                        | 3.45 sec                                                 | 3.56 sec: 1.03x slower                                                         |
| python_startup             | 16.0 ms                                                  | 16.6 ms: 1.04x slower                                                          |
| logging_silent             | 135 ns                                                   | 140 ns: 1.04x slower                                                           |
| python_startup_no_site     | 8.79 ms                                                  | 9.15 ms: 1.04x slower                                                          |
| deltablue                  | 3.97 ms                                                  | 4.15 ms: 1.05x slower                                                          |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.06x slower                                                         |
| django_template            | 39.4 ms                                                  | 41.9 ms: 1.06x slower                                                          |
| sympy_expand               | 472 ms                                                   | 503 ms: 1.06x slower                                                           |
| genshi_xml                 | 61.6 ms                                                  | 65.9 ms: 1.07x slower                                                          |
| unpickle_pure_python       | 265 us                                                   | 284 us: 1.07x slower                                                           |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                                           |
| raytrace                   | 310 ms                                                   | 335 ms: 1.08x slower                                                           |
| sympy_str                  | 265 ms                                                   | 288 ms: 1.09x slower                                                           |
| docutils                   | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                         |
| json_loads                 | 32.8 us                                                  | 35.9 us: 1.09x slower                                                          |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                          |
| pickle_pure_python         | 374 us                                                   | 411 us: 1.10x slower                                                           |
| sqlglot_parse              | 1.43 ms                                                  | 1.58 ms: 1.10x slower                                                          |
| nbody                      | 118 ms                                                   | 132 ms: 1.11x slower                                                           |
| typing_runtime_protocols   | 197 us                                                   | 220 us: 1.12x slower                                                           |
| fannkuch                   | 478 ms                                                   | 544 ms: 1.14x slower                                                           |
| crypto_pyaes               | 84.9 ms                                                  | 98.7 ms: 1.16x slower                                                          |
| gc_traversal               | 5.92 ms                                                  | 6.93 ms: 1.17x slower                                                          |
| comprehensions             | 20.8 us                                                  | 24.4 us: 1.17x slower                                                          |
| nqueens                    | 105 ms                                                   | 127 ms: 1.21x slower                                                           |
| hexiom                     | 7.34 ms                                                  | 9.15 ms: 1.25x slower                                                          |
| subparsers                 | 20.3 ms                                                  | 26.3 ms: 1.29x slower                                                          |
| pprint_pformat             | 1.99 sec                                                 | 2.77 sec: 1.39x slower                                                         |
| pprint_safe_repr           | 962 ms                                                   | 1.35 sec: 1.40x slower                                                         |
| many_optionals             | 626 us                                                   | 895 us: 1.43x slower                                                           |
| bench_mp_pool              | 8.07 ms                                                  | 2.14 sec: 264.98x slower                                                       |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                                   |

Benchmark hidden because not significant (39): pylint, telco, pathlib, scimark_lu, scimark_monte_carlo, richards, regex_compile, chaos, logging_format, regex_v8, sqlite_synth, html5lib, xml_etree_generate, k_core, async_generators, sqlalchemy_declarative, coroutines, scimark_sor, pidigits, sphinx, xml_etree_process, pyflate, asyncio_websockets, logging_simple, richards_super, bench_thread_pool, 2to3, mako, sqlglot_normalize, sqlglot_optimize, genshi_text, sympy_integrate, json, sqlglot_transpile, json_dumps, scimark_sparse_mat_mult, sympy_sum, go, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: dulwich_log

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 69.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x