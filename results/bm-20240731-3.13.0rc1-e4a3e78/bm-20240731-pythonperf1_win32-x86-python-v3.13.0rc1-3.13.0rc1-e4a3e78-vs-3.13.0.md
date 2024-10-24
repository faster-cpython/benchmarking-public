# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-x86
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 244 ms: 1.04x faster                                                  |
| chameleon      | 6.14 ms                                                         | 5.80 ms: 1.06x faster                                                 |
| docutils       | 1.82 sec                                                        | 1.88 sec: 1.03x slower                                                |
| html5lib       | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 266 ms: 1.08x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                  |
| async_tree_none            | 246 ms                                                          | 237 ms: 1.04x faster                                                  |
| asyncio_tcp                | 842 ms                                                          | 816 ms: 1.03x faster                                                  |
| async_tree_none_tg         | 219 ms                                                          | 213 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 485 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                |
| async_generators           | 274 ms                                                          | 280 ms: 1.02x slower                                                  |
| async_tree_io              | 537 ms                                                          | 550 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 509 ms                                                          | 549 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                          |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 54.2 ms: 1.07x faster                                                 |
| nbody          | 81.9 ms                                                         | 77.1 ms: 1.06x faster                                                 |
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                           | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 99.2 ms: 1.04x faster                                                 |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                 |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| regex_dna      | 117 ms                                                          | 123 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                           | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 148 us: 1.09x faster                                                  |
| pickle_pure_python   | 238 us                                                          | 226 us: 1.05x faster                                                  |
| xml_etree_process    | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                                 |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.04x faster                                                  |
| xml_etree_generate   | 62.6 ms                                                         | 60.5 ms: 1.03x faster                                                 |
| tomli_loads          | 1.73 sec                                                        | 1.68 sec: 1.03x faster                                                |
| xml_etree_iterparse  | 65.1 ms                                                         | 65.7 ms: 1.01x slower                                                 |
| json_dumps           | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.3 ms: 1.03x faster                                                 |
| python_startup         | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 20.4 ms: 1.10x faster                                                 |
| genshi_xml      | 49.5 ms                                                         | 45.2 ms: 1.09x faster                                                 |
| mako            | 7.31 ms                                                         | 6.96 ms: 1.05x faster                                                 |
| django_template | 32.7 ms                                                         | 31.3 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nqueens                    | 75.1 ms                                                         | 67.1 ms: 1.12x faster                                                 |
| telco                      | 6.67 ms                                                         | 6.04 ms: 1.10x faster                                                 |
| go                         | 111 ms                                                          | 101 ms: 1.10x faster                                                  |
| scimark_sor                | 91.8 ms                                                         | 83.5 ms: 1.10x faster                                                 |
| genshi_text                | 22.4 ms                                                         | 20.4 ms: 1.10x faster                                                 |
| genshi_xml                 | 49.5 ms                                                         | 45.2 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 162 us                                                          | 148 us: 1.09x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 24.0 us: 1.09x faster                                                 |
| hexiom                     | 4.64 ms                                                         | 4.28 ms: 1.08x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 266 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 644 ms                                                          | 602 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.05 ms                                                         | 985 us: 1.07x faster                                                  |
| float                      | 57.8 ms                                                         | 54.2 ms: 1.07x faster                                                 |
| pycparser                  | 869 ms                                                          | 815 ms: 1.07x faster                                                  |
| raytrace                   | 205 ms                                                          | 193 ms: 1.06x faster                                                  |
| logging_silent             | 61.6 ns                                                         | 57.9 ns: 1.06x faster                                                 |
| comprehensions             | 12.7 us                                                         | 12.0 us: 1.06x faster                                                 |
| nbody                      | 81.9 ms                                                         | 77.1 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.29 ms                                                         | 1.22 ms: 1.06x faster                                                 |
| chaos                      | 51.2 ms                                                         | 48.3 ms: 1.06x faster                                                 |
| chameleon                  | 6.14 ms                                                         | 5.80 ms: 1.06x faster                                                 |
| deltablue                  | 2.41 ms                                                         | 2.27 ms: 1.06x faster                                                 |
| coverage                   | 333 ms                                                          | 315 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 50.3 ms                                                         | 47.6 ms: 1.06x faster                                                 |
| pickle_pure_python         | 238 us                                                          | 226 us: 1.05x faster                                                  |
| xml_etree_process          | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                                 |
| deepcopy                   | 307 us                                                          | 292 us: 1.05x faster                                                  |
| pyflate                    | 326 ms                                                          | 310 ms: 1.05x faster                                                  |
| mako                       | 7.31 ms                                                         | 6.96 ms: 1.05x faster                                                 |
| richards_super             | 38.0 ms                                                         | 36.1 ms: 1.05x faster                                                 |
| pprint_pformat             | 1.30 sec                                                        | 1.23 sec: 1.05x faster                                                |
| richards                   | 33.8 ms                                                         | 32.2 ms: 1.05x faster                                                 |
| fannkuch                   | 293 ms                                                          | 280 ms: 1.05x faster                                                  |
| deepcopy_reduce            | 2.85 us                                                         | 2.72 us: 1.05x faster                                                 |
| logging_simple             | 7.87 us                                                         | 7.53 us: 1.05x faster                                                 |
| django_template            | 32.7 ms                                                         | 31.3 ms: 1.04x faster                                                 |
| scimark_lu                 | 63.5 ms                                                         | 60.8 ms: 1.04x faster                                                 |
| sqlglot_normalize          | 220 ms                                                          | 211 ms: 1.04x faster                                                  |
| crypto_pyaes               | 58.2 ms                                                         | 55.7 ms: 1.04x faster                                                 |
| regex_compile              | 103 ms                                                          | 99.2 ms: 1.04x faster                                                 |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.04x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                  |
| bench_thread_pool          | 1.02 ms                                                         | 981 us: 1.04x faster                                                  |
| 2to3                       | 253 ms                                                          | 244 ms: 1.04x faster                                                  |
| meteor_contest             | 77.0 ms                                                         | 74.2 ms: 1.04x faster                                                 |
| logging_format             | 8.57 us                                                         | 8.25 us: 1.04x faster                                                 |
| async_tree_none            | 246 ms                                                          | 237 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 42.5 ms                                                         | 41.0 ms: 1.03x faster                                                 |
| xml_etree_generate         | 62.6 ms                                                         | 60.5 ms: 1.03x faster                                                 |
| asyncio_tcp                | 842 ms                                                          | 816 ms: 1.03x faster                                                  |
| python_startup_no_site     | 19.9 ms                                                         | 19.3 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.82 ms: 1.03x faster                                                 |
| tomli_loads                | 1.73 sec                                                        | 1.68 sec: 1.03x faster                                                |
| async_tree_none_tg         | 219 ms                                                          | 213 ms: 1.03x faster                                                  |
| python_startup             | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                 |
| html5lib                   | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                                 |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                  |
| bench_mp_pool              | 74.3 ms                                                         | 72.8 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 485 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                  |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                |
| sympy_str                  | 215 ms                                                          | 212 ms: 1.01x faster                                                  |
| mdp                        | 1.67 sec                                                        | 1.65 sec: 1.01x faster                                                |
| generators                 | 22.1 ms                                                         | 21.8 ms: 1.01x faster                                                 |
| sympy_expand               | 375 ms                                                          | 371 ms: 1.01x faster                                                  |
| scimark_fft                | 206 ms                                                          | 205 ms: 1.01x faster                                                  |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                  |
| dulwich_log                | 49.7 ms                                                         | 49.3 ms: 1.01x faster                                                 |
| gc_traversal               | 1.45 ms                                                         | 1.46 ms: 1.01x slower                                                 |
| xml_etree_iterparse        | 65.1 ms                                                         | 65.7 ms: 1.01x slower                                                 |
| async_generators           | 274 ms                                                          | 280 ms: 1.02x slower                                                  |
| async_tree_io              | 537 ms                                                          | 550 ms: 1.03x slower                                                  |
| json_dumps                 | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                 |
| docutils                   | 1.82 sec                                                        | 1.88 sec: 1.03x slower                                                |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                 |
| create_gc_cycles           | 713 us                                                          | 744 us: 1.04x slower                                                  |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| regex_dna                  | 117 ms                                                          | 123 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 136 us                                                          | 144 us: 1.05x slower                                                  |
| async_tree_io_tg           | 509 ms                                                          | 549 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (8): json, spectral_norm, coroutines, thrift, json_loads, tornado_http, pathlib, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown