# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.043x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 305 ms: 1.03x faster                                                               |
| html5lib       | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                              |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                             |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                               |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                               |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 896 ms: 1.30x faster                                                               |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                               |
| async_generators           | 500 ms                                                   | 427 ms: 1.17x faster                                                               |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                       |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                                              |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                       |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                              |
| regex_v8       | 32.5 ms                                                  | 29.8 ms: 1.09x faster                                                              |
| regex_dna      | 263 ms                                                   | 242 ms: 1.08x faster                                                               |
| Geometric mean | (ref)                                                    | 1.12x faster                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                                               |
| xml_etree_generate  | 118 ms                                                   | 106 ms: 1.12x faster                                                               |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                               |
| xml_etree_process   | 82.1 ms                                                  | 75.7 ms: 1.08x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                             |
| pickle_pure_python  | 374 us                                                   | 407 us: 1.09x slower                                                               |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                       |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                              |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                              |
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                              |
| genshi_xml     | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 320 us: 1.50x faster                                                               |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                               |
| async_tree_memoization     | 664 ms                                                   | 478 ms: 1.39x faster                                                               |
| async_tree_none            | 504 ms                                                   | 379 ms: 1.33x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 896 ms: 1.30x faster                                                               |
| regex_effbot               | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                               |
| spectral_norm              | 143 ms                                                   | 113 ms: 1.27x faster                                                               |
| deepcopy_reduce            | 4.24 us                                                  | 3.38 us: 1.26x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                               |
| go                         | 164 ms                                                   | 138 ms: 1.19x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 662 ms: 1.19x faster                                                               |
| async_generators           | 500 ms                                                   | 427 ms: 1.17x faster                                                               |
| float                      | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                               |
| xml_etree_generate         | 118 ms                                                   | 106 ms: 1.12x faster                                                               |
| scimark_fft                | 463 ms                                                   | 415 ms: 1.11x faster                                                               |
| generators                 | 40.3 ms                                                  | 36.2 ms: 1.11x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                               |
| pylint                     | 345 ms                                                   | 313 ms: 1.10x faster                                                               |
| telco                      | 10.5 ms                                                  | 9.52 ms: 1.10x faster                                                              |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                               |
| regex_v8                   | 32.5 ms                                                  | 29.8 ms: 1.09x faster                                                              |
| xml_etree_process          | 82.1 ms                                                  | 75.7 ms: 1.08x faster                                                              |
| regex_dna                  | 263 ms                                                   | 242 ms: 1.08x faster                                                               |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                              |
| logging_format             | 8.10 us                                                  | 7.53 us: 1.08x faster                                                              |
| thrift                     | 1.01 ms                                                  | 940 us: 1.08x faster                                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 5.60 sec: 1.07x faster                                                             |
| genshi_text                | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                             |
| coverage                   | 106 ms                                                   | 99.6 ms: 1.06x faster                                                              |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                              |
| chaos                      | 70.7 ms                                                  | 67.0 ms: 1.05x faster                                                              |
| html5lib                   | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                              |
| logging_simple             | 7.25 us                                                  | 6.88 us: 1.05x faster                                                              |
| pyflate                    | 582 ms                                                   | 553 ms: 1.05x faster                                                               |
| richards                   | 54.5 ms                                                  | 52.0 ms: 1.05x faster                                                              |
| sqlalchemy_declarative     | 154 ms                                                   | 147 ms: 1.05x faster                                                               |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.04x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                             |
| mdp                        | 3.45 sec                                                 | 3.33 sec: 1.04x faster                                                             |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                               |
| 2to3                       | 313 ms                                                   | 305 ms: 1.03x faster                                                               |
| genshi_xml                 | 61.6 ms                                                  | 60.4 ms: 1.02x faster                                                              |
| sympy_str                  | 265 ms                                                   | 269 ms: 1.01x slower                                                               |
| meteor_contest             | 117 ms                                                   | 121 ms: 1.03x slower                                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.51 ms: 1.03x slower                                                              |
| sqlalchemy_imperative      | 16.1 ms                                                  | 16.9 ms: 1.05x slower                                                              |
| typing_runtime_protocols   | 197 us                                                   | 211 us: 1.07x slower                                                               |
| sqlglot_parse              | 1.43 ms                                                  | 1.54 ms: 1.08x slower                                                              |
| pickle_pure_python         | 374 us                                                   | 407 us: 1.09x slower                                                               |
| fannkuch                   | 478 ms                                                   | 529 ms: 1.11x slower                                                               |
| gc_traversal               | 5.92 ms                                                  | 6.67 ms: 1.13x slower                                                              |
| comprehensions             | 20.8 us                                                  | 23.6 us: 1.13x slower                                                              |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                              |
| crypto_pyaes               | 84.9 ms                                                  | 102 ms: 1.20x slower                                                               |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.25x slower                                                              |
| many_optionals             | 626 us                                                   | 856 us: 1.37x slower                                                               |
| bench_mp_pool              | 8.07 ms                                                  | 548 ms: 67.96x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                                       |

Benchmark hidden because not significant (27): json_dumps, regex_compile, scimark_monte_carlo, richards_super, coroutines, json, sympy_sum, sympy_integrate, scimark_lu, asyncio_websockets, hexiom, django_template, bench_thread_pool, sympy_expand, python_startup, connected_components, raytrace, shortest_path, pidigits, scimark_sparse_mat_mult, nqueens, pycparser, deltablue, sqlglot_transpile, nbody, unpickle_pure_python, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
Ignored benchmarks (1) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: dulwich_log

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x