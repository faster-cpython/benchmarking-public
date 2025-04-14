# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-x86
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 229 ms: 1.22x faster                                                                  |
| docutils       | 1.98 sec                                                        | 1.72 sec: 1.15x faster                                                                |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 367 ms: 1.84x faster                                                                  |
| async_tree_io              | 693 ms                                                          | 379 ms: 1.83x faster                                                                  |
| async_tree_none_tg         | 278 ms                                                          | 158 ms: 1.75x faster                                                                  |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 211 ms: 1.66x faster                                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 436 ms: 1.29x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 430 ms: 1.27x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.62x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 69.2 ms: 1.84x faster                                                                 |
| float          | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                                 |
| pidigits       | 199 ms                                                          | 217 ms: 1.09x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.41x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 88.5 ms: 1.46x faster                                                                 |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                                 |
| regex_dna      | 127 ms                                                          | 132 ms: 1.04x slower                                                                  |
| regex_v8       | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                                |
| unpickle_pure_python | 210 us                                                          | 153 us: 1.37x faster                                                                  |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                                  |
| xml_etree_process    | 53.2 ms                                                         | 46.9 ms: 1.14x faster                                                                 |
| xml_etree_generate   | 72.1 ms                                                         | 67.2 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 73.1 ms: 1.06x faster                                                                 |
| xml_etree_parse      | 113 ms                                                          | 114 ms: 1.01x slower                                                                  |
| json_dumps           | 7.40 ms                                                         | 7.52 ms: 1.02x slower                                                                 |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.05x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                                 |
| python_startup         | 22.4 ms                                                         | 28.6 ms: 1.28x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                                 |
| mako            | 9.96 ms                                                         | 7.82 ms: 1.27x faster                                                                 |
| Geometric mean  | (ref)                                                           | 1.31x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 32.9 ms: 2.78x faster                                                                 |
| generators                 | 38.5 ms                                                         | 17.1 ms: 2.26x faster                                                                 |
| deepcopy_memo              | 38.4 us                                                         | 18.2 us: 2.11x faster                                                                 |
| deepcopy                   | 360 us                                                          | 190 us: 1.90x faster                                                                  |
| async_tree_io_tg           | 677 ms                                                          | 367 ms: 1.84x faster                                                                  |
| nbody                      | 127 ms                                                          | 69.2 ms: 1.84x faster                                                                 |
| async_tree_io              | 693 ms                                                          | 379 ms: 1.83x faster                                                                  |
| deltablue                  | 3.58 ms                                                         | 2.00 ms: 1.79x faster                                                                 |
| async_tree_none_tg         | 278 ms                                                          | 158 ms: 1.75x faster                                                                  |
| spectral_norm              | 104 ms                                                          | 59.7 ms: 1.74x faster                                                                 |
| go                         | 137 ms                                                          | 79.3 ms: 1.73x faster                                                                 |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                                  |
| scimark_sor                | 130 ms                                                          | 75.5 ms: 1.72x faster                                                                 |
| async_tree_memoization     | 364 ms                                                          | 213 ms: 1.71x faster                                                                  |
| deepcopy_reduce            | 3.23 us                                                         | 1.92 us: 1.68x faster                                                                 |
| float                      | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                                 |
| async_tree_memoization_tg  | 350 ms                                                          | 211 ms: 1.66x faster                                                                  |
| raytrace                   | 308 ms                                                          | 193 ms: 1.60x faster                                                                  |
| logging_silent             | 101 ns                                                          | 63.3 ns: 1.60x faster                                                                 |
| tomli_loads                | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                                |
| comprehensions             | 19.2 us                                                         | 12.3 us: 1.56x faster                                                                 |
| coroutines                 | 20.9 ms                                                         | 13.5 ms: 1.55x faster                                                                 |
| hexiom                     | 6.82 ms                                                         | 4.40 ms: 1.55x faster                                                                 |
| chaos                      | 69.4 ms                                                         | 45.1 ms: 1.54x faster                                                                 |
| scimark_monte_carlo        | 66.4 ms                                                         | 43.8 ms: 1.52x faster                                                                 |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.57 ms: 1.50x faster                                                                 |
| regex_compile              | 129 ms                                                          | 88.5 ms: 1.46x faster                                                                 |
| sqlglot_parse              | 1.25 ms                                                         | 871 us: 1.43x faster                                                                  |
| pyflate                    | 424 ms                                                          | 300 ms: 1.41x faster                                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.10 ms: 1.39x faster                                                                 |
| pprint_pformat             | 1.50 sec                                                        | 1.08 sec: 1.39x faster                                                                |
| scimark_fft                | 271 ms                                                          | 196 ms: 1.38x faster                                                                  |
| pprint_safe_repr           | 721 ms                                                          | 525 ms: 1.37x faster                                                                  |
| unpickle_pure_python       | 210 us                                                          | 153 us: 1.37x faster                                                                  |
| logging_simple             | 9.75 us                                                         | 7.16 us: 1.36x faster                                                                 |
| logging_format             | 10.4 us                                                         | 7.65 us: 1.36x faster                                                                 |
| async_generators           | 313 ms                                                          | 231 ms: 1.36x faster                                                                  |
| django_template            | 36.9 ms                                                         | 27.3 ms: 1.35x faster                                                                 |
| nqueens                    | 93.7 ms                                                         | 69.6 ms: 1.35x faster                                                                 |
| pycparser                  | 978 ms                                                          | 754 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 436 ms: 1.29x faster                                                                  |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                                  |
| richards_super             | 46.5 ms                                                         | 36.2 ms: 1.28x faster                                                                 |
| fannkuch                   | 354 ms                                                          | 277 ms: 1.28x faster                                                                  |
| dulwich_log                | 58.5 ms                                                         | 45.8 ms: 1.28x faster                                                                 |
| mako                       | 9.96 ms                                                         | 7.82 ms: 1.27x faster                                                                 |
| richards                   | 41.3 ms                                                         | 32.5 ms: 1.27x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 430 ms: 1.27x faster                                                                  |
| scimark_lu                 | 93.2 ms                                                         | 74.0 ms: 1.26x faster                                                                 |
| sqlglot_optimize           | 48.5 ms                                                         | 38.6 ms: 1.26x faster                                                                 |
| sympy_str                  | 240 ms                                                          | 191 ms: 1.26x faster                                                                  |
| sympy_sum                  | 123 ms                                                          | 97.9 ms: 1.25x faster                                                                 |
| sympy_integrate            | 17.5 ms                                                         | 14.2 ms: 1.24x faster                                                                 |
| 2to3                       | 280 ms                                                          | 229 ms: 1.22x faster                                                                  |
| sympy_expand               | 398 ms                                                          | 327 ms: 1.22x faster                                                                  |
| crypto_pyaes               | 69.2 ms                                                         | 58.6 ms: 1.18x faster                                                                 |
| docutils                   | 1.98 sec                                                        | 1.72 sec: 1.15x faster                                                                |
| xml_etree_process          | 53.2 ms                                                         | 46.9 ms: 1.14x faster                                                                 |
| meteor_contest             | 86.9 ms                                                         | 77.0 ms: 1.13x faster                                                                 |
| sqlite_synth               | 2.07 us                                                         | 1.84 us: 1.12x faster                                                                 |
| xml_etree_generate         | 72.1 ms                                                         | 67.2 ms: 1.07x faster                                                                 |
| mdp                        | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 73.1 ms: 1.06x faster                                                                 |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                                 |
| typing_runtime_protocols   | 126 us                                                          | 122 us: 1.03x faster                                                                  |
| xml_etree_parse            | 113 ms                                                          | 114 ms: 1.01x slower                                                                  |
| json_dumps                 | 7.40 ms                                                         | 7.52 ms: 1.02x slower                                                                 |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                                 |
| regex_dna                  | 127 ms                                                          | 132 ms: 1.04x slower                                                                  |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.05x slower                                                                 |
| bench_thread_pool          | 1.10 ms                                                         | 1.18 ms: 1.07x slower                                                                 |
| telco                      | 5.51 ms                                                         | 5.90 ms: 1.07x slower                                                                 |
| pidigits                   | 199 ms                                                          | 217 ms: 1.09x slower                                                                  |
| coverage                   | 48.4 ms                                                         | 54.9 ms: 1.13x slower                                                                 |
| python_startup_no_site     | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                                 |
| regex_v8                   | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                                 |
| bench_mp_pool              | 75.4 ms                                                         | 92.2 ms: 1.22x slower                                                                 |
| python_startup             | 22.4 ms                                                         | 28.6 ms: 1.28x slower                                                                 |
| gc_traversal               | 1.44 ms                                                         | 2.43 ms: 1.69x slower                                                                 |
| create_gc_cycles           | 652 us                                                          | 1.17 ms: 1.79x slower                                                                 |
| sqlglot_normalize          | 100 ms                                                          | 195 ms: 1.94x slower                                                                  |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                          |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.292x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown