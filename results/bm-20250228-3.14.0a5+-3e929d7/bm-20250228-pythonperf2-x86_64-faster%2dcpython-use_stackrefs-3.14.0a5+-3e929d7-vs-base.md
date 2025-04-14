# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                       | 290 ms: 1.02x slower                                                            |
| docutils       | 2.87 sec                                                                     | 2.91 sec: 1.01x slower                                                          |
| html5lib       | 68.7 ms                                                                      | 69.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 21.2 ms                                                                      | 21.0 ms: 1.01x faster                                                           |
| async_tree_memoization     | 348 ms                                                                       | 351 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 510 ms: 1.01x slower                                                            |
| async_tree_io              | 641 ms                                                                       | 646 ms: 1.01x slower                                                            |
| async_tree_memoization_tg  | 335 ms                                                                       | 338 ms: 1.01x slower                                                            |
| async_tree_none            | 286 ms                                                                       | 291 ms: 1.02x slower                                                            |
| async_generators           | 407 ms                                                                       | 419 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 69.9 ms                                                                      | 70.9 ms: 1.02x slower                                                           |
| nbody          | 101 ms                                                                       | 105 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                      | 25.3 ms: 1.03x faster                                                           |
| regex_compile  | 135 ms                                                                       | 137 ms: 1.01x slower                                                            |
| regex_dna      | 238 ms                                                                       | 245 ms: 1.03x slower                                                            |
| regex_effbot   | 3.05 ms                                                                      | 3.14 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 26.1 us                                                                      | 25.5 us: 1.02x faster                                                           |
| json_dumps           | 11.6 ms                                                                      | 11.4 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.0 ms                                                                      | 59.2 ms: 1.01x faster                                                           |
| pickle_pure_python   | 333 us                                                                       | 334 us: 1.01x slower                                                            |
| xml_etree_generate   | 83.4 ms                                                                      | 84.1 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 97.3 ms                                                                      | 99.7 ms: 1.02x slower                                                           |
| tomli_loads          | 2.11 sec                                                                     | 2.16 sec: 1.03x slower                                                          |
| xml_etree_parse      | 138 ms                                                                       | 143 ms: 1.04x slower                                                            |
| unpickle_pure_python | 212 us                                                                       | 221 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.15 ms                                                                      | 9.14 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 24.8 ms                                                                      | 24.2 ms: 1.02x faster                                                           |
| django_template | 36.3 ms                                                                      | 36.0 ms: 1.01x faster                                                           |
| mako            | 10.9 ms                                                                      | 11.3 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_silent             | 98.0 ns                                                                      | 94.1 ns: 1.04x faster                                                           |
| scimark_sparse_mat_mult    | 4.97 ms                                                                      | 4.80 ms: 1.03x faster                                                           |
| regex_v8                   | 26.0 ms                                                                      | 25.3 ms: 1.03x faster                                                           |
| deepcopy_memo              | 29.9 us                                                                      | 29.1 us: 1.03x faster                                                           |
| sqlglot_normalize          | 120 ms                                                                       | 117 ms: 1.03x faster                                                            |
| json_loads                 | 26.1 us                                                                      | 25.5 us: 1.02x faster                                                           |
| genshi_text                | 24.8 ms                                                                      | 24.2 ms: 1.02x faster                                                           |
| pyflate                    | 449 ms                                                                       | 441 ms: 1.02x faster                                                            |
| json_dumps                 | 11.6 ms                                                                      | 11.4 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 58.9 ms                                                                      | 58.0 ms: 1.02x faster                                                           |
| xml_etree_process          | 60.0 ms                                                                      | 59.2 ms: 1.01x faster                                                           |
| coroutines                 | 21.2 ms                                                                      | 21.0 ms: 1.01x faster                                                           |
| django_template            | 36.3 ms                                                                      | 36.0 ms: 1.01x faster                                                           |
| scimark_sor                | 111 ms                                                                       | 110 ms: 1.01x faster                                                            |
| coverage                   | 84.5 ms                                                                      | 83.9 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.81 us                                                                      | 2.80 us: 1.00x faster                                                           |
| python_startup_no_site     | 9.15 ms                                                                      | 9.14 ms: 1.00x faster                                                           |
| pprint_pformat             | 1.61 sec                                                                     | 1.61 sec: 1.00x slower                                                          |
| pickle_pure_python         | 333 us                                                                       | 334 us: 1.01x slower                                                            |
| sympy_expand               | 497 ms                                                                       | 500 ms: 1.01x slower                                                            |
| mdp                        | 2.50 sec                                                                     | 2.51 sec: 1.01x slower                                                          |
| sqlalchemy_declarative     | 145 ms                                                                       | 146 ms: 1.01x slower                                                            |
| dulwich_log                | 68.1 ms                                                                      | 68.6 ms: 1.01x slower                                                           |
| async_tree_memoization     | 348 ms                                                                       | 351 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 510 ms: 1.01x slower                                                            |
| xml_etree_generate         | 83.4 ms                                                                      | 84.1 ms: 1.01x slower                                                           |
| async_tree_io              | 641 ms                                                                       | 646 ms: 1.01x slower                                                            |
| html5lib                   | 68.7 ms                                                                      | 69.3 ms: 1.01x slower                                                           |
| async_tree_memoization_tg  | 335 ms                                                                       | 338 ms: 1.01x slower                                                            |
| shortest_path              | 446 ms                                                                       | 450 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.76 ms                                                                      | 1.77 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.36 ms                                                                      | 1.38 ms: 1.01x slower                                                           |
| docutils                   | 2.87 sec                                                                     | 2.91 sec: 1.01x slower                                                          |
| k_core                     | 2.08 sec                                                                     | 2.11 sec: 1.01x slower                                                          |
| scimark_lu                 | 100 ms                                                                       | 102 ms: 1.01x slower                                                            |
| many_optionals             | 1.01 ms                                                                      | 1.03 ms: 1.01x slower                                                           |
| regex_compile              | 135 ms                                                                       | 137 ms: 1.01x slower                                                            |
| sympy_sum                  | 152 ms                                                                       | 154 ms: 1.01x slower                                                            |
| float                      | 69.9 ms                                                                      | 70.9 ms: 1.02x slower                                                           |
| sympy_str                  | 290 ms                                                                       | 294 ms: 1.02x slower                                                            |
| sqlalchemy_imperative      | 17.9 ms                                                                      | 18.2 ms: 1.02x slower                                                           |
| telco                      | 8.09 ms                                                                      | 8.21 ms: 1.02x slower                                                           |
| async_tree_none            | 286 ms                                                                       | 291 ms: 1.02x slower                                                            |
| scimark_fft                | 333 ms                                                                       | 339 ms: 1.02x slower                                                            |
| sympy_integrate            | 23.0 ms                                                                      | 23.4 ms: 1.02x slower                                                           |
| deltablue                  | 3.35 ms                                                                      | 3.41 ms: 1.02x slower                                                           |
| logging_simple             | 6.41 us                                                                      | 6.53 us: 1.02x slower                                                           |
| nqueens                    | 92.4 ms                                                                      | 94.3 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 4.67 sec                                                                     | 4.77 sec: 1.02x slower                                                          |
| 2to3                       | 284 ms                                                                       | 290 ms: 1.02x slower                                                            |
| richards                   | 47.0 ms                                                                      | 47.9 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 169 us                                                                       | 173 us: 1.02x slower                                                            |
| deepcopy_reduce            | 2.95 us                                                                      | 3.01 us: 1.02x slower                                                           |
| logging_format             | 7.00 us                                                                      | 7.17 us: 1.02x slower                                                           |
| xml_etree_iterparse        | 97.3 ms                                                                      | 99.7 ms: 1.02x slower                                                           |
| hexiom                     | 6.11 ms                                                                      | 6.27 ms: 1.02x slower                                                           |
| comprehensions             | 17.3 us                                                                      | 17.8 us: 1.03x slower                                                           |
| tomli_loads                | 2.11 sec                                                                     | 2.16 sec: 1.03x slower                                                          |
| regex_dna                  | 238 ms                                                                       | 245 ms: 1.03x slower                                                            |
| async_generators           | 407 ms                                                                       | 419 ms: 1.03x slower                                                            |
| richards_super             | 53.2 ms                                                                      | 54.8 ms: 1.03x slower                                                           |
| deepcopy                   | 281 us                                                                       | 289 us: 1.03x slower                                                            |
| regex_effbot               | 3.05 ms                                                                      | 3.14 ms: 1.03x slower                                                           |
| subparsers                 | 22.6 ms                                                                      | 23.3 ms: 1.03x slower                                                           |
| generators                 | 28.4 ms                                                                      | 29.2 ms: 1.03x slower                                                           |
| raytrace                   | 280 ms                                                                       | 289 ms: 1.03x slower                                                            |
| meteor_contest             | 124 ms                                                                       | 128 ms: 1.03x slower                                                            |
| spectral_norm              | 87.6 ms                                                                      | 90.5 ms: 1.03x slower                                                           |
| pycparser                  | 1.24 sec                                                                     | 1.28 sec: 1.03x slower                                                          |
| go                         | 129 ms                                                                       | 134 ms: 1.03x slower                                                            |
| pathlib                    | 16.5 ms                                                                      | 17.1 ms: 1.03x slower                                                           |
| create_gc_cycles           | 2.69 ms                                                                      | 2.79 ms: 1.04x slower                                                           |
| fannkuch                   | 364 ms                                                                       | 377 ms: 1.04x slower                                                            |
| connected_components       | 415 ms                                                                       | 430 ms: 1.04x slower                                                            |
| mako                       | 10.9 ms                                                                      | 11.3 ms: 1.04x slower                                                           |
| xml_etree_parse            | 138 ms                                                                       | 143 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 212 us                                                                       | 221 us: 1.04x slower                                                            |
| nbody                      | 101 ms                                                                       | 105 ms: 1.04x slower                                                            |
| gc_traversal               | 6.27 ms                                                                      | 6.54 ms: 1.04x slower                                                           |
| chaos                      | 60.6 ms                                                                      | 65.2 ms: 1.08x slower                                                           |
| crypto_pyaes               | 76.9 ms                                                                      | 84.2 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (15): bench_mp_pool, thrift, pidigits, pprint_safe_repr, python_startup, scimark_monte_carlo, json, genshi_xml, asyncio_websockets, async_tree_cpu_io_mixed, pylint, async_tree_io_tg, sphinx, async_tree_none_tg, bench_thread_pool

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x