# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-x86
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.09x faster                                                                   |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io              | 693 ms                                                          | 486 ms: 1.43x faster                                                                   |
| async_tree_io_tg           | 677 ms                                                          | 484 ms: 1.40x faster                                                                   |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                                   |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.32x faster                                                                   |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                                   |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                                   |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                                   |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 91.0 ms: 1.40x faster                                                                  |
| float          | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                                  |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                                  |
| regex_compile  | 129 ms                                                          | 111 ms: 1.17x faster                                                                   |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                                   |
| regex_v8       | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.75 sec: 1.26x faster                                                                 |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                                  |
| unpickle_pure_python | 210 us                                                          | 186 us: 1.13x faster                                                                   |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                                   |
| xml_etree_generate   | 72.1 ms                                                         | 68.8 ms: 1.05x faster                                                                  |
| xml_etree_process    | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                                  |
| pickle_pure_python   | 286 us                                                          | 287 us: 1.00x slower                                                                   |
| json_loads           | 20.4 us                                                         | 21.6 us: 1.06x slower                                                                  |
| json_dumps           | 7.40 ms                                                         | 8.32 ms: 1.12x slower                                                                  |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.5 ms: 1.13x slower                                                                  |
| python_startup         | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                                  |
| Geometric mean         | (ref)                                                           | 1.19x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.97 ms: 1.25x faster                                                                  |
| django_template | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                                  |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 34.1 ms: 2.68x faster                                                                  |
| deepcopy_memo              | 38.4 us                                                         | 22.3 us: 1.72x faster                                                                  |
| deepcopy                   | 360 us                                                          | 244 us: 1.48x faster                                                                   |
| generators                 | 38.5 ms                                                         | 26.9 ms: 1.43x faster                                                                  |
| async_tree_io              | 693 ms                                                          | 486 ms: 1.43x faster                                                                   |
| async_tree_io_tg           | 677 ms                                                          | 484 ms: 1.40x faster                                                                   |
| nbody                      | 127 ms                                                          | 91.0 ms: 1.40x faster                                                                  |
| logging_silent             | 101 ns                                                          | 72.8 ns: 1.39x faster                                                                  |
| float                      | 76.7 ms                                                         | 55.3 ms: 1.39x faster                                                                  |
| spectral_norm              | 104 ms                                                          | 75.1 ms: 1.38x faster                                                                  |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                                  |
| scimark_lu                 | 93.2 ms                                                         | 69.6 ms: 1.34x faster                                                                  |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                                   |
| async_tree_none_tg         | 278 ms                                                          | 209 ms: 1.32x faster                                                                   |
| coroutines                 | 20.9 ms                                                         | 16.0 ms: 1.31x faster                                                                  |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                                   |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.30x faster                                                                   |
| hexiom                     | 6.82 ms                                                         | 5.31 ms: 1.28x faster                                                                  |
| regex_effbot               | 2.04 ms                                                         | 1.59 ms: 1.28x faster                                                                  |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                                  |
| go                         | 137 ms                                                          | 108 ms: 1.27x faster                                                                   |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                                   |
| tomli_loads                | 2.20 sec                                                        | 1.75 sec: 1.26x faster                                                                 |
| deltablue                  | 3.58 ms                                                         | 2.86 ms: 1.25x faster                                                                  |
| mako                       | 9.96 ms                                                         | 7.97 ms: 1.25x faster                                                                  |
| deepcopy_reduce            | 3.23 us                                                         | 2.63 us: 1.23x faster                                                                  |
| raytrace                   | 308 ms                                                          | 254 ms: 1.21x faster                                                                   |
| pyflate                    | 424 ms                                                          | 354 ms: 1.20x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                                   |
| nqueens                    | 93.7 ms                                                         | 79.8 ms: 1.17x faster                                                                  |
| fannkuch                   | 354 ms                                                          | 301 ms: 1.17x faster                                                                   |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 481 ms: 1.17x faster                                                                   |
| chaos                      | 69.4 ms                                                         | 59.2 ms: 1.17x faster                                                                  |
| scimark_fft                | 271 ms                                                          | 231 ms: 1.17x faster                                                                   |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.9 ms: 1.17x faster                                                                  |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.6 ms: 1.17x faster                                                                  |
| regex_compile              | 129 ms                                                          | 111 ms: 1.17x faster                                                                   |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                                 |
| unpickle_pure_python       | 210 us                                                          | 186 us: 1.13x faster                                                                   |
| crypto_pyaes               | 69.2 ms                                                         | 61.7 ms: 1.12x faster                                                                  |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.12x faster                                                                   |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                                  |
| richards                   | 41.3 ms                                                         | 37.3 ms: 1.11x faster                                                                  |
| logging_simple             | 9.75 us                                                         | 8.82 us: 1.11x faster                                                                  |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                                  |
| sqlglot_transpile          | 1.53 ms                                                         | 1.40 ms: 1.09x faster                                                                  |
| logging_format             | 10.4 us                                                         | 9.55 us: 1.09x faster                                                                  |
| sympy_integrate            | 17.5 ms                                                         | 16.1 ms: 1.09x faster                                                                  |
| 2to3                       | 280 ms                                                          | 258 ms: 1.09x faster                                                                   |
| sqlglot_parse              | 1.25 ms                                                         | 1.15 ms: 1.08x faster                                                                  |
| sqlglot_optimize           | 48.5 ms                                                         | 44.7 ms: 1.08x faster                                                                  |
| django_template            | 36.9 ms                                                         | 34.1 ms: 1.08x faster                                                                  |
| richards_super             | 46.5 ms                                                         | 43.0 ms: 1.08x faster                                                                  |
| pprint_pformat             | 1.50 sec                                                        | 1.39 sec: 1.08x faster                                                                 |
| meteor_contest             | 86.9 ms                                                         | 80.6 ms: 1.08x faster                                                                  |
| sympy_str                  | 240 ms                                                          | 222 ms: 1.08x faster                                                                   |
| pprint_safe_repr           | 721 ms                                                          | 669 ms: 1.08x faster                                                                   |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                                                 |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                                   |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                                   |
| pycparser                  | 978 ms                                                          | 930 ms: 1.05x faster                                                                   |
| xml_etree_generate         | 72.1 ms                                                         | 68.8 ms: 1.05x faster                                                                  |
| xml_etree_process          | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                                  |
| bench_thread_pool          | 1.10 ms                                                         | 1.06 ms: 1.04x faster                                                                  |
| sympy_expand               | 398 ms                                                          | 391 ms: 1.02x faster                                                                   |
| pickle_pure_python         | 286 us                                                          | 287 us: 1.00x slower                                                                   |
| async_generators           | 313 ms                                                          | 317 ms: 1.01x slower                                                                   |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                                   |
| regex_v8                   | 15.0 ms                                                         | 15.5 ms: 1.03x slower                                                                  |
| json_loads                 | 20.4 us                                                         | 21.6 us: 1.06x slower                                                                  |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                                  |
| json                       | 4.15 ms                                                         | 4.46 ms: 1.07x slower                                                                  |
| json_dumps                 | 7.40 ms                                                         | 8.32 ms: 1.12x slower                                                                  |
| python_startup_no_site     | 19.1 ms                                                         | 21.5 ms: 1.13x slower                                                                  |
| telco                      | 5.51 ms                                                         | 6.57 ms: 1.19x slower                                                                  |
| bench_mp_pool              | 75.4 ms                                                         | 90.0 ms: 1.19x slower                                                                  |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.20x slower                                                                   |
| python_startup             | 22.4 ms                                                         | 27.8 ms: 1.24x slower                                                                  |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                                                  |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                                  |
| sqlglot_normalize          | 100 ms                                                          | 235 ms: 2.34x slower                                                                   |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                           |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown