# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 256 ms: 1.01x slower                                                |
| chameleon      | 6.14 ms                                                         | 6.01 ms: 1.02x faster                                               |
| tornado_http   | 104 ms                                                          | 99.9 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 632 ms: 1.33x faster                                                |
| coroutines                 | 15.7 ms                                                         | 14.9 ms: 1.05x faster                                               |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.7 sec: 1.04x faster                                              |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 515 ms: 1.04x slower                                                |
| async_tree_none            | 246 ms                                                          | 260 ms: 1.06x slower                                                |
| async_tree_memoization     | 302 ms                                                          | 325 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 503 ms: 1.08x slower                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 313 ms: 1.09x slower                                                |
| async_generators           | 274 ms                                                          | 300 ms: 1.09x slower                                                |
| async_tree_none_tg         | 219 ms                                                          | 246 ms: 1.13x slower                                                |
| async_tree_io              | 537 ms                                                          | 624 ms: 1.16x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 612 ms: 1.20x slower                                                |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 53.9 ms: 1.07x faster                                               |
| nbody          | 81.9 ms                                                         | 89.7 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 120 ms: 1.03x slower                                                |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                               |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                               |
| regex_compile  | 103 ms                                                          | 110 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 19.9 us: 1.09x faster                                               |
| unpickle_list        | 3.09 us                                                         | 2.87 us: 1.08x faster                                               |
| pickle_pure_python   | 238 us                                                          | 223 us: 1.07x faster                                                |
| json_dumps           | 7.40 ms                                                         | 6.95 ms: 1.07x faster                                               |
| xml_etree_process    | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                               |
| tomli_loads          | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                              |
| unpickle             | 10.5 us                                                         | 10.1 us: 1.04x faster                                               |
| xml_etree_generate   | 62.6 ms                                                         | 60.2 ms: 1.04x faster                                               |
| pickle               | 8.42 us                                                         | 8.11 us: 1.04x faster                                               |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                |
| json_loads           | 21.0 us                                                         | 20.3 us: 1.03x faster                                               |
| pickle_list          | 3.40 us                                                         | 3.35 us: 1.01x faster                                               |
| xml_etree_iterparse  | 65.1 ms                                                         | 65.9 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.5 ms: 1.08x faster                                               |
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 7.31 ms                                                         | 7.43 ms: 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                          | 98.7 us: 1.38x faster                                               |
| asyncio_tcp                | 842 ms                                                          | 632 ms: 1.33x faster                                                |
| deepcopy_reduce            | 2.85 us                                                         | 2.51 us: 1.14x faster                                               |
| create_gc_cycles           | 713 us                                                          | 646 us: 1.10x faster                                                |
| sqlglot_parse              | 1.05 ms                                                         | 961 us: 1.09x faster                                                |
| pickle_dict                | 21.7 us                                                         | 19.9 us: 1.09x faster                                               |
| unpickle_list              | 3.09 us                                                         | 2.87 us: 1.08x faster                                               |
| deepcopy                   | 307 us                                                          | 285 us: 1.08x faster                                                |
| python_startup             | 24.3 ms                                                         | 22.5 ms: 1.08x faster                                               |
| float                      | 57.8 ms                                                         | 53.9 ms: 1.07x faster                                               |
| sqlglot_transpile          | 1.29 ms                                                         | 1.21 ms: 1.07x faster                                               |
| pickle_pure_python         | 238 us                                                          | 223 us: 1.07x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.95 ms: 1.07x faster                                               |
| pathlib                    | 89.4 ms                                                         | 84.3 ms: 1.06x faster                                               |
| sqlite_synth               | 1.97 us                                                         | 1.85 us: 1.06x faster                                               |
| xml_etree_process          | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                               |
| richards                   | 33.8 ms                                                         | 32.2 ms: 1.05x faster                                               |
| coroutines                 | 15.7 ms                                                         | 14.9 ms: 1.05x faster                                               |
| tomli_loads                | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                              |
| tornado_http               | 104 ms                                                          | 99.9 ms: 1.04x faster                                               |
| unpickle                   | 10.5 us                                                         | 10.1 us: 1.04x faster                                               |
| richards_super             | 38.0 ms                                                         | 36.5 ms: 1.04x faster                                               |
| bench_mp_pool              | 74.3 ms                                                         | 71.5 ms: 1.04x faster                                               |
| xml_etree_generate         | 62.6 ms                                                         | 60.2 ms: 1.04x faster                                               |
| pickle                     | 8.42 us                                                         | 8.11 us: 1.04x faster                                               |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.7 sec: 1.04x faster                                              |
| unpickle_pure_python       | 162 us                                                          | 156 us: 1.04x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 25.3 us: 1.03x faster                                               |
| json_loads                 | 21.0 us                                                         | 20.3 us: 1.03x faster                                               |
| gc_traversal               | 1.45 ms                                                         | 1.42 ms: 1.03x faster                                               |
| scimark_sor                | 91.8 ms                                                         | 89.6 ms: 1.03x faster                                               |
| chameleon                  | 6.14 ms                                                         | 6.01 ms: 1.02x faster                                               |
| telco                      | 6.67 ms                                                         | 6.55 ms: 1.02x faster                                               |
| pickle_list                | 3.40 us                                                         | 3.35 us: 1.01x faster                                               |
| unpack_sequence            | 42.9 ns                                                         | 42.6 ns: 1.01x faster                                               |
| 2to3                       | 253 ms                                                          | 256 ms: 1.01x slower                                                |
| sympy_expand               | 375 ms                                                          | 379 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 65.1 ms                                                         | 65.9 ms: 1.01x slower                                               |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.02x slower                                                |
| mako                       | 7.31 ms                                                         | 7.43 ms: 1.02x slower                                               |
| sqlglot_normalize          | 220 ms                                                          | 224 ms: 1.02x slower                                                |
| python_startup_no_site     | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                               |
| sympy_sum                  | 108 ms                                                          | 110 ms: 1.02x slower                                                |
| pycparser                  | 869 ms                                                          | 891 ms: 1.03x slower                                                |
| regex_dna                  | 117 ms                                                          | 120 ms: 1.03x slower                                                |
| spectral_norm              | 71.3 ms                                                         | 73.2 ms: 1.03x slower                                               |
| sqlglot_optimize           | 42.5 ms                                                         | 43.7 ms: 1.03x slower                                               |
| scimark_lu                 | 63.5 ms                                                         | 65.6 ms: 1.03x slower                                               |
| regex_v8                   | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 515 ms: 1.04x slower                                                |
| logging_format             | 8.57 us                                                         | 8.97 us: 1.05x slower                                               |
| crypto_pyaes               | 58.2 ms                                                         | 61.0 ms: 1.05x slower                                               |
| sympy_integrate            | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                               |
| async_tree_none            | 246 ms                                                          | 260 ms: 1.06x slower                                                |
| regex_effbot               | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                               |
| logging_simple             | 7.87 us                                                         | 8.35 us: 1.06x slower                                               |
| regex_compile              | 103 ms                                                          | 110 ms: 1.07x slower                                                |
| deltablue                  | 2.41 ms                                                         | 2.58 ms: 1.07x slower                                               |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.12 ms: 1.07x slower                                               |
| async_tree_memoization     | 302 ms                                                          | 325 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 503 ms: 1.08x slower                                                |
| meteor_contest             | 77.0 ms                                                         | 83.8 ms: 1.09x slower                                               |
| logging_silent             | 61.6 ns                                                         | 67.1 ns: 1.09x slower                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 313 ms: 1.09x slower                                                |
| async_generators           | 274 ms                                                          | 300 ms: 1.09x slower                                                |
| nbody                      | 81.9 ms                                                         | 89.7 ms: 1.10x slower                                               |
| fannkuch                   | 293 ms                                                          | 322 ms: 1.10x slower                                                |
| go                         | 111 ms                                                          | 123 ms: 1.10x slower                                                |
| mdp                        | 1.67 sec                                                        | 1.85 sec: 1.10x slower                                              |
| pprint_safe_repr           | 644 ms                                                          | 713 ms: 1.11x slower                                                |
| comprehensions             | 12.7 us                                                         | 14.1 us: 1.11x slower                                               |
| generators                 | 22.1 ms                                                         | 24.6 ms: 1.11x slower                                               |
| async_tree_none_tg         | 219 ms                                                          | 246 ms: 1.13x slower                                                |
| pyflate                    | 326 ms                                                          | 370 ms: 1.14x slower                                                |
| pprint_pformat             | 1.30 sec                                                        | 1.47 sec: 1.14x slower                                              |
| scimark_fft                | 206 ms                                                          | 239 ms: 1.16x slower                                                |
| async_tree_io              | 537 ms                                                          | 624 ms: 1.16x slower                                                |
| raytrace                   | 205 ms                                                          | 240 ms: 1.17x slower                                                |
| nqueens                    | 75.1 ms                                                         | 88.7 ms: 1.18x slower                                               |
| chaos                      | 51.2 ms                                                         | 61.0 ms: 1.19x slower                                               |
| async_tree_io_tg           | 509 ms                                                          | 612 ms: 1.20x slower                                                |
| coverage                   | 333 ms                                                          | 464 ms: 1.40x slower                                                |
| scimark_monte_carlo        | 50.3 ms                                                         | 71.6 ms: 1.42x slower                                               |
| hexiom                     | 4.64 ms                                                         | 6.61 ms: 1.42x slower                                               |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                        |

Benchmark hidden because not significant (5): pidigits, json, docutils, bench_thread_pool, xml_etree_parse
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown