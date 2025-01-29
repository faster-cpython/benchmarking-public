# Results vs. base

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.002x faster
- HPT reliability: 86.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 283 ms: 1.01x slower                                                              |
| html5lib       | 66.5 ms                                                                      | 67.4 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 357 ms                                                                       | 347 ms: 1.03x faster                                                              |
| async_tree_none            | 293 ms                                                                       | 287 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed    | 523 ms                                                                       | 515 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 503 ms: 1.01x faster                                                              |
| async_tree_memoization_tg  | 339 ms                                                                       | 334 ms: 1.01x faster                                                              |
| async_tree_none_tg         | 280 ms                                                                       | 277 ms: 1.01x faster                                                              |
| async_tree_io              | 651 ms                                                                       | 645 ms: 1.01x faster                                                              |
| async_generators           | 414 ms                                                                       | 418 ms: 1.01x slower                                                              |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                                      | 26.0 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 211 us                                                                       | 207 us: 1.02x faster                                                              |
| tomli_loads          | 2.08 sec                                                                     | 2.06 sec: 1.01x faster                                                            |
| json_loads           | 26.7 us                                                                      | 26.8 us: 1.01x slower                                                             |
| xml_etree_parse      | 136 ms                                                                       | 137 ms: 1.01x slower                                                              |
| json_dumps           | 11.5 ms                                                                      | 11.6 ms: 1.01x slower                                                             |
| xml_etree_iterparse  | 95.5 ms                                                                      | 96.4 ms: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                             |
| python_startup_no_site | 8.99 ms                                                                      | 8.98 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 53.9 ms                                                                      | 52.6 ms: 1.03x faster                                                             |
| genshi_text    | 23.9 ms                                                                      | 23.4 ms: 1.02x faster                                                             |
| mako           | 10.8 ms                                                                      | 10.8 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| coverage                   | 80.7 ms                                                                      | 76.6 ms: 1.05x faster                                                             |
| pycparser                  | 1.26 sec                                                                     | 1.21 sec: 1.04x faster                                                            |
| thrift                     | 883 us                                                                       | 848 us: 1.04x faster                                                              |
| async_tree_memoization     | 357 ms                                                                       | 347 ms: 1.03x faster                                                              |
| genshi_xml                 | 53.9 ms                                                                      | 52.6 ms: 1.03x faster                                                             |
| typing_runtime_protocols   | 175 us                                                                       | 170 us: 1.03x faster                                                              |
| unpickle_pure_python       | 211 us                                                                       | 207 us: 1.02x faster                                                              |
| genshi_text                | 23.9 ms                                                                      | 23.4 ms: 1.02x faster                                                             |
| async_tree_none            | 293 ms                                                                       | 287 ms: 1.02x faster                                                              |
| k_core                     | 2.13 sec                                                                     | 2.10 sec: 1.02x faster                                                            |
| richards                   | 46.4 ms                                                                      | 45.7 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed    | 523 ms                                                                       | 515 ms: 1.02x faster                                                              |
| sqlalchemy_imperative      | 18.0 ms                                                                      | 17.7 ms: 1.01x faster                                                             |
| shortest_path              | 445 ms                                                                       | 439 ms: 1.01x faster                                                              |
| richards_super             | 51.9 ms                                                                      | 51.2 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 503 ms: 1.01x faster                                                              |
| logging_simple             | 6.25 us                                                                      | 6.17 us: 1.01x faster                                                             |
| async_tree_memoization_tg  | 339 ms                                                                       | 334 ms: 1.01x faster                                                              |
| meteor_contest             | 128 ms                                                                       | 127 ms: 1.01x faster                                                              |
| deltablue                  | 3.34 ms                                                                      | 3.30 ms: 1.01x faster                                                             |
| comprehensions             | 17.5 us                                                                      | 17.3 us: 1.01x faster                                                             |
| async_tree_none_tg         | 280 ms                                                                       | 277 ms: 1.01x faster                                                              |
| generators                 | 28.6 ms                                                                      | 28.3 ms: 1.01x faster                                                             |
| sqlglot_parse              | 1.34 ms                                                                      | 1.33 ms: 1.01x faster                                                             |
| hexiom                     | 6.12 ms                                                                      | 6.06 ms: 1.01x faster                                                             |
| tomli_loads                | 2.08 sec                                                                     | 2.06 sec: 1.01x faster                                                            |
| fannkuch                   | 367 ms                                                                       | 364 ms: 1.01x faster                                                              |
| async_tree_io              | 651 ms                                                                       | 645 ms: 1.01x faster                                                              |
| dulwich_log                | 67.0 ms                                                                      | 66.4 ms: 1.01x faster                                                             |
| spectral_norm              | 84.3 ms                                                                      | 83.6 ms: 1.01x faster                                                             |
| sqlalchemy_declarative     | 145 ms                                                                       | 143 ms: 1.01x faster                                                              |
| sqlglot_transpile          | 1.73 ms                                                                      | 1.72 ms: 1.01x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                                      | 2.91 us: 1.01x faster                                                             |
| scimark_sparse_mat_mult    | 4.57 ms                                                                      | 4.55 ms: 1.00x faster                                                             |
| logging_silent             | 96.9 ns                                                                      | 96.6 ns: 1.00x faster                                                             |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                             |
| sympy_integrate            | 23.2 ms                                                                      | 23.1 ms: 1.00x faster                                                             |
| python_startup_no_site     | 8.99 ms                                                                      | 8.98 ms: 1.00x faster                                                             |
| pprint_pformat             | 1.61 sec                                                                     | 1.62 sec: 1.00x slower                                                            |
| scimark_fft                | 302 ms                                                                       | 303 ms: 1.00x slower                                                              |
| json_loads                 | 26.7 us                                                                      | 26.8 us: 1.01x slower                                                             |
| sympy_sum                  | 150 ms                                                                       | 151 ms: 1.01x slower                                                              |
| deepcopy                   | 280 us                                                                       | 282 us: 1.01x slower                                                              |
| 2to3                       | 281 ms                                                                       | 283 ms: 1.01x slower                                                              |
| many_optionals             | 1.01 ms                                                                      | 1.02 ms: 1.01x slower                                                             |
| subparsers                 | 22.9 ms                                                                      | 23.1 ms: 1.01x slower                                                             |
| xml_etree_parse            | 136 ms                                                                       | 137 ms: 1.01x slower                                                              |
| mako                       | 10.8 ms                                                                      | 10.8 ms: 1.01x slower                                                             |
| json_dumps                 | 11.5 ms                                                                      | 11.6 ms: 1.01x slower                                                             |
| async_generators           | 414 ms                                                                       | 418 ms: 1.01x slower                                                              |
| xml_etree_iterparse        | 95.5 ms                                                                      | 96.4 ms: 1.01x slower                                                             |
| crypto_pyaes               | 73.6 ms                                                                      | 74.4 ms: 1.01x slower                                                             |
| json                       | 5.47 ms                                                                      | 5.53 ms: 1.01x slower                                                             |
| scimark_lu                 | 94.9 ms                                                                      | 95.9 ms: 1.01x slower                                                             |
| scimark_monte_carlo        | 62.8 ms                                                                      | 63.5 ms: 1.01x slower                                                             |
| nqueens                    | 87.4 ms                                                                      | 88.7 ms: 1.01x slower                                                             |
| html5lib                   | 66.5 ms                                                                      | 67.4 ms: 1.01x slower                                                             |
| pathlib                    | 15.7 ms                                                                      | 16.0 ms: 1.02x slower                                                             |
| chaos                      | 59.4 ms                                                                      | 60.5 ms: 1.02x slower                                                             |
| sqlglot_optimize           | 57.3 ms                                                                      | 58.5 ms: 1.02x slower                                                             |
| deepcopy_memo              | 30.0 us                                                                      | 30.7 us: 1.02x slower                                                             |
| sqlglot_normalize          | 114 ms                                                                       | 117 ms: 1.02x slower                                                              |
| create_gc_cycles           | 2.74 ms                                                                      | 2.81 ms: 1.03x slower                                                             |
| regex_v8                   | 25.1 ms                                                                      | 26.0 ms: 1.04x slower                                                             |
| mdp                        | 2.42 sec                                                                     | 2.52 sec: 1.04x slower                                                            |
| pyflate                    | 431 ms                                                                       | 452 ms: 1.05x slower                                                              |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (30): bench_mp_pool, nbody, bench_thread_pool, async_tree_io_tg, asyncio_websockets, telco, logging_format, sqlite_synth, pylint, pickle_pure_python, raytrace, xml_etree_generate, sympy_expand, sympy_str, bpe_tokeniser, django_template, sphinx, docutils, float, regex_dna, connected_components, scimark_sor, pidigits, pprint_safe_repr, regex_effbot, xml_etree_process, go, coroutines, gc_traversal, regex_compile

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 86.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x