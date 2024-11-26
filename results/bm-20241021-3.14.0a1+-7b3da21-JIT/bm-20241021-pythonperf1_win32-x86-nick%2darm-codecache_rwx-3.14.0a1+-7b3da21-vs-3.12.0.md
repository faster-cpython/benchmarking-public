# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.12x faster                                                         |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                       |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.36x faster                                                         |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                         |
| async_tree_io              | 693 ms                                                          | 525 ms: 1.32x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                         |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 56.4 ms: 2.25x faster                                                        |
| float          | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                        |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                           | 1.54x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 98.5 ms: 1.31x faster                                                        |
| regex_effbot   | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                        |
| regex_dna      | 127 ms                                                          | 116 ms: 1.09x faster                                                         |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.52 sec: 1.45x faster                                                       |
| unpickle_pure_python | 210 us                                                          | 158 us: 1.33x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 55.5 ms: 1.30x faster                                                        |
| xml_etree_process    | 53.2 ms                                                         | 41.0 ms: 1.30x faster                                                        |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.1 ms: 1.21x faster                                                        |
| pickle_pure_python   | 286 us                                                          | 241 us: 1.18x faster                                                         |
| xml_etree_parse      | 113 ms                                                          | 111 ms: 1.01x faster                                                         |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                        |
| json_dumps           | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                        |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                        |
| django_template | 36.9 ms                                                         | 33.5 ms: 1.10x faster                                                        |
| Geometric mean  | (ref)                                                           | 1.39x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.3 us: 2.36x faster                                                        |
| nbody                      | 127 ms                                                          | 56.4 ms: 2.25x faster                                                        |
| scimark_sor                | 130 ms                                                          | 70.4 ms: 1.84x faster                                                        |
| logging_silent             | 101 ns                                                          | 55.8 ns: 1.81x faster                                                        |
| spectral_norm              | 104 ms                                                          | 58.4 ms: 1.78x faster                                                        |
| generators                 | 38.5 ms                                                         | 21.8 ms: 1.76x faster                                                        |
| mako                       | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                        |
| scimark_monte_carlo        | 66.4 ms                                                         | 38.3 ms: 1.73x faster                                                        |
| float                      | 76.7 ms                                                         | 45.8 ms: 1.67x faster                                                        |
| comprehensions             | 19.2 us                                                         | 11.7 us: 1.64x faster                                                        |
| fannkuch                   | 354 ms                                                          | 219 ms: 1.61x faster                                                         |
| deepcopy                   | 360 us                                                          | 227 us: 1.59x faster                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.46 ms: 1.57x faster                                                        |
| scimark_lu                 | 93.2 ms                                                         | 59.6 ms: 1.56x faster                                                        |
| go                         | 137 ms                                                          | 92.2 ms: 1.49x faster                                                        |
| scimark_fft                | 271 ms                                                          | 184 ms: 1.47x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.52 sec: 1.45x faster                                                       |
| hexiom                     | 6.82 ms                                                         | 4.75 ms: 1.43x faster                                                        |
| pyflate                    | 424 ms                                                          | 296 ms: 1.43x faster                                                         |
| deltablue                  | 3.58 ms                                                         | 2.54 ms: 1.41x faster                                                        |
| crypto_pyaes               | 69.2 ms                                                         | 49.7 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.36x faster                                                         |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.41 us: 1.34x faster                                                        |
| unpickle_pure_python       | 210 us                                                          | 158 us: 1.33x faster                                                         |
| async_tree_io              | 693 ms                                                          | 525 ms: 1.32x faster                                                         |
| regex_compile              | 129 ms                                                          | 98.5 ms: 1.31x faster                                                        |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 55.5 ms: 1.30x faster                                                        |
| xml_etree_process          | 53.2 ms                                                         | 41.0 ms: 1.30x faster                                                        |
| logging_simple             | 9.75 us                                                         | 7.58 us: 1.29x faster                                                        |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                       |
| chaos                      | 69.4 ms                                                         | 54.5 ms: 1.27x faster                                                        |
| pprint_safe_repr           | 721 ms                                                          | 570 ms: 1.26x faster                                                         |
| logging_format             | 10.4 us                                                         | 8.28 us: 1.26x faster                                                        |
| meteor_contest             | 86.9 ms                                                         | 69.9 ms: 1.24x faster                                                        |
| sqlglot_parse              | 1.25 ms                                                         | 1.01 ms: 1.24x faster                                                        |
| nqueens                    | 93.7 ms                                                         | 75.9 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                         |
| pycparser                  | 978 ms                                                          | 798 ms: 1.23x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.1 ms: 1.21x faster                                                        |
| dulwich_log                | 58.5 ms                                                         | 48.3 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.21x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 17.6 ms: 1.19x faster                                                        |
| pickle_pure_python         | 286 us                                                          | 241 us: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.31 ms: 1.17x faster                                                        |
| regex_effbot               | 2.04 ms                                                         | 1.79 ms: 1.14x faster                                                        |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                       |
| raytrace                   | 308 ms                                                          | 274 ms: 1.13x faster                                                         |
| richards                   | 41.3 ms                                                         | 36.7 ms: 1.13x faster                                                        |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.12x faster                                                         |
| 2to3                       | 280 ms                                                          | 251 ms: 1.12x faster                                                         |
| richards_super             | 46.5 ms                                                         | 41.6 ms: 1.12x faster                                                        |
| django_template            | 36.9 ms                                                         | 33.5 ms: 1.10x faster                                                        |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.09x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                        |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 16.8 ms: 1.04x faster                                                        |
| pathlib                    | 91.4 ms                                                         | 88.1 ms: 1.04x faster                                                        |
| sqlglot_optimize           | 48.5 ms                                                         | 46.9 ms: 1.03x faster                                                        |
| sympy_expand               | 398 ms                                                          | 387 ms: 1.03x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                       |
| xml_etree_parse            | 113 ms                                                          | 111 ms: 1.01x faster                                                         |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                        |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                         |
| async_generators           | 313 ms                                                          | 324 ms: 1.03x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                        |
| telco                      | 5.51 ms                                                         | 5.72 ms: 1.04x slower                                                        |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                         |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                        |
| json_dumps                 | 7.40 ms                                                         | 8.11 ms: 1.10x slower                                                        |
| coverage                   | 48.4 ms                                                         | 53.1 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                         |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                        |
| json                       | 4.15 ms                                                         | 5.03 ms: 1.21x slower                                                        |
| bench_mp_pool              | 75.4 ms                                                         | 91.8 ms: 1.22x slower                                                        |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                        |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.83x slower                                                        |
| sqlglot_normalize          | 100 ms                                                          | 236 ms: 2.36x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                 |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.212x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown