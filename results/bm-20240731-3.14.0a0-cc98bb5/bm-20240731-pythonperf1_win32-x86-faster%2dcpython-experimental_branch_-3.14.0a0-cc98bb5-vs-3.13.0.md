# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 262 ms: 1.03x slower                                                                     |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.06x slower                                                                   |
| html5lib       | 48.3 ms                                                         | 49.1 ms: 1.02x slower                                                                    |
| tornado_http   | 104 ms                                                          | 106 ms: 1.02x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 708 ms: 1.19x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 202 ms: 1.08x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 232 ms: 1.06x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 285 ms: 1.06x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 486 ms: 1.02x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 474 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 509 ms                                                          | 523 ms: 1.03x slower                                                                     |
| async_tree_io              | 537 ms                                                          | 564 ms: 1.05x slower                                                                     |
| async_generators           | 274 ms                                                          | 294 ms: 1.08x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 201 ms: 1.00x faster                                                                     |
| float          | 57.8 ms                                                         | 60.0 ms: 1.04x slower                                                                    |
| nbody          | 81.9 ms                                                         | 99.2 ms: 1.21x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                                    |
| regex_compile  | 103 ms                                                          | 109 ms: 1.05x slower                                                                     |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.05x faster                                                                     |
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                                    |
| json_dumps           | 7.40 ms                                                         | 7.35 ms: 1.01x faster                                                                    |
| tomli_loads          | 1.73 sec                                                        | 1.79 sec: 1.03x slower                                                                   |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                                    |
| xml_etree_generate   | 62.6 ms                                                         | 66.2 ms: 1.06x slower                                                                    |
| unpickle_pure_python | 162 us                                                          | 173 us: 1.07x slower                                                                     |
| xml_etree_process    | 45.0 ms                                                         | 48.6 ms: 1.08x slower                                                                    |
| pickle_pure_python   | 238 us                                                          | 257 us: 1.08x slower                                                                     |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.4 ms: 1.02x faster                                                                    |
| django_template | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                                                    |
| mako            | 7.31 ms                                                         | 8.24 ms: 1.13x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 769 us: 13.19x faster                                                                    |
| coverage                   | 333 ms                                                          | 51.9 ms: 6.41x faster                                                                    |
| asyncio_tcp                | 842 ms                                                          | 708 ms: 1.19x faster                                                                     |
| deepcopy                   | 307 us                                                          | 259 us: 1.18x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                                     |
| deepcopy_memo              | 26.2 us                                                         | 23.3 us: 1.12x faster                                                                    |
| deepcopy_reduce            | 2.85 us                                                         | 2.60 us: 1.10x faster                                                                    |
| async_tree_none_tg         | 219 ms                                                          | 202 ms: 1.08x faster                                                                     |
| telco                      | 6.67 ms                                                         | 6.24 ms: 1.07x faster                                                                    |
| async_tree_none            | 246 ms                                                          | 232 ms: 1.06x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 285 ms: 1.06x faster                                                                     |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.05x faster                                                                     |
| bench_thread_pool          | 1.02 ms                                                         | 991 us: 1.03x faster                                                                     |
| json_loads                 | 21.0 us                                                         | 20.4 us: 1.03x faster                                                                    |
| genshi_xml                 | 49.5 ms                                                         | 48.4 ms: 1.02x faster                                                                    |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 486 ms: 1.02x faster                                                                     |
| bench_mp_pool              | 74.3 ms                                                         | 73.7 ms: 1.01x faster                                                                    |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                                    |
| json_dumps                 | 7.40 ms                                                         | 7.35 ms: 1.01x faster                                                                    |
| pidigits                   | 202 ms                                                          | 201 ms: 1.00x faster                                                                     |
| tornado_http               | 104 ms                                                          | 106 ms: 1.02x slower                                                                     |
| crypto_pyaes               | 58.2 ms                                                         | 59.1 ms: 1.02x slower                                                                    |
| html5lib                   | 48.3 ms                                                         | 49.1 ms: 1.02x slower                                                                    |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                                     |
| mdp                        | 1.67 sec                                                        | 1.71 sec: 1.02x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 474 ms: 1.02x slower                                                                     |
| python_startup_no_site     | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                                    |
| async_tree_io_tg           | 509 ms                                                          | 523 ms: 1.03x slower                                                                     |
| pycparser                  | 869 ms                                                          | 893 ms: 1.03x slower                                                                     |
| dulwich_log                | 49.7 ms                                                         | 51.1 ms: 1.03x slower                                                                    |
| tomli_loads                | 1.73 sec                                                        | 1.79 sec: 1.03x slower                                                                   |
| 2to3                       | 253 ms                                                          | 262 ms: 1.03x slower                                                                     |
| django_template            | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                                                    |
| float                      | 57.8 ms                                                         | 60.0 ms: 1.04x slower                                                                    |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                                     |
| regex_v8                   | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                                    |
| sqlglot_parse              | 1.05 ms                                                         | 1.09 ms: 1.04x slower                                                                    |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                                    |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.05x slower                                                                    |
| logging_format             | 8.57 us                                                         | 8.98 us: 1.05x slower                                                                    |
| logging_simple             | 7.87 us                                                         | 8.26 us: 1.05x slower                                                                    |
| sympy_integrate            | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                                    |
| sqlglot_normalize          | 220 ms                                                          | 231 ms: 1.05x slower                                                                     |
| sqlglot_optimize           | 42.5 ms                                                         | 44.6 ms: 1.05x slower                                                                    |
| create_gc_cycles           | 713 us                                                          | 749 us: 1.05x slower                                                                     |
| async_tree_io              | 537 ms                                                          | 564 ms: 1.05x slower                                                                     |
| regex_compile              | 103 ms                                                          | 109 ms: 1.05x slower                                                                     |
| nqueens                    | 75.1 ms                                                         | 79.1 ms: 1.05x slower                                                                    |
| chaos                      | 51.2 ms                                                         | 54.0 ms: 1.05x slower                                                                    |
| pprint_safe_repr           | 644 ms                                                          | 680 ms: 1.06x slower                                                                     |
| xml_etree_generate         | 62.6 ms                                                         | 66.2 ms: 1.06x slower                                                                    |
| pylint                     | 225 ms                                                          | 238 ms: 1.06x slower                                                                     |
| sympy_str                  | 215 ms                                                          | 229 ms: 1.06x slower                                                                     |
| docutils                   | 1.82 sec                                                        | 1.94 sec: 1.06x slower                                                                   |
| regex_effbot               | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                                    |
| go                         | 111 ms                                                          | 119 ms: 1.07x slower                                                                     |
| pprint_pformat             | 1.30 sec                                                        | 1.39 sec: 1.07x slower                                                                   |
| unpickle_pure_python       | 162 us                                                          | 173 us: 1.07x slower                                                                     |
| scimark_sor                | 91.8 ms                                                         | 98.5 ms: 1.07x slower                                                                    |
| async_generators           | 274 ms                                                          | 294 ms: 1.08x slower                                                                     |
| sympy_expand               | 375 ms                                                          | 404 ms: 1.08x slower                                                                     |
| xml_etree_process          | 45.0 ms                                                         | 48.6 ms: 1.08x slower                                                                    |
| pickle_pure_python         | 238 us                                                          | 257 us: 1.08x slower                                                                     |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.16 ms: 1.09x slower                                                                    |
| pyflate                    | 326 ms                                                          | 355 ms: 1.09x slower                                                                     |
| meteor_contest             | 77.0 ms                                                         | 84.3 ms: 1.09x slower                                                                    |
| raytrace                   | 205 ms                                                          | 226 ms: 1.10x slower                                                                     |
| scimark_lu                 | 63.5 ms                                                         | 70.0 ms: 1.10x slower                                                                    |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.6 ms: 1.11x slower                                                                    |
| spectral_norm              | 71.3 ms                                                         | 79.2 ms: 1.11x slower                                                                    |
| coroutines                 | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                                    |
| comprehensions             | 12.7 us                                                         | 14.3 us: 1.12x slower                                                                    |
| fannkuch                   | 293 ms                                                          | 330 ms: 1.13x slower                                                                     |
| mako                       | 7.31 ms                                                         | 8.24 ms: 1.13x slower                                                                    |
| deltablue                  | 2.41 ms                                                         | 2.74 ms: 1.14x slower                                                                    |
| hexiom                     | 4.64 ms                                                         | 5.31 ms: 1.14x slower                                                                    |
| scimark_fft                | 206 ms                                                          | 237 ms: 1.15x slower                                                                     |
| typing_runtime_protocols   | 136 us                                                          | 158 us: 1.16x slower                                                                     |
| richards                   | 33.8 ms                                                         | 39.1 ms: 1.16x slower                                                                    |
| richards_super             | 38.0 ms                                                         | 44.2 ms: 1.16x slower                                                                    |
| nbody                      | 81.9 ms                                                         | 99.2 ms: 1.21x slower                                                                    |
| logging_silent             | 61.6 ns                                                         | 74.9 ns: 1.22x slower                                                                    |
| generators                 | 22.1 ms                                                         | 27.6 ms: 1.25x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                             |

Benchmark hidden because not significant (4): genshi_text, pathlib, python_startup, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown