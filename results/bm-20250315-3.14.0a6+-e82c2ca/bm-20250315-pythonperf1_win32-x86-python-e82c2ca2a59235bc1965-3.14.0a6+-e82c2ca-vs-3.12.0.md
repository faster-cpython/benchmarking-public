# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-x86
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 462 ms: 1.47x faster                                                            |
| async_tree_io              | 693 ms                                                          | 481 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 82.5 ms: 1.54x faster                                                           |
| float          | 76.7 ms                                                         | 54.9 ms: 1.40x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| regex_compile  | 129 ms                                                          | 109 ms: 1.19x faster                                                            |
| regex_dna      | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.78 sec: 1.23x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.3 ms: 1.17x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 182 us: 1.15x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 291 us: 1.02x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.3 us: 1.07x slower                                                           |
| json_loads           | 20.4 us                                                         | 22.2 us: 1.09x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.48 ms: 1.15x slower                                                           |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.16x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.90 us: 1.16x slower                                                           |
| pickle               | 7.79 us                                                         | 9.14 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 22.8 ms: 1.19x slower                                                           |
| python_startup         | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                           |
| django_template | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 37.9 ms: 2.41x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 21.5 us: 1.79x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 39.7 ns: 1.57x faster                                                           |
| generators                 | 38.5 ms                                                         | 25.0 ms: 1.54x faster                                                           |
| nbody                      | 127 ms                                                          | 82.5 ms: 1.54x faster                                                           |
| logging_silent             | 101 ns                                                          | 67.3 ns: 1.50x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 462 ms: 1.47x faster                                                            |
| deepcopy                   | 360 us                                                          | 249 us: 1.45x faster                                                            |
| async_tree_io              | 693 ms                                                          | 481 ms: 1.44x faster                                                            |
| spectral_norm              | 104 ms                                                          | 72.9 ms: 1.42x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 66.4 ms: 1.40x faster                                                           |
| float                      | 76.7 ms                                                         | 54.9 ms: 1.40x faster                                                           |
| scimark_sor                | 130 ms                                                          | 93.5 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 269 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 224 ms: 1.33x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 5.21 ms: 1.31x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.7 us: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.79 ms: 1.29x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.6 ms: 1.26x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 53.1 ms: 1.25x faster                                                           |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.78 sec: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.18 ms: 1.22x faster                                                           |
| regex_compile              | 129 ms                                                          | 109 ms: 1.19x faster                                                            |
| pyflate                    | 424 ms                                                          | 357 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 461 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.74 us: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.3 ms: 1.17x faster                                                           |
| scimark_fft                | 271 ms                                                          | 231 ms: 1.17x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.32 ms: 1.16x faster                                                           |
| raytrace                   | 308 ms                                                          | 266 ms: 1.16x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 182 us: 1.15x faster                                                            |
| chaos                      | 69.4 ms                                                         | 60.9 ms: 1.14x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 52.1 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.79 us: 1.11x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 84.6 ms: 1.11x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.11x faster                                                            |
| fannkuch                   | 354 ms                                                          | 321 ms: 1.10x faster                                                            |
| richards                   | 41.3 ms                                                         | 37.5 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.37 sec: 1.10x faster                                                          |
| richards_super             | 46.5 ms                                                         | 42.7 ms: 1.09x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.2 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 667 ms: 1.08x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.67 us: 1.08x faster                                                           |
| sympy_str                  | 240 ms                                                          | 225 ms: 1.06x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 66.1 ms: 1.05x faster                                                           |
| django_template            | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                           |
| pycparser                  | 978 ms                                                          | 939 ms: 1.04x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 84.9 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.3 sec: 1.02x faster                                                          |
| regex_dna                  | 127 ms                                                          | 126 ms: 1.01x faster                                                            |
| async_generators           | 313 ms                                                          | 311 ms: 1.01x faster                                                            |
| sympy_expand               | 398 ms                                                          | 401 ms: 1.01x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 291 us: 1.02x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 15.3 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.03x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.3 us: 1.07x slower                                                           |
| json_loads                 | 20.4 us                                                         | 22.2 us: 1.09x slower                                                           |
| json                       | 4.15 ms                                                         | 4.56 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.3 ms: 1.10x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.48 ms: 1.15x slower                                                           |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.16x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.90 us: 1.16x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.29 ms: 1.17x slower                                                           |
| pickle                     | 7.79 us                                                         | 9.14 us: 1.17x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 150 us: 1.19x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 22.8 ms: 1.19x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.25x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.92 ms: 1.26x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 96.0 ms: 1.27x slower                                                           |
| python_startup             | 22.4 ms                                                         | 29.0 ms: 1.30x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.06 ms: 1.63x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_process, xml_etree_generate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1_win32-x86-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown