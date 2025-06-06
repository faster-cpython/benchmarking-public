# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.492x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 285 ms: 1.02x slower                                                             |
| docutils       | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 426 ms: 1.32x faster                                                             |
| async_tree_io              | 693 ms                                                          | 535 ms: 1.30x faster                                                             |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 424 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 279 ms: 1.26x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 228 ms: 1.22x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.8 ms: 2.28x faster                                                            |
| pidigits       | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| float          | 76.7 ms                                                         | 78.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.45x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 112 ms: 1.15x faster                                                             |
| regex_effbot   | 2.04 ms                                                         | 1.78 ms: 1.14x faster                                                            |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.55 sec: 1.42x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 155 us: 1.35x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.09x faster                                                             |
| xml_etree_process    | 53.2 ms                                                         | 50.9 ms: 1.05x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 69.5 ms: 1.04x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 3.05 us: 1.04x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 84.8 ms: 1.09x slower                                                            |
| pickle_dict          | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| pickle_pure_python   | 286 us                                                          | 318 us: 1.11x slower                                                             |
| unpickle             | 9.71 us                                                         | 11.2 us: 1.15x slower                                                            |
| pickle_list          | 3.37 us                                                         | 3.93 us: 1.17x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                            |
| pickle               | 7.79 us                                                         | 9.45 us: 1.21x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                            |
| python_startup         | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.11 ms: 1.40x faster                                                            |
| django_template | 36.9 ms                                                         | 37.3 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pprint_pformat             | 1.50 sec                                                        | 1.56 us: 959178.19x faster                                                       |
| pprint_safe_repr           | 721 ms                                                          | 900 ns: 800802.83x faster                                                        |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.49 sec: 11.89x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 33.8 ms: 2.70x faster                                                            |
| nbody                      | 127 ms                                                          | 55.8 ms: 2.28x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.20 sec: 1.60x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.61 ms: 1.48x faster                                                            |
| scimark_fft                | 271 ms                                                          | 184 ms: 1.47x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.55 sec: 1.42x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.11 ms: 1.40x faster                                                            |
| pidigits                   | 199 ms                                                          | 145 ms: 1.37x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 155 us: 1.35x faster                                                             |
| deepcopy                   | 360 us                                                          | 269 us: 1.34x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 426 ms: 1.32x faster                                                             |
| async_tree_io              | 693 ms                                                          | 535 ms: 1.30x faster                                                             |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                             |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 424 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 279 ms: 1.26x faster                                                             |
| comprehensions             | 19.2 us                                                         | 15.4 us: 1.25x faster                                                            |
| fannkuch                   | 354 ms                                                          | 285 ms: 1.24x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 228 ms: 1.22x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.73 us: 1.19x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 557 ms: 1.19x faster                                                             |
| regex_compile              | 129 ms                                                          | 112 ms: 1.15x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 2.80 us: 1.15x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.78 ms: 1.14x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 981 us: 1.12x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 34.2 us: 1.12x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 52.2 ms: 1.12x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 62.0 ms: 1.12x faster                                                            |
| pyflate                    | 424 ms                                                          | 383 ms: 1.11x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.09x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 113 ms: 1.09x faster                                                             |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                             |
| telco                      | 5.51 ms                                                         | 5.13 ms: 1.07x faster                                                            |
| chaos                      | 69.4 ms                                                         | 64.9 ms: 1.07x faster                                                            |
| generators                 | 38.5 ms                                                         | 36.3 ms: 1.06x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 82.2 ms: 1.06x faster                                                            |
| logging_format             | 10.4 us                                                         | 9.89 us: 1.05x faster                                                            |
| pycparser                  | 978 ms                                                          | 930 ms: 1.05x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 50.9 ms: 1.05x faster                                                            |
| sympy_str                  | 240 ms                                                          | 231 ms: 1.04x faster                                                             |
| logging_simple             | 9.75 us                                                         | 9.40 us: 1.04x faster                                                            |
| go                         | 137 ms                                                          | 132 ms: 1.04x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 69.5 ms: 1.04x faster                                                            |
| json                       | 4.15 ms                                                         | 4.01 ms: 1.04x faster                                                            |
| raytrace                   | 308 ms                                                          | 299 ms: 1.03x faster                                                             |
| nqueens                    | 93.7 ms                                                         | 91.1 ms: 1.03x faster                                                            |
| django_template            | 36.9 ms                                                         | 37.3 ms: 1.01x slower                                                            |
| scimark_sor                | 130 ms                                                          | 131 ms: 1.01x slower                                                             |
| sympy_expand               | 398 ms                                                          | 403 ms: 1.01x slower                                                             |
| float                      | 76.7 ms                                                         | 78.1 ms: 1.02x slower                                                            |
| 2to3                       | 280 ms                                                          | 285 ms: 1.02x slower                                                             |
| unpickle_list              | 2.95 us                                                         | 3.05 us: 1.04x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                            |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 84.8 ms: 1.09x slower                                                            |
| pickle_dict                | 19.9 us                                                         | 22.0 us: 1.10x slower                                                            |
| scimark_monte_carlo        | 66.4 ms                                                         | 73.8 ms: 1.11x slower                                                            |
| pickle_pure_python         | 286 us                                                          | 318 us: 1.11x slower                                                             |
| spectral_norm              | 104 ms                                                          | 116 ms: 1.12x slower                                                             |
| async_generators           | 313 ms                                                          | 352 ms: 1.12x slower                                                             |
| hexiom                     | 6.82 ms                                                         | 7.69 ms: 1.13x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                             |
| unpickle                   | 9.71 us                                                         | 11.2 us: 1.15x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.93 us: 1.17x slower                                                            |
| unpack_sequence            | 62.5 ns                                                         | 73.7 ns: 1.18x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.76 ms: 1.18x slower                                                            |
| deltablue                  | 3.58 ms                                                         | 4.30 ms: 1.20x slower                                                            |
| coroutines                 | 20.9 ms                                                         | 25.1 ms: 1.20x slower                                                            |
| pickle                     | 7.79 us                                                         | 9.45 us: 1.21x slower                                                            |
| python_startup             | 22.4 ms                                                         | 27.2 ms: 1.22x slower                                                            |
| richards                   | 41.3 ms                                                         | 51.4 ms: 1.24x slower                                                            |
| richards_super             | 46.5 ms                                                         | 58.2 ms: 1.25x slower                                                            |
| scimark_lu                 | 93.2 ms                                                         | 120 ms: 1.29x slower                                                             |
| bench_mp_pool              | 75.4 ms                                                         | 103 ms: 1.36x slower                                                             |
| gc_traversal               | 1.44 ms                                                         | 2.72 ms: 1.89x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.41 ms: 2.16x slower                                                            |
| logging_silent             | 101 ns                                                          | 498 ns: 4.93x slower                                                             |
| coverage                   | 48.4 ms                                                         | 479 ms: 9.90x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.492x faster

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown