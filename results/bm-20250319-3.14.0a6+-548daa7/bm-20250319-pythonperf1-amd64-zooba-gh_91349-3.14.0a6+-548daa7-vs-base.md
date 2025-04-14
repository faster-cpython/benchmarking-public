# Results vs. base

- fork: zooba
- ref: gh_91349
- machine: windows-amd64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.001x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 227 ms                                                                      | 230 ms: 1.01x slower                                           |
| html5lib       | 41.3 ms                                                                     | 41.8 ms: 1.01x slower                                          |
| sphinx         | 660 ms                                                                      | 673 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets | 308 ms                                                                      | 156 ms: 1.97x faster                                           |
| coroutines         | 13.6 ms                                                                     | 13.5 ms: 1.01x faster                                          |
| async_tree_none_tg | 181 ms                                                                      | 180 ms: 1.01x faster                                           |
| async_generators   | 229 ms                                                                      | 232 ms: 1.01x slower                                           |
| Geometric mean     | (ref)                                                                       | 1.06x faster                                                   |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 46.5 ms                                                                     | 46.8 ms: 1.01x slower                                          |
| nbody          | 67.0 ms                                                                     | 72.9 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 1.45 ms                                                                     | 1.44 ms: 1.01x faster                                          |
| regex_v8       | 13.8 ms                                                                     | 13.9 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 42.1 ms                                                                     | 42.3 ms: 1.00x slower                                          |
| unpickle_pure_python | 152 us                                                                      | 152 us: 1.00x slower                                           |
| json_loads           | 15.2 us                                                                     | 15.4 us: 1.01x slower                                          |
| xml_etree_parse      | 88.7 ms                                                                     | 90.3 ms: 1.02x slower                                          |
| xml_etree_iterparse  | 63.7 ms                                                                     | 65.3 ms: 1.03x slower                                          |
| pickle_pure_python   | 228 us                                                                      | 236 us: 1.03x slower                                           |
| tomli_loads          | 1.44 sec                                                                    | 1.49 sec: 1.04x slower                                         |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                   |

