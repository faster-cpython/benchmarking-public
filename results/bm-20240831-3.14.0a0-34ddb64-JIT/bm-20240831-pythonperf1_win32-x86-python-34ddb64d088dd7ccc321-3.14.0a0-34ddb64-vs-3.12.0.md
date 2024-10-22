# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 263 ms: 1.06x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                         |
| tornado_http   | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                           |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.38x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 47.8 ms: 2.65x faster                                                          |
| float          | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                          |
| pidigits       | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.68x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 102 ms: 1.27x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                          |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 54.5 ms: 1.32x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 162 us: 1.30x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 62.5 ms: 1.24x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 233 us: 1.23x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.86 ms: 1.08x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.0 ms: 1.10x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.60 ms: 1.78x faster                                                          |
| django_template | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 47.8 ms: 2.65x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 15.0 us: 2.56x faster                                                          |
| spectral_norm              | 104 ms                                                          | 46.3 ms: 2.24x faster                                                          |
| scimark_sor                | 130 ms                                                          | 69.4 ms: 1.87x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.60 ms: 1.78x faster                                                          |
| float                      | 76.7 ms                                                         | 43.9 ms: 1.75x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.06 ms: 1.74x faster                                                          |
| logging_silent             | 101 ns                                                          | 59.4 ns: 1.70x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.8 us: 1.63x faster                                                          |
| scimark_fft                | 271 ms                                                          | 168 ms: 1.62x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.5 ms: 1.57x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 59.5 ms: 1.57x faster                                                          |
| deepcopy                   | 360 us                                                          | 230 us: 1.56x faster                                                           |
| pyflate                    | 424 ms                                                          | 279 ms: 1.52x faster                                                           |
| fannkuch                   | 354 ms                                                          | 237 ms: 1.49x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.48 sec: 1.48x faster                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.64 ms: 1.46x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 48.2 ms: 1.44x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 251 ms: 1.39x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.91 ms: 1.39x faster                                                          |
| async_tree_none            | 298 ms                                                          | 215 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 202 ms: 1.38x faster                                                           |
| go                         | 137 ms                                                          | 102 ms: 1.34x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.8 ms: 1.33x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 54.5 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| richards_super             | 46.5 ms                                                         | 35.5 ms: 1.31x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 162 us: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.6 ms: 1.29x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 41.4 ms: 1.29x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.28x faster                                                          |
| richards                   | 41.3 ms                                                         | 32.4 ms: 1.27x faster                                                          |
| regex_compile              | 129 ms                                                          | 102 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.71 us: 1.27x faster                                                          |
| raytrace                   | 308 ms                                                          | 245 ms: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.34 us: 1.25x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 62.5 ms: 1.24x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 233 us: 1.23x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.24 sec: 1.21x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 596 ms: 1.21x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 78.3 ms: 1.20x faster                                                          |
| pycparser                  | 978 ms                                                          | 819 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 473 ms: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 73.2 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.9 ms: 1.17x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                         |
| django_template            | 36.9 ms                                                         | 33.6 ms: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.86 ms: 1.08x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.07x faster                                                           |
| sympy_str                  | 240 ms                                                          | 223 ms: 1.07x faster                                                           |
| 2to3                       | 280 ms                                                          | 263 ms: 1.06x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 45.9 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 86.8 ms: 1.05x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.05x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.04x faster                                                          |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                                         |
| pidigits                   | 199 ms                                                          | 195 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 309 ms: 1.02x faster                                                           |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                         |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| tornado_http               | 105 ms                                                          | 108 ms: 1.03x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 687 ms: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.6 ms: 1.06x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 82.7 ms: 1.10x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 21.0 ms: 1.10x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| telco                      | 5.51 ms                                                         | 6.14 ms: 1.11x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 144 us: 1.14x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 769 us: 1.18x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 232 ms: 2.31x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): json, sympy_expand
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown