# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.083x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 266 ms: 1.05x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                            |
| async_tree_io              | 693 ms                                                          | 471 ms: 1.47x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 243 ms: 1.44x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                            |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 51.9 ms: 1.48x faster                                                           |
| nbody          | 127 ms                                                          | 97.0 ms: 1.31x faster                                                           |
| pidigits       | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| regex_compile  | 129 ms                                                          | 112 ms: 1.16x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 200 us: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 72.7 ms: 1.01x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 291 us: 1.02x slower                                                            |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.92 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.96 ms                                                         | 7.45 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.63x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 451 ms: 1.50x faster                                                            |
| float                      | 76.7 ms                                                         | 51.9 ms: 1.48x faster                                                           |
| async_tree_io              | 693 ms                                                          | 471 ms: 1.47x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 243 ms: 1.44x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 195 ms: 1.42x faster                                                            |
| spectral_norm              | 104 ms                                                          | 73.4 ms: 1.42x faster                                                           |
| scimark_sor                | 130 ms                                                          | 95.2 ms: 1.36x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.45 ms: 1.34x faster                                                           |
| deepcopy                   | 360 us                                                          | 271 us: 1.33x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                            |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 70.8 ms: 1.32x faster                                                           |
| nbody                      | 127 ms                                                          | 97.0 ms: 1.31x faster                                                           |
| logging_silent             | 101 ns                                                          | 78.5 ns: 1.29x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.6 ms: 1.26x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.76 sec: 1.25x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 439 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                                           |
| regex_compile              | 129 ms                                                          | 112 ms: 1.16x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 50.6 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.80 us: 1.15x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.50 us: 1.15x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.10 us: 1.14x faster                                                           |
| pyflate                    | 424 ms                                                          | 374 ms: 1.13x faster                                                            |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.13x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.17 ms: 1.13x faster                                                           |
| go                         | 137 ms                                                          | 122 ms: 1.13x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.12 ms: 1.11x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.7 ms: 1.11x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.39 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 61.2 ms: 1.09x faster                                                           |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                            |
| raytrace                   | 308 ms                                                          | 289 ms: 1.07x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.05 ms: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 266 ms: 1.05x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                          |
| pycparser                  | 978 ms                                                          | 931 ms: 1.05x faster                                                            |
| fannkuch                   | 354 ms                                                          | 337 ms: 1.05x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 200 us: 1.05x faster                                                            |
| chaos                      | 69.4 ms                                                         | 66.4 ms: 1.05x faster                                                           |
| comprehensions             | 19.2 us                                                         | 18.5 us: 1.04x faster                                                           |
| generators                 | 38.5 ms                                                         | 37.4 ms: 1.03x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                          |
| sympy_str                  | 240 ms                                                          | 234 ms: 1.02x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.01x faster                                                           |
| richards_super             | 46.5 ms                                                         | 45.8 ms: 1.01x faster                                                           |
| richards                   | 41.3 ms                                                         | 40.8 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 200 ms: 1.00x slower                                                            |
| meteor_contest             | 86.9 ms                                                         | 87.4 ms: 1.01x slower                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 72.7 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 729 ms: 1.01x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 291 us: 1.02x slower                                                            |
| sympy_expand               | 398 ms                                                          | 406 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                           |
| hexiom                     | 6.82 ms                                                         | 7.02 ms: 1.03x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 97.3 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 50.4 ms: 1.04x slower                                                           |
| async_generators           | 313 ms                                                          | 329 ms: 1.05x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 106 ms: 1.06x slower                                                            |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                           |
| json                       | 4.15 ms                                                         | 4.46 ms: 1.07x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.5 ms: 1.08x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 87.4 ms: 1.16x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.92 ms: 1.21x slower                                                           |
| mypy2                      | 584 ms                                                          | 727 ms: 1.25x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.01 ms: 1.27x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 164 us: 1.29x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.61x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): django_template, pprint_pformat, crypto_pyaes, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.083x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown