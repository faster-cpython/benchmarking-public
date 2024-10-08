# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 262 ms: 1.07x faster                                                                     |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.03x faster                                                                   |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                                     |
| async_tree_io_tg           | 677 ms                                                          | 523 ms: 1.30x faster                                                                     |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                                     |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.27x faster                                                                     |
| async_tree_io              | 693 ms                                                          | 564 ms: 1.23x faster                                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 474 ms: 1.15x faster                                                                     |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 99.2 ms: 1.28x faster                                                                    |
| float          | 76.7 ms                                                         | 60.0 ms: 1.28x faster                                                                    |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 109 ms: 1.19x faster                                                                     |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                                    |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                                   |
| unpickle_pure_python | 210 us                                                          | 173 us: 1.21x faster                                                                     |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                                    |
| pickle_pure_python   | 286 us                                                          | 257 us: 1.11x faster                                                                     |
| xml_etree_process    | 53.2 ms                                                         | 48.6 ms: 1.10x faster                                                                    |
| xml_etree_generate   | 72.1 ms                                                         | 66.2 ms: 1.09x faster                                                                    |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                                     |
| json_dumps           | 7.40 ms                                                         | 7.35 ms: 1.01x faster                                                                    |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                                    |
| python_startup         | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.24 ms: 1.21x faster                                                                    |
| django_template | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.3 us: 1.65x faster                                                                    |
| generators                 | 38.5 ms                                                         | 27.6 ms: 1.40x faster                                                                    |
| deepcopy                   | 360 us                                                          | 259 us: 1.39x faster                                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.38x faster                                                                     |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.37x faster                                                                     |
| raytrace                   | 308 ms                                                          | 226 ms: 1.36x faster                                                                     |
| logging_silent             | 101 ns                                                          | 74.9 ns: 1.35x faster                                                                    |
| comprehensions             | 19.2 us                                                         | 14.3 us: 1.34x faster                                                                    |
| scimark_lu                 | 93.2 ms                                                         | 70.0 ms: 1.33x faster                                                                    |
| scimark_sor                | 130 ms                                                          | 98.5 ms: 1.32x faster                                                                    |
| spectral_norm              | 104 ms                                                          | 79.2 ms: 1.31x faster                                                                    |
| deltablue                  | 3.58 ms                                                         | 2.74 ms: 1.31x faster                                                                    |
| async_tree_io_tg           | 677 ms                                                          | 523 ms: 1.30x faster                                                                     |
| chaos                      | 69.4 ms                                                         | 54.0 ms: 1.29x faster                                                                    |
| hexiom                     | 6.82 ms                                                         | 5.31 ms: 1.28x faster                                                                    |
| async_tree_none            | 298 ms                                                          | 232 ms: 1.28x faster                                                                     |
| nbody                      | 127 ms                                                          | 99.2 ms: 1.28x faster                                                                    |
| float                      | 76.7 ms                                                         | 60.0 ms: 1.28x faster                                                                    |
| async_tree_memoization     | 364 ms                                                          | 285 ms: 1.27x faster                                                                     |
| deepcopy_reduce            | 3.23 us                                                         | 2.60 us: 1.24x faster                                                                    |
| async_tree_io              | 693 ms                                                          | 564 ms: 1.23x faster                                                                     |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.23x faster                                                                   |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.16 ms: 1.22x faster                                                                    |
| unpickle_pure_python       | 210 us                                                          | 173 us: 1.21x faster                                                                     |
| mako                       | 9.96 ms                                                         | 8.24 ms: 1.21x faster                                                                    |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.6 ms: 1.19x faster                                                                    |
| pyflate                    | 424 ms                                                          | 355 ms: 1.19x faster                                                                     |
| regex_compile              | 129 ms                                                          | 109 ms: 1.19x faster                                                                     |
| nqueens                    | 93.7 ms                                                         | 79.1 ms: 1.18x faster                                                                    |
| logging_simple             | 9.75 us                                                         | 8.26 us: 1.18x faster                                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 59.1 ms: 1.17x faster                                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                                     |
| logging_format             | 10.4 us                                                         | 8.98 us: 1.16x faster                                                                    |
| go                         | 137 ms                                                          | 119 ms: 1.15x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 474 ms: 1.15x faster                                                                     |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                                    |
| dulwich_log                | 58.5 ms                                                         | 51.1 ms: 1.14x faster                                                                    |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.14x faster                                                                    |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.13x faster                                                                    |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                                   |
| bench_thread_pool          | 1.10 ms                                                         | 991 us: 1.11x faster                                                                     |
| pickle_pure_python         | 286 us                                                          | 257 us: 1.11x faster                                                                     |
| sympy_integrate            | 17.5 ms                                                         | 15.9 ms: 1.10x faster                                                                    |
| xml_etree_process          | 53.2 ms                                                         | 48.6 ms: 1.10x faster                                                                    |
| pycparser                  | 978 ms                                                          | 893 ms: 1.10x faster                                                                     |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.09x faster                                                                     |
| xml_etree_generate         | 72.1 ms                                                         | 66.2 ms: 1.09x faster                                                                    |
| django_template            | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                                    |
| sqlglot_optimize           | 48.5 ms                                                         | 44.6 ms: 1.09x faster                                                                    |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                                     |
| pprint_pformat             | 1.50 sec                                                        | 1.39 sec: 1.08x faster                                                                   |
| fannkuch                   | 354 ms                                                          | 330 ms: 1.07x faster                                                                     |
| 2to3                       | 280 ms                                                          | 262 ms: 1.07x faster                                                                     |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                                     |
| async_generators           | 313 ms                                                          | 294 ms: 1.06x faster                                                                     |
| pprint_safe_repr           | 721 ms                                                          | 680 ms: 1.06x faster                                                                     |
| richards                   | 41.3 ms                                                         | 39.1 ms: 1.06x faster                                                                    |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                                    |
| richards_super             | 46.5 ms                                                         | 44.2 ms: 1.05x faster                                                                    |
| sympy_str                  | 240 ms                                                          | 229 ms: 1.05x faster                                                                     |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                                   |
| meteor_contest             | 86.9 ms                                                         | 84.3 ms: 1.03x faster                                                                    |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.03x faster                                                                   |
| bench_mp_pool              | 75.4 ms                                                         | 73.7 ms: 1.02x faster                                                                    |
| pathlib                    | 91.4 ms                                                         | 89.6 ms: 1.02x faster                                                                    |
| json_dumps                 | 7.40 ms                                                         | 7.35 ms: 1.01x faster                                                                    |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                                     |
| sympy_expand               | 398 ms                                                          | 404 ms: 1.02x slower                                                                     |
| json                       | 4.15 ms                                                         | 4.29 ms: 1.03x slower                                                                    |
| asyncio_tcp                | 662 ms                                                          | 708 ms: 1.07x slower                                                                     |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                                    |
| coverage                   | 48.4 ms                                                         | 51.9 ms: 1.07x slower                                                                    |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                                    |
| python_startup             | 22.4 ms                                                         | 24.3 ms: 1.09x slower                                                                    |
| telco                      | 5.51 ms                                                         | 6.24 ms: 1.13x slower                                                                    |
| create_gc_cycles           | 652 us                                                          | 749 us: 1.15x slower                                                                     |
| typing_runtime_protocols   | 126 us                                                          | 158 us: 1.25x slower                                                                     |
| sqlglot_normalize          | 100 ms                                                          | 231 ms: 2.30x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                             |

Benchmark hidden because not significant (3): gc_traversal, json_loads, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown