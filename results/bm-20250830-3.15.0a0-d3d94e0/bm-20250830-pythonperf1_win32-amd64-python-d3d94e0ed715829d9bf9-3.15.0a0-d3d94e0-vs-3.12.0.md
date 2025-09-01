# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 384 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 391 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 171 ms: 1.62x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.5 ms: 1.94x faster                                                            |
| float          | 76.7 ms                                                         | 44.4 ms: 1.73x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                           | 1.66x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 80.8 ms: 1.60x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 140 us: 1.50x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 5.45 ms: 1.36x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 39.8 ms: 1.34x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 218 us: 1.31x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 87.8 ms: 1.29x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.53 us: 1.14x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| pickle               | 7.79 us                                                         | 8.12 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| mako            | 9.96 ms                                                         | 6.79 ms: 1.47x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.49x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.32 sec: 13.42x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 29.8 ms: 3.07x faster                                                            |
| mdp                        | 1.91 sec                                                        | 815 ms: 2.35x faster                                                             |
| deepcopy                   | 360 us                                                          | 173 us: 2.08x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.1 ms: 2.01x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 19.5 us: 1.97x faster                                                            |
| nbody                      | 127 ms                                                          | 65.5 ms: 1.94x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 33.0 ns: 1.90x faster                                                            |
| async_tree_io              | 693 ms                                                          | 384 ms: 1.81x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| go                         | 137 ms                                                          | 77.5 ms: 1.77x faster                                                            |
| logging_silent             | 101 ns                                                          | 57.3 ns: 1.76x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                            |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 391 ms: 1.73x faster                                                             |
| float                      | 76.7 ms                                                         | 44.4 ms: 1.73x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 326 ms: 1.73x faster                                                             |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| async_tree_none            | 298 ms                                                          | 174 ms: 1.71x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.0 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| scimark_sor                | 130 ms                                                          | 78.0 ms: 1.66x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.14 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 332 ms: 1.65x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 171 ms: 1.62x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.0 ms: 1.62x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.47 us: 1.61x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                            |
| spectral_norm              | 104 ms                                                          | 64.8 ms: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.10 us: 1.60x faster                                                            |
| regex_compile              | 129 ms                                                          | 80.8 ms: 1.60x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.4 ms: 1.60x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 61.1 ms: 1.53x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 140 us: 1.50x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.58 ms: 1.49x faster                                                            |
| scimark_fft                | 271 ms                                                          | 181 ms: 1.49x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 446 ms: 1.48x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.4 ms: 1.48x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.79 ms: 1.47x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.1 ms: 1.46x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 47.4 ms: 1.46x faster                                                            |
| richards                   | 41.3 ms                                                         | 28.4 ms: 1.45x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.03 sec: 1.45x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 506 ms: 1.42x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| pyflate                    | 424 ms                                                          | 298 ms: 1.42x faster                                                             |
| sympy_str                  | 240 ms                                                          | 169 ms: 1.42x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.8 ms: 1.40x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| json                       | 4.15 ms                                                         | 2.99 ms: 1.39x faster                                                            |
| sympy_expand               | 398 ms                                                          | 287 ms: 1.39x faster                                                             |
| async_generators           | 313 ms                                                          | 226 ms: 1.38x faster                                                             |
| pidigits                   | 199 ms                                                          | 145 ms: 1.38x faster                                                             |
| pycparser                  | 978 ms                                                          | 711 ms: 1.38x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 5.45 ms: 1.36x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.52 ms: 1.34x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 39.8 ms: 1.34x faster                                                            |
| fannkuch                   | 354 ms                                                          | 267 ms: 1.33x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.16 ms: 1.32x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 218 us: 1.31x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.60 us: 1.29x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 87.8 ms: 1.29x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 856 us: 1.29x faster                                                             |
| 2to3                       | 280 ms                                                          | 218 ms: 1.28x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 56.9 ms: 1.27x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.23x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.21x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.7 ms: 1.20x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 72.6 ms: 1.20x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.53 us: 1.14x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.3 ms: 1.13x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.83 us: 1.04x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.32 us: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.7 us: 1.01x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.03x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.12 us: 1.04x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 93.3 ms: 1.24x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.09 ms: 1.45x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.29 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown