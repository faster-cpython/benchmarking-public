# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.065x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 355 ms: 1.38x faster                                                                  |
| Geometric mean             | (ref)                                                       | 1.63x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.2 ms: 1.33x faster                                                                 |
| float          | 56.8 ms                                                     | 49.2 ms: 1.15x faster                                                                 |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.7 ms: 1.08x faster                                                                 |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 107 us: 1.24x faster                                                                  |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                                 |
| xml_etree_parse      | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.2 ms: 1.06x faster                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                                 |
| pickle_pure_python   | 195 us                                                      | 192 us: 1.02x faster                                                                  |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                                 |
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                                 |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                                  |
| async_tree_io              | 731 ms                                                      | 404 ms: 1.81x faster                                                                  |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                  |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                  |
| async_tree_none            | 291 ms                                                      | 179 ms: 1.63x faster                                                                  |
| async_tree_memoization     | 339 ms                                                      | 219 ms: 1.55x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.43x faster                                                                  |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 355 ms: 1.38x faster                                                                  |
| mako                       | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                                 |
| nbody                      | 71.9 ms                                                     | 54.2 ms: 1.33x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 141 ms: 1.31x faster                                                                  |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                                  |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.03 ms: 1.26x faster                                                                 |
| unpickle_pure_python       | 133 us                                                      | 107 us: 1.24x faster                                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 35.8 ms: 1.22x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.20x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                                |
| float                      | 56.8 ms                                                     | 49.2 ms: 1.15x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 39.8 ms: 1.11x faster                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 80.7 ms: 1.08x faster                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 971 ms: 1.08x faster                                                                  |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                                  |
| pyflate                    | 295 ms                                                      | 275 ms: 1.07x faster                                                                  |
| xml_etree_parse            | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                                 |
| pathlib                    | 80.5 ms                                                     | 75.4 ms: 1.07x faster                                                                 |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.2 ms: 1.06x faster                                                                 |
| go                         | 91.6 ms                                                     | 86.1 ms: 1.06x faster                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                                 |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                                  |
| spectral_norm              | 66.9 ms                                                     | 63.5 ms: 1.05x faster                                                                 |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 495 ms: 1.04x faster                                                                  |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                                  |
| chaos                      | 43.3 ms                                                     | 41.9 ms: 1.03x faster                                                                 |
| fannkuch                   | 247 ms                                                      | 239 ms: 1.03x faster                                                                  |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                                                  |
| sympy_sum                  | 91.5 ms                                                     | 89.0 ms: 1.03x faster                                                                 |
| pickle_pure_python         | 195 us                                                      | 192 us: 1.02x faster                                                                  |
| meteor_contest             | 74.6 ms                                                     | 73.4 ms: 1.02x faster                                                                 |
| logging_simple             | 6.28 us                                                     | 6.18 us: 1.02x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                                 |
| sympy_str                  | 175 ms                                                      | 173 ms: 1.01x faster                                                                  |
| logging_format             | 6.72 us                                                     | 6.65 us: 1.01x faster                                                                 |
| generators                 | 22.5 ms                                                     | 23.0 ms: 1.02x slower                                                                 |
| pycparser                  | 699 ms                                                      | 714 ms: 1.02x slower                                                                  |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                                  |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 61.9 ms: 1.05x slower                                                                 |
| logging_silent             | 60.5 ns                                                     | 63.6 ns: 1.05x slower                                                                 |
| sqlglot_normalize          | 187 ms                                                      | 197 ms: 1.05x slower                                                                  |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                                  |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.06x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.37 ms: 1.06x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 856 us: 1.06x slower                                                                  |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.08x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                                 |
| scimark_sor                | 78.8 ms                                                     | 86.1 ms: 1.09x slower                                                                 |
| richards                   | 28.4 ms                                                     | 31.0 ms: 1.09x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.49 ms: 1.09x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.10x slower                                                                |
| richards_super             | 32.1 ms                                                     | 35.4 ms: 1.10x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.39 ms: 1.12x slower                                                                 |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                 |
| regex_v8                   | 14.2 ms                                                     | 16.9 ms: 1.19x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                                  |
| bench_mp_pool              | 69.2 ms                                                     | 82.4 ms: 1.19x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                                 |
| mypy2                      | 509 ms                                                      | 630 ms: 1.24x slower                                                                  |
| gc_traversal               | 1.52 ms                                                     | 1.98 ms: 1.30x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                          |

Benchmark hidden because not significant (2): coroutines, 2to3
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown