# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.003x faster
- HPT reliability: 77.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                       | 285 ms: 1.01x slower                                                                |
| html5lib       | 68.3 ms                                                                      | 66.8 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|---------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 336 ms                                                                       | 334 ms: 1.00x faster                                                                |
| async_generators          | 406 ms                                                                       | 414 ms: 1.02x slower                                                                |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                                        |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_io, asyncio_websockets, coroutines, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 92.7 ms                                                                      | 89.1 ms: 1.04x faster                                                               |
| float          | 70.6 ms                                                                      | 69.7 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.14 ms                                                                      | 3.05 ms: 1.03x faster                                                               |
| regex_compile  | 137 ms                                                                       | 135 ms: 1.02x faster                                                                |
| regex_dna      | 238 ms                                                                       | 239 ms: 1.00x slower                                                                |
| regex_v8       | 26.0 ms                                                                      | 26.1 ms: 1.00x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 138 ms                                                                       | 133 ms: 1.04x faster                                                                |
| json_dumps           | 11.7 ms                                                                      | 11.4 ms: 1.02x faster                                                               |
| xml_etree_iterparse  | 96.5 ms                                                                      | 94.6 ms: 1.02x faster                                                               |
| json_loads           | 26.6 us                                                                      | 26.1 us: 1.02x faster                                                               |
| xml_etree_process    | 58.9 ms                                                                      | 58.3 ms: 1.01x faster                                                               |
| unpickle_pure_python | 205 us                                                                       | 204 us: 1.00x faster                                                                |
| tomli_loads          | 2.09 sec                                                                     | 2.11 sec: 1.01x slower                                                              |
| pickle_pure_python   | 329 us                                                                       | 333 us: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup | 16.1 ms                                                                      | 16.2 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako           | 10.9 ms                                                                      | 10.8 ms: 1.01x faster                                                               |
| genshi_text    | 24.0 ms                                                                      | 24.3 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                 | bm-20250214-pythonperf2-x86_64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|---------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| scimark_monte_carlo       | 64.8 ms                                                                      | 61.8 ms: 1.05x faster                                                               |
| gc_traversal              | 6.57 ms                                                                      | 6.31 ms: 1.04x faster                                                               |
| nbody                     | 92.7 ms                                                                      | 89.1 ms: 1.04x faster                                                               |
| xml_etree_parse           | 138 ms                                                                       | 133 ms: 1.04x faster                                                                |
| typing_runtime_protocols  | 172 us                                                                       | 166 us: 1.03x faster                                                                |
| regex_effbot              | 3.14 ms                                                                      | 3.05 ms: 1.03x faster                                                               |
| logging_format            | 7.00 us                                                                      | 6.83 us: 1.02x faster                                                               |
| pprint_safe_repr          | 796 ms                                                                       | 778 ms: 1.02x faster                                                                |
| sqlite_synth              | 2.83 us                                                                      | 2.77 us: 1.02x faster                                                               |
| thrift                    | 863 us                                                                       | 845 us: 1.02x faster                                                                |
| html5lib                  | 68.3 ms                                                                      | 66.8 ms: 1.02x faster                                                               |
| json_dumps                | 11.7 ms                                                                      | 11.4 ms: 1.02x faster                                                               |
| xml_etree_iterparse       | 96.5 ms                                                                      | 94.6 ms: 1.02x faster                                                               |
| json_loads                | 26.6 us                                                                      | 26.1 us: 1.02x faster                                                               |
| regex_compile             | 137 ms                                                                       | 135 ms: 1.02x faster                                                                |
| sqlalchemy_imperative     | 17.8 ms                                                                      | 17.5 ms: 1.02x faster                                                               |
| pycparser                 | 1.26 sec                                                                     | 1.24 sec: 1.02x faster                                                              |
| sqlglot_optimize          | 57.1 ms                                                                      | 56.3 ms: 1.02x faster                                                               |
| logging_simple            | 6.41 us                                                                      | 6.32 us: 1.01x faster                                                               |
| float                     | 70.6 ms                                                                      | 69.7 ms: 1.01x faster                                                               |
| mako                      | 10.9 ms                                                                      | 10.8 ms: 1.01x faster                                                               |
| scimark_sparse_mat_mult   | 4.69 ms                                                                      | 4.63 ms: 1.01x faster                                                               |
| deepcopy_memo             | 29.6 us                                                                      | 29.2 us: 1.01x faster                                                               |
| nqueens                   | 89.8 ms                                                                      | 88.6 ms: 1.01x faster                                                               |
| sympy_expand              | 496 ms                                                                       | 489 ms: 1.01x faster                                                                |
| mdp                       | 2.48 sec                                                                     | 2.46 sec: 1.01x faster                                                              |
| sympy_str                 | 291 ms                                                                       | 288 ms: 1.01x faster                                                                |
| xml_etree_process         | 58.9 ms                                                                      | 58.3 ms: 1.01x faster                                                               |
| pathlib                   | 16.4 ms                                                                      | 16.3 ms: 1.01x faster                                                               |
| pprint_pformat            | 1.63 sec                                                                     | 1.61 sec: 1.01x faster                                                              |
| sqlglot_normalize         | 115 ms                                                                       | 114 ms: 1.01x faster                                                                |
| chaos                     | 61.0 ms                                                                      | 60.6 ms: 1.01x faster                                                               |
| unpickle_pure_python      | 205 us                                                                       | 204 us: 1.00x faster                                                                |
| sqlalchemy_declarative    | 143 ms                                                                       | 142 ms: 1.00x faster                                                                |
| async_tree_memoization_tg | 336 ms                                                                       | 334 ms: 1.00x faster                                                                |
| crypto_pyaes              | 74.1 ms                                                                      | 73.9 ms: 1.00x faster                                                               |
| many_optionals            | 1.01 ms                                                                      | 1.01 ms: 1.00x faster                                                               |
| sympy_sum                 | 152 ms                                                                       | 151 ms: 1.00x faster                                                                |
| regex_dna                 | 238 ms                                                                       | 239 ms: 1.00x slower                                                                |
| connected_components      | 411 ms                                                                       | 412 ms: 1.00x slower                                                                |
| regex_v8                  | 26.0 ms                                                                      | 26.1 ms: 1.00x slower                                                               |
| shortest_path             | 443 ms                                                                       | 445 ms: 1.00x slower                                                                |
| sqlglot_parse             | 1.35 ms                                                                      | 1.36 ms: 1.00x slower                                                               |
| deepcopy                  | 282 us                                                                       | 284 us: 1.00x slower                                                                |
| python_startup            | 16.1 ms                                                                      | 16.2 ms: 1.01x slower                                                               |
| meteor_contest            | 124 ms                                                                       | 125 ms: 1.01x slower                                                                |
| scimark_sor               | 108 ms                                                                       | 109 ms: 1.01x slower                                                                |
| telco                     | 7.85 ms                                                                      | 7.92 ms: 1.01x slower                                                               |
| tomli_loads               | 2.09 sec                                                                     | 2.11 sec: 1.01x slower                                                              |
| hexiom                    | 6.14 ms                                                                      | 6.20 ms: 1.01x slower                                                               |
| 2to3                      | 282 ms                                                                       | 285 ms: 1.01x slower                                                                |
| pickle_pure_python        | 329 us                                                                       | 333 us: 1.01x slower                                                                |
| scimark_lu                | 94.9 ms                                                                      | 95.9 ms: 1.01x slower                                                               |
| comprehensions            | 16.9 us                                                                      | 17.1 us: 1.01x slower                                                               |
| scimark_fft               | 305 ms                                                                       | 309 ms: 1.01x slower                                                                |
| genshi_text               | 24.0 ms                                                                      | 24.3 ms: 1.01x slower                                                               |
| coverage                  | 77.3 ms                                                                      | 78.7 ms: 1.02x slower                                                               |
| async_generators          | 406 ms                                                                       | 414 ms: 1.02x slower                                                                |
| go                        | 126 ms                                                                       | 129 ms: 1.02x slower                                                                |
| spectral_norm             | 83.7 ms                                                                      | 85.8 ms: 1.02x slower                                                               |
| richards_super            | 50.9 ms                                                                      | 52.5 ms: 1.03x slower                                                               |
| richards                  | 45.2 ms                                                                      | 47.3 ms: 1.05x slower                                                               |
| pyflate                   | 428 ms                                                                       | 453 ms: 1.06x slower                                                                |
| Geometric mean            | (ref)                                                                        | 1.00x faster                                                                        |

Benchmark hidden because not significant (33): bench_mp_pool, logging_silent, bench_thread_pool, deepcopy_reduce, sphinx, k_core, docutils, pylint, genshi_xml, deltablue, subparsers, dulwich_log, sympy_integrate, sqlglot_transpile, django_template, async_tree_cpu_io_mixed_tg, python_startup_no_site, fannkuch, async_tree_none_tg, xml_etree_generate, pidigits, bpe_tokeniser, async_tree_memoization, async_tree_io, asyncio_websockets, coroutines, raytrace, async_tree_cpu_io_mixed, async_tree_none, generators, json, async_tree_io_tg, create_gc_cycles

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 77.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x