# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 228 ms                                                                     | 238 ms: 1.05x slower                                                               |
| docutils       | 1.66 sec                                                                   | 1.72 sec: 1.04x slower                                                             |
| html5lib       | 38.7 ms                                                                    | 38.3 ms: 1.01x faster                                                              |
| sphinx         | 652 ms                                                                     | 673 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization    | 223 ms                                                                     | 217 ms: 1.03x faster                                                               |
| async_tree_cpu_io_mixed   | 333 ms                                                                     | 338 ms: 1.02x slower                                                               |
| async_tree_memoization_tg | 213 ms                                                                     | 217 ms: 1.02x slower                                                               |
| async_tree_none_tg        | 173 ms                                                                     | 178 ms: 1.03x slower                                                               |
| async_tree_io_tg          | 405 ms                                                                     | 418 ms: 1.03x slower                                                               |
| async_tree_none           | 174 ms                                                                     | 180 ms: 1.03x slower                                                               |
| async_tree_io             | 404 ms                                                                     | 418 ms: 1.03x slower                                                               |
| coroutines                | 13.6 ms                                                                    | 14.5 ms: 1.06x slower                                                              |
| async_generators          | 233 ms                                                                     | 256 ms: 1.10x slower                                                               |
| Geometric mean            | (ref)                                                                      | 1.03x slower                                                                       |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                     | 150 ms: 1.01x slower                                                               |
| float          | 43.9 ms                                                                    | 44.9 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 121 ms                                                                     | 120 ms: 1.01x faster                                                               |
| regex_compile  | 81.4 ms                                                                    | 82.7 ms: 1.02x slower                                                              |
| regex_v8       | 14.1 ms                                                                    | 14.3 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.41 sec                                                                   | 1.42 sec: 1.01x slower                                                             |
| pickle_pure_python   | 213 us                                                                     | 216 us: 1.01x slower                                                               |
| unpickle_pure_python | 134 us                                                                     | 136 us: 1.02x slower                                                               |
| json_loads           | 15.1 us                                                                    | 15.4 us: 1.02x slower                                                              |
| xml_etree_iterparse  | 65.6 ms                                                                    | 68.0 ms: 1.04x slower                                                              |
| xml_etree_parse      | 92.5 ms                                                                    | 96.9 ms: 1.05x slower                                                              |
| xml_etree_process    | 39.9 ms                                                                    | 42.2 ms: 1.06x slower                                                              |
| json_dumps           | 6.78 ms                                                                    | 7.19 ms: 1.06x slower                                                              |
| xml_etree_generate   | 56.7 ms                                                                    | 60.5 ms: 1.07x slower                                                              |
| Geometric mean       | (ref)                                                                      | 1.04x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 19.6 ms                                                                    | 20.0 ms: 1.02x slower                                                              |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako           | 6.77 ms                                                                    | 6.57 ms: 1.03x faster                                                              |
| genshi_xml     | 34.2 ms                                                                    | 34.8 ms: 1.02x slower                                                              |
| genshi_text    | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                    | 103 ms                                                                     | 528 us: 194.07x faster                                                             |
| coverage                  | 294 ms                                                                     | 55.9 ms: 5.25x faster                                                              |
| gc_traversal              | 2.23 ms                                                                    | 2.15 ms: 1.04x faster                                                              |
| mako                      | 6.77 ms                                                                    | 6.57 ms: 1.03x faster                                                              |
| async_tree_memoization    | 223 ms                                                                     | 217 ms: 1.03x faster                                                               |
| html5lib                  | 38.7 ms                                                                    | 38.3 ms: 1.01x faster                                                              |
| regex_dna                 | 121 ms                                                                     | 120 ms: 1.01x faster                                                               |
| bench_mp_pool             | 97.6 ms                                                                    | 98.1 ms: 1.01x slower                                                              |
| hexiom                    | 4.07 ms                                                                    | 4.10 ms: 1.01x slower                                                              |
| richards                  | 27.9 ms                                                                    | 28.2 ms: 1.01x slower                                                              |
| tomli_loads               | 1.41 sec                                                                   | 1.42 sec: 1.01x slower                                                             |
| shortest_path             | 363 ms                                                                     | 366 ms: 1.01x slower                                                               |
| sqlglot_v2_transpile      | 1.03 ms                                                                    | 1.04 ms: 1.01x slower                                                              |
| pathlib                   | 32.1 ms                                                                    | 32.4 ms: 1.01x slower                                                              |
| spectral_norm             | 58.8 ms                                                                    | 59.4 ms: 1.01x slower                                                              |
| pidigits                  | 149 ms                                                                     | 150 ms: 1.01x slower                                                               |
| scimark_monte_carlo       | 39.7 ms                                                                    | 40.2 ms: 1.01x slower                                                              |
| create_gc_cycles          | 1.31 ms                                                                    | 1.33 ms: 1.01x slower                                                              |
| pickle_pure_python        | 213 us                                                                     | 216 us: 1.01x slower                                                               |
| richards_super            | 31.7 ms                                                                    | 32.1 ms: 1.01x slower                                                              |
| unpickle_pure_python      | 134 us                                                                     | 136 us: 1.02x slower                                                               |
| regex_compile             | 81.4 ms                                                                    | 82.7 ms: 1.02x slower                                                              |
| async_tree_cpu_io_mixed   | 333 ms                                                                     | 338 ms: 1.02x slower                                                               |
| dulwich_log               | 42.2 ms                                                                    | 42.9 ms: 1.02x slower                                                              |
| regex_v8                  | 14.1 ms                                                                    | 14.3 ms: 1.02x slower                                                              |
| async_tree_memoization_tg | 213 ms                                                                     | 217 ms: 1.02x slower                                                               |
| logging_format            | 6.69 us                                                                    | 6.82 us: 1.02x slower                                                              |
| genshi_xml                | 34.2 ms                                                                    | 34.8 ms: 1.02x slower                                                              |
| json_loads                | 15.1 us                                                                    | 15.4 us: 1.02x slower                                                              |
| python_startup_no_site    | 19.6 ms                                                                    | 20.0 ms: 1.02x slower                                                              |
| pycparser                 | 717 ms                                                                     | 733 ms: 1.02x slower                                                               |
| chaos                     | 38.4 ms                                                                    | 39.3 ms: 1.02x slower                                                              |
| many_optionals            | 444 us                                                                     | 454 us: 1.02x slower                                                               |
| float                     | 43.9 ms                                                                    | 44.9 ms: 1.02x slower                                                              |
| genshi_text               | 15.4 ms                                                                    | 15.7 ms: 1.02x slower                                                              |
| async_tree_none_tg        | 173 ms                                                                     | 178 ms: 1.03x slower                                                               |
| pprint_pformat            | 1.02 sec                                                                   | 1.04 sec: 1.03x slower                                                             |
| json                      | 2.99 ms                                                                    | 3.07 ms: 1.03x slower                                                              |
| scimark_sor               | 75.5 ms                                                                    | 77.6 ms: 1.03x slower                                                              |
| sympy_sum                 | 88.8 ms                                                                    | 91.3 ms: 1.03x slower                                                              |
| deltablue                 | 2.14 ms                                                                    | 2.20 ms: 1.03x slower                                                              |
| scimark_lu                | 57.1 ms                                                                    | 58.9 ms: 1.03x slower                                                              |
| generators                | 19.2 ms                                                                    | 19.9 ms: 1.03x slower                                                              |
| async_tree_io_tg          | 405 ms                                                                     | 418 ms: 1.03x slower                                                               |
| sympy_integrate           | 12.4 ms                                                                    | 12.8 ms: 1.03x slower                                                              |
| sphinx                    | 652 ms                                                                     | 673 ms: 1.03x slower                                                               |
| subparsers                | 16.9 ms                                                                    | 17.4 ms: 1.03x slower                                                              |
| async_tree_none           | 174 ms                                                                     | 180 ms: 1.03x slower                                                               |
| crypto_pyaes              | 47.0 ms                                                                    | 48.6 ms: 1.03x slower                                                              |
| async_tree_io             | 404 ms                                                                     | 418 ms: 1.03x slower                                                               |
| typing_runtime_protocols  | 110 us                                                                     | 114 us: 1.04x slower                                                               |
| xml_etree_iterparse       | 65.6 ms                                                                    | 68.0 ms: 1.04x slower                                                              |
| pprint_safe_repr          | 495 ms                                                                     | 513 ms: 1.04x slower                                                               |
| deepcopy_memo             | 18.3 us                                                                    | 19.0 us: 1.04x slower                                                              |
| docutils                  | 1.66 sec                                                                   | 1.72 sec: 1.04x slower                                                             |
| comprehensions            | 11.5 us                                                                    | 12.0 us: 1.04x slower                                                              |
| sqlite_synth              | 1.60 us                                                                    | 1.67 us: 1.04x slower                                                              |
| meteor_contest            | 74.7 ms                                                                    | 78.0 ms: 1.04x slower                                                              |
| 2to3                      | 228 ms                                                                     | 238 ms: 1.05x slower                                                               |
| xml_etree_parse           | 92.5 ms                                                                    | 96.9 ms: 1.05x slower                                                              |
| sympy_str                 | 171 ms                                                                     | 179 ms: 1.05x slower                                                               |
| sqlglot_v2_optimize       | 34.4 ms                                                                    | 36.1 ms: 1.05x slower                                                              |
| deepcopy_reduce           | 1.84 us                                                                    | 1.93 us: 1.05x slower                                                              |
| bpe_tokeniser             | 2.91 sec                                                                   | 3.06 sec: 1.05x slower                                                             |
| logging_silent            | 55.4 ns                                                                    | 58.6 ns: 1.06x slower                                                              |
| nqueens                   | 60.7 ms                                                                    | 64.2 ms: 1.06x slower                                                              |
| xml_etree_process         | 39.9 ms                                                                    | 42.2 ms: 1.06x slower                                                              |
| coroutines                | 13.6 ms                                                                    | 14.5 ms: 1.06x slower                                                              |
| scimark_sparse_mat_mult   | 2.48 ms                                                                    | 2.63 ms: 1.06x slower                                                              |
| sympy_expand              | 292 ms                                                                     | 310 ms: 1.06x slower                                                               |
| json_dumps                | 6.78 ms                                                                    | 7.19 ms: 1.06x slower                                                              |
| xml_etree_generate        | 56.7 ms                                                                    | 60.5 ms: 1.07x slower                                                              |
| deepcopy                  | 171 us                                                                     | 183 us: 1.07x slower                                                               |
| scimark_fft               | 172 ms                                                                     | 184 ms: 1.07x slower                                                               |
| mdp                       | 795 ms                                                                     | 855 ms: 1.07x slower                                                               |
| pyflate                   | 284 ms                                                                     | 308 ms: 1.09x slower                                                               |
| telco                     | 4.67 ms                                                                    | 5.11 ms: 1.09x slower                                                              |
| async_generators          | 233 ms                                                                     | 256 ms: 1.10x slower                                                               |
| fannkuch                  | 251 ms                                                                     | 279 ms: 1.11x slower                                                               |
| Geometric mean            | (ref)                                                                      | 1.05x faster                                                                       |

Benchmark hidden because not significant (15): bench_thread_pool, sqlglot_v2_parse, async_tree_cpu_io_mixed_tg, raytrace, connected_components, go, nbody, regex_effbot, django_template, logging_simple, python_startup, asyncio_websockets, k_core, sqlglot_v2_normalize, pylint

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown