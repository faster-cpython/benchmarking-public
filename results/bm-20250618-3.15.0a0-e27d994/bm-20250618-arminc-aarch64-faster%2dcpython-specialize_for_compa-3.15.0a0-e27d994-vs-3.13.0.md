# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-aarch64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                              |
| html5lib       | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| Geometric mean | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 466 ms: 1.42x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                              |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 893 ms: 1.28x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.18x faster                                                              |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                              |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.5 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                             |
| regex_dna      | 263 ms                                                   | 219 ms: 1.20x faster                                                              |
| regex_v8       | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                             |
| Geometric mean | (ref)                                                    | 1.20x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                              |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| tomli_loads         | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                            |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                              |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                                      |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 60.6 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 466 ms: 1.42x faster                                                              |
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                              |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                              |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                             |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                             |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                              |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                              |
| async_tree_io              | 1.14 sec                                                 | 893 ms: 1.28x faster                                                              |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                              |
| regex_dna                  | 263 ms                                                   | 219 ms: 1.20x faster                                                              |
| regex_v8                   | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                             |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.19x faster                                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 666 ms: 1.18x faster                                                              |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                              |
| generators                 | 40.3 ms                                                  | 35.4 ms: 1.14x faster                                                             |
| deepcopy_reduce            | 4.24 us                                                  | 3.74 us: 1.13x faster                                                             |
| pyflate                    | 582 ms                                                   | 518 ms: 1.12x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                              |
| float                      | 95.8 ms                                                  | 85.5 ms: 1.12x faster                                                             |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                              |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                              |
| pylint                     | 345 ms                                                   | 316 ms: 1.09x faster                                                              |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                              |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.09x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                            |
| meteor_contest             | 117 ms                                                   | 108 ms: 1.09x faster                                                              |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                            |
| telco                      | 10.5 ms                                                  | 9.70 ms: 1.08x faster                                                             |
| thrift                     | 1.01 ms                                                  | 940 us: 1.08x faster                                                              |
| nqueens                    | 105 ms                                                   | 97.7 ms: 1.07x faster                                                             |
| html5lib                   | 65.6 ms                                                  | 61.2 ms: 1.07x faster                                                             |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.4 ms: 1.07x faster                                                             |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                              |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                             |
| hexiom                     | 7.34 ms                                                  | 6.94 ms: 1.06x faster                                                             |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.06x faster                                                            |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.05x faster                                                            |
| sqlite_synth               | 4.08 us                                                  | 3.91 us: 1.05x faster                                                             |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                              |
| comprehensions             | 20.8 us                                                  | 20.1 us: 1.04x faster                                                             |
| richards_super             | 60.8 ms                                                  | 59.3 ms: 1.03x faster                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                             |
| genshi_xml                 | 61.6 ms                                                  | 60.6 ms: 1.02x faster                                                             |
| connected_components       | 547 ms                                                   | 567 ms: 1.04x slower                                                              |
| logging_simple             | 7.25 us                                                  | 7.55 us: 1.04x slower                                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.08 sec: 1.05x slower                                                            |
| raytrace                   | 310 ms                                                   | 327 ms: 1.06x slower                                                              |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.06x slower                                                            |
| shortest_path              | 565 ms                                                   | 605 ms: 1.07x slower                                                              |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                             |
| gc_traversal               | 5.92 ms                                                  | 6.97 ms: 1.18x slower                                                             |
| many_optionals             | 626 us                                                   | 770 us: 1.23x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                                             |
| logging_silent             | 135 ns                                                   | 646 ns: 4.80x slower                                                              |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (30): regex_compile, sympy_sum, json_dumps, genshi_text, sympy_integrate, json, coverage, crypto_pyaes, chaos, xml_etree_process, sympy_expand, fannkuch, docutils, asyncio_websockets, richards, typing_runtime_protocols, mako, deltablue, pidigits, json_loads, sympy_str, scimark_lu, coroutines, unpickle_pure_python, nbody, djangocms, logging_format, django_template, scimark_sparse_mat_mult, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x