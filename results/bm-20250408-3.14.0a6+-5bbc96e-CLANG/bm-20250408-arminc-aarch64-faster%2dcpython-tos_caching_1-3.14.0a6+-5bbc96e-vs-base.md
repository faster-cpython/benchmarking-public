# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-aarch64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.002x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators           | 421 ms                                                                   | 408 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                   | 712 ms: 1.01x slower                                                        |
| async_tree_memoization     | 453 ms                                                                   | 457 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.2 ms                                                                  | 82.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_dna, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps         | 14.3 ms                                                                  | 14.0 ms: 1.02x faster                                                       |
| tomli_loads        | 2.37 sec                                                                 | 2.33 sec: 1.01x faster                                                      |
| pickle_pure_python | 372 us                                                                   | 378 us: 1.02x slower                                                        |
| Geometric mean     | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (6): json_loads, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 16.2 ms                                                                  | 16.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                  | 14.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-arminc-aarch64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sor                | 144 ms                                                                   | 135 ms: 1.07x faster                                                        |
| scimark_fft                | 398 ms                                                                   | 385 ms: 1.03x faster                                                        |
| async_generators           | 421 ms                                                                   | 408 ms: 1.03x faster                                                        |
| meteor_contest             | 115 ms                                                                   | 111 ms: 1.03x faster                                                        |
| crypto_pyaes               | 85.4 ms                                                                  | 83.1 ms: 1.03x faster                                                       |
| float                      | 84.2 ms                                                                  | 82.1 ms: 1.03x faster                                                       |
| json_dumps                 | 14.3 ms                                                                  | 14.0 ms: 1.02x faster                                                       |
| deltablue                  | 3.77 ms                                                                  | 3.69 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 78.2 ms                                                                  | 76.9 ms: 1.02x faster                                                       |
| pyflate                    | 523 ms                                                                   | 515 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 6.45 ms                                                                  | 6.36 ms: 1.01x faster                                                       |
| tomli_loads                | 2.37 sec                                                                 | 2.33 sec: 1.01x faster                                                      |
| sqlite_synth               | 3.86 us                                                                  | 3.84 us: 1.01x faster                                                       |
| python_startup             | 16.2 ms                                                                  | 16.1 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                   | 712 ms: 1.01x slower                                                        |
| logging_format             | 7.51 us                                                                  | 7.57 us: 1.01x slower                                                       |
| async_tree_memoization     | 453 ms                                                                   | 457 ms: 1.01x slower                                                        |
| coverage                   | 93.6 ms                                                                  | 94.6 ms: 1.01x slower                                                       |
| pickle_pure_python         | 372 us                                                                   | 378 us: 1.02x slower                                                        |
| pycparser                  | 1.21 sec                                                                 | 1.24 sec: 1.02x slower                                                      |
| mako                       | 13.8 ms                                                                  | 14.3 ms: 1.03x slower                                                       |
| deepcopy_reduce            | 3.32 us                                                                  | 3.45 us: 1.04x slower                                                       |
| bench_mp_pool              | 2.12 sec                                                                 | 2.97 sec: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (72): generators, spectral_norm, sqlalchemy_imperative, fannkuch, sqlalchemy_declarative, pathlib, comprehensions, json_loads, nqueens, gc_traversal, create_gc_cycles, subparsers, pylint, sympy_integrate, mdp, pidigits, regex_effbot, django_template, shortest_path, chaos, sqlglot_v2_transpile, regex_dna, xml_etree_iterparse, 2to3, raytrace, pprint_pformat, dulwich_log, sqlglot_v2_normalize, bpe_tokeniser, deepcopy_memo, sympy_expand, telco, sqlglot_v2_parse, unpickle_pure_python, async_tree_cpu_io_mixed, nbody, deepcopy, logging_simple, regex_v8, go, sympy_str, connected_components, async_tree_io_tg, json, async_tree_io, html5lib, regex_compile, logging_silent, xml_etree_parse, k_core, hexiom, asyncio_websockets, python_startup_no_site, async_tree_memoization_tg, pprint_safe_repr, docutils, typing_runtime_protocols, bench_thread_pool, sympy_sum, sphinx, async_tree_none_tg, genshi_xml, async_tree_none, many_optionals, xml_etree_process, richards, scimark_lu, genshi_text, richards_super, sqlglot_v2_optimize, xml_etree_generate, coroutines

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x