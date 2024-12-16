# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.014x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| sphinx         | 1.26 sec                                                                 | 1.22 sec: 1.03x faster                                                             |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                       |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_generators | 532 ms                                                                   | 495 ms: 1.07x faster                                                               |
| async_tree_io    | 945 ms                                                                   | 920 ms: 1.03x faster                                                               |
| Geometric mean   | (ref)                                                                    | 1.01x faster                                                                       |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                   | 266 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                       |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_process | 81.2 ms                                                                  | 78.0 ms: 1.04x faster                                                              |
| tomli_loads       | 2.51 sec                                                                 | 2.59 sec: 1.03x slower                                                             |
| Geometric mean    | (ref)                                                                    | 1.00x slower                                                                       |

Benchmark hidden because not significant (7): json_dumps, xml_etree_generate, xml_etree_parse, xml_etree_iterparse, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml      | 80.3 ms                                                                  | 70.1 ms: 1.15x faster                                                              |
| genshi_text     | 32.4 ms                                                                  | 28.8 ms: 1.13x faster                                                              |
| django_template | 48.0 ms                                                                  | 43.2 ms: 1.11x faster                                                              |
| Geometric mean  | (ref)                                                                    | 1.09x faster                                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark             | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| bench_mp_pool         | 1.66 sec                                                                 | 984 ms: 1.69x faster                                                               |
| generators            | 50.7 ms                                                                  | 37.2 ms: 1.36x faster                                                              |
| nqueens               | 130 ms                                                                   | 111 ms: 1.16x faster                                                               |
| genshi_xml            | 80.3 ms                                                                  | 70.1 ms: 1.15x faster                                                              |
| go                    | 171 ms                                                                   | 150 ms: 1.14x faster                                                               |
| deepcopy_reduce       | 4.15 us                                                                  | 3.64 us: 1.14x faster                                                              |
| deepcopy              | 399 us                                                                   | 350 us: 1.14x faster                                                               |
| genshi_text           | 32.4 ms                                                                  | 28.8 ms: 1.13x faster                                                              |
| scimark_lu            | 155 ms                                                                   | 140 ms: 1.11x faster                                                               |
| django_template       | 48.0 ms                                                                  | 43.2 ms: 1.11x faster                                                              |
| hexiom                | 9.31 ms                                                                  | 8.46 ms: 1.10x faster                                                              |
| raytrace              | 370 ms                                                                   | 338 ms: 1.10x faster                                                               |
| async_generators      | 532 ms                                                                   | 495 ms: 1.07x faster                                                               |
| coverage              | 107 ms                                                                   | 101 ms: 1.06x faster                                                               |
| pylint                | 339 ms                                                                   | 319 ms: 1.06x faster                                                               |
| logging_simple        | 7.96 us                                                                  | 7.60 us: 1.05x faster                                                              |
| bench_thread_pool     | 1.39 ms                                                                  | 1.33 ms: 1.05x faster                                                              |
| xml_etree_process     | 81.2 ms                                                                  | 78.0 ms: 1.04x faster                                                              |
| sympy_integrate       | 23.3 ms                                                                  | 22.4 ms: 1.04x faster                                                              |
| mdp                   | 3.56 sec                                                                 | 3.43 sec: 1.04x faster                                                             |
| sphinx                | 1.26 sec                                                                 | 1.22 sec: 1.03x faster                                                             |
| pprint_safe_repr      | 1.27 sec                                                                 | 1.23 sec: 1.03x faster                                                             |
| async_tree_io         | 945 ms                                                                   | 920 ms: 1.03x faster                                                               |
| connected_components  | 547 ms                                                                   | 562 ms: 1.03x slower                                                               |
| tomli_loads           | 2.51 sec                                                                 | 2.59 sec: 1.03x slower                                                             |
| sqlglot_transpile     | 1.91 ms                                                                  | 1.98 ms: 1.04x slower                                                              |
| pycparser             | 1.43 sec                                                                 | 1.49 sec: 1.05x slower                                                             |
| deltablue             | 4.27 ms                                                                  | 4.56 ms: 1.07x slower                                                              |
| regex_dna             | 247 ms                                                                   | 266 ms: 1.08x slower                                                               |
| sqlalchemy_imperative | 16.3 ms                                                                  | 18.3 ms: 1.12x slower                                                              |
| dulwich_log           | 69.9 ms                                                                  | 86.4 ms: 1.24x slower                                                              |
| Geometric mean        | (ref)                                                                    | 1.02x faster                                                                       |

Benchmark hidden because not significant (67): richards, regex_compile, logging_silent, spectral_norm, sympy_str, json, richards_super, scimark_monte_carlo, typing_runtime_protocols, telco, nbody, pyflate, async_tree_none_tg, json_dumps, xml_etree_generate, sqlite_synth, logging_format, 2to3, sqlalchemy_declarative, async_tree_memoization_tg, k_core, pathlib, meteor_contest, sqlglot_parse, python_startup, pidigits, regex_effbot, python_startup_no_site, gc_traversal, mypy2, sqlglot_normalize, many_optionals, deepcopy_memo, async_tree_cpu_io_mixed, async_tree_none, comprehensions, crypto_pyaes, pprint_pformat, xml_etree_parse, scimark_sor, bpe_tokeniser, async_tree_io_tg, xml_etree_iterparse, json_loads, docutils, async_tree_cpu_io_mixed_tg, unpickle_pure_python, djangocms, asyncio_websockets, float, regex_v8, scimark_fft, shortest_path, scimark_sparse_mat_mult, create_gc_cycles, async_tree_memoization, html5lib, thrift, fannkuch, sympy_expand, chaos, sqlglot_optimize, mako, coroutines, subparsers, pickle_pure_python, sympy_sum

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x