Benchmark hidden because not significant (2): xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 38.5 ms                                                                     | 38.1 ms: 1.01x faster                                          |
| mako           | 6.73 ms                                                                     | 6.86 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                   |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets       | 308 ms                                                                      | 156 ms: 1.97x faster                                           |
| mdp                      | 1.62 sec                                                                    | 1.54 sec: 1.05x faster                                         |
| sqlite_synth             | 1.65 us                                                                     | 1.60 us: 1.04x faster                                          |
| logging_simple           | 6.82 us                                                                     | 6.66 us: 1.02x faster                                          |
| logging_format           | 7.36 us                                                                     | 7.22 us: 1.02x faster                                          |
| create_gc_cycles         | 1.25 ms                                                                     | 1.23 ms: 1.02x faster                                          |
| generators               | 19.6 ms                                                                     | 19.3 ms: 1.01x faster                                          |
| genshi_xml               | 38.5 ms                                                                     | 38.1 ms: 1.01x faster                                          |
| dulwich_log              | 43.5 ms                                                                     | 43.1 ms: 1.01x faster                                          |
| coroutines               | 13.6 ms                                                                     | 13.5 ms: 1.01x faster                                          |
| regex_effbot             | 1.45 ms                                                                     | 1.44 ms: 1.01x faster                                          |
| async_tree_none_tg       | 181 ms                                                                      | 180 ms: 1.01x faster                                           |
| scimark_monte_carlo      | 44.1 ms                                                                     | 43.9 ms: 1.01x faster                                          |
| xml_etree_process        | 42.1 ms                                                                     | 42.3 ms: 1.00x slower                                          |
| sympy_str                | 178 ms                                                                      | 179 ms: 1.00x slower                                           |
| unpickle_pure_python     | 152 us                                                                      | 152 us: 1.00x slower                                           |
| bench_mp_pool            | 88.8 ms                                                                     | 89.3 ms: 1.01x slower                                          |
| hexiom                   | 4.46 ms                                                                     | 4.48 ms: 1.01x slower                                          |
| sqlglot_v2_transpile     | 1.13 ms                                                                     | 1.13 ms: 1.01x slower                                          |
| pprint_safe_repr         | 545 ms                                                                      | 548 ms: 1.01x slower                                           |
| comprehensions           | 12.1 us                                                                     | 12.1 us: 1.01x slower                                          |
| scimark_lu               | 60.9 ms                                                                     | 61.4 ms: 1.01x slower                                          |
| float                    | 46.5 ms                                                                     | 46.8 ms: 1.01x slower                                          |
| sqlglot_v2_parse         | 912 us                                                                      | 919 us: 1.01x slower                                           |
| fannkuch                 | 273 ms                                                                      | 275 ms: 1.01x slower                                           |
| pprint_pformat           | 1.10 sec                                                                    | 1.11 sec: 1.01x slower                                         |
| regex_v8                 | 13.8 ms                                                                     | 13.9 ms: 1.01x slower                                          |
| 2to3                     | 227 ms                                                                      | 230 ms: 1.01x slower                                           |
| sqlglot_v2_optimize      | 36.3 ms                                                                     | 36.6 ms: 1.01x slower                                          |
| async_generators         | 229 ms                                                                      | 232 ms: 1.01x slower                                           |
| html5lib                 | 41.3 ms                                                                     | 41.8 ms: 1.01x slower                                          |
| spectral_norm            | 57.2 ms                                                                     | 57.9 ms: 1.01x slower                                          |
| meteor_contest           | 76.9 ms                                                                     | 77.8 ms: 1.01x slower                                          |
| json_loads               | 15.2 us                                                                     | 15.4 us: 1.01x slower                                          |
| crypto_pyaes             | 49.3 ms                                                                     | 49.9 ms: 1.01x slower                                          |
| coverage                 | 48.4 ms                                                                     | 49.1 ms: 1.01x slower                                          |
| scimark_fft              | 184 ms                                                                      | 187 ms: 1.01x slower                                           |
| pycparser                | 754 ms                                                                      | 765 ms: 1.02x slower                                           |
| json                     | 3.06 ms                                                                     | 3.11 ms: 1.02x slower                                          |
| xml_etree_parse          | 88.7 ms                                                                     | 90.3 ms: 1.02x slower                                          |
| richards_super           | 33.3 ms                                                                     | 33.9 ms: 1.02x slower                                          |
| mako                     | 6.73 ms                                                                     | 6.86 ms: 1.02x slower                                          |
| sphinx                   | 660 ms                                                                      | 673 ms: 1.02x slower                                           |
| pyflate                  | 314 ms                                                                      | 321 ms: 1.02x slower                                           |
| bpe_tokeniser            | 3.00 sec                                                                    | 3.06 sec: 1.02x slower                                         |
| chaos                    | 43.4 ms                                                                     | 44.4 ms: 1.02x slower                                          |
| raytrace                 | 199 ms                                                                      | 204 ms: 1.02x slower                                           |
| connected_components     | 333 ms                                                                      | 341 ms: 1.03x slower                                           |
| typing_runtime_protocols | 111 us                                                                      | 114 us: 1.03x slower                                           |
| xml_etree_iterparse      | 63.7 ms                                                                     | 65.3 ms: 1.03x slower                                          |
| sqlglot_v2_normalize     | 75.2 ms                                                                     | 77.2 ms: 1.03x slower                                          |
| deepcopy_memo            | 19.1 us                                                                     | 19.7 us: 1.03x slower                                          |
| k_core                   | 1.71 sec                                                                    | 1.77 sec: 1.03x slower                                         |
| scimark_sor              | 81.9 ms                                                                     | 84.7 ms: 1.03x slower                                          |
| pickle_pure_python       | 228 us                                                                      | 236 us: 1.03x slower                                           |
| thrift                   | 522 us                                                                      | 541 us: 1.04x slower                                           |
| tomli_loads              | 1.44 sec                                                                    | 1.49 sec: 1.04x slower                                         |
| nqueens                  | 65.2 ms                                                                     | 67.8 ms: 1.04x slower                                          |
| richards                 | 29.3 ms                                                                     | 30.8 ms: 1.05x slower                                          |
| nbody                    | 67.0 ms                                                                     | 72.9 ms: 1.09x slower                                          |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                   |

Benchmark hidden because not significant (34): bench_thread_pool, async_tree_memoization_tg, genshi_text, many_optionals, xml_etree_generate, django_template, shortest_path, docutils, regex_dna, subparsers, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, python_startup_no_site, regex_compile, go, deepcopy, async_tree_io, sympy_sum, deepcopy_reduce, python_startup, async_tree_cpu_io_mixed, deltablue, sympy_expand, pidigits, logging_silent, pathlib, sympy_integrate, gc_traversal, async_tree_none, scimark_sparse_mat_mult, pylint, json_dumps, telco

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown