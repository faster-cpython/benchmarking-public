# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-x86
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                          | 259 ms: 1.01x faster                                                                      |
| docutils       | 1.93 sec                                                                        | 1.91 sec: 1.01x faster                                                                    |
| html5lib       | 49.5 ms                                                                         | 45.8 ms: 1.08x faster                                                                     |
| sphinx         | 792 ms                                                                          | 756 ms: 1.05x faster                                                                      |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| async_generators           | 328 ms                                                                          | 294 ms: 1.12x faster                                                                      |
| async_tree_cpu_io_mixed    | 502 ms                                                                          | 472 ms: 1.06x faster                                                                      |
| async_tree_none            | 225 ms                                                                          | 216 ms: 1.04x faster                                                                      |
| asyncio_websockets         | 356 ms                                                                          | 348 ms: 1.02x faster                                                                      |
| async_tree_io              | 473 ms                                                                          | 466 ms: 1.02x faster                                                                      |
| async_tree_memoization     | 277 ms                                                                          | 273 ms: 1.02x faster                                                                      |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                          | 452 ms: 1.01x faster                                                                      |
| async_tree_none_tg         | 194 ms                                                                          | 194 ms: 1.00x faster                                                                      |
| async_tree_memoization_tg  | 245 ms                                                                          | 249 ms: 1.02x slower                                                                      |
| async_tree_io_tg           | 443 ms                                                                          | 453 ms: 1.02x slower                                                                      |
| coroutines                 | 16.7 ms                                                                         | 17.3 ms: 1.03x slower                                                                     |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                                          | 200 ms: 1.02x faster                                                                      |
| nbody          | 99.3 ms                                                                         | 98.2 ms: 1.01x faster                                                                     |
| float          | 56.1 ms                                                                         | 56.9 ms: 1.01x slower                                                                     |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| regex_compile  | 114 ms                                                                          | 110 ms: 1.04x faster                                                                      |
| regex_v8       | 15.7 ms                                                                         | 15.5 ms: 1.01x faster                                                                     |
| regex_dna      | 114 ms                                                                          | 114 ms: 1.00x faster                                                                      |
| regex_effbot   | 1.59 ms                                                                         | 1.58 ms: 1.00x faster                                                                     |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| json_dumps           | 9.22 ms                                                                         | 9.00 ms: 1.02x faster                                                                     |
| xml_etree_parse      | 107 ms                                                                          | 107 ms: 1.01x slower                                                                      |
| unpickle_pure_python | 203 us                                                                          | 206 us: 1.01x slower                                                                      |
| pickle_pure_python   | 298 us                                                                          | 303 us: 1.02x slower                                                                      |
| xml_etree_iterparse  | 65.3 ms                                                                         | 66.4 ms: 1.02x slower                                                                     |
| tomli_loads          | 1.74 sec                                                                        | 1.79 sec: 1.02x slower                                                                    |
| xml_etree_process    | 51.7 ms                                                                         | 53.5 ms: 1.03x slower                                                                     |
| xml_etree_generate   | 69.3 ms                                                                         | 71.9 ms: 1.04x slower                                                                     |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| genshi_xml      | 57.0 ms                                                                         | 51.5 ms: 1.11x faster                                                                     |
| django_template | 36.1 ms                                                                         | 33.9 ms: 1.06x faster                                                                     |
| genshi_text     | 25.7 ms                                                                         | 24.7 ms: 1.04x faster                                                                     |
| mako            | 7.33 ms                                                                         | 7.49 ms: 1.02x slower                                                                     |
| Geometric mean  | (ref)                                                                           | 1.05x faster                                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| generators                 | 36.5 ms                                                                         | 26.3 ms: 1.39x faster                                                                     |
| hexiom                     | 7.15 ms                                                                         | 5.36 ms: 1.33x faster                                                                     |
| raytrace                   | 300 ms                                                                          | 242 ms: 1.24x faster                                                                      |
| deepcopy                   | 270 us                                                                          | 230 us: 1.17x faster                                                                      |
| deltablue                  | 3.14 ms                                                                         | 2.69 ms: 1.16x faster                                                                     |
| go                         | 119 ms                                                                          | 104 ms: 1.15x faster                                                                      |
| deepcopy_reduce            | 2.79 us                                                                         | 2.44 us: 1.14x faster                                                                     |
| deepcopy_memo              | 23.7 us                                                                         | 21.0 us: 1.13x faster                                                                     |
| nqueens                    | 97.5 ms                                                                         | 86.5 ms: 1.13x faster                                                                     |
| async_generators           | 328 ms                                                                          | 294 ms: 1.12x faster                                                                      |
| pyflate                    | 390 ms                                                                          | 350 ms: 1.12x faster                                                                      |
| genshi_xml                 | 57.0 ms                                                                         | 51.5 ms: 1.11x faster                                                                     |
| comprehensions             | 18.4 us                                                                         | 16.7 us: 1.10x faster                                                                     |
| html5lib                   | 49.5 ms                                                                         | 45.8 ms: 1.08x faster                                                                     |
| dulwich_log                | 50.3 ms                                                                         | 47.0 ms: 1.07x faster                                                                     |
| richards_super             | 46.6 ms                                                                         | 43.6 ms: 1.07x faster                                                                     |
| async_tree_cpu_io_mixed    | 502 ms                                                                          | 472 ms: 1.06x faster                                                                      |
| django_template            | 36.1 ms                                                                         | 33.9 ms: 1.06x faster                                                                     |
| mdp                        | 1.85 sec                                                                        | 1.75 sec: 1.06x faster                                                                    |
| sympy_expand               | 409 ms                                                                          | 388 ms: 1.05x faster                                                                      |
| sympy_str                  | 235 ms                                                                          | 223 ms: 1.05x faster                                                                      |
| sympy_integrate            | 17.4 ms                                                                         | 16.5 ms: 1.05x faster                                                                     |
| sympy_sum                  | 116 ms                                                                          | 110 ms: 1.05x faster                                                                      |
| richards                   | 41.5 ms                                                                         | 39.6 ms: 1.05x faster                                                                     |
| sphinx                     | 792 ms                                                                          | 756 ms: 1.05x faster                                                                      |
| scimark_lu                 | 73.4 ms                                                                         | 70.1 ms: 1.05x faster                                                                     |
| chaos                      | 65.2 ms                                                                         | 62.6 ms: 1.04x faster                                                                     |
| genshi_text                | 25.7 ms                                                                         | 24.7 ms: 1.04x faster                                                                     |
| async_tree_none            | 225 ms                                                                          | 216 ms: 1.04x faster                                                                      |
| scimark_sparse_mat_mult    | 3.13 ms                                                                         | 3.02 ms: 1.04x faster                                                                     |
| regex_compile              | 114 ms                                                                          | 110 ms: 1.04x faster                                                                      |
| coverage                   | 53.1 ms                                                                         | 51.6 ms: 1.03x faster                                                                     |
| logging_silent             | 77.5 ns                                                                         | 75.6 ns: 1.03x faster                                                                     |
| spectral_norm              | 73.7 ms                                                                         | 71.9 ms: 1.03x faster                                                                     |
| logging_simple             | 8.43 us                                                                         | 8.22 us: 1.02x faster                                                                     |
| json_dumps                 | 9.22 ms                                                                         | 9.00 ms: 1.02x faster                                                                     |
| logging_format             | 9.04 us                                                                         | 8.83 us: 1.02x faster                                                                     |
| scimark_sor                | 100 ms                                                                          | 97.8 ms: 1.02x faster                                                                     |
| asyncio_websockets         | 356 ms                                                                          | 348 ms: 1.02x faster                                                                      |
| meteor_contest             | 89.3 ms                                                                         | 87.5 ms: 1.02x faster                                                                     |
| pidigits                   | 204 ms                                                                          | 200 ms: 1.02x faster                                                                      |
| async_tree_io              | 473 ms                                                                          | 466 ms: 1.02x faster                                                                      |
| scimark_monte_carlo        | 61.7 ms                                                                         | 60.8 ms: 1.02x faster                                                                     |
| async_tree_memoization     | 277 ms                                                                          | 273 ms: 1.02x faster                                                                      |
| shortest_path              | 317 ms                                                                          | 312 ms: 1.01x faster                                                                      |
| pycparser                  | 924 ms                                                                          | 912 ms: 1.01x faster                                                                      |
| regex_v8                   | 15.7 ms                                                                         | 15.5 ms: 1.01x faster                                                                     |
| nbody                      | 99.3 ms                                                                         | 98.2 ms: 1.01x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                          | 452 ms: 1.01x faster                                                                      |
| docutils                   | 1.93 sec                                                                        | 1.91 sec: 1.01x faster                                                                    |
| 2to3                       | 262 ms                                                                          | 259 ms: 1.01x faster                                                                      |
| typing_runtime_protocols   | 168 us                                                                          | 167 us: 1.01x faster                                                                      |
| sqlglot_normalize          | 105 ms                                                                          | 105 ms: 1.01x faster                                                                      |
| pprint_safe_repr           | 741 ms                                                                          | 736 ms: 1.01x faster                                                                      |
| bench_mp_pool              | 87.6 ms                                                                         | 87.1 ms: 1.01x faster                                                                     |
| async_tree_none_tg         | 194 ms                                                                          | 194 ms: 1.00x faster                                                                      |
| regex_dna                  | 114 ms                                                                          | 114 ms: 1.00x faster                                                                      |
| regex_effbot               | 1.59 ms                                                                         | 1.58 ms: 1.00x faster                                                                     |
| xml_etree_parse            | 107 ms                                                                          | 107 ms: 1.01x slower                                                                      |
| sqlite_synth               | 1.92 us                                                                         | 1.93 us: 1.01x slower                                                                     |
| subparsers                 | 21.3 ms                                                                         | 21.5 ms: 1.01x slower                                                                     |
| fannkuch                   | 343 ms                                                                          | 346 ms: 1.01x slower                                                                      |
| pathlib                    | 83.4 ms                                                                         | 84.2 ms: 1.01x slower                                                                     |
| crypto_pyaes               | 68.0 ms                                                                         | 68.9 ms: 1.01x slower                                                                     |
| float                      | 56.1 ms                                                                         | 56.9 ms: 1.01x slower                                                                     |
| unpickle_pure_python       | 203 us                                                                          | 206 us: 1.01x slower                                                                      |
| sqlglot_optimize           | 50.4 ms                                                                         | 51.2 ms: 1.01x slower                                                                     |
| pickle_pure_python         | 298 us                                                                          | 303 us: 1.02x slower                                                                      |
| xml_etree_iterparse        | 65.3 ms                                                                         | 66.4 ms: 1.02x slower                                                                     |
| scimark_fft                | 241 ms                                                                          | 245 ms: 1.02x slower                                                                      |
| async_tree_memoization_tg  | 245 ms                                                                          | 249 ms: 1.02x slower                                                                      |
| mako                       | 7.33 ms                                                                         | 7.49 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 443 ms                                                                          | 453 ms: 1.02x slower                                                                      |
| tomli_loads                | 1.74 sec                                                                        | 1.79 sec: 1.02x slower                                                                    |
| bpe_tokeniser              | 3.78 sec                                                                        | 3.87 sec: 1.02x slower                                                                    |
| sqlglot_transpile          | 1.41 ms                                                                         | 1.45 ms: 1.03x slower                                                                     |
| coroutines                 | 16.7 ms                                                                         | 17.3 ms: 1.03x slower                                                                     |
| sqlglot_parse              | 1.13 ms                                                                         | 1.17 ms: 1.03x slower                                                                     |
| xml_etree_process          | 51.7 ms                                                                         | 53.5 ms: 1.03x slower                                                                     |
| xml_etree_generate         | 69.3 ms                                                                         | 71.9 ms: 1.04x slower                                                                     |
| Geometric mean             | (ref)                                                                           | 1.03x faster                                                                              |

Benchmark hidden because not significant (15): bench_thread_pool, pylint, k_core, connected_components, mypy2, pprint_pformat, python_startup, thrift, json_loads, python_startup_no_site, gc_traversal, telco, json, many_optionals, create_gc_cycles

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown