# Results vs. base

- fork: Fidget-Spinner
- ref: init_slots
- machine: linux-x86_64
- commit hash: 8757207
- commit date: 2024-12-25
- overall geometric mean: 1.005x faster
- HPT reliability: 98.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 271 ms                                                                       | 265 ms: 1.02x faster                                                         |
| async_tree_io              | 650 ms                                                                       | 635 ms: 1.02x faster                                                         |
| async_tree_memoization     | 356 ms                                                                       | 349 ms: 1.02x faster                                                         |
| async_tree_none            | 292 ms                                                                       | 286 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 500 ms                                                                       | 492 ms: 1.02x faster                                                         |
| async_tree_memoization_tg  | 331 ms                                                                       | 326 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 516 ms                                                                       | 509 ms: 1.01x faster                                                         |
| async_generators           | 434 ms                                                                       | 430 ms: 1.01x faster                                                         |
| coroutines                 | 20.8 ms                                                                      | 20.9 ms: 1.00x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 75.4 ms                                                                      | 70.7 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                       | 236 ms: 1.01x slower                                                         |
| regex_effbot   | 3.15 ms                                                                      | 3.21 ms: 1.02x slower                                                        |
| regex_v8       | 25.0 ms                                                                      | 25.9 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|--------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps         | 11.6 ms                                                                      | 11.3 ms: 1.02x faster                                                        |
| tomli_loads        | 2.08 sec                                                                     | 2.05 sec: 1.01x faster                                                       |
| pickle_pure_python | 330 us                                                                       | 326 us: 1.01x faster                                                         |
| xml_etree_parse    | 135 ms                                                                       | 136 ms: 1.01x slower                                                         |
| xml_etree_generate | 82.8 ms                                                                      | 83.7 ms: 1.01x slower                                                        |
| xml_etree_process  | 58.9 ms                                                                      | 59.5 ms: 1.01x slower                                                        |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.04 ms: 1.00x slower                                                        |
| python_startup         | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|-----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 24.4 ms                                                                      | 23.8 ms: 1.02x faster                                                        |
| django_template | 36.2 ms                                                                      | 35.6 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3+-d61542b | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float                      | 75.4 ms                                                                      | 70.7 ms: 1.07x faster                                                        |
| raytrace                   | 277 ms                                                                       | 264 ms: 1.05x faster                                                         |
| richards_super             | 53.7 ms                                                                      | 51.7 ms: 1.04x faster                                                        |
| go                         | 129 ms                                                                       | 125 ms: 1.04x faster                                                         |
| coverage                   | 80.6 ms                                                                      | 78.3 ms: 1.03x faster                                                        |
| richards                   | 47.1 ms                                                                      | 45.8 ms: 1.03x faster                                                        |
| genshi_text                | 24.4 ms                                                                      | 23.8 ms: 1.02x faster                                                        |
| json_dumps                 | 11.6 ms                                                                      | 11.3 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 271 ms                                                                       | 265 ms: 1.02x faster                                                         |
| async_tree_io              | 650 ms                                                                       | 635 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 788 ms                                                                       | 771 ms: 1.02x faster                                                         |
| deltablue                  | 3.41 ms                                                                      | 3.34 ms: 1.02x faster                                                        |
| crypto_pyaes               | 74.4 ms                                                                      | 72.8 ms: 1.02x faster                                                        |
| nqueens                    | 90.0 ms                                                                      | 88.2 ms: 1.02x faster                                                        |
| async_tree_memoization     | 356 ms                                                                       | 349 ms: 1.02x faster                                                         |
| async_tree_none            | 292 ms                                                                       | 286 ms: 1.02x faster                                                         |
| subparsers                 | 22.9 ms                                                                      | 22.4 ms: 1.02x faster                                                        |
| logging_format             | 6.98 us                                                                      | 6.86 us: 1.02x faster                                                        |
| telco                      | 7.97 ms                                                                      | 7.85 ms: 1.02x faster                                                        |
| comprehensions             | 17.8 us                                                                      | 17.5 us: 1.02x faster                                                        |
| pprint_pformat             | 1.59 sec                                                                     | 1.57 sec: 1.02x faster                                                       |
| django_template            | 36.2 ms                                                                      | 35.6 ms: 1.02x faster                                                        |
| hexiom                     | 6.10 ms                                                                      | 6.01 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 500 ms                                                                       | 492 ms: 1.02x faster                                                         |
| tomli_loads                | 2.08 sec                                                                     | 2.05 sec: 1.01x faster                                                       |
| generators                 | 29.0 ms                                                                      | 28.5 ms: 1.01x faster                                                        |
| k_core                     | 2.12 sec                                                                     | 2.08 sec: 1.01x faster                                                       |
| async_tree_memoization_tg  | 331 ms                                                                       | 326 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 516 ms                                                                       | 509 ms: 1.01x faster                                                         |
| meteor_contest             | 127 ms                                                                       | 126 ms: 1.01x faster                                                         |
| pickle_pure_python         | 330 us                                                                       | 326 us: 1.01x faster                                                         |
| async_generators           | 434 ms                                                                       | 430 ms: 1.01x faster                                                         |
| many_optionals             | 1.03 ms                                                                      | 1.02 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.35 ms                                                                      | 1.33 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 174 us                                                                       | 172 us: 1.01x faster                                                         |
| deepcopy_reduce            | 2.89 us                                                                      | 2.87 us: 1.01x faster                                                        |
| sqlite_synth               | 2.86 us                                                                      | 2.84 us: 1.01x faster                                                        |
| thrift                     | 865 us                                                                       | 859 us: 1.01x faster                                                         |
| sympy_str                  | 292 ms                                                                       | 291 ms: 1.01x faster                                                         |
| fannkuch                   | 365 ms                                                                       | 364 ms: 1.00x faster                                                         |
| sympy_expand               | 500 ms                                                                       | 498 ms: 1.00x faster                                                         |
| python_startup_no_site     | 9.02 ms                                                                      | 9.04 ms: 1.00x slower                                                        |
| shortest_path              | 440 ms                                                                       | 441 ms: 1.00x slower                                                         |
| python_startup             | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                        |
| connected_components       | 416 ms                                                                       | 417 ms: 1.00x slower                                                         |
| coroutines                 | 20.8 ms                                                                      | 20.9 ms: 1.00x slower                                                        |
| sqlalchemy_imperative      | 17.8 ms                                                                      | 17.9 ms: 1.00x slower                                                        |
| xml_etree_parse            | 135 ms                                                                       | 136 ms: 1.01x slower                                                         |
| pathlib                    | 16.0 ms                                                                      | 16.1 ms: 1.01x slower                                                        |
| spectral_norm              | 87.7 ms                                                                      | 88.5 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 62.0 ms                                                                      | 62.6 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 114 ms                                                                       | 115 ms: 1.01x slower                                                         |
| regex_dna                  | 234 ms                                                                       | 236 ms: 1.01x slower                                                         |
| xml_etree_generate         | 82.8 ms                                                                      | 83.7 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.9 ms                                                                      | 59.5 ms: 1.01x slower                                                        |
| chaos                      | 61.7 ms                                                                      | 62.5 ms: 1.01x slower                                                        |
| scimark_lu                 | 94.0 ms                                                                      | 95.4 ms: 1.02x slower                                                        |
| regex_effbot               | 3.15 ms                                                                      | 3.21 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.75 ms                                                                      | 4.84 ms: 1.02x slower                                                        |
| scimark_sor                | 110 ms                                                                       | 113 ms: 1.03x slower                                                         |
| scimark_fft                | 303 ms                                                                       | 311 ms: 1.03x slower                                                         |
| regex_v8                   | 25.0 ms                                                                      | 25.9 ms: 1.04x slower                                                        |
| gc_traversal               | 6.33 ms                                                                      | 6.58 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (35): create_gc_cycles, nbody, asyncio_websockets, async_tree_io_tg, mypy2, html5lib, genshi_xml, logging_simple, unpickle_pure_python, regex_compile, sqlalchemy_declarative, logging_silent, mdp, djangocms, sympy_integrate, sympy_sum, 2to3, docutils, sqlglot_optimize, deepcopy_memo, bpe_tokeniser, dulwich_log, bench_thread_pool, sqlglot_transpile, sphinx, pidigits, pyflate, json_loads, json, mako, pycparser, deepcopy, xml_etree_iterparse, pylint, bench_mp_pool

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 98.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x