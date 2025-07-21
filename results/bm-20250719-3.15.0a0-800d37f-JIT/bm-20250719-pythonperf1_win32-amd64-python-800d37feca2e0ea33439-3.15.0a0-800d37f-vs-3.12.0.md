# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.502x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| docutils       | 1.98 sec                                                        | 1.65 sec: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 338 ms: 1.61x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 57.3 ms: 2.22x faster                                                            |
| float          | 76.7 ms                                                         | 43.2 ms: 1.77x faster                                                            |
| pidigits       | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 78.6 ms: 1.64x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| regex_v8       | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 105 us: 2.00x faster                                                             |
| tomli_loads          | 2.20 sec                                                        | 1.11 sec: 1.98x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 51.0 ms: 1.41x faster                                                            |
| json_loads           | 20.4 us                                                         | 14.4 us: 1.41x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 203 us: 1.41x faster                                                             |
| xml_etree_parse      | 113 ms                                                          | 87.3 ms: 1.30x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.18 ms: 1.20x faster                                                            |
| unpickle             | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_dict          | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle               | 7.79 us                                                         | 7.59 us: 1.03x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                            |
| python_startup         | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.42 ms: 1.84x faster                                                            |
| django_template | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.66x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.7 sec                                                        | 1.42 sec: 12.45x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 30.2 ms: 3.03x faster                                                            |
| mdp                        | 1.91 sec                                                        | 796 ms: 2.40x faster                                                             |
| nbody                      | 127 ms                                                          | 57.3 ms: 2.22x faster                                                            |
| deepcopy_memo              | 38.4 us                                                         | 18.0 us: 2.13x faster                                                            |
| deepcopy                   | 360 us                                                          | 170 us: 2.12x faster                                                             |
| unpickle_pure_python       | 210 us                                                          | 105 us: 2.00x faster                                                             |
| tomli_loads                | 2.20 sec                                                        | 1.11 sec: 1.98x faster                                                           |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.96x faster                                                            |
| logging_silent             | 101 ns                                                          | 54.1 ns: 1.87x faster                                                            |
| mako                       | 9.96 ms                                                         | 5.42 ms: 1.84x faster                                                            |
| comprehensions             | 19.2 us                                                         | 10.5 us: 1.83x faster                                                            |
| scimark_fft                | 271 ms                                                          | 149 ms: 1.81x faster                                                             |
| unpack_sequence            | 62.5 ns                                                         | 34.5 ns: 1.81x faster                                                            |
| go                         | 137 ms                                                          | 76.7 ms: 1.79x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 204 ms: 1.79x faster                                                             |
| float                      | 76.7 ms                                                         | 43.2 ms: 1.77x faster                                                            |
| async_tree_none            | 298 ms                                                          | 168 ms: 1.77x faster                                                             |
| async_tree_io              | 693 ms                                                          | 393 ms: 1.76x faster                                                             |
| deepcopy_reduce            | 3.23 us                                                         | 1.84 us: 1.75x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 388 ms: 1.74x faster                                                             |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.23 ms: 1.73x faster                                                            |
| raytrace                   | 308 ms                                                          | 178 ms: 1.73x faster                                                             |
| chaos                      | 69.4 ms                                                         | 40.6 ms: 1.71x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 332 ms: 1.70x faster                                                             |
| pyflate                    | 424 ms                                                          | 251 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 350 ms                                                          | 208 ms: 1.69x faster                                                             |
| hexiom                     | 6.82 ms                                                         | 4.08 ms: 1.67x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 897 ms: 1.67x faster                                                             |
| scimark_sor                | 130 ms                                                          | 78.0 ms: 1.66x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 167 ms: 1.66x faster                                                             |
| fannkuch                   | 354 ms                                                          | 213 ms: 1.66x faster                                                             |
| spectral_norm              | 104 ms                                                          | 63.1 ms: 1.65x faster                                                            |
| regex_compile              | 129 ms                                                          | 78.6 ms: 1.64x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.19 ms: 1.64x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 443 ms: 1.62x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 338 ms: 1.61x faster                                                             |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.5 ms: 1.60x faster                                                            |
| logging_simple             | 9.75 us                                                         | 6.14 us: 1.59x faster                                                            |
| logging_format             | 10.4 us                                                         | 6.57 us: 1.58x faster                                                            |
| richards                   | 41.3 ms                                                         | 26.8 ms: 1.54x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 61.1 ms: 1.53x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 45.6 ms: 1.52x faster                                                            |
| richards_super             | 46.5 ms                                                         | 30.8 ms: 1.51x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 35.3 ms: 1.51x faster                                                            |
| django_template            | 36.9 ms                                                         | 24.6 ms: 1.50x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 14.2 ms: 1.47x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 63.8 ms: 1.46x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                            |
| pycparser                  | 978 ms                                                          | 689 ms: 1.42x faster                                                             |
| xml_etree_generate         | 72.1 ms                                                         | 51.0 ms: 1.41x faster                                                            |
| json_loads                 | 20.4 us                                                         | 14.4 us: 1.41x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 203 us: 1.41x faster                                                             |
| sympy_sum                  | 123 ms                                                          | 87.7 ms: 1.40x faster                                                            |
| sympy_str                  | 240 ms                                                          | 171 ms: 1.40x faster                                                             |
| sympy_integrate            | 17.5 ms                                                         | 12.6 ms: 1.39x faster                                                            |
| json                       | 4.15 ms                                                         | 3.01 ms: 1.38x faster                                                            |
| pidigits                   | 199 ms                                                          | 146 ms: 1.37x faster                                                             |
| sympy_expand               | 398 ms                                                          | 293 ms: 1.36x faster                                                             |
| regex_effbot               | 2.04 ms                                                         | 1.54 ms: 1.32x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.58 us: 1.32x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 506 ms: 1.31x faster                                                             |
| bench_thread_pool          | 1.10 ms                                                         | 847 us: 1.30x faster                                                             |
| xml_etree_parse            | 113 ms                                                          | 87.3 ms: 1.30x faster                                                            |
| telco                      | 5.51 ms                                                         | 4.29 ms: 1.28x faster                                                            |
| 2to3                       | 280 ms                                                          | 219 ms: 1.28x faster                                                             |
| async_generators           | 313 ms                                                          | 248 ms: 1.26x faster                                                             |
| meteor_contest             | 86.9 ms                                                         | 69.1 ms: 1.26x faster                                                            |
| typing_runtime_protocols   | 126 us                                                          | 101 us: 1.25x faster                                                             |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.65 sec: 1.21x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.18 ms: 1.20x faster                                                            |
| unpickle                   | 9.71 us                                                         | 8.68 us: 1.12x faster                                                            |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                             |
| regex_v8                   | 15.0 ms                                                         | 13.8 ms: 1.09x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.77 us: 1.06x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.4 us: 1.03x faster                                                            |
| pickle                     | 7.79 us                                                         | 7.59 us: 1.03x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.29 us: 1.02x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 19.2 ms: 1.01x slower                                                            |
| coverage                   | 48.4 ms                                                         | 49.7 ms: 1.03x slower                                                            |
| python_startup             | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.5 ms: 1.25x slower                                                            |
| gc_traversal               | 1.44 ms                                                         | 2.11 ms: 1.46x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 1.29 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                     |
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.502x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.51x
- 95% likely to have a speedup of 1.49x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown