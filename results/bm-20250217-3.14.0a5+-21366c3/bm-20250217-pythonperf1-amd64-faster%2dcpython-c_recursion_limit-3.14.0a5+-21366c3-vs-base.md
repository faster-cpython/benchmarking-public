# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-amd64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.004x faster
- HPT reliability: 61.17%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| html5lib       | 38.6 ms                                                                     | 39.9 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 412 ms                                                                      | 407 ms: 1.01x faster                                                               |
| async_tree_io              | 415 ms                                                                      | 411 ms: 1.01x faster                                                               |
| async_tree_none_tg         | 178 ms                                                                      | 176 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                               |
| coroutines                 | 13.3 ms                                                                     | 13.7 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, asyncio_websockets, async_generators, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 44.7 ms                                                                     | 45.3 ms: 1.01x slower                                                              |
| nbody          | 69.7 ms                                                                     | 71.2 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.46 ms                                                                     | 1.45 ms: 1.01x faster                                                              |
| regex_v8       | 14.3 ms                                                                     | 14.4 ms: 1.00x slower                                                              |
| regex_compile  | 84.2 ms                                                                     | 85.1 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 15.4 us                                                                     | 14.2 us: 1.08x faster                                                              |
| pickle_pure_python   | 221 us                                                                      | 219 us: 1.01x faster                                                               |
| unpickle_pure_python | 143 us                                                                      | 145 us: 1.01x slower                                                               |
| xml_etree_parse      | 90.2 ms                                                                     | 91.1 ms: 1.01x slower                                                              |
| tomli_loads          | 1.37 sec                                                                    | 1.40 sec: 1.02x slower                                                             |
| xml_etree_process    | 39.8 ms                                                                     | 40.5 ms: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 24.5 ms                                                                     | 24.8 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml      | 36.5 ms                                                                     | 35.3 ms: 1.03x faster                                                              |
| genshi_text     | 17.0 ms                                                                     | 16.5 ms: 1.03x faster                                                              |
| django_template | 25.1 ms                                                                     | 25.5 ms: 1.01x slower                                                              |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads                 | 15.4 us                                                                     | 14.2 us: 1.08x faster                                                              |
| json                       | 3.10 ms                                                                     | 2.91 ms: 1.07x faster                                                              |
| spectral_norm              | 60.6 ms                                                                     | 57.6 ms: 1.05x faster                                                              |
| coverage                   | 46.9 ms                                                                     | 45.2 ms: 1.04x faster                                                              |
| typing_runtime_protocols   | 111 us                                                                      | 107 us: 1.04x faster                                                               |
| scimark_monte_carlo        | 45.7 ms                                                                     | 44.0 ms: 1.04x faster                                                              |
| subparsers                 | 16.5 ms                                                                     | 16.0 ms: 1.03x faster                                                              |
| genshi_xml                 | 36.5 ms                                                                     | 35.3 ms: 1.03x faster                                                              |
| genshi_text                | 17.0 ms                                                                     | 16.5 ms: 1.03x faster                                                              |
| scimark_fft                | 188 ms                                                                      | 182 ms: 1.03x faster                                                               |
| crypto_pyaes               | 49.6 ms                                                                     | 48.5 ms: 1.02x faster                                                              |
| mdp                        | 1.48 sec                                                                    | 1.44 sec: 1.02x faster                                                             |
| deepcopy                   | 188 us                                                                      | 184 us: 1.02x faster                                                               |
| bpe_tokeniser              | 2.85 sec                                                                    | 2.80 sec: 1.02x faster                                                             |
| comprehensions             | 11.2 us                                                                     | 11.0 us: 1.01x faster                                                              |
| generators                 | 19.6 ms                                                                     | 19.4 ms: 1.01x faster                                                              |
| async_tree_io_tg           | 412 ms                                                                      | 407 ms: 1.01x faster                                                               |
| sympy_sum                  | 89.2 ms                                                                     | 88.2 ms: 1.01x faster                                                              |
| async_tree_io              | 415 ms                                                                      | 411 ms: 1.01x faster                                                               |
| pathlib                    | 29.4 ms                                                                     | 29.1 ms: 1.01x faster                                                              |
| regex_effbot               | 1.46 ms                                                                     | 1.45 ms: 1.01x faster                                                              |
| pickle_pure_python         | 221 us                                                                      | 219 us: 1.01x faster                                                               |
| many_optionals             | 432 us                                                                      | 428 us: 1.01x faster                                                               |
| sympy_str                  | 174 ms                                                                      | 173 ms: 1.01x faster                                                               |
| async_tree_none_tg         | 178 ms                                                                      | 176 ms: 1.01x faster                                                               |
| fannkuch                   | 281 ms                                                                      | 278 ms: 1.01x faster                                                               |
| deltablue                  | 2.16 ms                                                                     | 2.14 ms: 1.01x faster                                                              |
| scimark_sor                | 83.9 ms                                                                     | 83.3 ms: 1.01x faster                                                              |
| sqlite_synth               | 1.57 us                                                                     | 1.56 us: 1.01x faster                                                              |
| richards                   | 29.4 ms                                                                     | 29.2 ms: 1.01x faster                                                              |
| regex_v8                   | 14.3 ms                                                                     | 14.4 ms: 1.00x slower                                                              |
| nqueens                    | 62.0 ms                                                                     | 62.3 ms: 1.01x slower                                                              |
| deepcopy_memo              | 19.5 us                                                                     | 19.7 us: 1.01x slower                                                              |
| thrift                     | 510 us                                                                      | 514 us: 1.01x slower                                                               |
| meteor_contest             | 75.8 ms                                                                     | 76.4 ms: 1.01x slower                                                              |
| scimark_sparse_mat_mult    | 2.57 ms                                                                     | 2.59 ms: 1.01x slower                                                              |
| go                         | 84.4 ms                                                                     | 85.0 ms: 1.01x slower                                                              |
| scimark_lu                 | 59.9 ms                                                                     | 60.3 ms: 1.01x slower                                                              |
| hexiom                     | 4.19 ms                                                                     | 4.22 ms: 1.01x slower                                                              |
| sqlglot_normalize          | 191 ms                                                                      | 193 ms: 1.01x slower                                                               |
| unpickle_pure_python       | 143 us                                                                      | 145 us: 1.01x slower                                                               |
| pprint_pformat             | 1.07 sec                                                                    | 1.08 sec: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                               |
| xml_etree_parse            | 90.2 ms                                                                     | 91.1 ms: 1.01x slower                                                              |
| telco                      | 4.66 ms                                                                     | 4.71 ms: 1.01x slower                                                              |
| regex_compile              | 84.2 ms                                                                     | 85.1 ms: 1.01x slower                                                              |
| float                      | 44.7 ms                                                                     | 45.3 ms: 1.01x slower                                                              |
| gc_traversal               | 1.98 ms                                                                     | 2.01 ms: 1.01x slower                                                              |
| shortest_path              | 347 ms                                                                      | 351 ms: 1.01x slower                                                               |
| python_startup             | 24.5 ms                                                                     | 24.8 ms: 1.01x slower                                                              |
| django_template            | 25.1 ms                                                                     | 25.5 ms: 1.01x slower                                                              |
| logging_simple             | 6.25 us                                                                     | 6.35 us: 1.02x slower                                                              |
| tomli_loads                | 1.37 sec                                                                    | 1.40 sec: 1.02x slower                                                             |
| xml_etree_process          | 39.8 ms                                                                     | 40.5 ms: 1.02x slower                                                              |
| bench_thread_pool          | 837 us                                                                      | 853 us: 1.02x slower                                                               |
| pyflate                    | 299 ms                                                                      | 305 ms: 1.02x slower                                                               |
| logging_silent             | 57.5 ns                                                                     | 58.8 ns: 1.02x slower                                                              |
| nbody                      | 69.7 ms                                                                     | 71.2 ms: 1.02x slower                                                              |
| coroutines                 | 13.3 ms                                                                     | 13.7 ms: 1.03x slower                                                              |
| html5lib                   | 38.6 ms                                                                     | 39.9 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (34): async_tree_none, python_startup_no_site, json_dumps, async_tree_memoization_tg, asyncio_websockets, async_generators, regex_dna, 2to3, sqlglot_optimize, chaos, dulwich_log, docutils, sympy_expand, pprint_safe_repr, sphinx, connected_components, xml_etree_generate, create_gc_cycles, sympy_integrate, raytrace, bench_mp_pool, pidigits, pylint, deepcopy_reduce, pycparser, sqlglot_parse, sqlglot_transpile, async_tree_cpu_io_mixed, xml_etree_iterparse, async_tree_memoization, mako, k_core, logging_format, richards_super

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 61.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown