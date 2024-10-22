# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: windows-x86
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 233 ms: 1.09x faster                                                |
| chameleon      | 6.14 ms                                                         | 5.71 ms: 1.07x faster                                               |
| docutils       | 1.82 sec                                                        | 1.81 sec: 1.00x faster                                              |
| html5lib       | 48.3 ms                                                         | 45.4 ms: 1.06x faster                                               |
| tornado_http   | 104 ms                                                          | 94.3 ms: 1.11x faster                                               |
| Geometric mean | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                |
| async_tree_none            | 246 ms                                                          | 228 ms: 1.08x faster                                                |
| async_tree_none_tg         | 219 ms                                                          | 203 ms: 1.08x faster                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 447 ms: 1.04x faster                                                |
| async_generators           | 274 ms                                                          | 266 ms: 1.03x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                              |
| coroutines                 | 15.7 ms                                                         | 15.5 ms: 1.01x faster                                               |
| async_tree_io_tg           | 509 ms                                                          | 529 ms: 1.04x slower                                                |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                        |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 52.4 ms: 1.10x faster                                               |
| nbody          | 81.9 ms                                                         | 76.9 ms: 1.06x faster                                               |
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 99.9 ms: 1.04x faster                                               |
| regex_v8       | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                               |
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| regex_effbot   | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 238 us                                                          | 213 us: 1.12x faster                                                |
| unpickle_pure_python | 162 us                                                          | 147 us: 1.10x faster                                                |
| json_dumps           | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                               |
| unpickle             | 10.5 us                                                         | 9.79 us: 1.08x faster                                               |
| xml_etree_process    | 45.0 ms                                                         | 42.1 ms: 1.07x faster                                               |
| unpickle_list        | 3.09 us                                                         | 2.93 us: 1.06x faster                                               |
| tomli_loads          | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                              |
| xml_etree_generate   | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                               |
| pickle_dict          | 21.7 us                                                         | 20.8 us: 1.05x faster                                               |
| pickle               | 8.42 us                                                         | 8.07 us: 1.04x faster                                               |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.04x faster                                                |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.02x faster                                               |
| xml_etree_iterparse  | 65.1 ms                                                         | 64.2 ms: 1.01x faster                                               |
| pickle_list          | 3.40 us                                                         | 3.57 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 18.2 ms: 1.09x faster                                               |
| python_startup         | 24.3 ms                                                         | 22.2 ms: 1.09x faster                                               |
| Geometric mean         | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 44.3 ms: 1.12x faster                                               |
| genshi_text     | 22.4 ms                                                         | 20.1 ms: 1.12x faster                                               |
| django_template | 32.7 ms                                                         | 30.1 ms: 1.09x faster                                               |
| mako            | 7.31 ms                                                         | 6.94 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                                |
| scimark_sor                | 91.8 ms                                                         | 81.0 ms: 1.13x faster                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 254 ms: 1.13x faster                                                |
| genshi_xml                 | 49.5 ms                                                         | 44.3 ms: 1.12x faster                                               |
| pycparser                  | 869 ms                                                          | 777 ms: 1.12x faster                                                |
| pickle_pure_python         | 238 us                                                          | 213 us: 1.12x faster                                                |
| genshi_text                | 22.4 ms                                                         | 20.1 ms: 1.12x faster                                               |
| deepcopy_memo              | 26.2 us                                                         | 23.5 us: 1.11x faster                                               |
| scimark_monte_carlo        | 50.3 ms                                                         | 45.2 ms: 1.11x faster                                               |
| go                         | 111 ms                                                          | 101 ms: 1.11x faster                                                |
| telco                      | 6.67 ms                                                         | 6.03 ms: 1.11x faster                                               |
| tornado_http               | 104 ms                                                          | 94.3 ms: 1.11x faster                                               |
| float                      | 57.8 ms                                                         | 52.4 ms: 1.10x faster                                               |
| deepcopy_reduce            | 2.85 us                                                         | 2.59 us: 1.10x faster                                               |
| async_tree_memoization     | 302 ms                                                          | 275 ms: 1.10x faster                                                |
| unpickle_pure_python       | 162 us                                                          | 147 us: 1.10x faster                                                |
| deepcopy                   | 307 us                                                          | 280 us: 1.10x faster                                                |
| hexiom                     | 4.64 ms                                                         | 4.23 ms: 1.10x faster                                               |
| python_startup_no_site     | 19.9 ms                                                         | 18.2 ms: 1.09x faster                                               |
| nqueens                    | 75.1 ms                                                         | 68.7 ms: 1.09x faster                                               |
| python_startup             | 24.3 ms                                                         | 22.2 ms: 1.09x faster                                               |
| sqlglot_parse              | 1.05 ms                                                         | 964 us: 1.09x faster                                                |
| raytrace                   | 205 ms                                                          | 189 ms: 1.09x faster                                                |
| django_template            | 32.7 ms                                                         | 30.1 ms: 1.09x faster                                               |
| 2to3                       | 253 ms                                                          | 233 ms: 1.09x faster                                                |
| sqlglot_transpile          | 1.29 ms                                                         | 1.19 ms: 1.09x faster                                               |
| fannkuch                   | 293 ms                                                          | 270 ms: 1.08x faster                                                |
| coverage                   | 333 ms                                                          | 307 ms: 1.08x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                               |
| richards                   | 33.8 ms                                                         | 31.2 ms: 1.08x faster                                               |
| async_tree_none            | 246 ms                                                          | 228 ms: 1.08x faster                                                |
| async_tree_none_tg         | 219 ms                                                          | 203 ms: 1.08x faster                                                |
| deltablue                  | 2.41 ms                                                         | 2.23 ms: 1.08x faster                                               |
| unpickle                   | 10.5 us                                                         | 9.79 us: 1.08x faster                                               |
| chameleon                  | 6.14 ms                                                         | 5.71 ms: 1.07x faster                                               |
| comprehensions             | 12.7 us                                                         | 11.9 us: 1.07x faster                                               |
| bench_mp_pool              | 74.3 ms                                                         | 69.4 ms: 1.07x faster                                               |
| scimark_lu                 | 63.5 ms                                                         | 59.4 ms: 1.07x faster                                               |
| xml_etree_process          | 45.0 ms                                                         | 42.1 ms: 1.07x faster                                               |
| richards_super             | 38.0 ms                                                         | 35.5 ms: 1.07x faster                                               |
| sqlglot_optimize           | 42.5 ms                                                         | 39.7 ms: 1.07x faster                                               |
| chaos                      | 51.2 ms                                                         | 48.0 ms: 1.07x faster                                               |
| sqlglot_normalize          | 220 ms                                                          | 206 ms: 1.07x faster                                                |
| pathlib                    | 89.4 ms                                                         | 83.9 ms: 1.07x faster                                               |
| nbody                      | 81.9 ms                                                         | 76.9 ms: 1.06x faster                                               |
| logging_silent             | 61.6 ns                                                         | 57.9 ns: 1.06x faster                                               |
| html5lib                   | 48.3 ms                                                         | 45.4 ms: 1.06x faster                                               |
| pprint_safe_repr           | 644 ms                                                          | 607 ms: 1.06x faster                                                |
| pyflate                    | 326 ms                                                          | 308 ms: 1.06x faster                                                |
| unpickle_list              | 3.09 us                                                         | 2.93 us: 1.06x faster                                               |
| logging_simple             | 7.87 us                                                         | 7.47 us: 1.05x faster                                               |
| logging_format             | 8.57 us                                                         | 8.13 us: 1.05x faster                                               |
| mako                       | 7.31 ms                                                         | 6.94 ms: 1.05x faster                                               |
| tomli_loads                | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                              |
| xml_etree_generate         | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                               |
| spectral_norm              | 71.3 ms                                                         | 68.0 ms: 1.05x faster                                               |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                |
| pickle_dict                | 21.7 us                                                         | 20.8 us: 1.05x faster                                               |
| generators                 | 22.1 ms                                                         | 21.2 ms: 1.04x faster                                               |
| pprint_pformat             | 1.30 sec                                                        | 1.24 sec: 1.04x faster                                              |
| mdp                        | 1.67 sec                                                        | 1.60 sec: 1.04x faster                                              |
| thrift                     | 10.1 ms                                                         | 9.73 ms: 1.04x faster                                               |
| pickle                     | 8.42 us                                                         | 8.07 us: 1.04x faster                                               |
| scimark_fft                | 206 ms                                                          | 198 ms: 1.04x faster                                                |
| crypto_pyaes               | 58.2 ms                                                         | 55.8 ms: 1.04x faster                                               |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.04x faster                                                |
| json                       | 4.27 ms                                                         | 4.10 ms: 1.04x faster                                               |
| meteor_contest             | 77.0 ms                                                         | 74.1 ms: 1.04x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.6 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 447 ms: 1.04x faster                                                |
| bench_thread_pool          | 1.02 ms                                                         | 985 us: 1.04x faster                                                |
| pylint                     | 225 ms                                                          | 217 ms: 1.04x faster                                                |
| regex_compile              | 103 ms                                                          | 99.9 ms: 1.04x faster                                               |
| async_generators           | 274 ms                                                          | 266 ms: 1.03x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                              |
| sympy_sum                  | 108 ms                                                          | 105 ms: 1.03x faster                                                |
| json_loads                 | 21.0 us                                                         | 20.5 us: 1.02x faster                                               |
| sympy_str                  | 215 ms                                                          | 211 ms: 1.02x faster                                                |
| pidigits                   | 202 ms                                                          | 199 ms: 1.02x faster                                                |
| xml_etree_iterparse        | 65.1 ms                                                         | 64.2 ms: 1.01x faster                                               |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                               |
| coroutines                 | 15.7 ms                                                         | 15.5 ms: 1.01x faster                                               |
| docutils                   | 1.82 sec                                                        | 1.81 sec: 1.00x faster                                              |
| flaskblogging              | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                              |
| regex_v8                   | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                               |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 529 ms: 1.04x slower                                                |
| regex_effbot               | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                               |
| pickle_list                | 3.40 us                                                         | 3.57 us: 1.05x slower                                               |
| create_gc_cycles           | 713 us                                                          | 756 us: 1.06x slower                                                |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                        |

Benchmark hidden because not significant (5): async_tree_io, scimark_sparse_mat_mult, typing_runtime_protocols, sqlite_synth, sympy_expand
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown