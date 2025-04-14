# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.009x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                                    | 1.69 sec: 1.02x slower                                                         |
| html5lib       | 40.2 ms                                                                     | 41.0 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 314 ms                                                                      | 308 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 340 ms                                                                      | 345 ms: 1.01x slower                                                           |
| async_tree_none            | 185 ms                                                                      | 188 ms: 1.01x slower                                                           |
| async_tree_io              | 417 ms                                                                      | 423 ms: 1.02x slower                                                           |
| async_tree_memoization     | 217 ms                                                                      | 221 ms: 1.02x slower                                                           |
| coroutines                 | 13.4 ms                                                                     | 13.7 ms: 1.02x slower                                                          |
| async_tree_none_tg         | 174 ms                                                                      | 178 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 339 ms                                                                      | 348 ms: 1.03x slower                                                           |
| async_tree_memoization_tg  | 211 ms                                                                      | 218 ms: 1.03x slower                                                           |
| async_generators           | 221 ms                                                                      | 230 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 398 ms                                                                      | 414 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 72.7 ms                                                                     | 68.6 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 86.9 ms                                                                     | 85.9 ms: 1.01x faster                                                          |
| regex_dna      | 119 ms                                                                      | 117 ms: 1.01x faster                                                           |
| regex_v8       | 14.9 ms                                                                     | 15.5 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 150 us                                                                      | 148 us: 1.02x faster                                                           |
| json_loads           | 14.6 us                                                                     | 14.7 us: 1.01x slower                                                          |
| xml_etree_parse      | 89.1 ms                                                                     | 90.3 ms: 1.01x slower                                                          |
| pickle_pure_python   | 227 us                                                                      | 230 us: 1.02x slower                                                           |
| xml_etree_generate   | 57.2 ms                                                                     | 58.7 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 62.0 ms                                                                     | 63.7 ms: 1.03x slower                                                          |
| json_dumps           | 6.76 ms                                                                     | 6.97 ms: 1.03x slower                                                          |
| xml_etree_process    | 40.3 ms                                                                     | 42.3 ms: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.0 ms                                                                     | 19.2 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                                     | 38.0 ms: 1.02x slower                                                          |
| mako            | 6.68 ms                                                                     | 6.93 ms: 1.04x slower                                                          |
| django_template | 25.2 ms                                                                     | 26.4 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250228-pythonperf1-amd64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sor                | 85.4 ms                                                                     | 80.3 ms: 1.06x faster                                                          |
| nbody                      | 72.7 ms                                                                     | 68.6 ms: 1.06x faster                                                          |
| deepcopy_memo              | 20.3 us                                                                     | 19.5 us: 1.04x faster                                                          |
| pprint_safe_repr           | 555 ms                                                                      | 540 ms: 1.03x faster                                                           |
| richards_super             | 34.0 ms                                                                     | 33.0 ms: 1.03x faster                                                          |
| richards                   | 29.8 ms                                                                     | 29.1 ms: 1.03x faster                                                          |
| spectral_norm              | 61.3 ms                                                                     | 60.0 ms: 1.02x faster                                                          |
| json                       | 3.13 ms                                                                     | 3.06 ms: 1.02x faster                                                          |
| asyncio_websockets         | 314 ms                                                                      | 308 ms: 1.02x faster                                                           |
| scimark_lu                 | 63.6 ms                                                                     | 62.4 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.12 sec                                                                    | 1.10 sec: 1.02x faster                                                         |
| logging_silent             | 59.6 ns                                                                     | 58.5 ns: 1.02x faster                                                          |
| unpickle_pure_python       | 150 us                                                                      | 148 us: 1.02x faster                                                           |
| meteor_contest             | 77.9 ms                                                                     | 76.8 ms: 1.01x faster                                                          |
| scimark_sparse_mat_mult    | 2.65 ms                                                                     | 2.61 ms: 1.01x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                                     | 44.6 ms: 1.01x faster                                                          |
| regex_compile              | 86.9 ms                                                                     | 85.9 ms: 1.01x faster                                                          |
| sympy_integrate            | 13.3 ms                                                                     | 13.2 ms: 1.01x faster                                                          |
| regex_dna                  | 119 ms                                                                      | 117 ms: 1.01x faster                                                           |
| create_gc_cycles           | 1.22 ms                                                                     | 1.21 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.59 us                                                                     | 1.58 us: 1.01x faster                                                          |
| many_optionals             | 435 us                                                                      | 432 us: 1.01x faster                                                           |
| fannkuch                   | 276 ms                                                                      | 277 ms: 1.01x slower                                                           |
| crypto_pyaes               | 50.2 ms                                                                     | 50.5 ms: 1.01x slower                                                          |
| sympy_sum                  | 88.9 ms                                                                     | 89.6 ms: 1.01x slower                                                          |
| mdp                        | 1.58 sec                                                                    | 1.59 sec: 1.01x slower                                                         |
| sqlglot_parse              | 883 us                                                                      | 892 us: 1.01x slower                                                           |
| python_startup_no_site     | 19.0 ms                                                                     | 19.2 ms: 1.01x slower                                                          |
| json_loads                 | 14.6 us                                                                     | 14.7 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 340 ms                                                                      | 345 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.09 ms                                                                     | 1.11 ms: 1.01x slower                                                          |
| sympy_expand               | 298 ms                                                                      | 301 ms: 1.01x slower                                                           |
| pathlib                    | 31.8 ms                                                                     | 32.2 ms: 1.01x slower                                                          |
| sympy_str                  | 174 ms                                                                      | 176 ms: 1.01x slower                                                           |
| xml_etree_parse            | 89.1 ms                                                                     | 90.3 ms: 1.01x slower                                                          |
| go                         | 87.6 ms                                                                     | 88.8 ms: 1.01x slower                                                          |
| async_tree_none            | 185 ms                                                                      | 188 ms: 1.01x slower                                                           |
| pickle_pure_python         | 227 us                                                                      | 230 us: 1.02x slower                                                           |
| async_tree_io              | 417 ms                                                                      | 423 ms: 1.02x slower                                                           |
| logging_simple             | 6.40 us                                                                     | 6.52 us: 1.02x slower                                                          |
| docutils                   | 1.66 sec                                                                    | 1.69 sec: 1.02x slower                                                         |
| html5lib                   | 40.2 ms                                                                     | 41.0 ms: 1.02x slower                                                          |
| raytrace                   | 193 ms                                                                      | 197 ms: 1.02x slower                                                           |
| async_tree_memoization     | 217 ms                                                                      | 221 ms: 1.02x slower                                                           |
| genshi_xml                 | 37.3 ms                                                                     | 38.0 ms: 1.02x slower                                                          |
| coverage                   | 47.5 ms                                                                     | 48.7 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 1.92 us                                                                     | 1.96 us: 1.02x slower                                                          |
| xml_etree_generate         | 57.2 ms                                                                     | 58.7 ms: 1.02x slower                                                          |
| coroutines                 | 13.4 ms                                                                     | 13.7 ms: 1.02x slower                                                          |
| async_tree_none_tg         | 174 ms                                                                      | 178 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 62.0 ms                                                                     | 63.7 ms: 1.03x slower                                                          |
| subparsers                 | 16.2 ms                                                                     | 16.7 ms: 1.03x slower                                                          |
| deltablue                  | 2.22 ms                                                                     | 2.28 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 339 ms                                                                      | 348 ms: 1.03x slower                                                           |
| async_tree_memoization_tg  | 211 ms                                                                      | 218 ms: 1.03x slower                                                           |
| json_dumps                 | 6.76 ms                                                                     | 6.97 ms: 1.03x slower                                                          |
| logging_format             | 6.85 us                                                                     | 7.06 us: 1.03x slower                                                          |
| bpe_tokeniser              | 2.90 sec                                                                    | 2.99 sec: 1.03x slower                                                         |
| telco                      | 4.77 ms                                                                     | 4.93 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 35.1 ms                                                                     | 36.4 ms: 1.03x slower                                                          |
| mako                       | 6.68 ms                                                                     | 6.93 ms: 1.04x slower                                                          |
| async_generators           | 221 ms                                                                      | 230 ms: 1.04x slower                                                           |
| async_tree_io_tg           | 398 ms                                                                      | 414 ms: 1.04x slower                                                           |
| connected_components       | 322 ms                                                                      | 335 ms: 1.04x slower                                                           |
| nqueens                    | 62.6 ms                                                                     | 65.3 ms: 1.04x slower                                                          |
| regex_v8                   | 14.9 ms                                                                     | 15.5 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 191 ms                                                                      | 199 ms: 1.04x slower                                                           |
| xml_etree_process          | 40.3 ms                                                                     | 42.3 ms: 1.05x slower                                                          |
| django_template            | 25.2 ms                                                                     | 26.4 ms: 1.05x slower                                                          |
| shortest_path              | 352 ms                                                                      | 370 ms: 1.05x slower                                                           |
| comprehensions             | 11.4 us                                                                     | 12.0 us: 1.06x slower                                                          |
| chaos                      | 41.5 ms                                                                     | 43.9 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 106 us                                                                      | 113 us: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (21): gc_traversal, regex_effbot, thrift, deepcopy, scimark_fft, bench_mp_pool, generators, hexiom, pyflate, tomli_loads, pidigits, dulwich_log, 2to3, float, python_startup, genshi_text, bench_thread_pool, sphinx, pycparser, k_core, pylint

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown