# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 225 ms: 1.02x slower                                                               |
| docutils       | 1.62 sec                                                                   | 1.67 sec: 1.03x slower                                                             |
| html5lib       | 38.5 ms                                                                    | 38.1 ms: 1.01x faster                                                              |
| sphinx         | 642 ms                                                                     | 660 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 162 ms                                                                     | 156 ms: 1.04x faster                                                               |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 335 ms: 1.02x slower                                                               |
| async_tree_none_tg         | 170 ms                                                                     | 174 ms: 1.03x slower                                                               |
| async_tree_memoization_tg  | 207 ms                                                                     | 213 ms: 1.03x slower                                                               |
| async_tree_none            | 171 ms                                                                     | 176 ms: 1.03x slower                                                               |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                     | 346 ms: 1.03x slower                                                               |
| async_tree_io              | 395 ms                                                                     | 409 ms: 1.04x slower                                                               |
| async_tree_memoization     | 205 ms                                                                     | 213 ms: 1.04x slower                                                               |
| async_tree_io_tg           | 389 ms                                                                     | 408 ms: 1.05x slower                                                               |
| coroutines                 | 13.7 ms                                                                    | 14.6 ms: 1.07x slower                                                              |
| async_generators           | 229 ms                                                                     | 252 ms: 1.10x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.04x slower                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 61.6 ms                                                                    | 60.7 ms: 1.01x faster                                                              |
| pidigits       | 148 ms                                                                     | 148 ms: 1.00x slower                                                               |
| float          | 42.5 ms                                                                    | 43.1 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 14.5 ms                                                                    | 13.6 ms: 1.07x faster                                                              |
| regex_effbot   | 1.54 ms                                                                    | 1.50 ms: 1.03x faster                                                              |
| regex_dna      | 118 ms                                                                     | 116 ms: 1.02x faster                                                               |
| regex_compile  | 79.9 ms                                                                    | 82.0 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 136 us                                                                     | 137 us: 1.01x slower                                                               |
| pickle_pure_python   | 208 us                                                                     | 213 us: 1.02x slower                                                               |
| tomli_loads          | 1.37 sec                                                                   | 1.40 sec: 1.03x slower                                                             |
| json_loads           | 15.0 us                                                                    | 15.6 us: 1.05x slower                                                              |
| xml_etree_iterparse  | 63.5 ms                                                                    | 66.6 ms: 1.05x slower                                                              |
| xml_etree_parse      | 88.2 ms                                                                    | 94.2 ms: 1.07x slower                                                              |
| json_dumps           | 6.17 ms                                                                    | 6.66 ms: 1.08x slower                                                              |
| xml_etree_generate   | 56.2 ms                                                                    | 60.7 ms: 1.08x slower                                                              |
| xml_etree_process    | 39.1 ms                                                                    | 42.3 ms: 1.08x slower                                                              |
| Geometric mean       | (ref)                                                                      | 1.05x slower                                                                       |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml      | 34.7 ms                                                                    | 36.6 ms: 1.05x slower                                                              |
| django_template | 24.0 ms                                                                    | 25.4 ms: 1.06x slower                                                              |
| genshi_text     | 15.2 ms                                                                    | 16.1 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                                      | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 92.4 ms                                                                    | 524 us: 176.44x faster                                                             |
| coverage                   | 295 ms                                                                     | 56.9 ms: 5.18x faster                                                              |
| regex_v8                   | 14.5 ms                                                                    | 13.6 ms: 1.07x faster                                                              |
| asyncio_websockets         | 162 ms                                                                     | 156 ms: 1.04x faster                                                               |
| regex_effbot               | 1.54 ms                                                                    | 1.50 ms: 1.03x faster                                                              |
| scimark_monte_carlo        | 40.4 ms                                                                    | 39.5 ms: 1.02x faster                                                              |
| regex_dna                  | 118 ms                                                                     | 116 ms: 1.02x faster                                                               |
| nbody                      | 61.6 ms                                                                    | 60.7 ms: 1.01x faster                                                              |
| html5lib                   | 38.5 ms                                                                    | 38.1 ms: 1.01x faster                                                              |
| pidigits                   | 148 ms                                                                     | 148 ms: 1.00x slower                                                               |
| go                         | 78.1 ms                                                                    | 78.6 ms: 1.01x slower                                                              |
| create_gc_cycles           | 1.28 ms                                                                    | 1.29 ms: 1.01x slower                                                              |
| unpickle_pure_python       | 136 us                                                                     | 137 us: 1.01x slower                                                               |
| bench_mp_pool              | 92.0 ms                                                                    | 92.7 ms: 1.01x slower                                                              |
| connected_components       | 325 ms                                                                     | 328 ms: 1.01x slower                                                               |
| pathlib                    | 29.6 ms                                                                    | 29.9 ms: 1.01x slower                                                              |
| float                      | 42.5 ms                                                                    | 43.1 ms: 1.01x slower                                                              |
| pycparser                  | 707 ms                                                                     | 717 ms: 1.01x slower                                                               |
| shortest_path              | 354 ms                                                                     | 360 ms: 1.02x slower                                                               |
| k_core                     | 1.67 sec                                                                   | 1.70 sec: 1.02x slower                                                             |
| crypto_pyaes               | 46.9 ms                                                                    | 47.6 ms: 1.02x slower                                                              |
| logging_format             | 6.91 us                                                                    | 7.03 us: 1.02x slower                                                              |
| logging_simple             | 6.44 us                                                                    | 6.55 us: 1.02x slower                                                              |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 335 ms: 1.02x slower                                                               |
| richards_super             | 30.8 ms                                                                    | 31.4 ms: 1.02x slower                                                              |
| richards                   | 27.0 ms                                                                    | 27.6 ms: 1.02x slower                                                              |
| pickle_pure_python         | 208 us                                                                     | 213 us: 1.02x slower                                                               |
| 2to3                       | 220 ms                                                                     | 225 ms: 1.02x slower                                                               |
| chaos                      | 38.1 ms                                                                    | 39.0 ms: 1.02x slower                                                              |
| many_optionals             | 441 us                                                                     | 451 us: 1.02x slower                                                               |
| deltablue                  | 2.12 ms                                                                    | 2.17 ms: 1.02x slower                                                              |
| deepcopy_memo              | 19.2 us                                                                    | 19.6 us: 1.02x slower                                                              |
| raytrace                   | 178 ms                                                                     | 182 ms: 1.03x slower                                                               |
| tomli_loads                | 1.37 sec                                                                   | 1.40 sec: 1.03x slower                                                             |
| async_tree_none_tg         | 170 ms                                                                     | 174 ms: 1.03x slower                                                               |
| regex_compile              | 79.9 ms                                                                    | 82.0 ms: 1.03x slower                                                              |
| pylint                     | 197 ms                                                                     | 203 ms: 1.03x slower                                                               |
| sphinx                     | 642 ms                                                                     | 660 ms: 1.03x slower                                                               |
| async_tree_memoization_tg  | 207 ms                                                                     | 213 ms: 1.03x slower                                                               |
| sympy_integrate            | 12.4 ms                                                                    | 12.8 ms: 1.03x slower                                                              |
| docutils                   | 1.62 sec                                                                   | 1.67 sec: 1.03x slower                                                             |
| async_tree_none            | 171 ms                                                                     | 176 ms: 1.03x slower                                                               |
| sqlite_synth               | 1.57 us                                                                    | 1.62 us: 1.03x slower                                                              |
| subparsers                 | 17.1 ms                                                                    | 17.7 ms: 1.03x slower                                                              |
| sympy_sum                  | 87.7 ms                                                                    | 90.6 ms: 1.03x slower                                                              |
| scimark_sor                | 76.0 ms                                                                    | 78.6 ms: 1.03x slower                                                              |
| async_tree_cpu_io_mixed_tg | 334 ms                                                                     | 346 ms: 1.03x slower                                                               |
| nqueens                    | 60.6 ms                                                                    | 62.8 ms: 1.04x slower                                                              |
| spectral_norm              | 57.5 ms                                                                    | 59.6 ms: 1.04x slower                                                              |
| async_tree_io              | 395 ms                                                                     | 409 ms: 1.04x slower                                                               |
| hexiom                     | 3.99 ms                                                                    | 4.14 ms: 1.04x slower                                                              |
| async_tree_memoization     | 205 ms                                                                     | 213 ms: 1.04x slower                                                               |
| pprint_safe_repr           | 489 ms                                                                     | 510 ms: 1.04x slower                                                               |
| comprehensions             | 11.4 us                                                                    | 11.9 us: 1.04x slower                                                              |
| pprint_pformat             | 994 ms                                                                     | 1.04 sec: 1.04x slower                                                             |
| deepcopy_reduce            | 1.85 us                                                                    | 1.93 us: 1.05x slower                                                              |
| json                       | 2.95 ms                                                                    | 3.08 ms: 1.05x slower                                                              |
| json_loads                 | 15.0 us                                                                    | 15.6 us: 1.05x slower                                                              |
| xml_etree_iterparse        | 63.5 ms                                                                    | 66.6 ms: 1.05x slower                                                              |
| deepcopy                   | 173 us                                                                     | 182 us: 1.05x slower                                                               |
| async_tree_io_tg           | 389 ms                                                                     | 408 ms: 1.05x slower                                                               |
| scimark_lu                 | 57.8 ms                                                                    | 60.7 ms: 1.05x slower                                                              |
| generators                 | 19.8 ms                                                                    | 20.9 ms: 1.05x slower                                                              |
| genshi_xml                 | 34.7 ms                                                                    | 36.6 ms: 1.05x slower                                                              |
| sympy_str                  | 169 ms                                                                     | 178 ms: 1.06x slower                                                               |
| django_template            | 24.0 ms                                                                    | 25.4 ms: 1.06x slower                                                              |
| sqlglot_v2_normalize       | 70.3 ms                                                                    | 74.5 ms: 1.06x slower                                                              |
| meteor_contest             | 73.0 ms                                                                    | 77.4 ms: 1.06x slower                                                              |
| genshi_text                | 15.2 ms                                                                    | 16.1 ms: 1.06x slower                                                              |
| bpe_tokeniser              | 2.89 sec                                                                   | 3.07 sec: 1.06x slower                                                             |
| scimark_sparse_mat_mult    | 2.46 ms                                                                    | 2.62 ms: 1.07x slower                                                              |
| sympy_expand               | 289 ms                                                                     | 308 ms: 1.07x slower                                                               |
| xml_etree_parse            | 88.2 ms                                                                    | 94.2 ms: 1.07x slower                                                              |
| typing_runtime_protocols   | 108 us                                                                     | 115 us: 1.07x slower                                                               |
| sqlglot_v2_optimize        | 34.2 ms                                                                    | 36.5 ms: 1.07x slower                                                              |
| scimark_fft                | 174 ms                                                                     | 186 ms: 1.07x slower                                                               |
| coroutines                 | 13.7 ms                                                                    | 14.6 ms: 1.07x slower                                                              |
| pyflate                    | 280 ms                                                                     | 301 ms: 1.07x slower                                                               |
| json_dumps                 | 6.17 ms                                                                    | 6.66 ms: 1.08x slower                                                              |
| xml_etree_generate         | 56.2 ms                                                                    | 60.7 ms: 1.08x slower                                                              |
| mdp                        | 779 ms                                                                     | 841 ms: 1.08x slower                                                               |
| xml_etree_process          | 39.1 ms                                                                    | 42.3 ms: 1.08x slower                                                              |
| logging_silent             | 316 ns                                                                     | 342 ns: 1.08x slower                                                               |
| async_generators           | 229 ms                                                                     | 252 ms: 1.10x slower                                                               |
| telco                      | 4.61 ms                                                                    | 5.09 ms: 1.10x slower                                                              |
| fannkuch                   | 246 ms                                                                     | 280 ms: 1.14x slower                                                               |
| Geometric mean             | (ref)                                                                      | 1.04x faster                                                                       |

Benchmark hidden because not significant (8): sqlglot_v2_parse, python_startup, gc_traversal, python_startup_no_site, dulwich_log, mako, sqlglot_v2_transpile, bench_thread_pool

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown