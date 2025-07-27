# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.478x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.43x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 225 ms: 1.24x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.67 sec: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| async_tree_io              | 693 ms                                                          | 401 ms: 1.73x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| async_tree_none            | 298 ms                                                          | 178 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 338 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 353 ms: 1.55x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.68x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 57.7 ms: 2.20x faster                                                            |
| float          | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| pidigits       | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                           | 1.74x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.7 ms: 1.62x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                            |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 108 us: 1.95x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.13 sec: 1.94x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.9 ms: 1.48x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 52.4 ms: 1.38x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 208 us: 1.37x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 88.8 ms: 1.27x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.36 ms: 1.16x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.90 us: 1.09x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.43 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmark hidden because not significant (3): unpickle_list, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.32 ms: 1.87x faster                                                            |
| django_template | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.42 sec: 12.40x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 32.8 ms: 2.79x faster                                                            |
| mdp                        | 1.91 sec                                                        | 797 ms: 2.40x faster                                                             |
| nbody                      | 127 ms                                                          | 57.7 ms: 2.20x faster                                                            |
| deepcopy                   | 360 us                                                          | 169 us: 2.13x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.2 us: 2.11x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 108 us: 1.95x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.13 sec: 1.94x faster                                                           |
| generators                 | 38.5 ms                                                         | 20.1 ms: 1.91x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.32 ms: 1.87x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 33.7 ns: 1.85x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.4 us: 1.85x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.2 ns: 1.83x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 203 ms: 1.79x faster                                                             |
| float                      | 76.7 ms                                                         | 43.1 ms: 1.78x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 1.81 us: 1.78x faster                                                            |
| scimark_fft                | 271 ms                                                          | 154 ms: 1.75x faster                                                             |
| async_tree_io              | 693 ms                                                          | 401 ms: 1.73x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 393 ms: 1.72x faster                                                             |
| go                         | 137 ms                                                          | 79.7 ms: 1.72x faster                                                            |
| chaos                      | 69.4 ms                                                         | 40.3 ms: 1.72x faster                                                            |
| raytrace                   | 308 ms                                                          | 183 ms: 1.69x faster                                                             |
| scimark_sor                | 130 ms                                                          | 77.3 ms: 1.68x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.30 ms: 1.68x faster                                                            |
| async_tree_none            | 298 ms                                                          | 178 ms: 1.67x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 338 ms: 1.67x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 212 ms: 1.65x faster                                                             |
| fannkuch                   | 354 ms                                                          | 215 ms: 1.65x faster                                                             |
| pprint_pformat             | 1.50 sec                                                        | 911 ms: 1.65x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.16 ms: 1.64x faster                                                            |
| pyflate                    | 424 ms                                                          | 260 ms: 1.63x faster                                                             |
| regex_compile              | 129 ms                                                          | 79.7 ms: 1.62x faster                                                            |
| spectral_norm              | 104 ms                                                          | 64.1 ms: 1.62x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.61x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.49 us: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.10 us: 1.60x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 42.3 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 353 ms: 1.55x faster                                                             |
| scimark_lu                 | 93.2 ms                                                         | 60.4 ms: 1.54x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 60.7 ms: 1.54x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 469 ms: 1.54x faster                                                             |
| django_template            | 36.9 ms                                                         | 24.5 ms: 1.51x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 46.1 ms: 1.50x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.7 ms: 1.49x faster                                                            |
| richards_super             | 46.5 ms                                                         | 31.3 ms: 1.48x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.9 ms: 1.48x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.6 ms: 1.43x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.3 us: 1.42x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 41.4 ms: 1.41x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 88.3 ms: 1.39x faster                                                            |
| pycparser                  | 978 ms                                                          | 703 ms: 1.39x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 52.4 ms: 1.38x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 208 us: 1.37x faster                                                             |
| json                       | 4.15 ms                                                         | 3.05 ms: 1.36x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 12.9 ms: 1.36x faster                                                            |
| sympy_str                  | 240 ms                                                          | 178 ms: 1.35x faster                                                             |
| pidigits                   | 199 ms                                                          | 149 ms: 1.34x faster                                                             |
| sympy_expand               | 398 ms                                                          | 305 ms: 1.30x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 853 us: 1.29x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 519 ms: 1.28x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 88.8 ms: 1.27x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.63 us: 1.27x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.43 ms: 1.24x faster                                                            |
| 2to3                       | 280 ms                                                          | 225 ms: 1.24x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.8 ms: 1.24x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                            |
| async_generators           | 313 ms                                                          | 255 ms: 1.23x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 71.4 ms: 1.22x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.21x faster                                                             |
| docutils                   | 1.98 sec                                                        | 1.67 sec: 1.19x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.36 ms: 1.16x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.90 us: 1.09x faster                                                            |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.6 ms: 1.03x faster                                                            |
| coverage                   | 48.4 ms                                                         | 49.0 ms: 1.01x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.43 us: 1.02x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 95.9 ms: 1.27x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.16 ms: 1.50x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.33 ms: 2.04x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                     |

Benchmark hidden because not significant (3): unpickle_list, pickle, pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.478x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.51x
- 95% likely to have a speedup of 1.48x
- 99% likely to have a speedup of 1.43x

# Memory
- memory change: unknown