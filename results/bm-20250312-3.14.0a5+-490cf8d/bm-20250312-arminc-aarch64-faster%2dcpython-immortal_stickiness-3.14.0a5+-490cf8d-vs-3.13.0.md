# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.044x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                              |
| html5lib       | 65.6 ms                                                  | 64.1 ms: 1.02x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                              |
| async_generators           | 500 ms                                                   | 449 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                             |
| regex_v8       | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                             |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                    | 1.13x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 175 ms: 1.15x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                            |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 60.2 ms: 1.02x faster                                                             |
| django_template | 39.4 ms                                                  | 41.9 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 334 us: 1.43x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 39.1 us: 1.36x faster                                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                              |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                              |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                              |
| deepcopy_reduce            | 4.24 us                                                  | 3.54 us: 1.20x faster                                                             |
| go                         | 164 ms                                                   | 139 ms: 1.18x faster                                                              |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.17x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 28.1 ms: 1.16x faster                                                             |
| xml_etree_parse            | 203 ms                                                   | 175 ms: 1.15x faster                                                              |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                              |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                                             |
| async_generators           | 500 ms                                                   | 449 ms: 1.11x faster                                                              |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                              |
| float                      | 95.8 ms                                                  | 87.5 ms: 1.09x faster                                                             |
| telco                      | 10.5 ms                                                  | 9.60 ms: 1.09x faster                                                             |
| scimark_sor                | 164 ms                                                   | 151 ms: 1.09x faster                                                              |
| coverage                   | 106 ms                                                   | 97.3 ms: 1.09x faster                                                             |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.48 sec: 1.08x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.61 sec: 1.07x faster                                                            |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.07x faster                                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.3 ms: 1.07x faster                                                             |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                            |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                              |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                            |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                              |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                              |
| mdp                        | 3.45 sec                                                 | 3.32 sec: 1.04x faster                                                            |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                                              |
| pprint_pformat             | 1.99 sec                                                 | 1.93 sec: 1.03x faster                                                            |
| genshi_xml                 | 61.6 ms                                                  | 60.2 ms: 1.02x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 64.1 ms: 1.02x faster                                                             |
| connected_components       | 547 ms                                                   | 557 ms: 1.02x slower                                                              |
| shortest_path              | 565 ms                                                   | 581 ms: 1.03x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.57 ms: 1.05x slower                                                             |
| fannkuch                   | 478 ms                                                   | 503 ms: 1.05x slower                                                              |
| django_template            | 39.4 ms                                                  | 41.9 ms: 1.06x slower                                                             |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                              |
| gc_traversal               | 5.92 ms                                                  | 6.63 ms: 1.12x slower                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                             |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                                             |
| many_optionals             | 626 us                                                   | 848 us: 1.35x slower                                                              |
| bench_mp_pool              | 8.07 ms                                                  | 4.51 sec: 559.06x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (39): thrift, regex_compile, xml_etree_generate, sqlalchemy_declarative, sympy_sum, genshi_text, sqlalchemy_imperative, logging_format, logging_simple, nqueens, xml_etree_process, scimark_sparse_mat_mult, asyncio_websockets, chaos, sympy_expand, json_dumps, json, pprint_safe_repr, richards_super, typing_runtime_protocols, pyflate, docutils, python_startup, richards, coroutines, bench_thread_pool, pidigits, mako, sympy_integrate, hexiom, sympy_str, deltablue, scimark_lu, unpickle_pure_python, comprehensions, raytrace, pickle_pure_python, crypto_pyaes, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x