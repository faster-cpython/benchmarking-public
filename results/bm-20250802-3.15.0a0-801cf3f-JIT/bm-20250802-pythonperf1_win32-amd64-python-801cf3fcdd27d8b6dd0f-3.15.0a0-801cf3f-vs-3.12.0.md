# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 224 ms: 1.25x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.67 sec: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_io              | 693 ms                                                          | 401 ms: 1.73x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 396 ms: 1.71x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 340 ms: 1.66x faster                                                             |
| async_tree_none            | 298 ms                                                          | 181 ms: 1.64x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 216 ms: 1.63x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 171 ms: 1.63x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 353 ms: 1.55x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.66x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.3 ms: 2.30x faster                                                            |
| float          | 76.7 ms                                                         | 44.3 ms: 1.73x faster                                                            |
| pidigits       | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 82.4 ms: 1.57x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.70 ms: 1.20x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 108 us: 1.95x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.14 sec: 1.92x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.9 ms: 1.48x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 51.0 ms: 1.41x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.7 us: 1.39x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 210 us: 1.36x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 89.3 ms: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.38 ms: 1.16x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.85 us: 1.10x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.90 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 26.5 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                            |
| django_template | 36.9 ms                                                         | 26.0 ms: 1.42x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.63x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.44 sec: 12.23x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 33.5 ms: 2.73x faster                                                            |
| mdp                        | 1.91 sec                                                        | 807 ms: 2.37x faster                                                             |
| nbody                      | 127 ms                                                          | 55.3 ms: 2.30x faster                                                            |
| deepcopy                   | 360 us                                                          | 179 us: 2.02x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.2 us: 2.00x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.8 ms: 1.95x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 108 us: 1.95x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.14 sec: 1.92x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                            |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.82x faster                                                             |
| logging_silent             | 101 ns                                                          | 56.4 ns: 1.79x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| float                      | 76.7 ms                                                         | 44.3 ms: 1.73x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 210 ms: 1.73x faster                                                             |
| async_tree_io              | 693 ms                                                          | 401 ms: 1.73x faster                                                             |
| go                         | 137 ms                                                          | 79.5 ms: 1.73x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 396 ms: 1.71x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.28 ms: 1.69x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.92 us: 1.68x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 37.4 ns: 1.67x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 340 ms: 1.66x faster                                                             |
| fannkuch                   | 354 ms                                                          | 214 ms: 1.65x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.9 ms: 1.65x faster                                                            |
| scimark_sor                | 130 ms                                                          | 78.5 ms: 1.65x faster                                                            |
| async_tree_none            | 298 ms                                                          | 181 ms: 1.64x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 919 ms: 1.63x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.7 ms: 1.63x faster                                                            |
| raytrace                   | 308 ms                                                          | 189 ms: 1.63x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 216 ms: 1.63x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 171 ms: 1.63x faster                                                             |
| spectral_norm              | 104 ms                                                          | 65.0 ms: 1.60x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.28 ms: 1.59x faster                                                            |
| pyflate                    | 424 ms                                                          | 267 ms: 1.59x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 456 ms: 1.58x faster                                                             |
| regex_compile              | 129 ms                                                          | 82.4 ms: 1.57x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 59.9 ms: 1.56x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 353 ms: 1.55x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.32 us: 1.54x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.34 ms: 1.53x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.85 us: 1.52x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 62.1 ms: 1.51x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.9 ms: 1.48x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.9 ms: 1.48x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.5 ms: 1.48x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 47.8 ms: 1.45x faster                                                            |
| django_template            | 36.9 ms                                                         | 26.0 ms: 1.42x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.8 ms: 1.41x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 51.0 ms: 1.41x faster                                                            |
| pycparser                  | 978 ms                                                          | 703 ms: 1.39x faster                                                             |
| json_loads                 | 20.4 us                                                         | 14.7 us: 1.39x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.2 ms: 1.38x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 89.8 ms: 1.37x faster                                                            |
| sympy_str                  | 240 ms                                                          | 175 ms: 1.37x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 210 us: 1.36x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 13.0 ms: 1.35x faster                                                            |
| pidigits                   | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 502 ms: 1.32x faster                                                             |
| sympy_expand               | 398 ms                                                          | 303 ms: 1.31x faster                                                             |
| json                       | 4.15 ms                                                         | 3.17 ms: 1.31x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.60 us: 1.29x faster                                                            |
| async_generators           | 313 ms                                                          | 244 ms: 1.28x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 870 us: 1.27x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 89.3 ms: 1.27x faster                                                            |
| 2to3                       | 280 ms                                                          | 224 ms: 1.25x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.4 ms: 1.22x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.70 ms: 1.20x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 73.1 ms: 1.19x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.67 sec: 1.19x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 107 us: 1.18x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.68 ms: 1.18x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.38 ms: 1.16x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.85 us: 1.10x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                             |
| unpickle_list              | 2.95 us                                                         | 2.90 us: 1.02x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                            |
| python_startup             | 22.4 ms                                                         | 26.5 ms: 1.19x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 96.6 ms: 1.28x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.21 ms: 1.53x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.36 ms: 2.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                     |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, pickle
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.48x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown