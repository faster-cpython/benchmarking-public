# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.086x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 272 ms: 1.03x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 481 ms: 1.44x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.33x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                                           |
| nbody          | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| regex_compile  | 129 ms                                                          | 117 ms: 1.10x faster                                                            |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.83 sec: 1.20x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 18.7 us: 1.07x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.28 us: 1.03x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 73.7 ms: 1.02x slower                                                           |
| xml_etree_process    | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                                           |
| unpickle_pure_python | 210 us                                                          | 226 us: 1.08x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.09x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 326 us: 1.14x slower                                                            |
| pickle               | 7.79 us                                                         | 9.54 us: 1.22x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.26 ms: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.9 ms: 1.15x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.63 ms: 1.30x faster                                                           |
| django_template | 36.9 ms                                                         | 35.8 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.79x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.4 ms: 1.65x faster                                                           |
| spectral_norm              | 104 ms                                                          | 65.9 ms: 1.57x faster                                                           |
| logging_silent             | 101 ns                                                          | 69.9 ns: 1.45x faster                                                           |
| async_tree_io              | 693 ms                                                          | 481 ms: 1.44x faster                                                            |
| deepcopy                   | 360 us                                                          | 252 us: 1.43x faster                                                            |
| float                      | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 477 ms: 1.42x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 66.2 ms: 1.41x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 67.7 ms: 1.35x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.33x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.8 ms: 1.32x faster                                                           |
| scimark_sor                | 130 ms                                                          | 98.7 ms: 1.32x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.55 ms: 1.31x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.63 ms: 1.30x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 51.0 ms: 1.30x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 231 ms: 1.29x faster                                                            |
| pyflate                    | 424 ms                                                          | 340 ms: 1.25x faster                                                            |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.63 us: 1.23x faster                                                           |
| chaos                      | 69.4 ms                                                         | 56.7 ms: 1.22x faster                                                           |
| raytrace                   | 308 ms                                                          | 253 ms: 1.22x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.97 ms: 1.20x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.83 sec: 1.20x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.21 us: 1.19x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.28 ms: 1.18x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.90 us: 1.17x faster                                                           |
| comprehensions             | 19.2 us                                                         | 16.4 us: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.4 ms: 1.15x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 54.3 ns: 1.15x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.93 ms: 1.15x faster                                                           |
| nbody                      | 127 ms                                                          | 114 ms: 1.12x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                           |
| regex_compile              | 129 ms                                                          | 117 ms: 1.10x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 53.4 ms: 1.10x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.1 ms: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 18.7 us: 1.07x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.8 ms: 1.06x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                                          |
| scimark_fft                | 271 ms                                                          | 258 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.19 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.46 ms: 1.05x faster                                                           |
| django_template            | 36.9 ms                                                         | 35.8 ms: 1.03x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 110 ms: 1.03x faster                                                            |
| 2to3                       | 280 ms                                                          | 272 ms: 1.03x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.1 ms: 1.03x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.28 us: 1.03x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.07 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.3 sec: 1.02x faster                                                          |
| sympy_str                  | 240 ms                                                          | 234 ms: 1.02x faster                                                            |
| pycparser                  | 978 ms                                                          | 968 ms: 1.01x faster                                                            |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 102 ms: 1.02x slower                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 73.7 ms: 1.02x slower                                                           |
| sympy_expand               | 398 ms                                                          | 409 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 50.2 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.04x slower                                                           |
| xml_etree_process          | 53.2 ms                                                         | 55.9 ms: 1.05x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.59 sec: 1.06x slower                                                          |
| meteor_contest             | 86.9 ms                                                         | 92.3 ms: 1.06x slower                                                           |
| async_generators           | 313 ms                                                          | 335 ms: 1.07x slower                                                            |
| pprint_safe_repr           | 721 ms                                                          | 773 ms: 1.07x slower                                                            |
| fannkuch                   | 354 ms                                                          | 380 ms: 1.07x slower                                                            |
| unpickle_pure_python       | 210 us                                                          | 226 us: 1.08x slower                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 74.6 ms: 1.08x slower                                                           |
| json                       | 4.15 ms                                                         | 4.52 ms: 1.09x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.09x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| nqueens                    | 93.7 ms                                                         | 106 ms: 1.13x slower                                                            |
| coverage                   | 48.4 ms                                                         | 55.1 ms: 1.14x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 326 us: 1.14x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 758 ms: 1.14x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 21.9 ms: 1.15x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.54 us: 1.22x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.26 ms: 1.25x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.4 ms: 1.27x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.85 ms: 1.29x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 173 us: 1.37x slower                                                            |
| telco                      | 5.51 ms                                                         | 7.89 ms: 1.43x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown