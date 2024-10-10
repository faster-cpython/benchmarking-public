# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 253 ms: 1.09x slower                                            |
| chameleon      | 5.71 ms                                                             | 6.14 ms: 1.07x slower                                           |
| docutils       | 1.81 sec                                                            | 1.82 sec: 1.00x slower                                          |
| html5lib       | 45.4 ms                                                             | 48.3 ms: 1.06x slower                                           |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                               | 1.07x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                            |
| async_tree_none_tg         | 203 ms                                                              | 219 ms: 1.08x slower                                            |
| async_tree_none            | 228 ms                                                              | 246 ms: 1.08x slower                                            |
| async_tree_memoization     | 275 ms                                                              | 302 ms: 1.10x slower                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 287 ms: 1.13x slower                                            |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                    |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 202 ms: 1.02x slower                                            |
| nbody          | 76.9 ms                                                             | 81.9 ms: 1.06x slower                                           |
| float          | 52.4 ms                                                             | 57.8 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.81 ms: 1.04x faster                                           |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                            |
| regex_v8       | 15.7 ms                                                             | 15.6 ms: 1.01x faster                                           |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                               | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.40 us: 1.05x faster                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 65.1 ms: 1.01x slower                                           |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                           |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                            |
| pickle               | 8.07 us                                                             | 8.42 us: 1.04x slower                                           |
| pickle_dict          | 20.8 us                                                             | 21.7 us: 1.05x slower                                           |
| xml_etree_generate   | 59.6 ms                                                             | 62.6 ms: 1.05x slower                                           |
| tomli_loads          | 1.65 sec                                                            | 1.73 sec: 1.05x slower                                          |
| unpickle_list        | 2.93 us                                                             | 3.09 us: 1.06x slower                                           |
| xml_etree_process    | 42.1 ms                                                             | 45.0 ms: 1.07x slower                                           |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.08x slower                                           |
| json_dumps           | 6.84 ms                                                             | 7.40 ms: 1.08x slower                                           |
| unpickle_pure_python | 147 us                                                              | 162 us: 1.10x slower                                            |
| pickle_pure_python   | 213 us                                                              | 238 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                               | 1.05x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                           |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 7.31 ms: 1.05x slower                                           |
| django_template | 30.1 ms                                                             | 32.7 ms: 1.09x slower                                           |
| genshi_text     | 20.1 ms                                                             | 22.4 ms: 1.12x slower                                           |
| genshi_xml      | 44.3 ms                                                             | 49.5 ms: 1.12x slower                                           |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 756 us                                                              | 713 us: 1.06x faster                                            |
| pickle_list                | 3.57 us                                                             | 3.40 us: 1.05x faster                                           |
| regex_effbot               | 1.88 ms                                                             | 1.81 ms: 1.04x faster                                           |
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                            |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                            |
| regex_v8                   | 15.7 ms                                                             | 15.6 ms: 1.01x faster                                           |
| flaskblogging              | 2.03 sec                                                            | 2.04 sec: 1.00x slower                                          |
| docutils                   | 1.81 sec                                                            | 1.82 sec: 1.00x slower                                          |
| coroutines                 | 15.5 ms                                                             | 15.7 ms: 1.01x slower                                           |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 65.1 ms: 1.01x slower                                           |
| pidigits                   | 199 ms                                                              | 202 ms: 1.02x slower                                            |
| sympy_str                  | 211 ms                                                              | 215 ms: 1.02x slower                                            |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                           |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                            |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                          |
| async_generators           | 266 ms                                                              | 274 ms: 1.03x slower                                            |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.04x slower                                            |
| pylint                     | 217 ms                                                              | 225 ms: 1.04x slower                                            |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                            |
| sympy_integrate            | 14.6 ms                                                             | 15.2 ms: 1.04x slower                                           |
| meteor_contest             | 74.1 ms                                                             | 77.0 ms: 1.04x slower                                           |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                           |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                            |
| crypto_pyaes               | 55.8 ms                                                             | 58.2 ms: 1.04x slower                                           |
| scimark_fft                | 198 ms                                                              | 206 ms: 1.04x slower                                            |
| pickle                     | 8.07 us                                                             | 8.42 us: 1.04x slower                                           |
| thrift                     | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                           |
| mdp                        | 1.60 sec                                                            | 1.67 sec: 1.04x slower                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.30 sec: 1.04x slower                                          |
| generators                 | 21.2 ms                                                             | 22.1 ms: 1.04x slower                                           |
| pickle_dict                | 20.8 us                                                             | 21.7 us: 1.05x slower                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                            |
| spectral_norm              | 68.0 ms                                                             | 71.3 ms: 1.05x slower                                           |
| xml_etree_generate         | 59.6 ms                                                             | 62.6 ms: 1.05x slower                                           |
| tomli_loads                | 1.65 sec                                                            | 1.73 sec: 1.05x slower                                          |
| mako                       | 6.94 ms                                                             | 7.31 ms: 1.05x slower                                           |
| logging_format             | 8.13 us                                                             | 8.57 us: 1.05x slower                                           |
| logging_simple             | 7.47 us                                                             | 7.87 us: 1.05x slower                                           |
| unpickle_list              | 2.93 us                                                             | 3.09 us: 1.06x slower                                           |
| pyflate                    | 308 ms                                                              | 326 ms: 1.06x slower                                            |
| pprint_safe_repr           | 607 ms                                                              | 644 ms: 1.06x slower                                            |
| html5lib                   | 45.4 ms                                                             | 48.3 ms: 1.06x slower                                           |
| logging_silent             | 57.9 ns                                                             | 61.6 ns: 1.06x slower                                           |
| nbody                      | 76.9 ms                                                             | 81.9 ms: 1.06x slower                                           |
| pathlib                    | 83.9 ms                                                             | 89.4 ms: 1.07x slower                                           |
| sqlglot_normalize          | 206 ms                                                              | 220 ms: 1.07x slower                                            |
| chaos                      | 48.0 ms                                                             | 51.2 ms: 1.07x slower                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 42.5 ms: 1.07x slower                                           |
| richards_super             | 35.5 ms                                                             | 38.0 ms: 1.07x slower                                           |
| xml_etree_process          | 42.1 ms                                                             | 45.0 ms: 1.07x slower                                           |
| scimark_lu                 | 59.4 ms                                                             | 63.5 ms: 1.07x slower                                           |
| bench_mp_pool              | 69.4 ms                                                             | 74.3 ms: 1.07x slower                                           |
| comprehensions             | 11.9 us                                                             | 12.7 us: 1.07x slower                                           |
| chameleon                  | 5.71 ms                                                             | 6.14 ms: 1.07x slower                                           |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.08x slower                                           |
| deltablue                  | 2.23 ms                                                             | 2.41 ms: 1.08x slower                                           |
| async_tree_none_tg         | 203 ms                                                              | 219 ms: 1.08x slower                                            |
| async_tree_none            | 228 ms                                                              | 246 ms: 1.08x slower                                            |
| richards                   | 31.2 ms                                                             | 33.8 ms: 1.08x slower                                           |
| json_dumps                 | 6.84 ms                                                             | 7.40 ms: 1.08x slower                                           |
| coverage                   | 307 ms                                                              | 333 ms: 1.08x slower                                            |
| fannkuch                   | 270 ms                                                              | 293 ms: 1.08x slower                                            |
| sqlglot_transpile          | 1.19 ms                                                             | 1.29 ms: 1.09x slower                                           |
| 2to3                       | 233 ms                                                              | 253 ms: 1.09x slower                                            |
| django_template            | 30.1 ms                                                             | 32.7 ms: 1.09x slower                                           |
| raytrace                   | 189 ms                                                              | 205 ms: 1.09x slower                                            |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                           |
| python_startup             | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                           |
| nqueens                    | 68.7 ms                                                             | 75.1 ms: 1.09x slower                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                           |
| hexiom                     | 4.23 ms                                                             | 4.64 ms: 1.10x slower                                           |
| deepcopy                   | 280 us                                                              | 307 us: 1.10x slower                                            |
| unpickle_pure_python       | 147 us                                                              | 162 us: 1.10x slower                                            |
| async_tree_memoization     | 275 ms                                                              | 302 ms: 1.10x slower                                            |
| deepcopy_reduce            | 2.59 us                                                             | 2.85 us: 1.10x slower                                           |
| float                      | 52.4 ms                                                             | 57.8 ms: 1.10x slower                                           |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.11x slower                                            |
| telco                      | 6.03 ms                                                             | 6.67 ms: 1.11x slower                                           |
| go                         | 101 ms                                                              | 111 ms: 1.11x slower                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 50.3 ms: 1.11x slower                                           |
| deepcopy_memo              | 23.5 us                                                             | 26.2 us: 1.11x slower                                           |
| genshi_text                | 20.1 ms                                                             | 22.4 ms: 1.12x slower                                           |
| pickle_pure_python         | 213 us                                                              | 238 us: 1.12x slower                                            |
| pycparser                  | 777 ms                                                              | 869 ms: 1.12x slower                                            |
| genshi_xml                 | 44.3 ms                                                             | 49.5 ms: 1.12x slower                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 287 ms: 1.13x slower                                            |
| scimark_sor                | 81.0 ms                                                             | 91.8 ms: 1.13x slower                                           |
| asyncio_tcp                | 662 ms                                                              | 842 ms: 1.27x slower                                            |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                    |

Benchmark hidden because not significant (5): sympy_expand, sqlite_synth, typing_runtime_protocols, scimark_sparse_mat_mult, async_tree_io
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown