# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 205 ms: 1.78x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 392 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 170 ms: 1.64x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.2 ms: 1.98x faster                                                            |
| float          | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| Geometric mean | (ref)                                                           | 1.68x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 79.9 ms: 1.62x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 135 us: 1.55x faster                                                             |
| json_loads           | 20.4 us                                                         | 14.1 us: 1.45x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 38.5 ms: 1.38x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 213 us: 1.34x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 86.8 ms: 1.30x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.9 ms: 1.29x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.31 ms: 1.17x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.42 us: 1.15x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.86 us: 1.03x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.39 us: 1.01x slower                                                            |
| pickle               | 7.79 us                                                         | 8.26 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.53 ms: 1.53x faster                                                            |
| django_template | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.51x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.29 sec: 13.73x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 30.5 ms: 3.00x faster                                                            |
| mdp                        | 1.91 sec                                                        | 804 ms: 2.38x faster                                                             |
| deepcopy                   | 360 us                                                          | 171 us: 2.10x faster                                                             |
| deepcopy_memo              | 38.4 us                                                         | 18.3 us: 2.10x faster                                                            |
| generators                 | 38.5 ms                                                         | 19.3 ms: 2.00x faster                                                            |
| nbody                      | 127 ms                                                          | 64.2 ms: 1.98x faster                                                            |
| unpack_sequence            | 62.5 ns                                                         | 32.6 ns: 1.91x faster                                                            |
| logging_silent             | 101 ns                                                          | 55.6 ns: 1.82x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.7 us: 1.79x faster                                                            |
| go                         | 137 ms                                                          | 77.1 ms: 1.78x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 205 ms: 1.78x faster                                                             |
| float                      | 76.7 ms                                                         | 43.4 ms: 1.77x faster                                                            |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_none            | 298 ms                                                          | 170 ms: 1.75x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.85 us: 1.75x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 392 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                             |
| chaos                      | 69.4 ms                                                         | 41.0 ms: 1.69x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 209 ms: 1.68x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.08 ms: 1.67x faster                                                            |
| raytrace                   | 308 ms                                                          | 184 ms: 1.67x faster                                                             |
| asyncio_tcp                | 662 ms                                                          | 398 ms: 1.67x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.4 ms: 1.65x faster                                                            |
| scimark_sor                | 130 ms                                                          | 79.2 ms: 1.64x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 170 ms: 1.64x faster                                                             |
| deltablue                  | 3.58 ms                                                         | 2.21 ms: 1.62x faster                                                            |
| regex_compile              | 129 ms                                                          | 79.9 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 339 ms: 1.61x faster                                                             |
| spectral_norm              | 104 ms                                                          | 64.5 ms: 1.61x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 58.6 ms: 1.59x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.41 sec: 1.56x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.55x faster                                                             |
| logging_simple             | 9.75 us                                                         | 6.29 us: 1.55x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.50 ms: 1.54x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.75 us: 1.54x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.53 ms: 1.53x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 62.2 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| richards                   | 41.3 ms                                                         | 27.8 ms: 1.48x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.02 sec: 1.47x faster                                                           |
| pyflate                    | 424 ms                                                          | 289 ms: 1.46x faster                                                             |
| richards_super             | 46.5 ms                                                         | 31.9 ms: 1.45x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.4 ms: 1.45x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.1 us: 1.45x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| json                       | 4.15 ms                                                         | 2.88 ms: 1.44x faster                                                            |
| scimark_fft                | 271 ms                                                          | 189 ms: 1.43x faster                                                             |
| crypto_pyaes               | 69.2 ms                                                         | 48.4 ms: 1.43x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 508 ms: 1.42x faster                                                             |
| sympy_str                  | 240 ms                                                          | 169 ms: 1.42x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.4 ms: 1.41x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 87.8 ms: 1.40x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 38.5 ms: 1.38x faster                                                            |
| sympy_expand               | 398 ms                                                          | 289 ms: 1.38x faster                                                             |
| pycparser                  | 978 ms                                                          | 714 ms: 1.37x faster                                                             |
| pidigits                   | 199 ms                                                          | 146 ms: 1.36x faster                                                             |
| async_generators           | 313 ms                                                          | 233 ms: 1.34x faster                                                             |
| pickle_pure_python         | 286 us                                                          | 213 us: 1.34x faster                                                             |
| fannkuch                   | 354 ms                                                          | 269 ms: 1.31x faster                                                             |
| sqlite_synth               | 2.07 us                                                         | 1.58 us: 1.31x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 86.8 ms: 1.30x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.30x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 849 us: 1.30x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 55.9 ms: 1.29x faster                                                            |
| 2to3                       | 280 ms                                                          | 221 ms: 1.27x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.1 ms: 1.23x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.62 sec: 1.22x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 105 us: 1.20x faster                                                             |
| telco                      | 5.51 ms                                                         | 4.60 ms: 1.20x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 72.6 ms: 1.20x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.31 ms: 1.17x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.42 us: 1.15x faster                                                            |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.86 us: 1.03x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.39 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.3 ms: 1.01x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.26 us: 1.06x slower                                                            |
| coverage                   | 48.4 ms                                                         | 51.8 ms: 1.07x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.2 ms: 1.25x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.47x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.30 ms: 2.00x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown