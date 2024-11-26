# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: windows-x86
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.001x slower
- HPT reliability: 75.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 244 ms                                                                          | 246 ms: 1.01x slower                                                        |
| docutils       | 1.82 sec                                                                        | 1.83 sec: 1.01x slower                                                      |
| html5lib       | 45.8 ms                                                                         | 44.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 464 ms                                                                          | 469 ms: 1.01x slower                                                        |
| asyncio_websockets      | 351 ms                                                                          | 357 ms: 1.02x slower                                                        |
| async_generators        | 285 ms                                                                          | 291 ms: 1.02x slower                                                        |
| async_tree_io           | 515 ms                                                                          | 527 ms: 1.02x slower                                                        |
| Geometric mean          | (ref)                                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                          | 202 ms: 1.01x slower                                                        |
| float          | 61.1 ms                                                                         | 62.8 ms: 1.03x slower                                                       |
| nbody          | 85.4 ms                                                                         | 93.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                                           | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                                         | 15.6 ms: 1.01x faster                                                       |
| regex_effbot   | 1.87 ms                                                                         | 1.88 ms: 1.01x slower                                                       |
| regex_dna      | 122 ms                                                                          | 123 ms: 1.01x slower                                                        |
| regex_compile  | 105 ms                                                                          | 108 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.79 sec                                                                        | 1.75 sec: 1.02x faster                                                      |
| unpickle_pure_python | 173 us                                                                          | 174 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 67.9 ms                                                                         | 68.9 ms: 1.01x slower                                                       |
| json_loads           | 20.6 us                                                                         | 20.9 us: 1.02x slower                                                       |
| xml_etree_generate   | 66.7 ms                                                                         | 67.8 ms: 1.02x slower                                                       |
| xml_etree_parse      | 110 ms                                                                          | 112 ms: 1.02x slower                                                        |
| pickle_pure_python   | 266 us                                                                          | 272 us: 1.02x slower                                                        |
| xml_etree_process    | 48.2 ms                                                                         | 49.7 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 19.3 ms                                                                         | 20.0 ms: 1.04x slower                                                       |
| python_startup         | 25.5 ms                                                                         | 26.6 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                           | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                                         | 31.4 ms: 1.03x faster                                                       |
| mako            | 7.76 ms                                                                         | 7.68 ms: 1.01x faster                                                       |
| genshi_text     | 20.8 ms                                                                         | 21.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20241116-pythonperf1_win32-x86-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| telco                   | 6.93 ms                                                                         | 6.42 ms: 1.08x faster                                                       |
| spectral_norm           | 75.7 ms                                                                         | 70.8 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult | 3.19 ms                                                                         | 3.01 ms: 1.06x faster                                                       |
| connected_components    | 273 ms                                                                          | 258 ms: 1.06x faster                                                        |
| django_template         | 32.5 ms                                                                         | 31.4 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 222 ms                                                                          | 215 ms: 1.03x faster                                                        |
| deepcopy_memo           | 22.4 us                                                                         | 21.7 us: 1.03x faster                                                       |
| chaos                   | 60.0 ms                                                                         | 58.3 ms: 1.03x faster                                                       |
| scimark_fft             | 228 ms                                                                          | 222 ms: 1.03x faster                                                        |
| html5lib                | 45.8 ms                                                                         | 44.5 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 42.5 ms                                                                         | 41.3 ms: 1.03x faster                                                       |
| richards                | 38.6 ms                                                                         | 37.6 ms: 1.03x faster                                                       |
| tomli_loads             | 1.79 sec                                                                        | 1.75 sec: 1.02x faster                                                      |
| sqlglot_parse           | 1.08 ms                                                                         | 1.06 ms: 1.02x faster                                                       |
| go                      | 102 ms                                                                          | 99.9 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.17 ms                                                                         | 1.15 ms: 1.02x faster                                                       |
| dulwich_log             | 50.8 ms                                                                         | 49.9 ms: 1.02x faster                                                       |
| shortest_path           | 292 ms                                                                          | 288 ms: 1.01x faster                                                        |
| scimark_lu              | 69.3 ms                                                                         | 68.4 ms: 1.01x faster                                                       |
| sympy_sum               | 107 ms                                                                          | 106 ms: 1.01x faster                                                        |
| mako                    | 7.76 ms                                                                         | 7.68 ms: 1.01x faster                                                       |
| pprint_pformat          | 1.33 sec                                                                        | 1.32 sec: 1.01x faster                                                      |
| sqlite_synth            | 1.94 us                                                                         | 1.92 us: 1.01x faster                                                       |
| sympy_expand            | 377 ms                                                                          | 374 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 640 ms                                                                          | 635 ms: 1.01x faster                                                        |
| sympy_str               | 216 ms                                                                          | 214 ms: 1.01x faster                                                        |
| thrift                  | 757 us                                                                          | 752 us: 1.01x faster                                                        |
| gc_traversal            | 1.78 ms                                                                         | 1.77 ms: 1.01x faster                                                       |
| regex_v8                | 15.7 ms                                                                         | 15.6 ms: 1.01x faster                                                       |
| crypto_pyaes            | 61.6 ms                                                                         | 61.2 ms: 1.01x faster                                                       |
| deltablue               | 2.62 ms                                                                         | 2.61 ms: 1.01x faster                                                       |
| subparsers              | 20.8 ms                                                                         | 20.7 ms: 1.00x faster                                                       |
| logging_simple          | 7.84 us                                                                         | 7.89 us: 1.01x slower                                                       |
| docutils                | 1.82 sec                                                                        | 1.83 sec: 1.01x slower                                                      |
| generators              | 23.6 ms                                                                         | 23.8 ms: 1.01x slower                                                       |
| sympy_integrate         | 15.3 ms                                                                         | 15.4 ms: 1.01x slower                                                       |
| pidigits                | 201 ms                                                                          | 202 ms: 1.01x slower                                                        |
| regex_effbot            | 1.87 ms                                                                         | 1.88 ms: 1.01x slower                                                       |
| logging_format          | 8.55 us                                                                         | 8.61 us: 1.01x slower                                                       |
| regex_dna               | 122 ms                                                                          | 123 ms: 1.01x slower                                                        |
| comprehensions          | 13.5 us                                                                         | 13.6 us: 1.01x slower                                                       |
| unpickle_pure_python    | 173 us                                                                          | 174 us: 1.01x slower                                                        |
| 2to3                    | 244 ms                                                                          | 246 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 464 ms                                                                          | 469 ms: 1.01x slower                                                        |
| genshi_text             | 20.8 ms                                                                         | 21.1 ms: 1.01x slower                                                       |
| richards_super          | 44.5 ms                                                                         | 45.0 ms: 1.01x slower                                                       |
| meteor_contest          | 80.5 ms                                                                         | 81.6 ms: 1.01x slower                                                       |
| pycparser               | 826 ms                                                                          | 837 ms: 1.01x slower                                                        |
| json                    | 4.26 ms                                                                         | 4.32 ms: 1.01x slower                                                       |
| scimark_sor             | 101 ms                                                                          | 103 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 67.9 ms                                                                         | 68.9 ms: 1.01x slower                                                       |
| json_loads              | 20.6 us                                                                         | 20.9 us: 1.02x slower                                                       |
| xml_etree_generate      | 66.7 ms                                                                         | 67.8 ms: 1.02x slower                                                       |
| bpe_tokeniser           | 3.48 sec                                                                        | 3.54 sec: 1.02x slower                                                      |
| asyncio_websockets      | 351 ms                                                                          | 357 ms: 1.02x slower                                                        |
| hexiom                  | 4.96 ms                                                                         | 5.05 ms: 1.02x slower                                                       |
| regex_compile           | 105 ms                                                                          | 108 ms: 1.02x slower                                                        |
| xml_etree_parse         | 110 ms                                                                          | 112 ms: 1.02x slower                                                        |
| async_generators        | 285 ms                                                                          | 291 ms: 1.02x slower                                                        |
| pickle_pure_python      | 266 us                                                                          | 272 us: 1.02x slower                                                        |
| async_tree_io           | 515 ms                                                                          | 527 ms: 1.02x slower                                                        |
| coverage                | 50.3 ms                                                                         | 51.6 ms: 1.03x slower                                                       |
| float                   | 61.1 ms                                                                         | 62.8 ms: 1.03x slower                                                       |
| fannkuch                | 310 ms                                                                          | 319 ms: 1.03x slower                                                        |
| xml_etree_process       | 48.2 ms                                                                         | 49.7 ms: 1.03x slower                                                       |
| deepcopy_reduce         | 2.40 us                                                                         | 2.48 us: 1.03x slower                                                       |
| python_startup_no_site  | 19.3 ms                                                                         | 20.0 ms: 1.04x slower                                                       |
| mdp                     | 1.65 sec                                                                        | 1.72 sec: 1.04x slower                                                      |
| python_startup          | 25.5 ms                                                                         | 26.6 ms: 1.04x slower                                                       |
| raytrace                | 256 ms                                                                          | 269 ms: 1.05x slower                                                        |
| bench_mp_pool           | 86.9 ms                                                                         | 92.1 ms: 1.06x slower                                                       |
| nqueens                 | 73.0 ms                                                                         | 78.9 ms: 1.08x slower                                                       |
| nbody                   | 85.4 ms                                                                         | 93.1 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (21): sqlglot_transpile, async_tree_none_tg, pylint, genshi_xml, pathlib, k_core, async_tree_memoization_tg, scimark_monte_carlo, json_dumps, bench_thread_pool, deepcopy, async_tree_none, typing_runtime_protocols, logging_silent, async_tree_cpu_io_mixed_tg, sphinx, async_tree_memoization, coroutines, many_optionals, async_tree_io_tg, pyflate

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 75.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown