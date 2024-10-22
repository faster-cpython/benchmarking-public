# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                                     |
| docutils       | 1.82 sec                                                        | 1.92 sec: 1.06x slower                                                                   |
| html5lib       | 48.3 ms                                                         | 49.5 ms: 1.03x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 702 ms: 1.20x faster                                                                     |
| async_tree_memoization_tg | 287 ms                                                          | 250 ms: 1.15x faster                                                                     |
| async_tree_none_tg        | 219 ms                                                          | 198 ms: 1.10x faster                                                                     |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                                     |
| async_tree_none           | 246 ms                                                          | 230 ms: 1.07x faster                                                                     |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 474 ms: 1.04x faster                                                                     |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                                   |
| async_tree_io_tg          | 509 ms                                                          | 517 ms: 1.02x slower                                                                     |
| async_tree_io             | 537 ms                                                          | 559 ms: 1.04x slower                                                                     |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                                    |
| async_generators          | 274 ms                                                          | 311 ms: 1.14x slower                                                                     |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                                     |
| float          | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                                    |
| nbody          | 81.9 ms                                                         | 93.6 ms: 1.14x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                                    |
| regex_compile  | 103 ms                                                          | 110 ms: 1.06x slower                                                                     |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.06x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.2 us: 1.04x faster                                                                    |
| xml_etree_parse      | 109 ms                                                          | 106 ms: 1.03x faster                                                                     |
| json_dumps           | 7.40 ms                                                         | 7.63 ms: 1.03x slower                                                                    |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.7 ms: 1.05x slower                                                                    |
| xml_etree_generate   | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                                    |
| pickle_pure_python   | 238 us                                                          | 257 us: 1.08x slower                                                                     |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.11x slower                                                                   |
| xml_etree_process    | 45.0 ms                                                         | 50.2 ms: 1.11x slower                                                                    |
| unpickle_pure_python | 162 us                                                          | 181 us: 1.12x slower                                                                     |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.5 ms: 1.02x faster                                                                    |
| python_startup         | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                                    |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template | 32.7 ms                                                         | 34.0 ms: 1.04x slower                                                                    |
| genshi_text     | 22.4 ms                                                         | 23.5 ms: 1.05x slower                                                                    |
| mako            | 7.31 ms                                                         | 8.15 ms: 1.12x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 769 us: 13.19x faster                                                                    |
| coverage                  | 333 ms                                                          | 52.1 ms: 6.39x faster                                                                    |
| asyncio_tcp               | 842 ms                                                          | 702 ms: 1.20x faster                                                                     |
| deepcopy                  | 307 us                                                          | 256 us: 1.20x faster                                                                     |
| async_tree_memoization_tg | 287 ms                                                          | 250 ms: 1.15x faster                                                                     |
| deepcopy_memo             | 26.2 us                                                         | 23.4 us: 1.12x faster                                                                    |
| async_tree_none_tg        | 219 ms                                                          | 198 ms: 1.10x faster                                                                     |
| deepcopy_reduce           | 2.85 us                                                         | 2.60 us: 1.10x faster                                                                    |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                                     |
| telco                     | 6.67 ms                                                         | 6.21 ms: 1.07x faster                                                                    |
| async_tree_none           | 246 ms                                                          | 230 ms: 1.07x faster                                                                     |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 474 ms: 1.04x faster                                                                     |
| json_loads                | 21.0 us                                                         | 20.2 us: 1.04x faster                                                                    |
| xml_etree_parse           | 109 ms                                                          | 106 ms: 1.03x faster                                                                     |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                                   |
| python_startup_no_site    | 19.9 ms                                                         | 19.5 ms: 1.02x faster                                                                    |
| python_startup            | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                                    |
| pathlib                   | 89.4 ms                                                         | 88.5 ms: 1.01x faster                                                                    |
| pidigits                  | 202 ms                                                          | 200 ms: 1.01x faster                                                                     |
| bench_mp_pool             | 74.3 ms                                                         | 73.8 ms: 1.01x faster                                                                    |
| pycparser                 | 869 ms                                                          | 873 ms: 1.01x slower                                                                     |
| crypto_pyaes              | 58.2 ms                                                         | 58.6 ms: 1.01x slower                                                                    |
| mdp                       | 1.67 sec                                                        | 1.69 sec: 1.01x slower                                                                   |
| async_tree_io_tg          | 509 ms                                                          | 517 ms: 1.02x slower                                                                     |
| regex_dna                 | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| dulwich_log               | 49.7 ms                                                         | 50.5 ms: 1.02x slower                                                                    |
| logging_format            | 8.57 us                                                         | 8.72 us: 1.02x slower                                                                    |
| 2to3                      | 253 ms                                                          | 258 ms: 1.02x slower                                                                     |
| chaos                     | 51.2 ms                                                         | 52.2 ms: 1.02x slower                                                                    |
| sqlglot_parse             | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                                    |
| sympy_sum                 | 108 ms                                                          | 110 ms: 1.02x slower                                                                     |
| nqueens                   | 75.1 ms                                                         | 76.8 ms: 1.02x slower                                                                    |
| html5lib                  | 48.3 ms                                                         | 49.5 ms: 1.03x slower                                                                    |
| sqlglot_transpile         | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                                    |
| json_dumps                | 7.40 ms                                                         | 7.63 ms: 1.03x slower                                                                    |
| sympy_integrate           | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                                    |
| logging_simple            | 7.87 us                                                         | 8.13 us: 1.03x slower                                                                    |
| regex_v8                  | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                                    |
| django_template           | 32.7 ms                                                         | 34.0 ms: 1.04x slower                                                                    |
| async_tree_io             | 537 ms                                                          | 559 ms: 1.04x slower                                                                     |
| sympy_str                 | 215 ms                                                          | 225 ms: 1.04x slower                                                                     |
| create_gc_cycles          | 713 us                                                          | 746 us: 1.05x slower                                                                     |
| genshi_text               | 22.4 ms                                                         | 23.5 ms: 1.05x slower                                                                    |
| pylint                    | 225 ms                                                          | 236 ms: 1.05x slower                                                                     |
| xml_etree_iterparse       | 65.1 ms                                                         | 68.7 ms: 1.05x slower                                                                    |
| sympy_expand              | 375 ms                                                          | 395 ms: 1.05x slower                                                                     |
| docutils                  | 1.82 sec                                                        | 1.92 sec: 1.06x slower                                                                   |
| sqlglot_optimize          | 42.5 ms                                                         | 45.0 ms: 1.06x slower                                                                    |
| fannkuch                  | 293 ms                                                          | 311 ms: 1.06x slower                                                                     |
| regex_compile             | 103 ms                                                          | 110 ms: 1.06x slower                                                                     |
| regex_effbot              | 1.81 ms                                                         | 1.93 ms: 1.06x slower                                                                    |
| float                     | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                                    |
| scimark_sor               | 91.8 ms                                                         | 98.0 ms: 1.07x slower                                                                    |
| xml_etree_generate        | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                                    |
| sqlglot_normalize         | 220 ms                                                          | 236 ms: 1.07x slower                                                                     |
| pprint_safe_repr          | 644 ms                                                          | 693 ms: 1.08x slower                                                                     |
| scimark_lu                | 63.5 ms                                                         | 68.4 ms: 1.08x slower                                                                    |
| meteor_contest            | 77.0 ms                                                         | 83.2 ms: 1.08x slower                                                                    |
| pickle_pure_python        | 238 us                                                          | 257 us: 1.08x slower                                                                     |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.14 ms: 1.08x slower                                                                    |
| pprint_pformat            | 1.30 sec                                                        | 1.41 sec: 1.09x slower                                                                   |
| raytrace                  | 205 ms                                                          | 226 ms: 1.10x slower                                                                     |
| tomli_loads               | 1.73 sec                                                        | 1.91 sec: 1.11x slower                                                                   |
| typing_runtime_protocols  | 136 us                                                          | 151 us: 1.11x slower                                                                     |
| scimark_monte_carlo       | 50.3 ms                                                         | 55.8 ms: 1.11x slower                                                                    |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                                    |
| scimark_fft               | 206 ms                                                          | 230 ms: 1.11x slower                                                                     |
| xml_etree_process         | 45.0 ms                                                         | 50.2 ms: 1.11x slower                                                                    |
| mako                      | 7.31 ms                                                         | 8.15 ms: 1.12x slower                                                                    |
| pyflate                   | 326 ms                                                          | 364 ms: 1.12x slower                                                                     |
| unpickle_pure_python      | 162 us                                                          | 181 us: 1.12x slower                                                                     |
| go                        | 111 ms                                                          | 125 ms: 1.12x slower                                                                     |
| comprehensions            | 12.7 us                                                         | 14.3 us: 1.13x slower                                                                    |
| richards                  | 33.8 ms                                                         | 38.3 ms: 1.13x slower                                                                    |
| async_generators          | 274 ms                                                          | 311 ms: 1.14x slower                                                                     |
| richards_super            | 38.0 ms                                                         | 43.3 ms: 1.14x slower                                                                    |
| nbody                     | 81.9 ms                                                         | 93.6 ms: 1.14x slower                                                                    |
| deltablue                 | 2.41 ms                                                         | 2.75 ms: 1.14x slower                                                                    |
| spectral_norm             | 71.3 ms                                                         | 81.6 ms: 1.14x slower                                                                    |
| hexiom                    | 4.64 ms                                                         | 5.36 ms: 1.15x slower                                                                    |
| logging_silent            | 61.6 ns                                                         | 76.2 ns: 1.24x slower                                                                    |
| generators                | 22.1 ms                                                         | 27.7 ms: 1.25x slower                                                                    |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                             |

Benchmark hidden because not significant (6): json, bench_thread_pool, genshi_xml, async_tree_cpu_io_mixed_tg, gc_traversal, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown