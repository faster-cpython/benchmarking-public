# Results vs. 3.12.0

- fork: kumaraditya303
- ref: future_iter
- machine: windows-x86
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.184x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 245 ms: 1.14x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                         |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 421 ms: 1.61x faster                                                           |
| async_tree_io              | 693 ms                                                          | 434 ms: 1.60x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 225 ms: 1.55x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 179 ms: 1.55x faster                                                           |
| async_tree_none            | 298 ms                                                          | 197 ms: 1.51x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 241 ms: 1.51x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 433 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 83.5 ms: 1.52x faster                                                          |
| float          | 76.7 ms                                                         | 53.8 ms: 1.42x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                          |
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                           |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.55 sec: 1.41x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 168 us: 1.25x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 95.4 ms: 1.19x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 252 us: 1.13x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 48.0 ms: 1.11x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                          |
| python_startup         | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.48 ms: 1.33x faster                                                          |
| django_template | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.5 us: 1.78x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 421 ms: 1.61x faster                                                           |
| async_tree_io              | 693 ms                                                          | 434 ms: 1.60x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.5 ms: 1.57x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 225 ms: 1.55x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 179 ms: 1.55x faster                                                           |
| deepcopy                   | 360 us                                                          | 234 us: 1.54x faster                                                           |
| spectral_norm              | 104 ms                                                          | 68.1 ms: 1.52x faster                                                          |
| nbody                      | 127 ms                                                          | 83.5 ms: 1.52x faster                                                          |
| async_tree_none            | 298 ms                                                          | 197 ms: 1.51x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 241 ms: 1.51x faster                                                           |
| go                         | 137 ms                                                          | 94.1 ms: 1.46x faster                                                          |
| logging_silent             | 101 ns                                                          | 69.7 ns: 1.45x faster                                                          |
| float                      | 76.7 ms                                                         | 53.8 ms: 1.42x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.52 ms: 1.42x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.55 sec: 1.41x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 66.0 ms: 1.41x faster                                                          |
| scimark_sor                | 130 ms                                                          | 93.1 ms: 1.39x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.91 ms: 1.39x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.48 ms: 1.33x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.5 ms: 1.31x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.46 us: 1.31x faster                                                          |
| raytrace                   | 308 ms                                                          | 235 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 433 ms: 1.30x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.98 ms: 1.29x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.9 ms: 1.29x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                          |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                           |
| pyflate                    | 424 ms                                                          | 333 ms: 1.27x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 168 us: 1.25x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.80 us: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.38 us: 1.24x faster                                                          |
| scimark_fft                | 271 ms                                                          | 222 ms: 1.22x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 76.6 ms: 1.22x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.6 ms: 1.22x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.03 ms: 1.21x faster                                                          |
| fannkuch                   | 354 ms                                                          | 292 ms: 1.21x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.20x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                         |
| pycparser                  | 978 ms                                                          | 819 ms: 1.19x faster                                                           |
| richards                   | 41.3 ms                                                         | 34.8 ms: 1.19x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 608 ms: 1.19x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 95.4 ms: 1.19x faster                                                          |
| django_template            | 36.9 ms                                                         | 31.2 ms: 1.18x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 59.9 ms: 1.15x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 42.3 ms: 1.15x faster                                                          |
| richards_super             | 46.5 ms                                                         | 40.7 ms: 1.14x faster                                                          |
| 2to3                       | 280 ms                                                          | 245 ms: 1.14x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 252 us: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                         |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.0 ms: 1.11x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 66.3 ms: 1.09x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                          |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 84.3 ms: 1.08x faster                                                          |
| async_generators           | 313 ms                                                          | 290 ms: 1.08x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.9 ms: 1.07x faster                                                          |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                          |
| json                       | 4.15 ms                                                         | 4.21 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.3 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 138 us: 1.09x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.4 ms: 1.14x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 87.0 ms: 1.15x slower                                                          |
| mypy2                      | 584 ms                                                          | 690 ms: 1.18x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.68 ms: 1.21x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.79 ms: 1.24x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 221 ms: 2.20x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                   |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.184x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown