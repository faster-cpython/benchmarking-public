# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 270 ms: 1.04x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 491 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 488 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 268 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 283 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 479 ms: 1.14x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.9 ms: 1.35x faster                                                           |
| float          | 76.7 ms                                                         | 59.8 ms: 1.28x faster                                                           |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| regex_compile  | 129 ms                                                          | 110 ms: 1.18x faster                                                            |
| regex_dna      | 127 ms                                                          | 125 ms: 1.02x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 184 us: 1.14x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 50.8 ms: 1.05x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| pickle_pure_python   | 286 us                                                          | 297 us: 1.04x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.76 us: 1.12x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.3 us: 1.16x slower                                                           |
| pickle               | 7.79 us                                                         | 9.66 us: 1.24x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.21 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| python_startup         | 22.4 ms                                                         | 28.9 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.22x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.13 ms: 1.22x faster                                                           |
| django_template | 36.9 ms                                                         | 37.9 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.4 us: 1.71x faster                                                           |
| async_tree_io              | 693 ms                                                          | 491 ms: 1.41x faster                                                            |
| deepcopy                   | 360 us                                                          | 258 us: 1.40x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 44.7 ns: 1.40x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 488 ms: 1.39x faster                                                            |
| generators                 | 38.5 ms                                                         | 28.1 ms: 1.37x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 67.5 ms: 1.35x faster                                                           |
| nbody                      | 127 ms                                                          | 93.9 ms: 1.35x faster                                                           |
| spectral_norm              | 104 ms                                                          | 76.9 ms: 1.35x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.88 ms: 1.34x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 69.8 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 268 ms: 1.31x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 214 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 283 ms: 1.28x faster                                                            |
| float                      | 76.7 ms                                                         | 59.8 ms: 1.28x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.3 ms: 1.28x faster                                                           |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.74 sec: 1.26x faster                                                          |
| scimark_fft                | 271 ms                                                          | 219 ms: 1.24x faster                                                            |
| logging_silent             | 101 ns                                                          | 81.6 ns: 1.24x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.55 ms: 1.23x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.13 ms: 1.22x faster                                                           |
| scimark_sor                | 130 ms                                                          | 107 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.71 us: 1.19x faster                                                           |
| fannkuch                   | 354 ms                                                          | 297 ms: 1.19x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.1 ms: 1.18x faster                                                           |
| go                         | 137 ms                                                          | 116 ms: 1.18x faster                                                            |
| regex_compile              | 129 ms                                                          | 110 ms: 1.18x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 3.05 ms: 1.18x faster                                                           |
| pyflate                    | 424 ms                                                          | 361 ms: 1.17x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 79.7 ms: 1.17x faster                                                           |
| chaos                      | 69.4 ms                                                         | 59.3 ms: 1.17x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 184 us: 1.14x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 479 ms: 1.14x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 61.4 ms: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 78.3 ms: 1.11x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.80 us: 1.11x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.40 us: 1.11x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 53.2 ms: 1.10x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                            |
| pycparser                  | 978 ms                                                          | 901 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.7 ms: 1.07x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.44 ms: 1.06x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.5 ms: 1.06x faster                                                           |
| raytrace                   | 308 ms                                                          | 290 ms: 1.06x faster                                                            |
| sympy_str                  | 240 ms                                                          | 226 ms: 1.06x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.8 ms: 1.05x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.19 ms: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.06 ms: 1.04x faster                                                           |
| 2to3                       | 280 ms                                                          | 270 ms: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 47.3 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 709 ms: 1.02x faster                                                            |
| regex_dna                  | 127 ms                                                          | 125 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.48 sec: 1.01x faster                                                          |
| sympy_expand               | 398 ms                                                          | 395 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                            |
| richards_super             | 46.5 ms                                                         | 47.5 ms: 1.02x slower                                                           |
| richards                   | 41.3 ms                                                         | 42.4 ms: 1.03x slower                                                           |
| django_template            | 36.9 ms                                                         | 37.9 ms: 1.03x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| pickle_pure_python         | 286 us                                                          | 297 us: 1.04x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 711 ms: 1.07x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                           |
| coverage                   | 48.4 ms                                                         | 52.9 ms: 1.09x slower                                                           |
| json                       | 4.15 ms                                                         | 4.56 ms: 1.10x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.4 us: 1.10x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.76 us: 1.12x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 22.1 ms: 1.16x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.3 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 154 us: 1.22x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.66 us: 1.24x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 9.21 ms: 1.24x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.79 ms: 1.24x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 95.5 ms: 1.27x slower                                                           |
| python_startup             | 22.4 ms                                                         | 28.9 ms: 1.29x slower                                                           |
| telco                      | 5.51 ms                                                         | 7.24 ms: 1.31x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 246 ms: 2.45x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                    |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (13) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown