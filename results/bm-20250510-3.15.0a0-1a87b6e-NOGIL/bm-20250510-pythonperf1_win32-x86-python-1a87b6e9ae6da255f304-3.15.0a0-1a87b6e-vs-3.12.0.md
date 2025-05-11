# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.046x faster
- HPT reliability: 98.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 276 ms: 1.01x faster                                                           |
| docutils       | 1.98 sec                                                        | 3.19 sec: 1.61x slower                                                         |
| Geometric mean | (ref)                                                           | 1.26x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 405 ms: 1.67x faster                                                           |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 230 ms: 1.52x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 184 ms: 1.51x faster                                                           |
| async_tree_none            | 298 ms                                                          | 207 ms: 1.44x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 254 ms: 1.43x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.44x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 59.3 ms: 1.29x faster                                                          |
| nbody          | 127 ms                                                          | 114 ms: 1.11x faster                                                           |
| pidigits       | 199 ms                                                          | 190 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                          |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| regex_compile  | 129 ms                                                          | 123 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 206 us: 1.02x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.02x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 77.9 ms: 1.08x slower                                                          |
| pickle_pure_python   | 286 us                                                          | 318 us: 1.11x slower                                                           |
| pickle_list          | 3.37 us                                                         | 4.00 us: 1.19x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.50 us: 1.19x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 24.4 us: 1.23x slower                                                          |
| json_loads           | 20.4 us                                                         | 25.7 us: 1.26x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 9.42 ms: 1.27x slower                                                          |
| pickle               | 7.79 us                                                         | 10.5 us: 1.35x slower                                                          |
| unpickle             | 9.71 us                                                         | 13.2 us: 1.36x slower                                                          |
| tomli_loads          | 2.20 sec                                                        | 3.32 sec: 1.51x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.17x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.9 ms: 1.15x slower                                                          |
| python_startup         | 22.4 ms                                                         | 29.4 ms: 1.31x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 38.2 ms: 1.03x slower                                                          |
| mako            | 9.96 ms                                                         | 12.0 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.4 ms: 2.44x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 405 ms: 1.67x faster                                                           |
| async_tree_io              | 693 ms                                                          | 428 ms: 1.62x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 230 ms: 1.52x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 184 ms: 1.51x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 25.7 us: 1.49x faster                                                          |
| async_tree_none            | 298 ms                                                          | 207 ms: 1.44x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 254 ms: 1.43x faster                                                           |
| generators                 | 38.5 ms                                                         | 28.5 ms: 1.35x faster                                                          |
| deepcopy                   | 360 us                                                          | 273 us: 1.32x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.1 ms: 1.29x faster                                                          |
| float                      | 76.7 ms                                                         | 59.3 ms: 1.29x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.12 ms: 1.28x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.51 sec: 1.27x faster                                                         |
| spectral_norm              | 104 ms                                                          | 83.8 ms: 1.24x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.68 us: 1.23x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.98 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 52.4 ns: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| scimark_sor                | 130 ms                                                          | 110 ms: 1.18x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                          |
| chaos                      | 69.4 ms                                                         | 60.6 ms: 1.15x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 6.01 ms: 1.13x faster                                                          |
| comprehensions             | 19.2 us                                                         | 17.0 us: 1.13x faster                                                          |
| go                         | 137 ms                                                          | 122 ms: 1.13x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 83.5 ms: 1.12x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.7 ms: 1.11x faster                                                          |
| nbody                      | 127 ms                                                          | 114 ms: 1.11x faster                                                           |
| regex_v8                   | 15.0 ms                                                         | 13.7 ms: 1.10x faster                                                          |
| raytrace                   | 308 ms                                                          | 281 ms: 1.10x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 604 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 60.8 ms: 1.09x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.95 us: 1.09x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 53.5 ms: 1.09x faster                                                          |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                           |
| pidigits                   | 199 ms                                                          | 190 ms: 1.05x faster                                                           |
| regex_compile              | 129 ms                                                          | 123 ms: 1.05x faster                                                           |
| pyflate                    | 424 ms                                                          | 407 ms: 1.04x faster                                                           |
| logging_format             | 10.4 us                                                         | 10.2 us: 1.02x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 206 us: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.79 ms: 1.02x faster                                                          |
| logging_simple             | 9.75 us                                                         | 9.58 us: 1.02x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.02x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.01x faster                                                          |
| 2to3                       | 280 ms                                                          | 276 ms: 1.01x faster                                                           |
| scimark_fft                | 271 ms                                                          | 269 ms: 1.01x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 95.4 ms: 1.02x slower                                                          |
| sympy_str                  | 240 ms                                                          | 244 ms: 1.02x slower                                                           |
| async_generators           | 313 ms                                                          | 321 ms: 1.02x slower                                                           |
| django_template            | 36.9 ms                                                         | 38.2 ms: 1.03x slower                                                          |
| xml_etree_process          | 53.2 ms                                                         | 56.5 ms: 1.06x slower                                                          |
| sympy_expand               | 398 ms                                                          | 423 ms: 1.06x slower                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 74.1 ms: 1.07x slower                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 77.9 ms: 1.08x slower                                                          |
| richards                   | 41.3 ms                                                         | 44.7 ms: 1.08x slower                                                          |
| fannkuch                   | 354 ms                                                          | 387 ms: 1.09x slower                                                           |
| richards_super             | 46.5 ms                                                         | 50.9 ms: 1.10x slower                                                          |
| pprint_safe_repr           | 721 ms                                                          | 794 ms: 1.10x slower                                                           |
| meteor_contest             | 86.9 ms                                                         | 96.4 ms: 1.11x slower                                                          |
| pickle_pure_python         | 286 us                                                          | 318 us: 1.11x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 86.6 ms: 1.15x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 21.9 ms: 1.15x slower                                                          |
| json                       | 4.15 ms                                                         | 4.82 ms: 1.16x slower                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.28 ms: 1.16x slower                                                          |
| pickle_list                | 3.37 us                                                         | 4.00 us: 1.19x slower                                                          |
| pycparser                  | 978 ms                                                          | 1.16 sec: 1.19x slower                                                         |
| unpickle_list              | 2.95 us                                                         | 3.50 us: 1.19x slower                                                          |
| mako                       | 9.96 ms                                                         | 12.0 ms: 1.20x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 24.4 us: 1.23x slower                                                          |
| json_loads                 | 20.4 us                                                         | 25.7 us: 1.26x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 9.42 ms: 1.27x slower                                                          |
| telco                      | 5.51 ms                                                         | 7.13 ms: 1.29x slower                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 22.9 sec: 1.29x slower                                                         |
| python_startup             | 22.4 ms                                                         | 29.4 ms: 1.31x slower                                                          |
| pickle                     | 7.79 us                                                         | 10.5 us: 1.35x slower                                                          |
| unpickle                   | 9.71 us                                                         | 13.2 us: 1.36x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 177 us: 1.40x slower                                                           |
| tomli_loads                | 2.20 sec                                                        | 3.32 sec: 1.51x slower                                                         |
| pprint_pformat             | 1.50 sec                                                        | 2.30 sec: 1.53x slower                                                         |
| coverage                   | 48.4 ms                                                         | 76.7 ms: 1.58x slower                                                          |
| docutils                   | 1.98 sec                                                        | 3.19 sec: 1.61x slower                                                         |
| create_gc_cycles           | 652 us                                                          | 1.09 ms: 1.67x slower                                                          |
| logging_silent             | 101 ns                                                          | 425 ns: 4.21x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): sympy_sum
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 98.20% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown