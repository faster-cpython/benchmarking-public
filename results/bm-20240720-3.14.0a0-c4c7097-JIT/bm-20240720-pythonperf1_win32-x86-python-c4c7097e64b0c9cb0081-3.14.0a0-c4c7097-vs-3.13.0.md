# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.10x faster
- HPT reliability: 98.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 256 ms: 1.01x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.8 ms: 1.01x faster                                                          |
| tornado_http   | 104 ms                                                          | 106 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 685 ms: 1.23x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 269 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 503 ms: 1.01x faster                                                           |
| async_generators           | 274 ms                                                          | 314 ms: 1.15x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.4 ms: 1.17x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 56.7 ms: 1.44x faster                                                          |
| float          | 57.8 ms                                                         | 43.5 ms: 1.33x faster                                                          |
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 94.3 ms: 1.10x faster                                                          |
| regex_dna      | 117 ms                                                          | 117 ms: 1.01x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                         |
| pickle_pure_python   | 238 us                                                          | 214 us: 1.11x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 151 us: 1.07x faster                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 105 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 62.8 ms: 1.04x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 44.5 ms: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.43 ms: 1.35x faster                                                          |
| django_template | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 52.7 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 751 us: 13.52x faster                                                          |
| coverage                   | 333 ms                                                          | 52.9 ms: 6.30x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 16.1 us: 1.63x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 47.9 ms: 1.49x faster                                                          |
| nbody                      | 81.9 ms                                                         | 56.7 ms: 1.44x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.43 ms: 1.35x faster                                                          |
| float                      | 57.8 ms                                                         | 43.5 ms: 1.33x faster                                                          |
| deepcopy                   | 307 us                                                          | 235 us: 1.31x faster                                                           |
| fannkuch                   | 293 ms                                                          | 233 ms: 1.26x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 46.3 ms: 1.26x faster                                                          |
| scimark_fft                | 206 ms                                                          | 168 ms: 1.23x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 685 ms: 1.23x faster                                                           |
| pyflate                    | 326 ms                                                          | 267 ms: 1.22x faster                                                           |
| telco                      | 6.67 ms                                                         | 5.53 ms: 1.21x faster                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.44 ms: 1.19x faster                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 43.1 ms: 1.17x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.46 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                         |
| pprint_safe_repr           | 644 ms                                                          | 570 ms: 1.13x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 269 ms: 1.12x faster                                                           |
| pickle_pure_python         | 238 us                                                          | 214 us: 1.11x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.17 sec: 1.11x faster                                                         |
| regex_compile              | 103 ms                                                          | 94.3 ms: 1.10x faster                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 959 us: 1.10x faster                                                           |
| comprehensions             | 12.7 us                                                         | 11.7 us: 1.09x faster                                                          |
| meteor_contest             | 77.0 ms                                                         | 70.7 ms: 1.09x faster                                                          |
| unpickle_pure_python       | 162 us                                                          | 151 us: 1.07x faster                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.22 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.05 ms: 1.05x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 58.7 ns: 1.05x faster                                                          |
| pycparser                  | 869 ms                                                          | 835 ms: 1.04x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 105 ms: 1.04x faster                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 62.8 ms: 1.04x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 989 us: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| logging_format             | 8.57 us                                                         | 8.36 us: 1.02x faster                                                          |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 73.5 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| python_startup             | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 87.9 ms: 1.02x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.74 us: 1.02x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 509 ms                                                          | 503 ms: 1.01x faster                                                           |
| xml_etree_process          | 45.0 ms                                                         | 44.5 ms: 1.01x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 47.8 ms: 1.01x faster                                                          |
| richards                   | 33.8 ms                                                         | 33.6 ms: 1.01x faster                                                          |
| hexiom                     | 4.64 ms                                                         | 4.62 ms: 1.00x faster                                                          |
| regex_dna                  | 117 ms                                                          | 117 ms: 1.01x slower                                                           |
| 2to3                       | 253 ms                                                          | 256 ms: 1.01x slower                                                           |
| bench_mp_pool              | 74.3 ms                                                         | 75.4 ms: 1.01x slower                                                          |
| tornado_http               | 104 ms                                                          | 106 ms: 1.02x slower                                                           |
| django_template            | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| genshi_text                | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| go                         | 111 ms                                                          | 114 ms: 1.02x slower                                                           |
| richards_super             | 38.0 ms                                                         | 38.7 ms: 1.02x slower                                                          |
| chaos                      | 51.2 ms                                                         | 52.3 ms: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                          | 383 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 43.6 ms: 1.03x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 231 ms: 1.05x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| genshi_xml                 | 49.5 ms                                                         | 52.7 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 146 us: 1.07x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 766 us: 1.07x slower                                                           |
| pylint                     | 225 ms                                                          | 242 ms: 1.08x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 102 ms: 1.11x slower                                                           |
| raytrace                   | 205 ms                                                          | 229 ms: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.74 ms: 1.14x slower                                                          |
| async_generators           | 274 ms                                                          | 314 ms: 1.15x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.4 ms: 1.17x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 77.6 ms: 1.22x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.5 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (7): python_startup_no_site, sympy_str, json_loads, mdp, sympy_sum, async_tree_io, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown