# Results vs. base

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.004x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                   | 298 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none | 396 ms                                                                   | 386 ms: 1.03x faster                                                              |
| async_tree_io   | 887 ms                                                                   | 877 ms: 1.01x faster                                                              |
| Geometric mean  | (ref)                                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (9): async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 83.2 ms                                                                  | 85.8 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                   | 242 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|---------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps          | 13.9 ms                                                                  | 14.1 ms: 1.01x slower                                                             |
| xml_etree_process   | 78.9 ms                                                                  | 79.8 ms: 1.01x slower                                                             |
| xml_etree_iterparse | 140 ms                                                                   | 142 ms: 1.01x slower                                                              |
| tomli_loads         | 2.44 sec                                                                 | 2.50 sec: 1.03x slower                                                            |
| xml_etree_parse     | 174 ms                                                                   | 180 ms: 1.03x slower                                                              |
| Geometric mean      | (ref)                                                                    | 1.02x slower                                                                      |

Benchmark hidden because not significant (4): pickle_pure_python, json_loads, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 60.1 ms                                                                  | 60.9 ms: 1.01x slower                                                             |
| django_template | 38.9 ms                                                                  | 41.2 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                                    | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna               | 250 ms                                                                   | 242 ms: 1.03x faster                                                              |
| async_tree_none         | 396 ms                                                                   | 386 ms: 1.03x faster                                                              |
| deepcopy_memo           | 38.3 us                                                                  | 37.5 us: 1.02x faster                                                             |
| async_tree_io           | 887 ms                                                                   | 877 ms: 1.01x faster                                                              |
| richards                | 51.7 ms                                                                  | 51.2 ms: 1.01x faster                                                             |
| hexiom                  | 7.06 ms                                                                  | 7.02 ms: 1.00x faster                                                             |
| sqlite_synth            | 3.81 us                                                                  | 3.84 us: 1.01x slower                                                             |
| deepcopy                | 327 us                                                                   | 331 us: 1.01x slower                                                              |
| json_dumps              | 13.9 ms                                                                  | 14.1 ms: 1.01x slower                                                             |
| xml_etree_process       | 78.9 ms                                                                  | 79.8 ms: 1.01x slower                                                             |
| genshi_xml              | 60.1 ms                                                                  | 60.9 ms: 1.01x slower                                                             |
| 2to3                    | 294 ms                                                                   | 298 ms: 1.01x slower                                                              |
| bench_thread_pool       | 1.33 ms                                                                  | 1.34 ms: 1.01x slower                                                             |
| xml_etree_iterparse     | 140 ms                                                                   | 142 ms: 1.01x slower                                                              |
| bpe_tokeniser           | 5.55 sec                                                                 | 5.65 sec: 1.02x slower                                                            |
| sympy_str               | 260 ms                                                                   | 264 ms: 1.02x slower                                                              |
| deepcopy_reduce         | 3.46 us                                                                  | 3.52 us: 1.02x slower                                                             |
| many_optionals          | 821 us                                                                   | 837 us: 1.02x slower                                                              |
| scimark_sparse_mat_mult | 6.70 ms                                                                  | 6.85 ms: 1.02x slower                                                             |
| logging_simple          | 7.12 us                                                                  | 7.28 us: 1.02x slower                                                             |
| tomli_loads             | 2.44 sec                                                                 | 2.50 sec: 1.03x slower                                                            |
| float                   | 83.2 ms                                                                  | 85.8 ms: 1.03x slower                                                             |
| telco                   | 9.19 ms                                                                  | 9.48 ms: 1.03x slower                                                             |
| pathlib                 | 21.8 ms                                                                  | 22.5 ms: 1.03x slower                                                             |
| xml_etree_parse         | 174 ms                                                                   | 180 ms: 1.03x slower                                                              |
| mdp                     | 1.61 sec                                                                 | 1.68 sec: 1.05x slower                                                            |
| scimark_fft             | 416 ms                                                                   | 435 ms: 1.05x slower                                                              |
| django_template         | 38.9 ms                                                                  | 41.2 ms: 1.06x slower                                                             |
| sqlalchemy_imperative   | 15.4 ms                                                                  | 16.4 ms: 1.06x slower                                                             |
| Geometric mean          | (ref)                                                                    | 1.01x slower                                                                      |

Benchmark hidden because not significant (66): bench_mp_pool, sqlglot_v2_transpile, nqueens, coverage, gc_traversal, sqlglot_v2_parse, richards_super, pickle_pure_python, create_gc_cycles, async_tree_memoization, regex_v8, asyncio_websockets, async_tree_none_tg, deltablue, sqlglot_v2_optimize, regex_effbot, dulwich_log, async_tree_memoization_tg, async_tree_cpu_io_mixed, coroutines, pycparser, async_tree_io_tg, docutils, logging_silent, sphinx, python_startup, typing_runtime_protocols, sympy_integrate, mako, k_core, pprint_pformat, comprehensions, connected_components, async_tree_cpu_io_mixed_tg, sqlalchemy_declarative, pylint, meteor_contest, pyflate, pprint_safe_repr, scimark_lu, shortest_path, python_startup_no_site, generators, logging_format, json_loads, fannkuch, go, pidigits, raytrace, subparsers, sympy_sum, chaos, async_generators, spectral_norm, scimark_sor, json, nbody, crypto_pyaes, regex_compile, sympy_expand, xml_etree_generate, unpickle_pure_python, html5lib, sqlglot_v2_normalize, scimark_monte_carlo, genshi_text

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x