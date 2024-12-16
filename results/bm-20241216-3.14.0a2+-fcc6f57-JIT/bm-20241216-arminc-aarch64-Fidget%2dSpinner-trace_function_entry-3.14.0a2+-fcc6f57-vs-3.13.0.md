# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.002x slower
- HPT reliability: 74.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.22 sec: 1.09x slower                                                             |
| html5lib       | 65.6 ms                                                  | 72.0 ms: 1.10x slower                                                              |
| Geometric mean | (ref)                                                    | 1.05x slower                                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                               |
| async_tree_memoization     | 664 ms                                                   | 516 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                               |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                               |
| async_tree_io              | 1.14 sec                                                 | 920 ms: 1.24x faster                                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 687 ms: 1.17x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                                               |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                                       |

Benchmark hidden because not significant (3): async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                              |
| Geometric mean | (ref)                                                    | 1.06x faster                                                                       |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                               |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                               |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.08x faster                                                               |
| xml_etree_process   | 82.1 ms                                                  | 78.0 ms: 1.05x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                                             |
| pickle_pure_python  | 374 us                                                   | 431 us: 1.15x slower                                                               |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                                       |

Benchmark hidden because not significant (3): json_loads, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 43.2 ms: 1.10x slower                                                              |
| genshi_xml      | 61.6 ms                                                  | 70.1 ms: 1.14x slower                                                              |
| Geometric mean  | (ref)                                                    | 1.06x slower                                                                       |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                               |
| deepcopy                   | 479 us                                                   | 350 us: 1.37x faster                                                               |
| async_tree_memoization     | 664 ms                                                   | 516 ms: 1.29x faster                                                               |
| deepcopy_memo              | 53.0 us                                                  | 41.4 us: 1.28x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                               |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                              |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                               |
| async_tree_io              | 1.14 sec                                                 | 920 ms: 1.24x faster                                                               |
| deepcopy_reduce            | 4.24 us                                                  | 3.64 us: 1.17x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 687 ms: 1.17x faster                                                               |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                                               |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                               |
| go                         | 164 ms                                                   | 150 ms: 1.10x faster                                                               |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.4 ms: 1.09x faster                                                              |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                                               |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                               |
| generators                 | 40.3 ms                                                  | 37.2 ms: 1.08x faster                                                              |
| pylint                     | 345 ms                                                   | 319 ms: 1.08x faster                                                               |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                                               |
| telco                      | 10.5 ms                                                  | 9.78 ms: 1.07x faster                                                              |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.06x faster                                                              |
| json                       | 5.94 ms                                                  | 5.63 ms: 1.05x faster                                                              |
| xml_etree_process          | 82.1 ms                                                  | 78.0 ms: 1.05x faster                                                              |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 5.76 sec: 1.04x faster                                                             |
| k_core                     | 2.99 sec                                                 | 2.90 sec: 1.03x faster                                                             |
| tomli_loads                | 2.67 sec                                                 | 2.59 sec: 1.03x faster                                                             |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                               |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                               |
| logging_silent             | 135 ns                                                   | 140 ns: 1.04x slower                                                               |
| logging_simple             | 7.25 us                                                  | 7.60 us: 1.05x slower                                                              |
| meteor_contest             | 117 ms                                                   | 123 ms: 1.05x slower                                                               |
| logging_format             | 8.10 us                                                  | 8.54 us: 1.05x slower                                                              |
| sqlglot_normalize          | 131 ms                                                   | 139 ms: 1.06x slower                                                               |
| sqlglot_optimize           | 65.2 ms                                                  | 70.2 ms: 1.08x slower                                                              |
| sqlglot_transpile          | 1.84 ms                                                  | 1.98 ms: 1.08x slower                                                              |
| fannkuch                   | 478 ms                                                   | 517 ms: 1.08x slower                                                               |
| docutils                   | 2.96 sec                                                 | 3.22 sec: 1.09x slower                                                             |
| raytrace                   | 310 ms                                                   | 338 ms: 1.09x slower                                                               |
| sympy_str                  | 265 ms                                                   | 289 ms: 1.09x slower                                                               |
| sympy_sum                  | 151 ms                                                   | 165 ms: 1.09x slower                                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                                              |
| django_template            | 39.4 ms                                                  | 43.2 ms: 1.10x slower                                                              |
| html5lib                   | 65.6 ms                                                  | 72.0 ms: 1.10x slower                                                              |
| sympy_expand               | 472 ms                                                   | 522 ms: 1.10x slower                                                               |
| crypto_pyaes               | 84.9 ms                                                  | 94.0 ms: 1.11x slower                                                              |
| pycparser                  | 1.34 sec                                                 | 1.49 sec: 1.11x slower                                                             |
| typing_runtime_protocols   | 197 us                                                   | 220 us: 1.12x slower                                                               |
| sqlglot_parse              | 1.43 ms                                                  | 1.62 ms: 1.13x slower                                                              |
| sqlalchemy_imperative      | 16.1 ms                                                  | 18.3 ms: 1.14x slower                                                              |
| genshi_xml                 | 61.6 ms                                                  | 70.1 ms: 1.14x slower                                                              |
| deltablue                  | 3.97 ms                                                  | 4.56 ms: 1.15x slower                                                              |
| hexiom                     | 7.34 ms                                                  | 8.46 ms: 1.15x slower                                                              |
| pickle_pure_python         | 374 us                                                   | 431 us: 1.15x slower                                                               |
| gc_traversal               | 5.92 ms                                                  | 6.90 ms: 1.16x slower                                                              |
| comprehensions             | 20.8 us                                                  | 24.7 us: 1.18x slower                                                              |
| chaos                      | 70.7 ms                                                  | 87.9 ms: 1.24x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 1.23 sec: 1.28x slower                                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.62 sec: 1.32x slower                                                             |
| many_optionals             | 626 us                                                   | 828 us: 1.32x slower                                                               |
| subparsers                 | 20.3 ms                                                  | 27.6 ms: 1.36x slower                                                              |
| bench_mp_pool              | 8.07 ms                                                  | 984 ms: 121.93x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                                       |

Benchmark hidden because not significant (32): scimark_lu, nbody, float, sqlalchemy_declarative, async_generators, sqlite_synth, json_loads, bench_thread_pool, mdp, scimark_sor, mako, regex_v8, coroutines, asyncio_websockets, 2to3, scimark_sparse_mat_mult, python_startup, pidigits, unpickle_pure_python, regex_compile, genshi_text, djangocms, regex_dna, sphinx, thrift, richards, python_startup_no_site, pyflate, richards_super, json_dumps, sympy_integrate, nqueens
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 74.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x