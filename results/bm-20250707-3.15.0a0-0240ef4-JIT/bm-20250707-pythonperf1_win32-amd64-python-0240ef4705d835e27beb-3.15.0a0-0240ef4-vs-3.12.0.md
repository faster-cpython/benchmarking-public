# Results vs. 3.12.0

- fork: python
- ref: 0240ef4705d835e27beb
- machine: windows-amd64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.505x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.65 sec: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                             |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 394 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.7 ms: 2.36x faster                                                            |
| float          | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.2 ms: 1.65x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.13 sec: 1.95x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 108 us: 1.94x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 34.9 ms: 1.52x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 49.9 ms: 1.45x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.5 us: 1.41x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 205 us: 1.39x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 86.1 ms: 1.31x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.32 ms: 1.17x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.47x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                            |
| django_template | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.66x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 29.1 ms: 3.15x faster                                                            |
| mdp                        | 1.91 sec                                                        | 793 ms: 2.41x faster                                                             |
| nbody                      | 127 ms                                                          | 53.7 ms: 2.36x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 18.0 us: 2.14x faster                                                            |
| deepcopy                   | 360 us                                                          | 170 us: 2.12x faster                                                             |
| generators                 | 38.5 ms                                                         | 19.4 ms: 1.98x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.13 sec: 1.95x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 108 us: 1.94x faster                                                             |
| logging_silent             | 101 ns                                                          | 54.4 ns: 1.86x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.84x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.46 ms: 1.82x faster                                                            |
| go                         | 137 ms                                                          | 76.2 ms: 1.80x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.78x faster                                                             |
| scimark_fft                | 271 ms                                                          | 152 ms: 1.78x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.82 us: 1.77x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 383 ms: 1.77x faster                                                             |
| float                      | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 394 ms: 1.76x faster                                                             |
| chaos                      | 69.4 ms                                                         | 39.9 ms: 1.74x faster                                                            |
| scimark_sor                | 130 ms                                                          | 75.3 ms: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 179 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.13 ms: 1.68x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.29 ms: 1.68x faster                                                            |
| pyflate                    | 424 ms                                                          | 252 ms: 1.68x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.09 ms: 1.67x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.2 ms: 1.65x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 169 ms: 1.65x faster                                                             |
| spectral_norm              | 104 ms                                                          | 63.5 ms: 1.63x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.8 ms: 1.63x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 923 ms: 1.62x faster                                                             |
| fannkuch                   | 354 ms                                                          | 219 ms: 1.62x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 447 ms: 1.61x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 341 ms: 1.60x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 58.5 ms: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.19 us: 1.58x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.69 us: 1.55x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.7 ms: 1.55x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.4 ms: 1.53x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 61.1 ms: 1.53x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 34.9 ms: 1.52x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 45.8 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 49.9 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.5 ms: 1.44x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.8 ms: 1.43x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 87.0 ms: 1.41x faster                                                            |
| sympy_str                  | 240 ms                                                          | 170 ms: 1.41x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.5 us: 1.41x faster                                                            |
| pycparser                  | 978 ms                                                          | 698 ms: 1.40x faster                                                             |
| json                       | 4.15 ms                                                         | 2.97 ms: 1.40x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 205 us: 1.39x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| sympy_expand               | 398 ms                                                          | 294 ms: 1.36x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 86.1 ms: 1.31x faster                                                            |
| 2to3                       | 280 ms                                                          | 216 ms: 1.29x faster                                                             |
| async_generators           | 313 ms                                                          | 243 ms: 1.29x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.58 ms: 1.29x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.30 ms: 1.28x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 71.1 ms: 1.22x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.65 sec: 1.20x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 106 us: 1.19x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.32 ms: 1.17x faster                                                            |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                            |
| coverage                   | 48.4 ms                                                         | 50.6 ms: 1.05x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.6 ms: 1.15x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.31 ms: 2.02x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.51x faster                                                                     |
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-pythonperf1_win32-amd64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.505x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.50x
- 99% likely to have a speedup of 1.46x

# Memory
- memory change: unknown