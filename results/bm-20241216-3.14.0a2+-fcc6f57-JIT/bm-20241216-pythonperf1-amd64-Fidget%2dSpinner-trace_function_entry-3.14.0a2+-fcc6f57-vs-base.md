# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.006x faster
- HPT reliability: 96.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 1.71 sec                                                                    | 1.75 sec: 1.02x slower                                                                |
| html5lib       | 39.2 ms                                                                     | 38.6 ms: 1.02x faster                                                                 |
| sphinx         | 677 ms                                                                      | 652 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators          | 255 ms                                                                      | 245 ms: 1.04x faster                                                                  |
| async_tree_memoization_tg | 216 ms                                                                      | 211 ms: 1.02x faster                                                                  |
| asyncio_websockets        | 310 ms                                                                      | 305 ms: 1.02x faster                                                                  |
| async_tree_none           | 181 ms                                                                      | 179 ms: 1.01x faster                                                                  |
| async_tree_none_tg        | 169 ms                                                                      | 171 ms: 1.01x slower                                                                  |
| async_tree_io_tg          | 391 ms                                                                      | 398 ms: 1.02x slower                                                                  |
| async_tree_io             | 395 ms                                                                      | 404 ms: 1.02x slower                                                                  |
| coroutines                | 13.5 ms                                                                     | 14.2 ms: 1.05x slower                                                                 |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                                      | 147 ms: 1.00x faster                                                                  |
| nbody          | 52.8 ms                                                                     | 54.2 ms: 1.03x slower                                                                 |
| float          | 45.3 ms                                                                     | 49.2 ms: 1.09x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 20.9 ms                                                                     | 16.9 ms: 1.23x faster                                                                 |
| regex_compile  | 81.3 ms                                                                     | 80.7 ms: 1.01x faster                                                                 |
| regex_dna      | 113 ms                                                                      | 118 ms: 1.04x slower                                                                  |
| regex_effbot   | 1.40 ms                                                                     | 1.52 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 208 us                                                                      | 192 us: 1.09x faster                                                                  |
| tomli_loads          | 1.23 sec                                                                    | 1.18 sec: 1.04x faster                                                                |
| unpickle_pure_python | 110 us                                                                      | 107 us: 1.03x faster                                                                  |
| xml_etree_process    | 36.4 ms                                                                     | 35.5 ms: 1.03x faster                                                                 |
| xml_etree_generate   | 50.8 ms                                                                     | 50.2 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 85.0 ms                                                                     | 86.8 ms: 1.02x slower                                                                 |
| json_dumps           | 6.22 ms                                                                     | 6.39 ms: 1.03x slower                                                                 |
| xml_etree_iterparse  | 58.3 ms                                                                     | 61.2 ms: 1.05x slower                                                                 |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.4 ms                                                                     | 17.7 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 48.5 ms                                                                     | 37.9 ms: 1.28x faster                                                                 |
| genshi_text     | 18.8 ms                                                                     | 16.2 ms: 1.16x faster                                                                 |
| django_template | 27.5 ms                                                                     | 25.9 ms: 1.07x faster                                                                 |
| mako            | 5.11 ms                                                                     | 5.18 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.12x faster                                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml                | 48.5 ms                                                                     | 37.9 ms: 1.28x faster                                                                 |
| regex_v8                  | 20.9 ms                                                                     | 16.9 ms: 1.23x faster                                                                 |
| genshi_text               | 18.8 ms                                                                     | 16.2 ms: 1.16x faster                                                                 |
| richards                  | 34.7 ms                                                                     | 31.0 ms: 1.12x faster                                                                 |
| raytrace                  | 208 ms                                                                      | 187 ms: 1.12x faster                                                                  |
| hexiom                    | 4.97 ms                                                                     | 4.49 ms: 1.11x faster                                                                 |
| richards_super            | 39.1 ms                                                                     | 35.4 ms: 1.10x faster                                                                 |
| pickle_pure_python        | 208 us                                                                      | 192 us: 1.09x faster                                                                  |
| django_template           | 27.5 ms                                                                     | 25.9 ms: 1.07x faster                                                                 |
| sqlglot_normalize         | 207 ms                                                                      | 197 ms: 1.05x faster                                                                  |
| go                        | 90.0 ms                                                                     | 86.1 ms: 1.05x faster                                                                 |
| tomli_loads               | 1.23 sec                                                                    | 1.18 sec: 1.04x faster                                                                |
| nqueens                   | 64.5 ms                                                                     | 61.9 ms: 1.04x faster                                                                 |
| async_generators          | 255 ms                                                                      | 245 ms: 1.04x faster                                                                  |
| scimark_sparse_mat_mult   | 2.11 ms                                                                     | 2.03 ms: 1.04x faster                                                                 |
| sphinx                    | 677 ms                                                                      | 652 ms: 1.04x faster                                                                  |
| generators                | 23.8 ms                                                                     | 23.0 ms: 1.04x faster                                                                 |
| unpickle_pure_python      | 110 us                                                                      | 107 us: 1.03x faster                                                                  |
| scimark_fft               | 146 ms                                                                      | 141 ms: 1.03x faster                                                                  |
| dulwich_log               | 40.9 ms                                                                     | 39.8 ms: 1.03x faster                                                                 |
| pylint                    | 207 ms                                                                      | 202 ms: 1.03x faster                                                                  |
| xml_etree_process         | 36.4 ms                                                                     | 35.5 ms: 1.03x faster                                                                 |
| fannkuch                  | 244 ms                                                                      | 239 ms: 1.02x faster                                                                  |
| sqlglot_optimize          | 38.0 ms                                                                     | 37.1 ms: 1.02x faster                                                                 |
| async_tree_memoization_tg | 216 ms                                                                      | 211 ms: 1.02x faster                                                                  |
| sympy_sum                 | 90.9 ms                                                                     | 89.0 ms: 1.02x faster                                                                 |
| sympy_str                 | 176 ms                                                                      | 173 ms: 1.02x faster                                                                  |
| pprint_pformat            | 988 ms                                                                      | 971 ms: 1.02x faster                                                                  |
| scimark_monte_carlo       | 36.4 ms                                                                     | 35.8 ms: 1.02x faster                                                                 |
| asyncio_websockets        | 310 ms                                                                      | 305 ms: 1.02x faster                                                                  |
| html5lib                  | 39.2 ms                                                                     | 38.6 ms: 1.02x faster                                                                 |
| sympy_expand              | 304 ms                                                                      | 300 ms: 1.02x faster                                                                  |
| meteor_contest            | 74.5 ms                                                                     | 73.4 ms: 1.02x faster                                                                 |
| many_optionals            | 466 us                                                                      | 460 us: 1.01x faster                                                                  |
| json                      | 2.97 ms                                                                     | 2.93 ms: 1.01x faster                                                                 |
| chaos                     | 42.4 ms                                                                     | 41.9 ms: 1.01x faster                                                                 |
| comprehensions            | 11.9 us                                                                     | 11.7 us: 1.01x faster                                                                 |
| xml_etree_generate        | 50.8 ms                                                                     | 50.2 ms: 1.01x faster                                                                 |
| pathlib                   | 76.2 ms                                                                     | 75.4 ms: 1.01x faster                                                                 |
| async_tree_none           | 181 ms                                                                      | 179 ms: 1.01x faster                                                                  |
| sympy_integrate           | 13.6 ms                                                                     | 13.5 ms: 1.01x faster                                                                 |
| connected_components      | 311 ms                                                                      | 308 ms: 1.01x faster                                                                  |
| typing_runtime_protocols  | 114 us                                                                      | 113 us: 1.01x faster                                                                  |
| regex_compile             | 81.3 ms                                                                     | 80.7 ms: 1.01x faster                                                                 |
| pyflate                   | 276 ms                                                                      | 275 ms: 1.01x faster                                                                  |
| pidigits                  | 148 ms                                                                      | 147 ms: 1.00x faster                                                                  |
| sqlite_synth              | 1.55 us                                                                     | 1.56 us: 1.00x slower                                                                 |
| bpe_tokeniser             | 2.61 sec                                                                    | 2.62 sec: 1.00x slower                                                                |
| deltablue                 | 2.29 ms                                                                     | 2.30 ms: 1.01x slower                                                                 |
| crypto_pyaes              | 40.7 ms                                                                     | 41.0 ms: 1.01x slower                                                                 |
| mdp                       | 1.49 sec                                                                    | 1.50 sec: 1.01x slower                                                                |
| pprint_safe_repr          | 489 ms                                                                      | 495 ms: 1.01x slower                                                                  |
| async_tree_none_tg        | 169 ms                                                                      | 171 ms: 1.01x slower                                                                  |
| mako                      | 5.11 ms                                                                     | 5.18 ms: 1.01x slower                                                                 |
| python_startup_no_site    | 17.4 ms                                                                     | 17.7 ms: 1.02x slower                                                                 |
| async_tree_io_tg          | 391 ms                                                                      | 398 ms: 1.02x slower                                                                  |
| sqlglot_transpile         | 1.09 ms                                                                     | 1.11 ms: 1.02x slower                                                                 |
| xml_etree_parse           | 85.0 ms                                                                     | 86.8 ms: 1.02x slower                                                                 |
| sqlglot_parse             | 838 us                                                                      | 856 us: 1.02x slower                                                                  |
| async_tree_io             | 395 ms                                                                      | 404 ms: 1.02x slower                                                                  |
| docutils                  | 1.71 sec                                                                    | 1.75 sec: 1.02x slower                                                                |
| json_dumps                | 6.22 ms                                                                     | 6.39 ms: 1.03x slower                                                                 |
| nbody                     | 52.8 ms                                                                     | 54.2 ms: 1.03x slower                                                                 |
| coverage                  | 47.1 ms                                                                     | 48.7 ms: 1.03x slower                                                                 |
| telco                     | 4.22 ms                                                                     | 4.37 ms: 1.04x slower                                                                 |
| regex_dna                 | 113 ms                                                                      | 118 ms: 1.04x slower                                                                  |
| coroutines                | 13.5 ms                                                                     | 14.2 ms: 1.05x slower                                                                 |
| xml_etree_iterparse       | 58.3 ms                                                                     | 61.2 ms: 1.05x slower                                                                 |
| deepcopy_reduce           | 1.81 us                                                                     | 1.92 us: 1.06x slower                                                                 |
| regex_effbot              | 1.40 ms                                                                     | 1.52 ms: 1.08x slower                                                                 |
| float                     | 45.3 ms                                                                     | 49.2 ms: 1.09x slower                                                                 |
| scimark_lu                | 55.5 ms                                                                     | 61.9 ms: 1.12x slower                                                                 |
| deepcopy_memo             | 16.6 us                                                                     | 20.8 us: 1.25x slower                                                                 |
| spectral_norm             | 49.1 ms                                                                     | 63.5 ms: 1.29x slower                                                                 |
| scimark_sor               | 61.2 ms                                                                     | 86.1 ms: 1.41x slower                                                                 |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (20): bench_thread_pool, k_core, thrift, async_tree_memoization, 2to3, mypy2, deepcopy, logging_simple, subparsers, create_gc_cycles, logging_format, gc_traversal, async_tree_cpu_io_mixed_tg, bench_mp_pool, json_loads, shortest_path, async_tree_cpu_io_mixed, python_startup, pycparser, logging_silent

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 96.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown