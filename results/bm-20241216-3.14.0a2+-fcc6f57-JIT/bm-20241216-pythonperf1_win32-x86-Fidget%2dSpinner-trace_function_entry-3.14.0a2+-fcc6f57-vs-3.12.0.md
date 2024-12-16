# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-x86
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 259 ms: 1.08x faster                                                                      |
| docutils       | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.49x faster                                                                      |
| async_tree_io              | 693 ms                                                          | 466 ms: 1.49x faster                                                                      |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                                      |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                                      |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                                      |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                                      |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                                      |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 56.9 ms: 1.35x faster                                                                     |
| nbody          | 127 ms                                                          | 98.2 ms: 1.29x faster                                                                     |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                                      |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                                     |
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                                      |
| regex_dna      | 127 ms                                                          | 114 ms: 1.12x faster                                                                      |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                                    |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                                     |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                                      |
| unpickle_pure_python | 210 us                                                          | 206 us: 1.02x faster                                                                      |
| xml_etree_process    | 53.2 ms                                                         | 53.5 ms: 1.00x slower                                                                     |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                                     |
| pickle_pure_python   | 286 us                                                          | 303 us: 1.06x slower                                                                      |
| json_dumps           | 7.40 ms                                                         | 9.00 ms: 1.22x slower                                                                     |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                              |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                                     |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                                     |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.49 ms: 1.33x faster                                                                     |
| django_template | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                                     |
| Geometric mean  | (ref)                                                           | 1.20x faster                                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.0 us: 1.83x faster                                                                     |
| deepcopy                   | 360 us                                                          | 230 us: 1.56x faster                                                                      |
| async_tree_io_tg           | 677 ms                                                          | 453 ms: 1.49x faster                                                                      |
| async_tree_io              | 693 ms                                                          | 466 ms: 1.49x faster                                                                      |
| generators                 | 38.5 ms                                                         | 26.3 ms: 1.47x faster                                                                     |
| spectral_norm              | 104 ms                                                          | 71.9 ms: 1.44x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 194 ms: 1.43x faster                                                                      |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                                      |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                                      |
| float                      | 76.7 ms                                                         | 56.9 ms: 1.35x faster                                                                     |
| logging_silent             | 101 ns                                                          | 75.6 ns: 1.34x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                                      |
| deltablue                  | 3.58 ms                                                         | 2.69 ms: 1.33x faster                                                                     |
| scimark_lu                 | 93.2 ms                                                         | 70.1 ms: 1.33x faster                                                                     |
| mako                       | 9.96 ms                                                         | 7.49 ms: 1.33x faster                                                                     |
| scimark_sor                | 130 ms                                                          | 97.8 ms: 1.33x faster                                                                     |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                                      |
| deepcopy_reduce            | 3.23 us                                                         | 2.44 us: 1.32x faster                                                                     |
| nbody                      | 127 ms                                                          | 98.2 ms: 1.29x faster                                                                     |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.02 ms: 1.28x faster                                                                     |
| hexiom                     | 6.82 ms                                                         | 5.36 ms: 1.27x faster                                                                     |
| raytrace                   | 308 ms                                                          | 242 ms: 1.27x faster                                                                      |
| dulwich_log                | 58.5 ms                                                         | 47.0 ms: 1.24x faster                                                                     |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                                    |
| pyflate                    | 424 ms                                                          | 350 ms: 1.21x faster                                                                      |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                                      |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.19x faster                                                                      |
| logging_simple             | 9.75 us                                                         | 8.22 us: 1.19x faster                                                                     |
| logging_format             | 10.4 us                                                         | 8.83 us: 1.18x faster                                                                     |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                                      |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.4 ms: 1.17x faster                                                                     |
| comprehensions             | 19.2 us                                                         | 16.7 us: 1.15x faster                                                                     |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.12x faster                                                                      |
| regex_dna                  | 127 ms                                                          | 114 ms: 1.12x faster                                                                      |
| chaos                      | 69.4 ms                                                         | 62.6 ms: 1.11x faster                                                                     |
| scimark_fft                | 271 ms                                                          | 245 ms: 1.11x faster                                                                      |
| scimark_monte_carlo        | 66.4 ms                                                         | 60.8 ms: 1.09x faster                                                                     |
| mdp                        | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                                    |
| django_template            | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                                     |
| pathlib                    | 91.4 ms                                                         | 84.2 ms: 1.09x faster                                                                     |
| nqueens                    | 93.7 ms                                                         | 86.5 ms: 1.08x faster                                                                     |
| 2to3                       | 280 ms                                                          | 259 ms: 1.08x faster                                                                      |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                                     |
| sympy_str                  | 240 ms                                                          | 223 ms: 1.07x faster                                                                      |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                                     |
| pycparser                  | 978 ms                                                          | 912 ms: 1.07x faster                                                                      |
| async_generators           | 313 ms                                                          | 294 ms: 1.07x faster                                                                      |
| richards_super             | 46.5 ms                                                         | 43.6 ms: 1.07x faster                                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.17 ms: 1.06x faster                                                                     |
| sympy_integrate            | 17.5 ms                                                         | 16.5 ms: 1.06x faster                                                                     |
| sqlglot_transpile          | 1.53 ms                                                         | 1.45 ms: 1.06x faster                                                                     |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                                      |
| richards                   | 41.3 ms                                                         | 39.6 ms: 1.04x faster                                                                     |
| docutils                   | 1.98 sec                                                        | 1.91 sec: 1.04x faster                                                                    |
| sympy_expand               | 398 ms                                                          | 388 ms: 1.03x faster                                                                      |
| fannkuch                   | 354 ms                                                          | 346 ms: 1.02x faster                                                                      |
| unpickle_pure_python       | 210 us                                                          | 206 us: 1.02x faster                                                                      |
| crypto_pyaes               | 69.2 ms                                                         | 68.9 ms: 1.01x faster                                                                     |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                                      |
| xml_etree_process          | 53.2 ms                                                         | 53.5 ms: 1.00x slower                                                                     |
| meteor_contest             | 86.9 ms                                                         | 87.5 ms: 1.01x slower                                                                     |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                                    |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                                     |
| pprint_safe_repr           | 721 ms                                                          | 736 ms: 1.02x slower                                                                      |
| json                       | 4.15 ms                                                         | 4.26 ms: 1.02x slower                                                                     |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                                     |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 105 ms: 1.04x slower                                                                      |
| sqlglot_optimize           | 48.5 ms                                                         | 51.2 ms: 1.06x slower                                                                     |
| pickle_pure_python         | 286 us                                                          | 303 us: 1.06x slower                                                                      |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.06x slower                                                                     |
| bench_mp_pool              | 75.4 ms                                                         | 87.1 ms: 1.15x slower                                                                     |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                                     |
| json_dumps                 | 7.40 ms                                                         | 9.00 ms: 1.22x slower                                                                     |
| mypy2                      | 584 ms                                                          | 716 ms: 1.23x slower                                                                      |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                                     |
| telco                      | 5.51 ms                                                         | 7.12 ms: 1.29x slower                                                                     |
| typing_runtime_protocols   | 126 us                                                          | 167 us: 1.32x slower                                                                      |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                              |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown