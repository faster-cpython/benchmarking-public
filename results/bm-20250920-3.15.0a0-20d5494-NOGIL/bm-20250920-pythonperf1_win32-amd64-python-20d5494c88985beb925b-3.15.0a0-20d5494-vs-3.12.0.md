# Results vs. 3.12.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| docutils       | 1.98 sec                                                        | 2.90 sec: 1.46x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 334 ms: 2.03x faster                                                             |
| async_tree_io              | 693 ms                                                          | 359 ms: 1.93x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 149 ms: 1.86x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 192 ms: 1.82x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 312 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 214 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.69x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 46.5 ms: 1.65x faster                                                            |
| nbody          | 127 ms                                                          | 82.1 ms: 1.55x faster                                                            |
| pidigits       | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 1.55x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 93.9 ms: 1.37x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                            |
| regex_dna      | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.4 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                             |
| json_loads           | 20.4 us                                                         | 15.9 us: 1.28x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 91.3 ms: 1.24x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 236 us: 1.21x faster                                                             |
| json_dumps           | 7.40 ms                                                         | 6.28 ms: 1.18x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 45.9 ms: 1.16x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.03 us: 1.11x faster                                                            |
| pickle               | 7.79 us                                                         | 7.94 us: 1.02x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                            |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| tomli_loads          | 2.20 sec                                                        | 2.41 sec: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.9 ms                                                         | 27.2 ms: 1.36x faster                                                            |
| mako            | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 2.17 sec: 8.15x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 29.7 ms: 3.08x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 334 ms: 2.03x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 19.4 us: 1.98x faster                                                            |
| async_tree_io              | 693 ms                                                          | 359 ms: 1.93x faster                                                             |
| deepcopy                   | 360 us                                                          | 190 us: 1.89x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 149 ms: 1.86x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 192 ms: 1.82x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 312 ms: 1.75x faster                                                             |
| async_tree_none            | 298 ms                                                          | 172 ms: 1.73x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 214 ms: 1.70x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 333 ms: 1.69x faster                                                             |
| mdp                        | 1.91 sec                                                        | 1.13 sec: 1.69x faster                                                           |
| float                      | 76.7 ms                                                         | 46.5 ms: 1.65x faster                                                            |
| logging_silent             | 101 ns                                                          | 61.9 ns: 1.63x faster                                                            |
| generators                 | 38.5 ms                                                         | 23.6 ms: 1.63x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.60x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 40.2 ns: 1.55x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.08 us: 1.55x faster                                                            |
| nbody                      | 127 ms                                                          | 82.1 ms: 1.55x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.36 us: 1.52x faster                                                            |
| go                         | 137 ms                                                          | 91.2 ms: 1.51x faster                                                            |
| chaos                      | 69.4 ms                                                         | 46.4 ms: 1.49x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 62.8 ms: 1.48x faster                                                            |
| scimark_sor                | 130 ms                                                          | 88.0 ms: 1.47x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.63 ms: 1.47x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 451 ms: 1.47x faster                                                             |
| pidigits                   | 199 ms                                                          | 136 ms: 1.46x faster                                                             |
| raytrace                   | 308 ms                                                          | 213 ms: 1.45x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.49 ms: 1.44x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.78 us: 1.44x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.27 us: 1.43x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 42.2 ms: 1.39x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 15.1 ms: 1.38x faster                                                            |
| regex_compile              | 129 ms                                                          | 93.9 ms: 1.37x faster                                                            |
| spectral_norm              | 104 ms                                                          | 75.5 ms: 1.37x faster                                                            |
| pyflate                    | 424 ms                                                          | 311 ms: 1.36x faster                                                             |
| django_template            | 36.9 ms                                                         | 27.2 ms: 1.36x faster                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.6 ms: 1.34x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                             |
| json                       | 4.15 ms                                                         | 3.13 ms: 1.33x faster                                                            |
| pycparser                  | 978 ms                                                          | 741 ms: 1.32x faster                                                             |
| pprint_safe_repr           | 721 ms                                                          | 558 ms: 1.29x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 73.0 ms: 1.28x faster                                                            |
| json_loads                 | 20.4 us                                                         | 15.9 us: 1.28x faster                                                            |
| scimark_fft                | 271 ms                                                          | 213 ms: 1.27x faster                                                             |
| sympy_str                  | 240 ms                                                          | 189 ms: 1.27x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 97.2 ms: 1.26x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 61.7 ms: 1.26x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.16 ms: 1.24x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 91.3 ms: 1.24x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.65 ms: 1.23x faster                                                            |
| 2to3                       | 280 ms                                                          | 228 ms: 1.23x faster                                                             |
| sympy_expand               | 398 ms                                                          | 324 ms: 1.23x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 14.3 ms: 1.23x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.6 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.16 ms: 1.22x faster                                                            |
| richards                   | 41.3 ms                                                         | 34.1 ms: 1.21x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 236 us: 1.21x faster                                                             |
| async_generators           | 313 ms                                                          | 264 ms: 1.19x faster                                                             |
| json_dumps                 | 7.40 ms                                                         | 6.28 ms: 1.18x faster                                                            |
| richards_super             | 46.5 ms                                                         | 39.8 ms: 1.17x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 45.9 ms: 1.16x faster                                                            |
| fannkuch                   | 354 ms                                                          | 310 ms: 1.14x faster                                                             |
| regex_dna                  | 127 ms                                                          | 112 ms: 1.13x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 64.0 ms: 1.13x faster                                                            |
| regex_v8                   | 15.0 ms                                                         | 13.4 ms: 1.12x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.03 us: 1.11x faster                                                            |
| telco                      | 5.51 ms                                                         | 5.03 ms: 1.10x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 85.6 ms: 1.01x faster                                                            |
| mako                       | 9.96 ms                                                         | 10.1 ms: 1.01x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.94 us: 1.02x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 132 us: 1.04x slower                                                             |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.10 us: 1.05x slower                                                            |
| tomli_loads                | 2.20 sec                                                        | 2.41 sec: 1.10x slower                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.69 sec: 1.13x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| coverage                   | 48.4 ms                                                         | 70.4 ms: 1.45x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.90 sec: 1.46x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.02 ms: 1.56x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                     |

Benchmark hidden because not significant (3): bench_mp_pool, bench_thread_pool, python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown