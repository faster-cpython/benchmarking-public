# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.045x faster
- HPT reliability: 98.92%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 288 ms: 1.03x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.11 sec: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 433 ms: 1.30x faster                                                             |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                             |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 288 ms: 1.26x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 285 ms: 1.23x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 229 ms: 1.21x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.4 ms: 2.38x faster                                                            |
| pidigits       | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| float          | 76.7 ms                                                         | 78.5 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.47x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.74 ms: 1.17x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| regex_compile  | 129 ms                                                          | 122 ms: 1.06x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.7 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                             |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                            |
| unpickle_list        | 2.95 us                                                         | 3.13 us: 1.06x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 88.1 ms: 1.13x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 329 us: 1.15x slower                                                             |
| pickle_list          | 3.37 us                                                         | 3.95 us: 1.17x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.68 ms: 1.17x slower                                                            |
| unpickle             | 9.71 us                                                         | 11.7 us: 1.20x slower                                                            |
| pickle               | 7.79 us                                                         | 9.73 us: 1.25x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                     |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                            |
| django_template | 36.9 ms                                                         | 38.7 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.51 sec: 11.71x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 34.9 ms: 2.62x faster                                                            |
| nbody                      | 127 ms                                                          | 53.4 ms: 2.38x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.20 sec: 1.59x faster                                                           |
| scimark_fft                | 271 ms                                                          | 184 ms: 1.47x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.72 ms: 1.42x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.12 ms: 1.40x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.59 sec: 1.38x faster                                                           |
| pidigits                   | 199 ms                                                          | 147 ms: 1.36x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                             |
| deepcopy                   | 360 us                                                          | 273 us: 1.32x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 433 ms: 1.30x faster                                                             |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 429 ms: 1.27x faster                                                             |
| async_tree_none            | 298 ms                                                          | 235 ms: 1.27x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 288 ms: 1.26x faster                                                             |
| fannkuch                   | 354 ms                                                          | 284 ms: 1.25x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 285 ms: 1.23x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 555 ms: 1.22x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 229 ms: 1.21x faster                                                             |
| comprehensions             | 19.2 us                                                         | 15.9 us: 1.21x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.74 us: 1.19x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.74 ms: 1.17x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 570 ms: 1.16x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.83 us: 1.14x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 984 us: 1.12x faster                                                             |
| dulwich_log                | 58.5 ms                                                         | 52.4 ms: 1.12x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 62.2 ms: 1.11x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.37 sec: 1.09x faster                                                           |
| pyflate                    | 424 ms                                                          | 390 ms: 1.09x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 35.5 us: 1.08x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 671 ms: 1.07x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                             |
| regex_compile              | 129 ms                                                          | 122 ms: 1.06x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                             |
| chaos                      | 69.4 ms                                                         | 65.9 ms: 1.05x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 83.0 ms: 1.05x faster                                                            |
| logging_format             | 10.4 us                                                         | 10.1 us: 1.03x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.0 ms: 1.03x faster                                                            |
| json                       | 4.15 ms                                                         | 4.07 ms: 1.02x faster                                                            |
| pycparser                  | 978 ms                                                          | 958 ms: 1.02x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 91.8 ms: 1.02x faster                                                            |
| logging_simple             | 9.75 us                                                         | 9.59 us: 1.02x faster                                                            |
| sympy_str                  | 240 ms                                                          | 236 ms: 1.01x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.44 ms: 1.01x faster                                                            |
| go                         | 137 ms                                                          | 136 ms: 1.01x faster                                                             |
| generators                 | 38.5 ms                                                         | 38.2 ms: 1.01x faster                                                            |
| raytrace                   | 308 ms                                                          | 306 ms: 1.01x faster                                                             |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                            |
| float                      | 76.7 ms                                                         | 78.5 ms: 1.02x slower                                                            |
| 2to3                       | 280 ms                                                          | 288 ms: 1.03x slower                                                             |
| sympy_expand               | 398 ms                                                          | 410 ms: 1.03x slower                                                             |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                            |
| django_template            | 36.9 ms                                                         | 38.7 ms: 1.05x slower                                                            |
| scimark_sor                | 130 ms                                                          | 137 ms: 1.05x slower                                                             |
| docutils                   | 1.98 sec                                                        | 2.11 sec: 1.06x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.13 us: 1.06x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.7 ms: 1.11x slower                                                            |
| spectral_norm              | 104 ms                                                          | 115 ms: 1.11x slower                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 74.8 ms: 1.13x slower                                                            |
| async_generators           | 313 ms                                                          | 354 ms: 1.13x slower                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 88.1 ms: 1.13x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.7 us: 1.14x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                             |
| pickle_pure_python         | 286 us                                                          | 329 us: 1.15x slower                                                             |
| hexiom                     | 6.82 ms                                                         | 7.98 ms: 1.17x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.95 us: 1.17x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.68 ms: 1.17x slower                                                            |
| unpickle                   | 9.71 us                                                         | 11.7 us: 1.20x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.3 ms: 1.22x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 77.8 ns: 1.25x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.73 us: 1.25x slower                                                            |
| deltablue                  | 3.58 ms                                                         | 4.52 ms: 1.26x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 26.8 ms: 1.29x slower                                                            |
| coverage                   | 48.4 ms                                                         | 62.6 ms: 1.29x slower                                                            |
| richards                   | 41.3 ms                                                         | 53.9 ms: 1.30x slower                                                            |
| richards_super             | 46.5 ms                                                         | 60.6 ms: 1.30x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 126 ms: 1.35x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 106 ms: 1.40x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.99 ms: 2.08x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.47 ms: 2.26x slower                                                            |
| logging_silent             | 101 ns                                                          | 507 ns: 5.02x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf1_win32-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 98.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown