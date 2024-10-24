# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.09x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                                   |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 517 ms: 1.31x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.6 ms: 1.36x faster                                                                    |
| float          | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                                    |
| pidigits       | 199 ms                                                          | 200 ms: 1.01x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                                     |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                                    |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 181 us: 1.16x faster                                                                     |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                                   |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                                    |
| pickle_pure_python   | 286 us                                                          | 257 us: 1.11x faster                                                                     |
| xml_etree_generate   | 72.1 ms                                                         | 66.8 ms: 1.08x faster                                                                    |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                                     |
| xml_etree_process    | 53.2 ms                                                         | 50.2 ms: 1.06x faster                                                                    |
| json_loads           | 20.4 us                                                         | 20.2 us: 1.01x faster                                                                    |
| json_dumps           | 7.40 ms                                                         | 7.63 ms: 1.03x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 23.8 ms: 1.06x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.15 ms: 1.22x faster                                                                    |
| django_template | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.4 us: 1.64x faster                                                                    |
| deepcopy                   | 360 us                                                          | 256 us: 1.41x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                                     |
| generators                 | 38.5 ms                                                         | 27.7 ms: 1.39x faster                                                                    |
| scimark_lu                 | 93.2 ms                                                         | 68.4 ms: 1.36x faster                                                                    |
| raytrace                   | 308 ms                                                          | 226 ms: 1.36x faster                                                                     |
| nbody                      | 127 ms                                                          | 93.6 ms: 1.36x faster                                                                    |
| comprehensions             | 19.2 us                                                         | 14.3 us: 1.34x faster                                                                    |
| chaos                      | 69.4 ms                                                         | 52.2 ms: 1.33x faster                                                                    |
| logging_silent             | 101 ns                                                          | 76.2 ns: 1.33x faster                                                                    |
| scimark_sor                | 130 ms                                                          | 98.0 ms: 1.32x faster                                                                    |
| async_tree_io_tg           | 677 ms                                                          | 517 ms: 1.31x faster                                                                     |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.30x faster                                                                    |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.30x faster                                                                     |
| hexiom                     | 6.82 ms                                                         | 5.36 ms: 1.27x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 81.6 ms: 1.27x faster                                                                    |
| float                      | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                                    |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                                    |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                                     |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                                    |
| mako                       | 9.96 ms                                                         | 8.15 ms: 1.22x faster                                                                    |
| nqueens                    | 93.7 ms                                                         | 76.8 ms: 1.22x faster                                                                    |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 8.13 us: 1.20x faster                                                                    |
| logging_format             | 10.4 us                                                         | 8.72 us: 1.19x faster                                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.8 ms: 1.19x faster                                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 474 ms: 1.19x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                                     |
| crypto_pyaes               | 69.2 ms                                                         | 58.6 ms: 1.18x faster                                                                    |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                                     |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                                    |
| pyflate                    | 424 ms                                                          | 364 ms: 1.16x faster                                                                     |
| unpickle_pure_python       | 210 us                                                          | 181 us: 1.16x faster                                                                     |
| dulwich_log                | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                                    |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                                    |
| tomli_loads                | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                                   |
| fannkuch                   | 354 ms                                                          | 311 ms: 1.14x faster                                                                     |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.7 ms: 1.13x faster                                                                    |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                                   |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                                    |
| pycparser                  | 978 ms                                                          | 873 ms: 1.12x faster                                                                     |
| pickle_pure_python         | 286 us                                                          | 257 us: 1.11x faster                                                                     |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.11x faster                                                                     |
| go                         | 137 ms                                                          | 125 ms: 1.10x faster                                                                     |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.10x faster                                                                    |
| 2to3                       | 280 ms                                                          | 258 ms: 1.09x faster                                                                     |
| django_template            | 36.9 ms                                                         | 34.0 ms: 1.09x faster                                                                    |
| xml_etree_generate         | 72.1 ms                                                         | 66.8 ms: 1.08x faster                                                                    |
| richards                   | 41.3 ms                                                         | 38.3 ms: 1.08x faster                                                                    |
| sqlglot_optimize           | 48.5 ms                                                         | 45.0 ms: 1.08x faster                                                                    |
| richards_super             | 46.5 ms                                                         | 43.3 ms: 1.07x faster                                                                    |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                                     |
| sympy_str                  | 240 ms                                                          | 225 ms: 1.07x faster                                                                     |
| xml_etree_process          | 53.2 ms                                                         | 50.2 ms: 1.06x faster                                                                    |
| pprint_pformat             | 1.50 sec                                                        | 1.41 sec: 1.06x faster                                                                   |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                                    |
| meteor_contest             | 86.9 ms                                                         | 83.2 ms: 1.04x faster                                                                    |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                                   |
| pprint_safe_repr           | 721 ms                                                          | 693 ms: 1.04x faster                                                                     |
| pathlib                    | 91.4 ms                                                         | 88.5 ms: 1.03x faster                                                                    |
| docutils                   | 1.98 sec                                                        | 1.92 sec: 1.03x faster                                                                   |
| bench_mp_pool              | 75.4 ms                                                         | 73.8 ms: 1.02x faster                                                                    |
| async_generators           | 313 ms                                                          | 311 ms: 1.01x faster                                                                     |
| json_loads                 | 20.4 us                                                         | 20.2 us: 1.01x faster                                                                    |
| sympy_expand               | 398 ms                                                          | 395 ms: 1.01x faster                                                                     |
| pidigits                   | 199 ms                                                          | 200 ms: 1.01x slower                                                                     |
| json                       | 4.15 ms                                                         | 4.19 ms: 1.01x slower                                                                    |
| python_startup_no_site     | 19.1 ms                                                         | 19.5 ms: 1.02x slower                                                                    |
| json_dumps                 | 7.40 ms                                                         | 7.63 ms: 1.03x slower                                                                    |
| asyncio_tcp                | 662 ms                                                          | 702 ms: 1.06x slower                                                                     |
| python_startup             | 22.4 ms                                                         | 23.8 ms: 1.06x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                                    |
| coverage                   | 48.4 ms                                                         | 52.1 ms: 1.08x slower                                                                    |
| telco                      | 5.51 ms                                                         | 6.21 ms: 1.13x slower                                                                    |
| create_gc_cycles           | 652 us                                                          | 746 us: 1.14x slower                                                                     |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.19x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.35x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                             |

Benchmark hidden because not significant (2): tornado_http, gc_traversal
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown