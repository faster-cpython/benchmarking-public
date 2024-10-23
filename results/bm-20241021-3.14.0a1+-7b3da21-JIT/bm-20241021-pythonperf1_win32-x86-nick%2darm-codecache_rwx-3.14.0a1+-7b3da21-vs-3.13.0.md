# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.08x faster
- HPT reliability: 95.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                         |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                       |
| html5lib       | 48.3 ms                                                         | 45.1 ms: 1.07x faster                                                        |
| tornado_http   | 104 ms                                                          | 109 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                         |
| async_tree_none           | 246 ms                                                          | 222 ms: 1.11x faster                                                         |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                         |
| async_tree_none_tg        | 219 ms                                                          | 203 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 468 ms: 1.06x faster                                                         |
| async_tree_io             | 537 ms                                                          | 525 ms: 1.02x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 549 ms: 1.08x slower                                                         |
| coroutines                | 15.7 ms                                                         | 17.6 ms: 1.12x slower                                                        |
| async_generators          | 274 ms                                                          | 324 ms: 1.18x slower                                                         |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 56.4 ms: 1.45x faster                                                        |
| float          | 57.8 ms                                                         | 45.8 ms: 1.26x faster                                                        |
| pidigits       | 202 ms                                                          | 204 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 98.5 ms: 1.05x faster                                                        |
| regex_effbot   | 1.81 ms                                                         | 1.79 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.52 sec: 1.14x faster                                                       |
| xml_etree_generate   | 62.6 ms                                                         | 55.5 ms: 1.13x faster                                                        |
| xml_etree_process    | 45.0 ms                                                         | 41.0 ms: 1.10x faster                                                        |
| unpickle_pure_python | 162 us                                                          | 158 us: 1.02x faster                                                         |
| xml_etree_iterparse  | 65.1 ms                                                         | 64.1 ms: 1.02x faster                                                        |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                        |
| pickle_pure_python   | 238 us                                                          | 241 us: 1.01x slower                                                         |
| xml_etree_parse      | 109 ms                                                          | 111 ms: 1.02x slower                                                         |
| json_dumps           | 7.40 ms                                                         | 8.11 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                        |
| python_startup         | 24.3 ms                                                         | 27.0 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.68 ms: 1.29x faster                                                        |
| django_template | 32.7 ms                                                         | 33.5 ms: 1.03x slower                                                        |
| genshi_xml      | 49.5 ms                                                         | 52.2 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 789 us: 12.86x faster                                                        |
| coverage                  | 333 ms                                                          | 53.1 ms: 6.27x faster                                                        |
| deepcopy_memo             | 26.2 us                                                         | 16.3 us: 1.61x faster                                                        |
| nbody                     | 81.9 ms                                                         | 56.4 ms: 1.45x faster                                                        |
| deepcopy                  | 307 us                                                          | 227 us: 1.35x faster                                                         |
| fannkuch                  | 293 ms                                                          | 219 ms: 1.34x faster                                                         |
| scimark_monte_carlo       | 50.3 ms                                                         | 38.3 ms: 1.31x faster                                                        |
| scimark_sor               | 91.8 ms                                                         | 70.4 ms: 1.31x faster                                                        |
| mako                      | 7.31 ms                                                         | 5.68 ms: 1.29x faster                                                        |
| float                     | 57.8 ms                                                         | 45.8 ms: 1.26x faster                                                        |
| spectral_norm             | 71.3 ms                                                         | 58.4 ms: 1.22x faster                                                        |
| go                        | 111 ms                                                          | 92.2 ms: 1.21x faster                                                        |
| deepcopy_reduce           | 2.85 us                                                         | 2.41 us: 1.18x faster                                                        |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.46 ms: 1.18x faster                                                        |
| crypto_pyaes              | 58.2 ms                                                         | 49.7 ms: 1.17x faster                                                        |
| telco                     | 6.67 ms                                                         | 5.72 ms: 1.17x faster                                                        |
| tomli_loads               | 1.73 sec                                                        | 1.52 sec: 1.14x faster                                                       |
| pprint_safe_repr          | 644 ms                                                          | 570 ms: 1.13x faster                                                         |
| xml_etree_generate        | 62.6 ms                                                         | 55.5 ms: 1.13x faster                                                        |
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                         |
| scimark_fft               | 206 ms                                                          | 184 ms: 1.12x faster                                                         |
| async_tree_none           | 246 ms                                                          | 222 ms: 1.11x faster                                                         |
| pprint_pformat            | 1.30 sec                                                        | 1.17 sec: 1.11x faster                                                       |
| logging_silent            | 61.6 ns                                                         | 55.8 ns: 1.10x faster                                                        |
| meteor_contest            | 77.0 ms                                                         | 69.9 ms: 1.10x faster                                                        |
| pyflate                   | 326 ms                                                          | 296 ms: 1.10x faster                                                         |
| xml_etree_process         | 45.0 ms                                                         | 41.0 ms: 1.10x faster                                                        |
| pycparser                 | 869 ms                                                          | 798 ms: 1.09x faster                                                         |
| comprehensions            | 12.7 us                                                         | 11.7 us: 1.09x faster                                                        |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                         |
| async_tree_none_tg        | 219 ms                                                          | 203 ms: 1.07x faster                                                         |
| html5lib                  | 48.3 ms                                                         | 45.1 ms: 1.07x faster                                                        |
| scimark_lu                | 63.5 ms                                                         | 59.6 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 468 ms: 1.06x faster                                                         |
| regex_compile             | 103 ms                                                          | 98.5 ms: 1.05x faster                                                        |
| sqlglot_parse             | 1.05 ms                                                         | 1.01 ms: 1.04x faster                                                        |
| logging_simple            | 7.87 us                                                         | 7.58 us: 1.04x faster                                                        |
| logging_format            | 8.57 us                                                         | 8.28 us: 1.03x faster                                                        |
| dulwich_log               | 49.7 ms                                                         | 48.3 ms: 1.03x faster                                                        |
| async_tree_io             | 537 ms                                                          | 525 ms: 1.02x faster                                                         |
| unpickle_pure_python      | 162 us                                                          | 158 us: 1.02x faster                                                         |
| pathlib                   | 89.4 ms                                                         | 88.1 ms: 1.02x faster                                                        |
| xml_etree_iterparse       | 65.1 ms                                                         | 64.1 ms: 1.02x faster                                                        |
| regex_effbot              | 1.81 ms                                                         | 1.79 ms: 1.01x faster                                                        |
| generators                | 22.1 ms                                                         | 21.8 ms: 1.01x faster                                                        |
| 2to3                      | 253 ms                                                          | 251 ms: 1.01x faster                                                         |
| json_loads                | 21.0 us                                                         | 20.8 us: 1.01x faster                                                        |
| nqueens                   | 75.1 ms                                                         | 75.9 ms: 1.01x slower                                                        |
| pidigits                  | 202 ms                                                          | 204 ms: 1.01x slower                                                         |
| sympy_sum                 | 108 ms                                                          | 109 ms: 1.01x slower                                                         |
| sqlglot_transpile         | 1.29 ms                                                         | 1.31 ms: 1.01x slower                                                        |
| pickle_pure_python        | 238 us                                                          | 241 us: 1.01x slower                                                         |
| sympy_str                 | 215 ms                                                          | 220 ms: 1.02x slower                                                         |
| python_startup_no_site    | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                        |
| xml_etree_parse           | 109 ms                                                          | 111 ms: 1.02x slower                                                         |
| hexiom                    | 4.64 ms                                                         | 4.75 ms: 1.02x slower                                                        |
| django_template           | 32.7 ms                                                         | 33.5 ms: 1.03x slower                                                        |
| sympy_expand              | 375 ms                                                          | 387 ms: 1.03x slower                                                         |
| typing_runtime_protocols  | 136 us                                                          | 143 us: 1.05x slower                                                         |
| tornado_http              | 104 ms                                                          | 109 ms: 1.05x slower                                                         |
| genshi_xml                | 49.5 ms                                                         | 52.2 ms: 1.05x slower                                                        |
| deltablue                 | 2.41 ms                                                         | 2.54 ms: 1.05x slower                                                        |
| chaos                     | 51.2 ms                                                         | 54.5 ms: 1.06x slower                                                        |
| docutils                  | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                       |
| sqlglot_normalize         | 220 ms                                                          | 236 ms: 1.08x slower                                                         |
| async_tree_io_tg          | 509 ms                                                          | 549 ms: 1.08x slower                                                         |
| richards                  | 33.8 ms                                                         | 36.7 ms: 1.09x slower                                                        |
| json_dumps                | 7.40 ms                                                         | 8.11 ms: 1.09x slower                                                        |
| richards_super            | 38.0 ms                                                         | 41.6 ms: 1.10x slower                                                        |
| sqlglot_optimize          | 42.5 ms                                                         | 46.9 ms: 1.11x slower                                                        |
| sympy_integrate           | 15.2 ms                                                         | 16.8 ms: 1.11x slower                                                        |
| python_startup            | 24.3 ms                                                         | 27.0 ms: 1.11x slower                                                        |
| coroutines                | 15.7 ms                                                         | 17.6 ms: 1.12x slower                                                        |
| pylint                    | 225 ms                                                          | 261 ms: 1.16x slower                                                         |
| json                      | 4.27 ms                                                         | 5.03 ms: 1.18x slower                                                        |
| async_generators          | 274 ms                                                          | 324 ms: 1.18x slower                                                         |
| bench_mp_pool             | 74.3 ms                                                         | 91.8 ms: 1.24x slower                                                        |
| gc_traversal              | 1.45 ms                                                         | 1.80 ms: 1.24x slower                                                        |
| raytrace                  | 205 ms                                                          | 274 ms: 1.33x slower                                                         |
| create_gc_cycles          | 713 us                                                          | 1.19 ms: 1.67x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.08x faster                                                                 |

Benchmark hidden because not significant (6): bench_thread_pool, genshi_text, async_tree_cpu_io_mixed_tg, regex_dna, regex_v8, mdp
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: sphinx

# HPT report

- Reliability score: 95.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown