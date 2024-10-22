# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.02x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| tornado_http   | 104 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 655 ms: 1.29x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| async_tree_none           | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 522 ms: 1.02x slower                                                           |
| async_generators          | 274 ms                                                          | 291 ms: 1.06x slower                                                           |
| coroutines                | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 61.6 ms: 1.07x slower                                                          |
| nbody          | 81.9 ms                                                         | 94.2 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                          |
| regex_compile  | 103 ms                                                          | 109 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| pickle               | 8.42 us                                                         | 7.99 us: 1.05x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.96 us: 1.05x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.7 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 67.8 ms: 1.08x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 50.1 ms: 1.11x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 269 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.9 ms: 1.01x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 21.7 ms: 1.03x faster                                                          |
| genshi_xml      | 49.5 ms                                                         | 48.9 ms: 1.01x faster                                                          |
| django_template | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| mako            | 7.31 ms                                                         | 8.00 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 748 us: 13.56x faster                                                          |
| coverage                  | 333 ms                                                          | 53.2 ms: 6.26x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 655 ms: 1.29x faster                                                           |
| deepcopy                  | 307 us                                                          | 244 us: 1.26x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 21.8 us: 1.20x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.14x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.53 us: 1.13x faster                                                          |
| async_tree_none           | 246 ms                                                          | 221 ms: 1.11x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| tornado_http              | 104 ms                                                          | 95.2 ms: 1.10x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pathlib                   | 89.4 ms                                                         | 82.9 ms: 1.08x faster                                                          |
| pickle_dict               | 21.7 us                                                         | 20.4 us: 1.06x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| pickle                    | 8.42 us                                                         | 7.99 us: 1.05x faster                                                          |
| unpickle_list             | 3.09 us                                                         | 2.96 us: 1.05x faster                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 71.5 ms: 1.04x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 21.7 ms: 1.03x faster                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.41 ms: 1.03x faster                                                          |
| unpickle                  | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| html5lib                  | 48.3 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| pidigits                  | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| 2to3                      | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| python_startup            | 24.3 ms                                                         | 23.9 ms: 1.01x faster                                                          |
| json_loads                | 21.0 us                                                         | 20.7 us: 1.01x faster                                                          |
| genshi_xml                | 49.5 ms                                                         | 48.9 ms: 1.01x faster                                                          |
| nqueens                   | 75.1 ms                                                         | 74.4 ms: 1.01x faster                                                          |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| sqlglot_parse             | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                                          |
| sympy_str                 | 215 ms                                                          | 217 ms: 1.01x slower                                                           |
| docutils                  | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                         |
| python_startup_no_site    | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.4 ms: 1.02x slower                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.32 ms: 1.02x slower                                                          |
| regex_dna                 | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 509 ms                                                          | 522 ms: 1.02x slower                                                           |
| dulwich_log               | 49.7 ms                                                         | 50.9 ms: 1.02x slower                                                          |
| sympy_expand              | 375 ms                                                          | 385 ms: 1.03x slower                                                           |
| logging_format            | 8.57 us                                                         | 8.81 us: 1.03x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 735 us: 1.03x slower                                                           |
| logging_simple            | 7.87 us                                                         | 8.15 us: 1.04x slower                                                          |
| pprint_safe_repr          | 644 ms                                                          | 670 ms: 1.04x slower                                                           |
| xml_etree_iterparse       | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 44.4 ms: 1.05x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 230 ms: 1.05x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 16.3 ms: 1.05x slower                                                          |
| meteor_contest            | 77.0 ms                                                         | 81.0 ms: 1.05x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                          |
| pprint_pformat            | 1.30 sec                                                        | 1.37 sec: 1.06x slower                                                         |
| telco                     | 6.67 ms                                                         | 7.04 ms: 1.06x slower                                                          |
| regex_compile             | 103 ms                                                          | 109 ms: 1.06x slower                                                           |
| spectral_norm             | 71.3 ms                                                         | 75.6 ms: 1.06x slower                                                          |
| unpack_sequence           | 42.9 ns                                                         | 45.5 ns: 1.06x slower                                                          |
| django_template           | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| async_generators          | 274 ms                                                          | 291 ms: 1.06x slower                                                           |
| float                     | 57.8 ms                                                         | 61.6 ms: 1.07x slower                                                          |
| chaos                     | 51.2 ms                                                         | 54.7 ms: 1.07x slower                                                          |
| scimark_sor               | 91.8 ms                                                         | 98.3 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.12 ms: 1.07x slower                                                          |
| mdp                       | 1.67 sec                                                        | 1.80 sec: 1.08x slower                                                         |
| pyflate                   | 326 ms                                                          | 353 ms: 1.08x slower                                                           |
| tomli_loads               | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| xml_etree_generate        | 62.6 ms                                                         | 67.8 ms: 1.08x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 148 us: 1.08x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 69.0 ms: 1.09x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.9 us: 1.09x slower                                                          |
| mako                      | 7.31 ms                                                         | 8.00 ms: 1.10x slower                                                          |
| fannkuch                  | 293 ms                                                          | 322 ms: 1.10x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_process         | 45.0 ms                                                         | 50.1 ms: 1.11x slower                                                          |
| pickle_pure_python        | 238 us                                                          | 269 us: 1.13x slower                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 56.9 ms: 1.13x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.27 ms: 1.14x slower                                                          |
| scimark_fft               | 206 ms                                                          | 236 ms: 1.14x slower                                                           |
| nbody                     | 81.9 ms                                                         | 94.2 ms: 1.15x slower                                                          |
| raytrace                  | 205 ms                                                          | 238 ms: 1.16x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.79 ms: 1.16x slower                                                          |
| generators                | 22.1 ms                                                         | 25.9 ms: 1.17x slower                                                          |
| coroutines                | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| richards                  | 33.8 ms                                                         | 40.0 ms: 1.18x slower                                                          |
| richards_super            | 38.0 ms                                                         | 46.0 ms: 1.21x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 75.0 ns: 1.22x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (12): bench_thread_pool, async_tree_cpu_io_mixed_tg, xml_etree_parse, sqlite_synth, json_dumps, crypto_pyaes, go, json, pycparser, async_tree_io, pickle_list, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown