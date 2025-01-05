# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.167x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 176 ms: 1.58x faster                                                            |
| async_tree_none            | 298 ms                                                          | 194 ms: 1.53x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 244 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.31x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 85.5 ms: 1.48x faster                                                           |
| float          | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                           |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 102 ms: 1.27x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.66 ms: 1.23x faster                                                           |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.61 sec: 1.36x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 171 us: 1.22x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 259 us: 1.11x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 48.7 ms: 1.09x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 66.7 ms: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.78 ms: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                           |
| django_template | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 23.1 us: 1.66x faster                                                           |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.58x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 176 ms: 1.58x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.7 ms: 1.56x faster                                                           |
| async_tree_none            | 298 ms                                                          | 194 ms: 1.53x faster                                                            |
| deepcopy                   | 360 us                                                          | 240 us: 1.50x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 244 ms: 1.49x faster                                                            |
| nbody                      | 127 ms                                                          | 85.5 ms: 1.48x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.6 ms: 1.45x faster                                                           |
| logging_silent             | 101 ns                                                          | 70.9 ns: 1.43x faster                                                           |
| go                         | 137 ms                                                          | 97.2 ms: 1.41x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.40x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.59 ms: 1.38x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.2 ms: 1.37x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.61 sec: 1.36x faster                                                          |
| float                      | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.07 ms: 1.35x faster                                                           |
| scimark_sor                | 130 ms                                                          | 98.2 ms: 1.32x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.92 ms: 1.32x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 432 ms: 1.31x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 16.1 ms: 1.30x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.69 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 423 ms: 1.29x faster                                                            |
| chaos                      | 69.4 ms                                                         | 54.4 ms: 1.28x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.54 us: 1.27x faster                                                           |
| raytrace                   | 308 ms                                                          | 243 ms: 1.27x faster                                                            |
| regex_compile              | 129 ms                                                          | 102 ms: 1.27x faster                                                            |
| pyflate                    | 424 ms                                                          | 336 ms: 1.26x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.7 ms: 1.26x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.75 us: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.43 us: 1.23x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 76.1 ms: 1.23x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.66 ms: 1.23x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 171 us: 1.22x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.26 ms: 1.21x faster                                                           |
| scimark_fft                | 271 ms                                                          | 225 ms: 1.20x faster                                                            |
| fannkuch                   | 354 ms                                                          | 296 ms: 1.19x faster                                                            |
| pycparser                  | 978 ms                                                          | 825 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.28 sec: 1.17x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 41.5 ms: 1.17x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 627 ms: 1.15x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                            |
| richards                   | 41.3 ms                                                         | 36.9 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 62.1 ms: 1.11x faster                                                           |
| richards_super             | 46.5 ms                                                         | 41.9 ms: 1.11x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 259 us: 1.11x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 48.7 ms: 1.09x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.6 ms: 1.09x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 66.7 ms: 1.08x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.1 ms: 1.07x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.06x faster                                                            |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| async_generators           | 313 ms                                                          | 304 ms: 1.03x faster                                                            |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                           |
| json                       | 4.15 ms                                                         | 4.33 ms: 1.04x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.0 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                            |
| mypy2                      | 584 ms                                                          | 683 ms: 1.17x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.3 ms: 1.18x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.78 ms: 1.19x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 93.0 ms: 1.23x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.81 ms: 1.24x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.62x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 216 ms: 2.16x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                    |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.167x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown