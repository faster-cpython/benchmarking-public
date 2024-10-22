# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: windows-x86
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 255 ms: 1.01x slower                                                    |
| docutils       | 1.82 sec                                                        | 1.90 sec: 1.04x slower                                                  |
| html5lib       | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                           | 1.00x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 680 ms: 1.24x faster                                                    |
| async_tree_memoization_tg | 287 ms                                                          | 254 ms: 1.13x faster                                                    |
| async_tree_none           | 246 ms                                                          | 218 ms: 1.13x faster                                                    |
| async_tree_memoization    | 302 ms                                                          | 274 ms: 1.10x faster                                                    |
| async_tree_none_tg        | 219 ms                                                          | 199 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 473 ms: 1.04x faster                                                    |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                  |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                    |
| async_generators          | 274 ms                                                          | 305 ms: 1.12x slower                                                    |
| coroutines                | 15.7 ms                                                         | 18.4 ms: 1.18x slower                                                   |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 201 ms: 1.00x faster                                                    |
| float          | 57.8 ms                                                         | 63.6 ms: 1.10x slower                                                   |
| nbody          | 81.9 ms                                                         | 96.4 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                           | 1.09x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                   |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                   |
| regex_compile  | 103 ms                                                          | 111 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                           | 1.04x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.3 us: 1.07x faster                                                   |
| pickle               | 8.42 us                                                         | 7.95 us: 1.06x faster                                                   |
| unpickle             | 10.5 us                                                         | 10.2 us: 1.03x faster                                                   |
| pickle_list          | 3.40 us                                                         | 3.31 us: 1.03x faster                                                   |
| unpickle_list        | 3.09 us                                                         | 3.02 us: 1.02x faster                                                   |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                    |
| json_loads           | 21.0 us                                                         | 20.9 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                   |
| json_dumps           | 7.40 ms                                                         | 7.75 ms: 1.05x slower                                                   |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                  |
| xml_etree_generate   | 62.6 ms                                                         | 69.3 ms: 1.11x slower                                                   |
| pickle_pure_python   | 238 us                                                          | 268 us: 1.13x slower                                                    |
| xml_etree_process    | 45.0 ms                                                         | 52.5 ms: 1.17x slower                                                   |
| unpickle_pure_python | 162 us                                                          | 190 us: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                   |
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.6 ms: 1.06x faster                                                   |
| genshi_text     | 22.4 ms                                                         | 23.0 ms: 1.02x slower                                                   |
| django_template | 32.7 ms                                                         | 35.2 ms: 1.08x slower                                                   |
| mako            | 7.31 ms                                                         | 8.22 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 745 us: 13.61x faster                                                   |
| coverage                  | 333 ms                                                          | 54.0 ms: 6.16x faster                                                   |
| deepcopy                  | 307 us                                                          | 244 us: 1.26x faster                                                    |
| asyncio_tcp               | 842 ms                                                          | 680 ms: 1.24x faster                                                    |
| deepcopy_memo             | 26.2 us                                                         | 22.1 us: 1.18x faster                                                   |
| async_tree_memoization_tg | 287 ms                                                          | 254 ms: 1.13x faster                                                    |
| async_tree_none           | 246 ms                                                          | 218 ms: 1.13x faster                                                    |
| deepcopy_reduce           | 2.85 us                                                         | 2.58 us: 1.10x faster                                                   |
| async_tree_memoization    | 302 ms                                                          | 274 ms: 1.10x faster                                                    |
| async_tree_none_tg        | 219 ms                                                          | 199 ms: 1.10x faster                                                    |
| pickle_dict               | 21.7 us                                                         | 20.3 us: 1.07x faster                                                   |
| genshi_xml                | 49.5 ms                                                         | 46.6 ms: 1.06x faster                                                   |
| pickle                    | 8.42 us                                                         | 7.95 us: 1.06x faster                                                   |
| html5lib                  | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 473 ms: 1.04x faster                                                    |
| pathlib                   | 89.4 ms                                                         | 86.5 ms: 1.03x faster                                                   |
| unpickle                  | 10.5 us                                                         | 10.2 us: 1.03x faster                                                   |
| pickle_list               | 3.40 us                                                         | 3.31 us: 1.03x faster                                                   |
| unpickle_list             | 3.09 us                                                         | 3.02 us: 1.02x faster                                                   |
| python_startup            | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                   |
| bench_mp_pool             | 74.3 ms                                                         | 73.1 ms: 1.02x faster                                                   |
| xml_etree_parse           | 109 ms                                                          | 107 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                  |
| python_startup_no_site    | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                   |
| sqlite_synth              | 1.97 us                                                         | 1.95 us: 1.01x faster                                                   |
| json_loads                | 21.0 us                                                         | 20.9 us: 1.01x faster                                                   |
| go                        | 111 ms                                                          | 111 ms: 1.00x faster                                                    |
| pidigits                  | 202 ms                                                          | 201 ms: 1.00x faster                                                    |
| 2to3                      | 253 ms                                                          | 255 ms: 1.01x slower                                                    |
| pycparser                 | 869 ms                                                          | 875 ms: 1.01x slower                                                    |
| sympy_sum                 | 108 ms                                                          | 109 ms: 1.01x slower                                                    |
| mdp                       | 1.67 sec                                                        | 1.70 sec: 1.01x slower                                                  |
| crypto_pyaes              | 58.2 ms                                                         | 59.0 ms: 1.01x slower                                                   |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                    |
| genshi_text               | 22.4 ms                                                         | 23.0 ms: 1.02x slower                                                   |
| telco                     | 6.67 ms                                                         | 6.85 ms: 1.03x slower                                                   |
| nqueens                   | 75.1 ms                                                         | 77.5 ms: 1.03x slower                                                   |
| regex_v8                  | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                   |
| sympy_str                 | 215 ms                                                          | 222 ms: 1.03x slower                                                    |
| logging_format            | 8.57 us                                                         | 8.90 us: 1.04x slower                                                   |
| meteor_contest            | 77.0 ms                                                         | 80.1 ms: 1.04x slower                                                   |
| xml_etree_iterparse       | 65.1 ms                                                         | 67.8 ms: 1.04x slower                                                   |
| docutils                  | 1.82 sec                                                        | 1.90 sec: 1.04x slower                                                  |
| logging_simple            | 7.87 us                                                         | 8.23 us: 1.05x slower                                                   |
| json_dumps                | 7.40 ms                                                         | 7.75 ms: 1.05x slower                                                   |
| dulwich_log               | 49.7 ms                                                         | 52.1 ms: 1.05x slower                                                   |
| sympy_expand              | 375 ms                                                          | 394 ms: 1.05x slower                                                    |
| pylint                    | 225 ms                                                          | 236 ms: 1.05x slower                                                    |
| regex_effbot              | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                   |
| pprint_safe_repr          | 644 ms                                                          | 679 ms: 1.05x slower                                                    |
| sympy_integrate           | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                                   |
| unpack_sequence           | 42.9 ns                                                         | 45.4 ns: 1.06x slower                                                   |
| sqlglot_transpile         | 1.29 ms                                                         | 1.37 ms: 1.06x slower                                                   |
| sqlglot_parse             | 1.05 ms                                                         | 1.12 ms: 1.06x slower                                                   |
| regex_compile             | 103 ms                                                          | 111 ms: 1.07x slower                                                    |
| create_gc_cycles          | 713 us                                                          | 764 us: 1.07x slower                                                    |
| typing_runtime_protocols  | 136 us                                                          | 146 us: 1.07x slower                                                    |
| django_template           | 32.7 ms                                                         | 35.2 ms: 1.08x slower                                                   |
| sqlglot_normalize         | 220 ms                                                          | 240 ms: 1.09x slower                                                    |
| sqlglot_optimize          | 42.5 ms                                                         | 46.4 ms: 1.09x slower                                                   |
| chaos                     | 51.2 ms                                                         | 56.1 ms: 1.10x slower                                                   |
| float                     | 57.8 ms                                                         | 63.6 ms: 1.10x slower                                                   |
| tomli_loads               | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                  |
| fannkuch                  | 293 ms                                                          | 324 ms: 1.10x slower                                                    |
| pprint_pformat            | 1.30 sec                                                        | 1.44 sec: 1.11x slower                                                  |
| xml_etree_generate        | 62.6 ms                                                         | 69.3 ms: 1.11x slower                                                   |
| comprehensions            | 12.7 us                                                         | 14.1 us: 1.11x slower                                                   |
| async_generators          | 274 ms                                                          | 305 ms: 1.12x slower                                                    |
| scimark_lu                | 63.5 ms                                                         | 71.1 ms: 1.12x slower                                                   |
| scimark_sor               | 91.8 ms                                                         | 103 ms: 1.12x slower                                                    |
| mako                      | 7.31 ms                                                         | 8.22 ms: 1.13x slower                                                   |
| spectral_norm             | 71.3 ms                                                         | 80.5 ms: 1.13x slower                                                   |
| pickle_pure_python        | 238 us                                                          | 268 us: 1.13x slower                                                    |
| pyflate                   | 326 ms                                                          | 369 ms: 1.13x slower                                                    |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.29 ms: 1.13x slower                                                   |
| scimark_fft               | 206 ms                                                          | 237 ms: 1.15x slower                                                    |
| hexiom                    | 4.64 ms                                                         | 5.34 ms: 1.15x slower                                                   |
| scimark_monte_carlo       | 50.3 ms                                                         | 58.6 ms: 1.16x slower                                                   |
| xml_etree_process         | 45.0 ms                                                         | 52.5 ms: 1.17x slower                                                   |
| deltablue                 | 2.41 ms                                                         | 2.82 ms: 1.17x slower                                                   |
| coroutines                | 15.7 ms                                                         | 18.4 ms: 1.18x slower                                                   |
| unpickle_pure_python      | 162 us                                                          | 190 us: 1.18x slower                                                    |
| nbody                     | 81.9 ms                                                         | 96.4 ms: 1.18x slower                                                   |
| richards                  | 33.8 ms                                                         | 40.8 ms: 1.21x slower                                                   |
| logging_silent            | 61.6 ns                                                         | 75.6 ns: 1.23x slower                                                   |
| richards_super            | 38.0 ms                                                         | 47.0 ms: 1.24x slower                                                   |
| generators                | 22.1 ms                                                         | 27.5 ms: 1.25x slower                                                   |
| raytrace                  | 205 ms                                                          | 259 ms: 1.26x slower                                                    |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                            |

Benchmark hidden because not significant (7): bench_thread_pool, async_tree_cpu_io_mixed_tg, regex_dna, gc_traversal, async_tree_io, tornado_http, json
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown