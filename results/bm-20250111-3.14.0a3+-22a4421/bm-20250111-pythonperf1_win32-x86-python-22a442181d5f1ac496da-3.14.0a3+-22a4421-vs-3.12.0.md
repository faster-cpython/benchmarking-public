# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-x86
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.59x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 176 ms: 1.57x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 242 ms: 1.50x faster                                                            |
| async_tree_none            | 298 ms                                                          | 199 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 438 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 426 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| float          | 76.7 ms                                                         | 56.2 ms: 1.37x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 99.9 ms: 1.29x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 169 us: 1.24x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 261 us: 1.10x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                           |
| json_loads           | 20.4 us                                                         | 21.3 us: 1.04x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.11 us: 1.06x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.4 us: 1.07x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.74 us: 1.11x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.9 us: 1.12x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.72 ms: 1.18x slower                                                           |
| pickle               | 7.79 us                                                         | 10.5 us: 1.34x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.3 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.54 ms: 1.32x faster                                                           |
| django_template | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.24x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.9 us: 1.75x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 408 ms: 1.66x faster                                                            |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                            |
| generators                 | 38.5 ms                                                         | 24.2 ms: 1.59x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 221 ms: 1.59x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 176 ms: 1.57x faster                                                            |
| deepcopy                   | 360 us                                                          | 235 us: 1.53x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 242 ms: 1.50x faster                                                            |
| async_tree_none            | 298 ms                                                          | 199 ms: 1.49x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 42.1 ns: 1.48x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.4 ms: 1.45x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.4 us: 1.43x faster                                                           |
| go                         | 137 ms                                                          | 96.2 ms: 1.43x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.78 ms: 1.43x faster                                                           |
| nbody                      | 127 ms                                                          | 89.4 ms: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.53 ms: 1.41x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 66.9 ms: 1.39x faster                                                           |
| logging_silent             | 101 ns                                                          | 73.1 ns: 1.38x faster                                                           |
| float                      | 76.7 ms                                                         | 56.2 ms: 1.37x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.37 us: 1.36x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.64 sec: 1.34x faster                                                          |
| mako                       | 9.96 ms                                                         | 7.54 ms: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.4 ms: 1.31x faster                                                           |
| regex_compile              | 129 ms                                                          | 99.9 ms: 1.29x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.8 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 438 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 426 ms: 1.28x faster                                                            |
| raytrace                   | 308 ms                                                          | 243 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.11 ms: 1.24x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 169 us: 1.24x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 75.9 ms: 1.23x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.0 ms: 1.23x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.03 ms: 1.21x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.20x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.20 us: 1.19x faster                                                           |
| pycparser                  | 978 ms                                                          | 827 ms: 1.18x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.2 ms: 1.17x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 41.4 ms: 1.17x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| richards                   | 41.3 ms                                                         | 35.4 ms: 1.17x faster                                                           |
| pyflate                    | 424 ms                                                          | 364 ms: 1.17x faster                                                            |
| scimark_fft                | 271 ms                                                          | 233 ms: 1.16x faster                                                            |
| fannkuch                   | 354 ms                                                          | 304 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.2 ms: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.97 us: 1.16x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| richards_super             | 46.5 ms                                                         | 40.6 ms: 1.14x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                           |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 61.7 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 261 us: 1.10x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 662 ms: 1.09x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 80.8 ms: 1.08x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.06x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 87.3 ms: 1.05x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| async_generators           | 313 ms                                                          | 306 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 2.03 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| json                       | 4.15 ms                                                         | 4.31 ms: 1.04x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.3 us: 1.04x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.11 us: 1.06x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.4 us: 1.07x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.74 us: 1.11x slower                                                           |
| coverage                   | 48.4 ms                                                         | 54.1 ms: 1.12x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.9 us: 1.12x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 744 ms: 1.12x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 88.4 ms: 1.17x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.3 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.72 ms: 1.18x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.67 ms: 1.21x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| pickle                     | 7.79 us                                                         | 10.5 us: 1.34x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 213 ms: 2.12x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                    |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown