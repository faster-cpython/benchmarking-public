# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-amd64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.046x faster
- HPT reliability: 82.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.03x slower                                                              |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                            |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                              |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 204 ms: 1.80x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                              |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 363 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                              |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                             |
| nbody          | 71.9 ms                                                     | 62.8 ms: 1.15x faster                                                             |
| pidigits       | 152 ms                                                      | 155 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.3 ms: 1.05x faster                                                             |
| regex_dna      | 126 ms                                                      | 133 ms: 1.05x slower                                                              |
| regex_v8       | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                             |
| regex_effbot   | 1.62 ms                                                     | 1.95 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.8 ms: 1.06x slower                                                             |
| pickle_pure_python   | 195 us                                                      | 210 us: 1.07x slower                                                              |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.09x slower                                                              |
| xml_etree_parse      | 93.0 ms                                                     | 102 ms: 1.10x slower                                                              |
| xml_etree_generate   | 55.8 ms                                                     | 63.9 ms: 1.14x slower                                                             |
| xml_etree_process    | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                             |
| json_dumps           | 5.70 ms                                                     | 7.80 ms: 1.37x slower                                                             |
| json_loads           | 13.9 us                                                     | 19.7 us: 1.41x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                             |
| python_startup         | 19.5 ms                                                     | 26.9 ms: 1.38x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                             |
| mako            | 7.09 ms                                                     | 7.58 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.7 ms: 2.71x faster                                                             |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                              |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                              |
| async_tree_memoization_tg  | 367 ms                                                      | 204 ms: 1.80x faster                                                              |
| async_tree_none_tg         | 285 ms                                                      | 166 ms: 1.72x faster                                                              |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                              |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                              |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 363 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 356 ms: 1.37x faster                                                              |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                              |
| generators                 | 22.5 ms                                                     | 17.1 ms: 1.32x faster                                                             |
| float                      | 56.8 ms                                                     | 43.6 ms: 1.30x faster                                                             |
| go                         | 91.6 ms                                                     | 70.3 ms: 1.30x faster                                                             |
| deepcopy_memo              | 23.7 us                                                     | 18.7 us: 1.27x faster                                                             |
| comprehensions             | 14.1 us                                                     | 11.4 us: 1.24x faster                                                             |
| deltablue                  | 2.16 ms                                                     | 1.79 ms: 1.20x faster                                                             |
| spectral_norm              | 66.9 ms                                                     | 56.4 ms: 1.19x faster                                                             |
| scimark_sor                | 78.8 ms                                                     | 67.2 ms: 1.17x faster                                                             |
| raytrace                   | 192 ms                                                      | 166 ms: 1.16x faster                                                              |
| nbody                      | 71.9 ms                                                     | 62.8 ms: 1.15x faster                                                             |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.9 ms: 1.12x faster                                                             |
| chaos                      | 43.3 ms                                                     | 38.8 ms: 1.12x faster                                                             |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                             |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                             |
| async_generators           | 239 ms                                                      | 219 ms: 1.10x faster                                                              |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                             |
| logging_silent             | 60.5 ns                                                     | 56.6 ns: 1.07x faster                                                             |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                                             |
| hexiom                     | 4.10 ms                                                     | 3.87 ms: 1.06x faster                                                             |
| regex_compile              | 87.5 ms                                                     | 83.3 ms: 1.05x faster                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.04x faster                                                             |
| pyflate                    | 295 ms                                                      | 285 ms: 1.03x faster                                                              |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.49 ms: 1.03x faster                                                             |
| richards                   | 28.4 ms                                                     | 28.0 ms: 1.02x faster                                                             |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                             |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                                              |
| richards_super             | 32.1 ms                                                     | 31.8 ms: 1.01x faster                                                             |
| sympy_sum                  | 91.5 ms                                                     | 91.0 ms: 1.01x faster                                                             |
| sqlglot_parse              | 804 us                                                      | 808 us: 1.00x slower                                                              |
| pprint_safe_repr           | 513 ms                                                      | 516 ms: 1.01x slower                                                              |
| logging_simple             | 6.28 us                                                     | 6.32 us: 1.01x slower                                                             |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                              |
| logging_format             | 6.72 us                                                     | 6.78 us: 1.01x slower                                                             |
| sqlglot_normalize          | 187 ms                                                      | 190 ms: 1.01x slower                                                              |
| pidigits                   | 152 ms                                                      | 155 ms: 1.02x slower                                                              |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                              |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.02x slower                                                             |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                             |
| bench_thread_pool          | 857 us                                                      | 879 us: 1.03x slower                                                              |
| 2to3                       | 218 ms                                                      | 226 ms: 1.03x slower                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 50.7 ms: 1.05x slower                                                             |
| regex_dna                  | 126 ms                                                      | 133 ms: 1.05x slower                                                              |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.8 ms: 1.06x slower                                                             |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                             |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.07x slower                                                              |
| mako                       | 7.09 ms                                                     | 7.58 ms: 1.07x slower                                                             |
| scimark_lu                 | 58.9 ms                                                     | 63.0 ms: 1.07x slower                                                             |
| pickle_pure_python         | 195 us                                                      | 210 us: 1.07x slower                                                              |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.09x slower                                                              |
| xml_etree_parse            | 93.0 ms                                                     | 102 ms: 1.10x slower                                                              |
| fannkuch                   | 247 ms                                                      | 272 ms: 1.10x slower                                                              |
| xml_etree_generate         | 55.8 ms                                                     | 63.9 ms: 1.14x slower                                                             |
| regex_v8                   | 14.2 ms                                                     | 16.7 ms: 1.17x slower                                                             |
| mdp                        | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                                            |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                              |
| xml_etree_process          | 37.7 ms                                                     | 44.5 ms: 1.18x slower                                                             |
| json                       | 3.05 ms                                                     | 3.65 ms: 1.20x slower                                                             |
| regex_effbot               | 1.62 ms                                                     | 1.95 ms: 1.20x slower                                                             |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                             |
| telco                      | 4.13 ms                                                     | 5.14 ms: 1.24x slower                                                             |
| coverage                   | 40.8 ms                                                     | 52.3 ms: 1.28x slower                                                             |
| bench_mp_pool              | 69.2 ms                                                     | 90.1 ms: 1.30x slower                                                             |
| json_dumps                 | 5.70 ms                                                     | 7.80 ms: 1.37x slower                                                             |
| python_startup             | 19.5 ms                                                     | 26.9 ms: 1.38x slower                                                             |
| json_loads                 | 13.9 us                                                     | 19.7 us: 1.41x slower                                                             |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                             |
| gc_traversal               | 1.52 ms                                                     | 2.71 ms: 1.78x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                      |

Benchmark hidden because not significant (2): sqlglot_transpile, pprint_pformat
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 82.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown