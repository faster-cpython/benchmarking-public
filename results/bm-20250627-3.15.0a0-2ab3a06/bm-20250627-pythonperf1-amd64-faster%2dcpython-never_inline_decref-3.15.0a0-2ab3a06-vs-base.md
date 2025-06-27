# Results vs. base

- fork: faster-cpython
- ref: never_inline_decref
- machine: windows-amd64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.001x slower
- HPT reliability: 77.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| sphinx         | 634 ms                                                                     | 642 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                        |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 333 ms                                                                     | 326 ms: 1.02x faster                                                                |
| asyncio_websockets         | 161 ms                                                                     | 158 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                     | 339 ms: 1.02x faster                                                                |
| async_tree_io_tg           | 398 ms                                                                     | 393 ms: 1.01x faster                                                                |
| async_generators           | 236 ms                                                                     | 243 ms: 1.03x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none, coroutines, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                     | 146 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                    | 13.7 ms: 1.04x faster                                                               |
| regex_dna      | 120 ms                                                                     | 119 ms: 1.01x faster                                                                |
| regex_compile  | 80.6 ms                                                                    | 81.8 ms: 1.01x slower                                                               |
| regex_effbot   | 1.51 ms                                                                    | 1.55 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_loads           | 14.4 us                                                                    | 14.3 us: 1.01x faster                                                               |
| pickle_pure_python   | 213 us                                                                     | 211 us: 1.01x faster                                                                |
| unpickle_pure_python | 134 us                                                                     | 135 us: 1.01x slower                                                                |
| json_dumps           | 6.35 ms                                                                    | 6.43 ms: 1.01x slower                                                               |
| tomli_loads          | 1.42 sec                                                                   | 1.44 sec: 1.01x slower                                                              |
| xml_etree_iterparse  | 64.6 ms                                                                    | 65.5 ms: 1.01x slower                                                               |
| xml_etree_process    | 38.9 ms                                                                    | 39.4 ms: 1.01x slower                                                               |
| xml_etree_parse      | 88.8 ms                                                                    | 92.1 ms: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup | 25.9 ms                                                                    | 25.5 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 24.5 ms                                                                    | 23.6 ms: 1.04x faster                                                               |
| genshi_text     | 15.7 ms                                                                    | 15.3 ms: 1.03x faster                                                               |
| genshi_xml      | 34.7 ms                                                                    | 34.0 ms: 1.02x faster                                                               |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| scimark_lu                 | 60.0 ms                                                                    | 57.1 ms: 1.05x faster                                                               |
| logging_silent             | 57.6 ns                                                                    | 55.2 ns: 1.04x faster                                                               |
| regex_v8                   | 14.3 ms                                                                    | 13.7 ms: 1.04x faster                                                               |
| django_template            | 24.5 ms                                                                    | 23.6 ms: 1.04x faster                                                               |
| deepcopy_memo              | 18.5 us                                                                    | 17.9 us: 1.04x faster                                                               |
| genshi_text                | 15.7 ms                                                                    | 15.3 ms: 1.03x faster                                                               |
| scimark_sor                | 78.7 ms                                                                    | 76.5 ms: 1.03x faster                                                               |
| scimark_fft                | 190 ms                                                                     | 185 ms: 1.03x faster                                                                |
| richards_super             | 31.2 ms                                                                    | 30.5 ms: 1.02x faster                                                               |
| async_tree_cpu_io_mixed    | 333 ms                                                                     | 326 ms: 1.02x faster                                                                |
| asyncio_websockets         | 161 ms                                                                     | 158 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                     | 339 ms: 1.02x faster                                                                |
| genshi_xml                 | 34.7 ms                                                                    | 34.0 ms: 1.02x faster                                                               |
| richards                   | 27.3 ms                                                                    | 26.8 ms: 1.02x faster                                                               |
| python_startup             | 25.9 ms                                                                    | 25.5 ms: 1.02x faster                                                               |
| chaos                      | 41.1 ms                                                                    | 40.4 ms: 1.02x faster                                                               |
| regex_dna                  | 120 ms                                                                     | 119 ms: 1.01x faster                                                                |
| go                         | 77.6 ms                                                                    | 76.5 ms: 1.01x faster                                                               |
| sqlglot_v2_transpile       | 1.04 ms                                                                    | 1.02 ms: 1.01x faster                                                               |
| raytrace                   | 179 ms                                                                     | 177 ms: 1.01x faster                                                                |
| async_tree_io_tg           | 398 ms                                                                     | 393 ms: 1.01x faster                                                                |
| json_loads                 | 14.4 us                                                                    | 14.3 us: 1.01x faster                                                               |
| sqlite_synth               | 1.60 us                                                                    | 1.58 us: 1.01x faster                                                               |
| spectral_norm              | 64.9 ms                                                                    | 64.3 ms: 1.01x faster                                                               |
| pickle_pure_python         | 213 us                                                                     | 211 us: 1.01x faster                                                                |
| sqlglot_v2_normalize       | 71.5 ms                                                                    | 70.8 ms: 1.01x faster                                                               |
| sqlglot_v2_optimize        | 34.0 ms                                                                    | 33.7 ms: 1.01x faster                                                               |
| sympy_integrate            | 12.6 ms                                                                    | 12.5 ms: 1.01x faster                                                               |
| sympy_expand               | 292 ms                                                                     | 290 ms: 1.01x faster                                                                |
| pidigits                   | 147 ms                                                                     | 146 ms: 1.01x faster                                                                |
| scimark_monte_carlo        | 40.8 ms                                                                    | 41.0 ms: 1.01x slower                                                               |
| sympy_sum                  | 87.3 ms                                                                    | 87.8 ms: 1.01x slower                                                               |
| crypto_pyaes               | 47.6 ms                                                                    | 47.9 ms: 1.01x slower                                                               |
| mdp                        | 800 ms                                                                     | 807 ms: 1.01x slower                                                                |
| unpickle_pure_python       | 134 us                                                                     | 135 us: 1.01x slower                                                                |
| shortest_path              | 364 ms                                                                     | 367 ms: 1.01x slower                                                                |
| logging_simple             | 6.13 us                                                                    | 6.19 us: 1.01x slower                                                               |
| json_dumps                 | 6.35 ms                                                                    | 6.43 ms: 1.01x slower                                                               |
| coverage                   | 51.6 ms                                                                    | 52.3 ms: 1.01x slower                                                               |
| sphinx                     | 634 ms                                                                     | 642 ms: 1.01x slower                                                                |
| tomli_loads                | 1.42 sec                                                                   | 1.44 sec: 1.01x slower                                                              |
| create_gc_cycles           | 1.31 ms                                                                    | 1.33 ms: 1.01x slower                                                               |
| xml_etree_iterparse        | 64.6 ms                                                                    | 65.5 ms: 1.01x slower                                                               |
| connected_components       | 333 ms                                                                     | 338 ms: 1.01x slower                                                                |
| xml_etree_process          | 38.9 ms                                                                    | 39.4 ms: 1.01x slower                                                               |
| regex_compile              | 80.6 ms                                                                    | 81.8 ms: 1.01x slower                                                               |
| logging_format             | 6.56 us                                                                    | 6.67 us: 1.02x slower                                                               |
| k_core                     | 1.71 sec                                                                   | 1.73 sec: 1.02x slower                                                              |
| deepcopy                   | 169 us                                                                     | 172 us: 1.02x slower                                                                |
| generators                 | 19.2 ms                                                                    | 19.6 ms: 1.02x slower                                                               |
| pprint_pformat             | 1.01 sec                                                                   | 1.03 sec: 1.02x slower                                                              |
| bpe_tokeniser              | 2.95 sec                                                                   | 3.01 sec: 1.02x slower                                                              |
| hexiom                     | 4.08 ms                                                                    | 4.18 ms: 1.02x slower                                                               |
| regex_effbot               | 1.51 ms                                                                    | 1.55 ms: 1.02x slower                                                               |
| nqueens                    | 61.6 ms                                                                    | 63.0 ms: 1.02x slower                                                               |
| json                       | 3.03 ms                                                                    | 3.11 ms: 1.03x slower                                                               |
| async_generators           | 236 ms                                                                     | 243 ms: 1.03x slower                                                                |
| meteor_contest             | 71.9 ms                                                                    | 73.9 ms: 1.03x slower                                                               |
| telco                      | 4.60 ms                                                                    | 4.73 ms: 1.03x slower                                                               |
| comprehensions             | 10.8 us                                                                    | 11.1 us: 1.03x slower                                                               |
| scimark_sparse_mat_mult    | 2.53 ms                                                                    | 2.62 ms: 1.03x slower                                                               |
| gc_traversal               | 2.11 ms                                                                    | 2.18 ms: 1.03x slower                                                               |
| pprint_safe_repr           | 492 ms                                                                     | 509 ms: 1.03x slower                                                                |
| deepcopy_reduce            | 1.80 us                                                                    | 1.87 us: 1.04x slower                                                               |
| xml_etree_parse            | 88.8 ms                                                                    | 92.1 ms: 1.04x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                                        |

Benchmark hidden because not significant (27): pylint, python_startup_no_site, async_tree_io, sympy_str, nbody, sqlglot_v2_parse, async_tree_memoization_tg, fannkuch, dulwich_log, thrift, float, async_tree_memoization, typing_runtime_protocols, many_optionals, pathlib, xml_etree_generate, async_tree_none, coroutines, 2to3, async_tree_none_tg, deltablue, subparsers, pyflate, docutils, mako, html5lib, pycparser

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 77.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown