# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 248 ms: 1.02x faster                                                       |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                     |
| html5lib       | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                      |
| tornado_http   | 104 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                           | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 650 ms: 1.30x faster                                                       |
| async_tree_memoization_tg  | 287 ms                                                          | 259 ms: 1.11x faster                                                       |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                       |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 219 ms                                                          | 208 ms: 1.05x faster                                                       |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 488 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 473 ms: 1.02x slower                                                       |
| async_tree_io              | 537 ms                                                          | 551 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 509 ms                                                          | 531 ms: 1.04x slower                                                       |
| async_generators           | 274 ms                                                          | 294 ms: 1.07x slower                                                       |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                       |
| float          | 57.8 ms                                                         | 61.0 ms: 1.06x slower                                                      |
| nbody          | 81.9 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 117 ms: 1.00x slower                                                       |
| regex_compile  | 103 ms                                                          | 107 ms: 1.04x slower                                                       |
| regex_v8       | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                      |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.3 us: 1.07x faster                                                      |
| pickle               | 8.42 us                                                         | 7.94 us: 1.06x faster                                                      |
| unpickle_list        | 3.09 us                                                         | 2.94 us: 1.05x faster                                                      |
| pickle_list          | 3.40 us                                                         | 3.34 us: 1.02x faster                                                      |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.8 ms: 1.03x slower                                                      |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                      |
| tomli_loads          | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                     |
| pickle_pure_python   | 238 us                                                          | 256 us: 1.08x slower                                                       |
| xml_etree_generate   | 62.6 ms                                                         | 69.2 ms: 1.11x slower                                                      |
| unpickle_pure_python | 162 us                                                          | 182 us: 1.12x slower                                                       |
| xml_etree_process    | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.6 ms: 1.03x faster                                                      |
| python_startup_no_site | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                      |
| genshi_text     | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                      |
| django_template | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                      |
| mako            | 7.31 ms                                                         | 8.08 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 763 us: 13.30x faster                                                      |
| coverage                   | 333 ms                                                          | 53.1 ms: 6.27x faster                                                      |
| asyncio_tcp                | 842 ms                                                          | 650 ms: 1.30x faster                                                       |
| deepcopy                   | 307 us                                                          | 242 us: 1.27x faster                                                       |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                                      |
| deepcopy_reduce            | 2.85 us                                                         | 2.49 us: 1.15x faster                                                      |
| async_tree_memoization_tg  | 287 ms                                                          | 259 ms: 1.11x faster                                                       |
| tornado_http               | 104 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| pathlib                    | 89.4 ms                                                         | 82.1 ms: 1.09x faster                                                      |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                       |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                       |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                       |
| telco                      | 6.67 ms                                                         | 6.19 ms: 1.08x faster                                                      |
| pickle_dict                | 21.7 us                                                         | 20.3 us: 1.07x faster                                                      |
| pickle                     | 8.42 us                                                         | 7.94 us: 1.06x faster                                                      |
| html5lib                   | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                      |
| unpickle_list              | 3.09 us                                                         | 2.94 us: 1.05x faster                                                      |
| genshi_xml                 | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 219 ms                                                          | 208 ms: 1.05x faster                                                       |
| bench_mp_pool              | 74.3 ms                                                         | 71.5 ms: 1.04x faster                                                      |
| python_startup             | 24.3 ms                                                         | 23.6 ms: 1.03x faster                                                      |
| python_startup_no_site     | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                      |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                       |
| bench_thread_pool          | 1.02 ms                                                         | 995 us: 1.03x faster                                                       |
| crypto_pyaes               | 58.2 ms                                                         | 56.8 ms: 1.02x faster                                                      |
| nqueens                    | 75.1 ms                                                         | 73.3 ms: 1.02x faster                                                      |
| gc_traversal               | 1.45 ms                                                         | 1.42 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                     |
| 2to3                       | 253 ms                                                          | 248 ms: 1.02x faster                                                       |
| pickle_list                | 3.40 us                                                         | 3.34 us: 1.02x faster                                                      |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 488 ms: 1.01x faster                                                       |
| genshi_text                | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                      |
| django_template            | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                      |
| regex_dna                  | 117 ms                                                          | 117 ms: 1.00x slower                                                       |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                      |
| sqlglot_parse              | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                                      |
| chaos                      | 51.2 ms                                                         | 51.8 ms: 1.01x slower                                                      |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.01x slower                                                       |
| pycparser                  | 869 ms                                                          | 882 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.29 ms                                                         | 1.31 ms: 1.02x slower                                                      |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 473 ms: 1.02x slower                                                       |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                     |
| xml_etree_iterparse        | 65.1 ms                                                         | 66.8 ms: 1.03x slower                                                      |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                     |
| async_tree_io              | 537 ms                                                          | 551 ms: 1.03x slower                                                       |
| pprint_safe_repr           | 644 ms                                                          | 666 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 136 us                                                          | 141 us: 1.04x slower                                                       |
| sympy_expand               | 375 ms                                                          | 388 ms: 1.04x slower                                                       |
| regex_compile              | 103 ms                                                          | 107 ms: 1.04x slower                                                       |
| create_gc_cycles           | 713 us                                                          | 741 us: 1.04x slower                                                       |
| json_dumps                 | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 509 ms                                                          | 531 ms: 1.04x slower                                                       |
| meteor_contest             | 77.0 ms                                                         | 80.5 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 42.5 ms                                                         | 44.4 ms: 1.05x slower                                                      |
| pprint_pformat             | 1.30 sec                                                        | 1.36 sec: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.04 ms: 1.05x slower                                                      |
| regex_v8                   | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                      |
| regex_effbot               | 1.81 ms                                                         | 1.91 ms: 1.05x slower                                                      |
| float                      | 57.8 ms                                                         | 61.0 ms: 1.06x slower                                                      |
| spectral_norm              | 71.3 ms                                                         | 75.7 ms: 1.06x slower                                                      |
| scimark_sor                | 91.8 ms                                                         | 97.5 ms: 1.06x slower                                                      |
| tomli_loads                | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                     |
| async_generators           | 274 ms                                                          | 294 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 220 ms                                                          | 236 ms: 1.07x slower                                                       |
| pickle_pure_python         | 238 us                                                          | 256 us: 1.08x slower                                                       |
| scimark_lu                 | 63.5 ms                                                         | 68.5 ms: 1.08x slower                                                      |
| unpack_sequence            | 42.9 ns                                                         | 46.6 ns: 1.09x slower                                                      |
| scimark_monte_carlo        | 50.3 ms                                                         | 54.8 ms: 1.09x slower                                                      |
| comprehensions             | 12.7 us                                                         | 13.9 us: 1.09x slower                                                      |
| pyflate                    | 326 ms                                                          | 360 ms: 1.11x slower                                                       |
| mako                       | 7.31 ms                                                         | 8.08 ms: 1.11x slower                                                      |
| hexiom                     | 4.64 ms                                                         | 5.13 ms: 1.11x slower                                                      |
| raytrace                   | 205 ms                                                          | 227 ms: 1.11x slower                                                       |
| xml_etree_generate         | 62.6 ms                                                         | 69.2 ms: 1.11x slower                                                      |
| nbody                      | 81.9 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| fannkuch                   | 293 ms                                                          | 328 ms: 1.12x slower                                                       |
| scimark_fft                | 206 ms                                                          | 231 ms: 1.12x slower                                                       |
| deltablue                  | 2.41 ms                                                         | 2.70 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 162 us                                                          | 182 us: 1.12x slower                                                       |
| xml_etree_process          | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                      |
| richards_super             | 38.0 ms                                                         | 43.8 ms: 1.15x slower                                                      |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                      |
| richards                   | 33.8 ms                                                         | 40.0 ms: 1.18x slower                                                      |
| logging_silent             | 61.6 ns                                                         | 74.4 ns: 1.21x slower                                                      |
| generators                 | 22.1 ms                                                         | 26.8 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (8): sympy_sum, json_loads, logging_format, unpickle, json, logging_simple, dulwich_log, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown