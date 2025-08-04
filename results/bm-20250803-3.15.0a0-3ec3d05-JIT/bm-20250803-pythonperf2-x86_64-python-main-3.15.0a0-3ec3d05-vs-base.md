# Results vs. base

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ec3d05
- commit date: 2025-08-03
- overall geometric mean: 1.000x slower
- HPT reliability: 69.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 287 ms                                                                      | 286 ms: 1.00x faster                                        |
| docutils       | 2.93 sec                                                                    | 2.94 sec: 1.00x slower                                      |
| html5lib       | 66.8 ms                                                                     | 67.7 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators        | 458 ms                                                                      | 440 ms: 1.04x faster                                        |
| coroutines              | 22.5 ms                                                                     | 22.4 ms: 1.00x faster                                       |
| async_tree_cpu_io_mixed | 501 ms                                                                      | 503 ms: 1.00x slower                                        |
| asyncio_websockets      | 380 ms                                                                      | 383 ms: 1.01x slower                                        |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 64.2 ms                                                                     | 64.6 ms: 1.01x slower                                       |
| nbody          | 97.9 ms                                                                     | 99.1 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.71 ms                                                                     | 3.64 ms: 1.02x faster                                       |
| regex_v8       | 23.5 ms                                                                     | 23.3 ms: 1.01x faster                                       |
| regex_compile  | 133 ms                                                                      | 135 ms: 1.01x slower                                        |
| regex_dna      | 222 ms                                                                      | 227 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|--------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads        | 1.93 sec                                                                    | 1.92 sec: 1.01x faster                                      |
| pickle_pure_python | 334 us                                                                      | 332 us: 1.01x faster                                        |
| xml_etree_process  | 55.8 ms                                                                     | 55.5 ms: 1.01x faster                                       |
| json_loads         | 26.7 us                                                                     | 26.5 us: 1.01x faster                                       |
| xml_etree_generate | 79.6 ms                                                                     | 80.5 ms: 1.01x slower                                       |
| xml_etree_parse    | 137 ms                                                                      | 141 ms: 1.03x slower                                        |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 10.0 ms                                                                     | 9.78 ms: 1.03x faster                                       |
| genshi_text    | 23.2 ms                                                                     | 22.9 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators        | 458 ms                                                                      | 440 ms: 1.04x faster                                        |
| generators              | 30.4 ms                                                                     | 29.5 ms: 1.03x faster                                       |
| nqueens                 | 93.3 ms                                                                     | 90.8 ms: 1.03x faster                                       |
| mdp                     | 1.32 sec                                                                    | 1.28 sec: 1.03x faster                                      |
| mako                    | 10.0 ms                                                                     | 9.78 ms: 1.03x faster                                       |
| scimark_sparse_mat_mult | 5.08 ms                                                                     | 4.96 ms: 1.02x faster                                       |
| telco                   | 162 ms                                                                      | 158 ms: 1.02x faster                                        |
| scimark_monte_carlo     | 64.1 ms                                                                     | 62.8 ms: 1.02x faster                                       |
| regex_effbot            | 3.71 ms                                                                     | 3.64 ms: 1.02x faster                                       |
| bpe_tokeniser           | 4.60 sec                                                                    | 4.51 sec: 1.02x faster                                      |
| scimark_fft             | 301 ms                                                                      | 297 ms: 1.02x faster                                        |
| genshi_text             | 23.2 ms                                                                     | 22.9 ms: 1.01x faster                                       |
| regex_v8                | 23.5 ms                                                                     | 23.3 ms: 1.01x faster                                       |
| chaos                   | 59.5 ms                                                                     | 59.0 ms: 1.01x faster                                       |
| spectral_norm           | 80.4 ms                                                                     | 79.7 ms: 1.01x faster                                       |
| pycparser               | 1.26 sec                                                                    | 1.25 sec: 1.01x faster                                      |
| tomli_loads             | 1.93 sec                                                                    | 1.92 sec: 1.01x faster                                      |
| pickle_pure_python      | 334 us                                                                      | 332 us: 1.01x faster                                        |
| xml_etree_process       | 55.8 ms                                                                     | 55.5 ms: 1.01x faster                                       |
| sympy_str               | 292 ms                                                                      | 291 ms: 1.01x faster                                        |
| sympy_expand            | 500 ms                                                                      | 498 ms: 1.01x faster                                        |
| json_loads              | 26.7 us                                                                     | 26.5 us: 1.01x faster                                       |
| comprehensions          | 17.4 us                                                                     | 17.3 us: 1.00x faster                                       |
| dulwich_log             | 59.1 ms                                                                     | 58.8 ms: 1.00x faster                                       |
| 2to3                    | 287 ms                                                                      | 286 ms: 1.00x faster                                        |
| sqlglot_v2_transpile    | 1.70 ms                                                                     | 1.69 ms: 1.00x faster                                       |
| coroutines              | 22.5 ms                                                                     | 22.4 ms: 1.00x faster                                       |
| sqlglot_v2_normalize    | 115 ms                                                                      | 114 ms: 1.00x faster                                        |
| connected_components    | 407 ms                                                                      | 407 ms: 1.00x slower                                        |
| create_gc_cycles        | 2.89 ms                                                                     | 2.90 ms: 1.00x slower                                       |
| many_optionals          | 1.23 ms                                                                     | 1.23 ms: 1.00x slower                                       |
| scimark_lu              | 95.0 ms                                                                     | 95.4 ms: 1.00x slower                                       |
| docutils                | 2.93 sec                                                                    | 2.94 sec: 1.00x slower                                      |
| async_tree_cpu_io_mixed | 501 ms                                                                      | 503 ms: 1.00x slower                                        |
| float                   | 64.2 ms                                                                     | 64.6 ms: 1.01x slower                                       |
| gc_traversal            | 6.47 ms                                                                     | 6.51 ms: 1.01x slower                                       |
| deepcopy_memo           | 27.9 us                                                                     | 28.1 us: 1.01x slower                                       |
| asyncio_websockets      | 380 ms                                                                      | 383 ms: 1.01x slower                                        |
| hexiom                  | 6.16 ms                                                                     | 6.21 ms: 1.01x slower                                       |
| pprint_pformat          | 1.49 sec                                                                    | 1.50 sec: 1.01x slower                                      |
| xml_etree_generate      | 79.6 ms                                                                     | 80.5 ms: 1.01x slower                                       |
| logging_format          | 6.62 us                                                                     | 6.69 us: 1.01x slower                                       |
| meteor_contest          | 119 ms                                                                      | 121 ms: 1.01x slower                                        |
| deltablue               | 2.87 ms                                                                     | 2.91 ms: 1.01x slower                                       |
| regex_compile           | 133 ms                                                                      | 135 ms: 1.01x slower                                        |
| nbody                   | 97.9 ms                                                                     | 99.1 ms: 1.01x slower                                       |
| go                      | 127 ms                                                                      | 129 ms: 1.01x slower                                        |
| html5lib                | 66.8 ms                                                                     | 67.7 ms: 1.01x slower                                       |
| logging_simple          | 6.00 us                                                                     | 6.10 us: 1.02x slower                                       |
| richards_super          | 40.7 ms                                                                     | 41.4 ms: 1.02x slower                                       |
| deepcopy                | 275 us                                                                      | 280 us: 1.02x slower                                        |
| raytrace                | 283 ms                                                                      | 288 ms: 1.02x slower                                        |
| regex_dna               | 222 ms                                                                      | 227 ms: 1.02x slower                                        |
| logging_silent          | 91.7 ns                                                                     | 93.7 ns: 1.02x slower                                       |
| richards                | 34.6 ms                                                                     | 35.4 ms: 1.02x slower                                       |
| xml_etree_parse         | 137 ms                                                                      | 141 ms: 1.03x slower                                        |
| coverage                | 78.0 ms                                                                     | 80.7 ms: 1.03x slower                                       |
| fannkuch                | 362 ms                                                                      | 376 ms: 1.04x slower                                        |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (35): typing_runtime_protocols, async_tree_memoization_tg, sqlglot_v2_parse, thrift, django_template, pylint, xml_etree_iterparse, sqlite_synth, async_tree_cpu_io_mixed_tg, json_dumps, sympy_integrate, scimark_sor, async_tree_none_tg, async_tree_io_tg, sqlglot_v2_optimize, pathlib, shortest_path, pidigits, python_startup, djangocms, subparsers, k_core, python_startup_no_site, async_tree_memoization, unpickle_pure_python, sympy_sum, json, crypto_pyaes, async_tree_none, pyflate, deepcopy_reduce, async_tree_io, pprint_safe_repr, genshi_xml, sphinx

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 69.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x