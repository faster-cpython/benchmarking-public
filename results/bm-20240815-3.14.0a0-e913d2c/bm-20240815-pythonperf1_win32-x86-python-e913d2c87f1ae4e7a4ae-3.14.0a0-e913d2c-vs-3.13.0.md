# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-x86
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 733 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 200 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_none           | 246 ms                                                          | 228 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 472 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| async_tree_io             | 537 ms                                                          | 552 ms: 1.03x slower                                                           |
| async_generators          | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.6 ms: 1.13x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                          |
| nbody          | 81.9 ms                                                         | 93.3 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| regex_compile  | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.3 us: 1.03x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 69.0 ms: 1.06x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 254 us: 1.07x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.88 sec: 1.09x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 70.0 ms: 1.12x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 51.2 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.8 ms: 1.06x faster                                                          |
| django_template | 32.7 ms                                                         | 31.8 ms: 1.03x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.7 ms: 1.01x slower                                                          |
| mako            | 7.31 ms                                                         | 8.13 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 737 us: 13.77x faster                                                          |
| coverage                  | 333 ms                                                          | 53.0 ms: 6.29x faster                                                          |
| deepcopy                  | 307 us                                                          | 255 us: 1.20x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 733 ms: 1.15x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 22.8 us: 1.15x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.55 us: 1.12x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 200 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_none           | 246 ms                                                          | 228 ms: 1.08x faster                                                           |
| telco                     | 6.67 ms                                                         | 6.20 ms: 1.08x faster                                                          |
| genshi_xml                | 49.5 ms                                                         | 46.8 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 472 ms: 1.05x faster                                                           |
| json_loads                | 21.0 us                                                         | 20.3 us: 1.03x faster                                                          |
| django_template           | 32.7 ms                                                         | 31.8 ms: 1.03x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 87.3 ms: 1.03x faster                                                          |
| pidigits                  | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| bench_mp_pool             | 74.3 ms                                                         | 72.7 ms: 1.02x faster                                                          |
| pycparser                 | 869 ms                                                          | 858 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| python_startup            | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| crypto_pyaes              | 58.2 ms                                                         | 57.6 ms: 1.01x faster                                                          |
| pprint_safe_repr          | 644 ms                                                          | 639 ms: 1.01x faster                                                           |
| gc_traversal              | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 22.7 ms: 1.01x slower                                                          |
| logging_simple            | 7.87 us                                                         | 7.95 us: 1.01x slower                                                          |
| chaos                     | 51.2 ms                                                         | 52.0 ms: 1.02x slower                                                          |
| sympy_expand              | 375 ms                                                          | 382 ms: 1.02x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 110 ms: 1.02x slower                                                           |
| mdp                       | 1.67 sec                                                        | 1.71 sec: 1.02x slower                                                         |
| regex_dna                 | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| sympy_str                 | 215 ms                                                          | 220 ms: 1.02x slower                                                           |
| async_tree_io             | 537 ms                                                          | 552 ms: 1.03x slower                                                           |
| sqlglot_optimize          | 42.5 ms                                                         | 43.8 ms: 1.03x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                          |
| regex_compile             | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| sqlglot_parse             | 1.05 ms                                                         | 1.09 ms: 1.04x slower                                                          |
| regex_v8                  | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| json_dumps                | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.35 ms: 1.04x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 230 ms: 1.04x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 746 us: 1.05x slower                                                           |
| pylint                    | 225 ms                                                          | 236 ms: 1.05x slower                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.36 sec: 1.05x slower                                                         |
| float                     | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 69.0 ms: 1.06x slower                                                          |
| raytrace                  | 205 ms                                                          | 218 ms: 1.06x slower                                                           |
| go                        | 111 ms                                                          | 118 ms: 1.06x slower                                                           |
| typing_runtime_protocols  | 136 us                                                          | 145 us: 1.06x slower                                                           |
| regex_effbot              | 1.81 ms                                                         | 1.93 ms: 1.06x slower                                                          |
| docutils                  | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| pickle_pure_python        | 238 us                                                          | 254 us: 1.07x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 80.6 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.12 ms: 1.07x slower                                                          |
| meteor_contest            | 77.0 ms                                                         | 82.9 ms: 1.08x slower                                                          |
| scimark_sor               | 91.8 ms                                                         | 99.6 ms: 1.08x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.8 us: 1.09x slower                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.88 sec: 1.09x slower                                                         |
| scimark_lu                | 63.5 ms                                                         | 69.4 ms: 1.09x slower                                                          |
| spectral_norm             | 71.3 ms                                                         | 78.2 ms: 1.10x slower                                                          |
| unpickle_pure_python      | 162 us                                                          | 178 us: 1.10x slower                                                           |
| mako                      | 7.31 ms                                                         | 8.13 ms: 1.11x slower                                                          |
| scimark_fft               | 206 ms                                                          | 230 ms: 1.11x slower                                                           |
| xml_etree_generate        | 62.6 ms                                                         | 70.0 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.6 ms: 1.13x slower                                                          |
| deltablue                 | 2.41 ms                                                         | 2.72 ms: 1.13x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 51.2 ms: 1.14x slower                                                          |
| nbody                     | 81.9 ms                                                         | 93.3 ms: 1.14x slower                                                          |
| scimark_monte_carlo       | 50.3 ms                                                         | 57.5 ms: 1.14x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.33 ms: 1.15x slower                                                          |
| richards                  | 33.8 ms                                                         | 38.8 ms: 1.15x slower                                                          |
| richards_super            | 38.0 ms                                                         | 43.6 ms: 1.15x slower                                                          |
| pyflate                   | 326 ms                                                          | 379 ms: 1.16x slower                                                           |
| fannkuch                  | 293 ms                                                          | 347 ms: 1.18x slower                                                           |
| generators                | 22.1 ms                                                         | 27.2 ms: 1.23x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 77.1 ns: 1.25x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (11): json, python_startup_no_site, xml_etree_parse, bench_thread_pool, async_tree_cpu_io_mixed_tg, logging_format, 2to3, dulwich_log, tornado_http, html5lib, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown