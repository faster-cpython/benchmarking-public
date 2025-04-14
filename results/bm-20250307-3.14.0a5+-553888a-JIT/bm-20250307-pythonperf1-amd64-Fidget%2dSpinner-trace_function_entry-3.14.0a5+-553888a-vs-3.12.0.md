# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.065x faster
- HPT reliability: 98.51%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3      | 218 ms                                                      | 225 ms: 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                                  |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 41.4 ms: 1.37x faster                                                                 |
| nbody          | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                                 |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                                  |
| regex_compile  | 87.5 ms                                                     | 85.5 ms: 1.02x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 117 us: 1.14x faster                                                                  |
| xml_etree_generate   | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.09x faster                                                                |
| xml_etree_process    | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                                 |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                                 |
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                                 |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                 |
| pickle_pure_python   | 195 us                                                      | 218 us: 1.11x slower                                                                  |
| json_dumps           | 5.70 ms                                                     | 6.87 ms: 1.21x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.7 ms: 1.27x slower                                                                 |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.46 ms: 1.30x faster                                                                 |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.52x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 418 ms: 1.75x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 215 ms: 1.71x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 175 ms: 1.63x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 185 ms: 1.58x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 216 ms: 1.57x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.46x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                                  |
| float                      | 56.8 ms                                                     | 41.4 ms: 1.37x faster                                                                 |
| mako                       | 7.09 ms                                                     | 5.46 ms: 1.30x faster                                                                 |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                                  |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.21x faster                                                                  |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.16 ms: 1.18x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                                 |
| nbody                      | 71.9 ms                                                     | 62.2 ms: 1.16x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.14x faster                                                                 |
| unpickle_pure_python       | 133 us                                                      | 117 us: 1.14x faster                                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.46 ms: 1.11x faster                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 50.9 ms: 1.10x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.09x faster                                                                |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                                 |
| async_generators           | 239 ms                                                      | 222 ms: 1.08x faster                                                                  |
| pyflate                    | 295 ms                                                      | 273 ms: 1.08x faster                                                                  |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                                  |
| go                         | 91.6 ms                                                     | 86.9 ms: 1.05x faster                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 36.0 ms: 1.05x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                                 |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 61.2 ms: 1.03x faster                                                                 |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 85.5 ms: 1.02x faster                                                                 |
| chaos                      | 43.3 ms                                                     | 42.4 ms: 1.02x faster                                                                 |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                                  |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                                 |
| spectral_norm              | 66.9 ms                                                     | 66.6 ms: 1.01x faster                                                                 |
| raytrace                   | 192 ms                                                      | 195 ms: 1.01x slower                                                                  |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                                  |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                                  |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                                 |
| richards_super             | 32.1 ms                                                     | 33.4 ms: 1.04x slower                                                                 |
| logging_format             | 6.72 us                                                     | 7.00 us: 1.04x slower                                                                 |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.05x slower                                                                 |
| logging_simple             | 6.28 us                                                     | 6.58 us: 1.05x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.05x slower                                                                 |
| logging_silent             | 60.5 ns                                                     | 63.8 ns: 1.05x slower                                                                 |
| pycparser                  | 699 ms                                                      | 739 ms: 1.06x slower                                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.5 ms: 1.06x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.40 ms: 1.07x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 865 us: 1.08x slower                                                                  |
| sympy_expand               | 284 ms                                                      | 306 ms: 1.08x slower                                                                  |
| hexiom                     | 4.10 ms                                                     | 4.43 ms: 1.08x slower                                                                 |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 64.7 ms: 1.10x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 218 us: 1.11x slower                                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                                  |
| scimark_sor                | 78.8 ms                                                     | 88.2 ms: 1.12x slower                                                                 |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                                |
| coverage                   | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.87 ms: 1.21x slower                                                                 |
| bench_mp_pool              | 69.2 ms                                                     | 87.5 ms: 1.26x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 20.7 ms: 1.27x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                 |
| gc_traversal               | 1.52 ms                                                     | 2.07 ms: 1.36x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                          |

Benchmark hidden because not significant (3): meteor_contest, bench_thread_pool, pidigits
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 98.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown