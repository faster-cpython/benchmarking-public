# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.523x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 386 ms: 1.80x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 389 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.8 ms: 2.27x faster                                                            |
| float          | 76.7 ms                                                         | 44.4 ms: 1.73x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.2 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.10 sec: 2.00x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 107 us: 1.97x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 34.9 ms: 1.52x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 49.1 ms: 1.47x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 201 us: 1.42x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 85.3 ms: 1.33x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.57 us: 1.13x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.72 us: 1.08x faster                                                            |
| pickle               | 7.79 us                                                         | 7.42 us: 1.05x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.0 us: 1.05x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                            |
| django_template | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.69x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.35 sec: 13.06x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.5 ms: 3.10x faster                                                            |
| mdp                        | 1.91 sec                                                        | 791 ms: 2.42x faster                                                             |
| nbody                      | 127 ms                                                          | 55.8 ms: 2.27x faster                                                            |
| deepcopy                   | 360 us                                                          | 171 us: 2.11x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.10 sec: 2.00x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.3 ms: 2.00x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 107 us: 1.97x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.9 us: 1.92x faster                                                            |
| logging_silent             | 101 ns                                                          | 53.6 ns: 1.88x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.4 us: 1.85x faster                                                            |
| scimark_fft                | 271 ms                                                          | 147 ms: 1.84x faster                                                             |
| async_tree_io              | 693 ms                                                          | 386 ms: 1.80x faster                                                             |
| go                         | 137 ms                                                          | 77.5 ms: 1.77x faster                                                            |
| raytrace                   | 308 ms                                                          | 174 ms: 1.77x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 206 ms: 1.77x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.83 us: 1.76x faster                                                            |
| fannkuch                   | 354 ms                                                          | 201 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 169 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 389 ms: 1.74x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.0 ms: 1.74x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 36.0 ns: 1.73x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 868 ms: 1.73x faster                                                             |
| float                      | 76.7 ms                                                         | 44.4 ms: 1.73x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.25 ms: 1.72x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 330 ms: 1.71x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 429 ms: 1.68x faster                                                             |
| spectral_norm              | 104 ms                                                          | 61.9 ms: 1.68x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 210 ms: 1.67x faster                                                             |
| scimark_sor                | 130 ms                                                          | 77.8 ms: 1.67x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.1 ms: 1.66x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.2 ms: 1.65x faster                                                            |
| logging_simple             | 9.75 us                                                         | 5.92 us: 1.65x faster                                                            |
| pyflate                    | 424 ms                                                          | 257 ms: 1.65x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.15 ms: 1.64x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.20 ms: 1.63x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.39 us: 1.63x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 58.9 ms: 1.59x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.7 ms: 1.56x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 44.6 ms: 1.55x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.0 ms: 1.54x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.0 ms: 1.53x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 34.9 ms: 1.52x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.7 ms: 1.51x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| telco                      | 5.51 ms                                                         | 3.75 ms: 1.47x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 49.1 ms: 1.47x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.0 us: 1.45x faster                                                            |
| json                       | 4.15 ms                                                         | 2.88 ms: 1.44x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 85.4 ms: 1.44x faster                                                            |
| sympy_str                  | 240 ms                                                          | 168 ms: 1.43x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 201 us: 1.42x faster                                                             |
| pycparser                  | 978 ms                                                          | 688 ms: 1.42x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 467 ms: 1.42x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 5.36 ms: 1.38x faster                                                            |
| sympy_expand               | 398 ms                                                          | 289 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.55 us: 1.34x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.53 ms: 1.33x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 85.3 ms: 1.33x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 843 us: 1.31x faster                                                             |
| async_generators           | 313 ms                                                          | 242 ms: 1.30x faster                                                             |
| 2to3                       | 280 ms                                                          | 217 ms: 1.29x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.1 ms: 1.27x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 102 us: 1.24x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.61 sec: 1.23x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 71.2 ms: 1.22x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.57 us: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.72 us: 1.08x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.42 us: 1.05x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.0 us: 1.05x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.27 us: 1.03x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.4 ms: 1.02x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 92.6 ms: 1.23x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.47x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.27 ms: 1.94x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.52x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.523x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.53x
- 95% likely to have a speedup of 1.52x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown