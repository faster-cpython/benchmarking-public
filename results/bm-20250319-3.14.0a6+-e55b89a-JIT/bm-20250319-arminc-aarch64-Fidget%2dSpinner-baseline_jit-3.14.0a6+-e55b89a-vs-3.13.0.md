# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-aarch64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.016x faster
- HPT reliability: 65.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 307 ms: 1.02x faster                                                       |
| docutils       | 2.96 sec                                                 | 3.10 sec: 1.05x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                                       |
| async_tree_memoization     | 664 ms                                                   | 485 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                       |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 1.16 sec                                                 | 921 ms: 1.26x faster                                                       |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                       |
| async_generators           | 500 ms                                                   | 470 ms: 1.06x faster                                                       |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.9 ms: 1.07x faster                                                      |
| nbody          | 118 ms                                                   | 127 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                    | 1.00x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                      |
| regex_v8       | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                      |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                    | 1.12x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 174 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.13x faster                                                       |
| tomli_loads          | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                     |
| pickle_pure_python   | 374 us                                                   | 400 us: 1.07x slower                                                       |
| unpickle_pure_python | 265 us                                                   | 293 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_generate, json_dumps, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.9 ms: 1.04x slower                                                      |
| mako            | 14.0 ms                                                  | 15.0 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 340 us: 1.41x faster                                                       |
| async_tree_memoization_tg  | 663 ms                                                   | 477 ms: 1.39x faster                                                       |
| deepcopy_memo              | 53.0 us                                                  | 38.3 us: 1.38x faster                                                      |
| async_tree_memoization     | 664 ms                                                   | 485 ms: 1.37x faster                                                       |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                       |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 1.16 sec                                                 | 921 ms: 1.26x faster                                                       |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                       |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 4.24 us                                                  | 3.55 us: 1.20x faster                                                      |
| regex_v8                   | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 668 ms: 1.18x faster                                                       |
| xml_etree_parse            | 203 ms                                                   | 174 ms: 1.17x faster                                                       |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                       |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                      |
| tomli_loads                | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                     |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.10x faster                                                       |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                                       |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.09x faster                                                      |
| pylint                     | 345 ms                                                   | 319 ms: 1.08x faster                                                       |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                                       |
| coverage                   | 106 ms                                                   | 98.3 ms: 1.07x faster                                                      |
| float                      | 95.8 ms                                                  | 89.9 ms: 1.07x faster                                                      |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                      |
| thrift                     | 1.01 ms                                                  | 949 us: 1.06x faster                                                       |
| async_generators           | 500 ms                                                   | 470 ms: 1.06x faster                                                       |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                                       |
| go                         | 164 ms                                                   | 156 ms: 1.05x faster                                                       |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.98 us: 1.04x faster                                                      |
| mdp                        | 3.45 sec                                                 | 3.35 sec: 1.03x faster                                                     |
| logging_silent             | 135 ns                                                   | 131 ns: 1.02x faster                                                       |
| bpe_tokeniser              | 6.02 sec                                                 | 5.88 sec: 1.02x faster                                                     |
| 2to3                       | 313 ms                                                   | 307 ms: 1.02x faster                                                       |
| richards                   | 54.5 ms                                                  | 53.6 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.99 sec                                                 | 2.04 sec: 1.03x slower                                                     |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                       |
| pyflate                    | 582 ms                                                   | 597 ms: 1.03x slower                                                       |
| sympy_expand               | 472 ms                                                   | 488 ms: 1.03x slower                                                       |
| django_template            | 39.4 ms                                                  | 40.9 ms: 1.04x slower                                                      |
| connected_components       | 547 ms                                                   | 568 ms: 1.04x slower                                                       |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.04x slower                                                       |
| docutils                   | 2.96 sec                                                 | 3.10 sec: 1.05x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.05x slower                                                     |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                                       |
| chaos                      | 70.7 ms                                                  | 75.5 ms: 1.07x slower                                                      |
| pickle_pure_python         | 374 us                                                   | 400 us: 1.07x slower                                                       |
| mako                       | 14.0 ms                                                  | 15.0 ms: 1.07x slower                                                      |
| nbody                      | 118 ms                                                   | 127 ms: 1.07x slower                                                       |
| create_gc_cycles           | 3.39 ms                                                  | 3.67 ms: 1.08x slower                                                      |
| deltablue                  | 3.97 ms                                                  | 4.34 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 197 us                                                   | 216 us: 1.10x slower                                                       |
| fannkuch                   | 478 ms                                                   | 528 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 265 us                                                   | 293 us: 1.11x slower                                                       |
| crypto_pyaes               | 84.9 ms                                                  | 94.3 ms: 1.11x slower                                                      |
| gc_traversal               | 5.92 ms                                                  | 6.61 ms: 1.12x slower                                                      |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                      |
| hexiom                     | 7.34 ms                                                  | 8.74 ms: 1.19x slower                                                      |
| comprehensions             | 20.8 us                                                  | 27.7 us: 1.33x slower                                                      |
| subparsers                 | 20.3 ms                                                  | 27.2 ms: 1.34x slower                                                      |
| many_optionals             | 626 us                                                   | 883 us: 1.41x slower                                                       |
| bench_mp_pool              | 8.07 ms                                                  | 2.37 sec: 293.56x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                               |

Benchmark hidden because not significant (28): logging_format, xml_etree_generate, genshi_text, sympy_sum, json_dumps, pidigits, regex_compile, sphinx, sqlalchemy_declarative, telco, asyncio_websockets, pycparser, genshi_xml, json, coroutines, xml_etree_process, nqueens, richards_super, meteor_contest, python_startup, sqlalchemy_imperative, html5lib, scimark_lu, sympy_integrate, bench_thread_pool, json_loads, scimark_monte_carlo, scimark_sparse_mat_mult
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 65.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x