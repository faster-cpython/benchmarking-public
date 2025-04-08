# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.011x faster
- HPT reliability: 98.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 202 ms                                                                      | 198 ms: 1.02x faster                                                           |
| docutils       | 1.54 sec                                                                    | 1.53 sec: 1.01x faster                                                         |
| html5lib       | 34.7 ms                                                                     | 33.3 ms: 1.04x faster                                                          |
| sphinx         | 600 ms                                                                      | 592 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators           | 185 ms                                                                      | 181 ms: 1.02x faster                                                           |
| coroutines                 | 11.0 ms                                                                     | 10.9 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 315 ms                                                                      | 317 ms: 1.01x slower                                                           |
| async_tree_none_tg         | 149 ms                                                                      | 152 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 344 ms                                                                      | 350 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.60 ms                                                                     | 1.47 ms: 1.09x faster                                                          |
| regex_v8       | 13.3 ms                                                                     | 12.3 ms: 1.09x faster                                                          |
| regex_dna      | 123 ms                                                                      | 116 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads        | 1.02 sec                                                                    | 981 ms: 1.04x faster                                                           |
| json_dumps         | 5.70 ms                                                                     | 5.58 ms: 1.02x faster                                                          |
| json_loads         | 14.2 us                                                                     | 14.1 us: 1.01x faster                                                          |
| pickle_pure_python | 164 us                                                                      | 165 us: 1.01x slower                                                           |
| xml_etree_parse    | 88.8 ms                                                                     | 89.6 ms: 1.01x slower                                                          |
| xml_etree_generate | 48.0 ms                                                                     | 48.8 ms: 1.02x slower                                                          |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 19.5 ms                                                                     | 18.8 ms: 1.04x faster                                                          |
| genshi_text     | 11.4 ms                                                                     | 11.1 ms: 1.03x faster                                                          |
| mako            | 5.65 ms                                                                     | 5.76 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot               | 1.60 ms                                                                     | 1.47 ms: 1.09x faster                                                          |
| regex_v8                   | 13.3 ms                                                                     | 12.3 ms: 1.09x faster                                                          |
| chaos                      | 31.9 ms                                                                     | 29.5 ms: 1.08x faster                                                          |
| go                         | 58.2 ms                                                                     | 54.8 ms: 1.06x faster                                                          |
| regex_dna                  | 123 ms                                                                      | 116 ms: 1.06x faster                                                           |
| generators                 | 14.9 ms                                                                     | 14.2 ms: 1.05x faster                                                          |
| json                       | 3.02 ms                                                                     | 2.88 ms: 1.05x faster                                                          |
| richards_super             | 24.6 ms                                                                     | 23.5 ms: 1.04x faster                                                          |
| raytrace                   | 139 ms                                                                      | 134 ms: 1.04x faster                                                           |
| html5lib                   | 34.7 ms                                                                     | 33.3 ms: 1.04x faster                                                          |
| nqueens                    | 48.1 ms                                                                     | 46.2 ms: 1.04x faster                                                          |
| django_template            | 19.5 ms                                                                     | 18.8 ms: 1.04x faster                                                          |
| hexiom                     | 2.92 ms                                                                     | 2.81 ms: 1.04x faster                                                          |
| coverage                   | 41.0 ms                                                                     | 39.5 ms: 1.04x faster                                                          |
| logging_format             | 5.91 us                                                                     | 5.70 us: 1.04x faster                                                          |
| tomli_loads                | 1.02 sec                                                                    | 981 ms: 1.04x faster                                                           |
| sqlglot_v2_parse           | 651 us                                                                      | 629 us: 1.04x faster                                                           |
| sqlglot_v2_transpile       | 845 us                                                                      | 818 us: 1.03x faster                                                           |
| logging_simple             | 5.46 us                                                                     | 5.29 us: 1.03x faster                                                          |
| pycparser                  | 641 ms                                                                      | 622 ms: 1.03x faster                                                           |
| genshi_text                | 11.4 ms                                                                     | 11.1 ms: 1.03x faster                                                          |
| spectral_norm              | 46.0 ms                                                                     | 44.9 ms: 1.02x faster                                                          |
| async_generators           | 185 ms                                                                      | 181 ms: 1.02x faster                                                           |
| crypto_pyaes               | 38.6 ms                                                                     | 37.8 ms: 1.02x faster                                                          |
| json_dumps                 | 5.70 ms                                                                     | 5.58 ms: 1.02x faster                                                          |
| scimark_monte_carlo        | 28.1 ms                                                                     | 27.5 ms: 1.02x faster                                                          |
| deltablue                  | 1.51 ms                                                                     | 1.48 ms: 1.02x faster                                                          |
| richards                   | 21.1 ms                                                                     | 20.8 ms: 1.02x faster                                                          |
| 2to3                       | 202 ms                                                                      | 198 ms: 1.02x faster                                                           |
| pathlib                    | 31.2 ms                                                                     | 30.7 ms: 1.02x faster                                                          |
| subparsers                 | 14.3 ms                                                                     | 14.1 ms: 1.01x faster                                                          |
| sphinx                     | 600 ms                                                                      | 592 ms: 1.01x faster                                                           |
| comprehensions             | 8.30 us                                                                     | 8.19 us: 1.01x faster                                                          |
| sqlglot_v2_normalize       | 60.8 ms                                                                     | 60.1 ms: 1.01x faster                                                          |
| coroutines                 | 11.0 ms                                                                     | 10.9 ms: 1.01x faster                                                          |
| json_loads                 | 14.2 us                                                                     | 14.1 us: 1.01x faster                                                          |
| docutils                   | 1.54 sec                                                                    | 1.53 sec: 1.01x faster                                                         |
| scimark_fft                | 140 ms                                                                      | 139 ms: 1.01x faster                                                           |
| sympy_sum                  | 78.9 ms                                                                     | 78.2 ms: 1.01x faster                                                          |
| scimark_sparse_mat_mult    | 2.15 ms                                                                     | 2.13 ms: 1.01x faster                                                          |
| many_optionals             | 394 us                                                                      | 391 us: 1.01x faster                                                           |
| sqlglot_v2_optimize        | 30.1 ms                                                                     | 30.0 ms: 1.01x faster                                                          |
| sympy_integrate            | 11.2 ms                                                                     | 11.2 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.49 us                                                                     | 1.48 us: 1.00x faster                                                          |
| sympy_str                  | 148 ms                                                                      | 149 ms: 1.01x slower                                                           |
| mdp                        | 666 ms                                                                      | 671 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 315 ms                                                                      | 317 ms: 1.01x slower                                                           |
| pickle_pure_python         | 164 us                                                                      | 165 us: 1.01x slower                                                           |
| bpe_tokeniser              | 2.46 sec                                                                    | 2.48 sec: 1.01x slower                                                         |
| sympy_expand               | 255 ms                                                                      | 257 ms: 1.01x slower                                                           |
| scimark_lu                 | 45.0 ms                                                                     | 45.4 ms: 1.01x slower                                                          |
| xml_etree_parse            | 88.8 ms                                                                     | 89.6 ms: 1.01x slower                                                          |
| pprint_pformat             | 802 ms                                                                      | 815 ms: 1.02x slower                                                           |
| xml_etree_generate         | 48.0 ms                                                                     | 48.8 ms: 1.02x slower                                                          |
| gc_traversal               | 2.72 ms                                                                     | 2.77 ms: 1.02x slower                                                          |
| meteor_contest             | 65.3 ms                                                                     | 66.4 ms: 1.02x slower                                                          |
| async_tree_none_tg         | 149 ms                                                                      | 152 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 344 ms                                                                      | 350 ms: 1.02x slower                                                           |
| mako                       | 5.65 ms                                                                     | 5.76 ms: 1.02x slower                                                          |
| pprint_safe_repr           | 391 ms                                                                      | 399 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 84.6 us                                                                     | 86.9 us: 1.03x slower                                                          |
| logging_silent             | 40.7 ns                                                                     | 42.4 ns: 1.04x slower                                                          |
| fannkuch                   | 192 ms                                                                      | 200 ms: 1.04x slower                                                           |
| dulwich_log                | 38.0 ms                                                                     | 40.1 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (29): pylint, pyflate, deepcopy_reduce, deepcopy, async_tree_none, regex_compile, async_tree_memoization, xml_etree_process, k_core, bench_mp_pool, pidigits, python_startup_no_site, create_gc_cycles, shortest_path, float, unpickle_pure_python, deepcopy_memo, connected_components, telco, scimark_sor, nbody, genshi_xml, python_startup, xml_etree_iterparse, async_tree_cpu_io_mixed, bench_thread_pool, async_tree_memoization_tg, async_tree_io, asyncio_websockets

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 98.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown