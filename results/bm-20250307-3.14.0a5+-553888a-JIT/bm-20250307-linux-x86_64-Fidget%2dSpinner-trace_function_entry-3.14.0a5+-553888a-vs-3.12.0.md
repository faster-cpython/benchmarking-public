# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3      | 274 ms                                                 | 261 ms: 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                             |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                            |
| nbody          | 97.0 ms                                                | 88.9 ms: 1.09x faster                                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                            |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 206 us: 1.12x faster                                                             |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                             |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                            |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                            |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                            |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                             |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                            |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                           |
| float                      | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                            |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                             |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                            |
| async_generators           | 463 ms                                                 | 391 ms: 1.19x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                            |
| spectral_norm              | 115 ms                                                 | 97.8 ms: 1.17x faster                                                            |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                            |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                            |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.12x faster                                                             |
| unpickle_pure_python       | 230 us                                                 | 206 us: 1.12x faster                                                             |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                            |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.10x faster                                                            |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                             |
| nbody                      | 97.0 ms                                                | 88.9 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                             |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                            |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                             |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                             |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                             |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                             |
| sympy_expand               | 478 ms                                                 | 464 ms: 1.03x faster                                                             |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                             |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                             |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                             |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                             |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                             |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                            |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                            |
| telco                      | 7.10 ms                                                | 7.74 ms: 1.09x slower                                                            |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                            |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.43x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, richards
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x