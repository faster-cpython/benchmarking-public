# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 230 ms: 1.10x faster                                                |
| chameleon      | 6.14 ms                                                         | 5.61 ms: 1.09x faster                                               |
| docutils       | 1.82 sec                                                        | 1.71 sec: 1.06x faster                                              |
| html5lib       | 48.3 ms                                                         | 43.9 ms: 1.10x faster                                               |
| tornado_http   | 104 ms                                                          | 93.5 ms: 1.11x faster                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 618 ms: 1.36x faster                                                |
| coroutines                 | 15.7 ms                                                         | 14.1 ms: 1.11x faster                                               |
| async_generators           | 274 ms                                                          | 262 ms: 1.04x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.8 sec: 1.04x faster                                              |
| async_tree_none            | 246 ms                                                          | 239 ms: 1.03x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 284 ms: 1.01x faster                                                |
| async_tree_none_tg         | 219 ms                                                          | 225 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 489 ms: 1.05x slower                                                |
| async_tree_io              | 537 ms                                                          | 584 ms: 1.09x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 570 ms: 1.12x slower                                                |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 52.8 ms: 1.09x faster                                               |
| nbody          | 81.9 ms                                                         | 76.8 ms: 1.07x faster                                               |
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 93.4 ms: 1.11x faster                                               |
| regex_dna      | 117 ms                                                          | 116 ms: 1.01x faster                                                |
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                               |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                           | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 140 us: 1.15x faster                                                |
| pickle_pure_python   | 238 us                                                          | 210 us: 1.13x faster                                                |
| json_dumps           | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                               |
| pickle_dict          | 21.7 us                                                         | 19.8 us: 1.09x faster                                               |
| xml_etree_process    | 45.0 ms                                                         | 41.2 ms: 1.09x faster                                               |
| unpickle_list        | 3.09 us                                                         | 2.88 us: 1.07x faster                                               |
| tomli_loads          | 1.73 sec                                                        | 1.62 sec: 1.07x faster                                              |
| pickle               | 8.42 us                                                         | 7.90 us: 1.07x faster                                               |
| unpickle             | 10.5 us                                                         | 10.0 us: 1.05x faster                                               |
| pickle_list          | 3.40 us                                                         | 3.25 us: 1.05x faster                                               |
| xml_etree_generate   | 62.6 ms                                                         | 60.0 ms: 1.04x faster                                               |
| json_loads           | 21.0 us                                                         | 20.2 us: 1.04x faster                                               |
| xml_etree_parse      | 109 ms                                                          | 110 ms: 1.01x slower                                                |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.2 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.0 ms: 1.10x faster                                               |
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 18.9 ms: 1.19x faster                                               |
| genshi_xml      | 49.5 ms                                                         | 41.8 ms: 1.18x faster                                               |
| mako            | 7.31 ms                                                         | 6.76 ms: 1.08x faster                                               |
| django_template | 32.7 ms                                                         | 30.4 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                          | 87.8 us: 1.55x faster                                               |
| asyncio_tcp                | 842 ms                                                          | 618 ms: 1.36x faster                                                |
| deepcopy_reduce            | 2.85 us                                                         | 2.32 us: 1.23x faster                                               |
| sqlglot_parse              | 1.05 ms                                                         | 868 us: 1.21x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                               |
| richards                   | 33.8 ms                                                         | 28.4 ms: 1.19x faster                                               |
| genshi_text                | 22.4 ms                                                         | 18.9 ms: 1.19x faster                                               |
| genshi_xml                 | 49.5 ms                                                         | 41.8 ms: 1.18x faster                                               |
| deepcopy                   | 307 us                                                          | 261 us: 1.17x faster                                                |
| go                         | 111 ms                                                          | 95.1 ms: 1.17x faster                                               |
| sqlglot_transpile          | 1.29 ms                                                         | 1.10 ms: 1.17x faster                                               |
| telco                      | 6.67 ms                                                         | 5.76 ms: 1.16x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 140 us: 1.15x faster                                                |
| scimark_sor                | 91.8 ms                                                         | 80.9 ms: 1.14x faster                                               |
| pickle_pure_python         | 238 us                                                          | 210 us: 1.13x faster                                                |
| pprint_safe_repr           | 644 ms                                                          | 568 ms: 1.13x faster                                                |
| richards_super             | 38.0 ms                                                         | 33.7 ms: 1.13x faster                                               |
| nqueens                    | 75.1 ms                                                         | 66.9 ms: 1.12x faster                                               |
| scimark_monte_carlo        | 50.3 ms                                                         | 44.9 ms: 1.12x faster                                               |
| tornado_http               | 104 ms                                                          | 93.5 ms: 1.11x faster                                               |
| pprint_pformat             | 1.30 sec                                                        | 1.16 sec: 1.11x faster                                              |
| sympy_str                  | 215 ms                                                          | 194 ms: 1.11x faster                                                |
| coroutines                 | 15.7 ms                                                         | 14.1 ms: 1.11x faster                                               |
| deltablue                  | 2.41 ms                                                         | 2.17 ms: 1.11x faster                                               |
| comprehensions             | 12.7 us                                                         | 11.5 us: 1.11x faster                                               |
| pycparser                  | 869 ms                                                          | 784 ms: 1.11x faster                                                |
| regex_compile              | 103 ms                                                          | 93.4 ms: 1.11x faster                                               |
| chaos                      | 51.2 ms                                                         | 46.3 ms: 1.11x faster                                               |
| crypto_pyaes               | 58.2 ms                                                         | 52.6 ms: 1.11x faster                                               |
| hexiom                     | 4.64 ms                                                         | 4.20 ms: 1.10x faster                                               |
| json_dumps                 | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                               |
| python_startup             | 24.3 ms                                                         | 22.0 ms: 1.10x faster                                               |
| 2to3                       | 253 ms                                                          | 230 ms: 1.10x faster                                                |
| sympy_expand               | 375 ms                                                          | 341 ms: 1.10x faster                                                |
| html5lib                   | 48.3 ms                                                         | 43.9 ms: 1.10x faster                                               |
| sqlglot_optimize           | 42.5 ms                                                         | 38.6 ms: 1.10x faster                                               |
| float                      | 57.8 ms                                                         | 52.8 ms: 1.09x faster                                               |
| chameleon                  | 6.14 ms                                                         | 5.61 ms: 1.09x faster                                               |
| sqlglot_normalize          | 220 ms                                                          | 201 ms: 1.09x faster                                                |
| pickle_dict                | 21.7 us                                                         | 19.8 us: 1.09x faster                                               |
| xml_etree_process          | 45.0 ms                                                         | 41.2 ms: 1.09x faster                                               |
| spectral_norm              | 71.3 ms                                                         | 65.4 ms: 1.09x faster                                               |
| sympy_sum                  | 108 ms                                                          | 99.4 ms: 1.09x faster                                               |
| fannkuch                   | 293 ms                                                          | 271 ms: 1.08x faster                                                |
| logging_silent             | 61.6 ns                                                         | 56.9 ns: 1.08x faster                                               |
| mako                       | 7.31 ms                                                         | 6.76 ms: 1.08x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.0 ms: 1.08x faster                                               |
| raytrace                   | 205 ms                                                          | 191 ms: 1.08x faster                                                |
| scimark_lu                 | 63.5 ms                                                         | 59.0 ms: 1.08x faster                                               |
| django_template            | 32.7 ms                                                         | 30.4 ms: 1.08x faster                                               |
| create_gc_cycles           | 713 us                                                          | 662 us: 1.08x faster                                                |
| unpickle_list              | 3.09 us                                                         | 2.88 us: 1.07x faster                                               |
| tomli_loads                | 1.73 sec                                                        | 1.62 sec: 1.07x faster                                              |
| nbody                      | 81.9 ms                                                         | 76.8 ms: 1.07x faster                                               |
| pickle                     | 8.42 us                                                         | 7.90 us: 1.07x faster                                               |
| mdp                        | 1.67 sec                                                        | 1.57 sec: 1.06x faster                                              |
| docutils                   | 1.82 sec                                                        | 1.71 sec: 1.06x faster                                              |
| pyflate                    | 326 ms                                                          | 307 ms: 1.06x faster                                                |
| sqlite_synth               | 1.97 us                                                         | 1.85 us: 1.06x faster                                               |
| logging_format             | 8.57 us                                                         | 8.10 us: 1.06x faster                                               |
| logging_simple             | 7.87 us                                                         | 7.46 us: 1.06x faster                                               |
| bench_mp_pool              | 74.3 ms                                                         | 70.4 ms: 1.06x faster                                               |
| unpickle                   | 10.5 us                                                         | 10.0 us: 1.05x faster                                               |
| pickle_list                | 3.40 us                                                         | 3.25 us: 1.05x faster                                               |
| async_generators           | 274 ms                                                          | 262 ms: 1.04x faster                                                |
| gc_traversal               | 1.45 ms                                                         | 1.39 ms: 1.04x faster                                               |
| xml_etree_generate         | 62.6 ms                                                         | 60.0 ms: 1.04x faster                                               |
| scimark_fft                | 206 ms                                                          | 198 ms: 1.04x faster                                                |
| json_loads                 | 21.0 us                                                         | 20.2 us: 1.04x faster                                               |
| bench_thread_pool          | 1.02 ms                                                         | 984 us: 1.04x faster                                                |
| pylint                     | 225 ms                                                          | 217 ms: 1.04x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.8 sec: 1.04x faster                                              |
| async_tree_none            | 246 ms                                                          | 239 ms: 1.03x faster                                                |
| thrift                     | 10.1 ms                                                         | 9.86 ms: 1.03x faster                                               |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                |
| python_startup_no_site     | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                               |
| async_tree_memoization_tg  | 287 ms                                                          | 284 ms: 1.01x faster                                                |
| pathlib                    | 89.4 ms                                                         | 88.6 ms: 1.01x faster                                               |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.88 ms: 1.01x faster                                               |
| regex_dna                  | 117 ms                                                          | 116 ms: 1.01x faster                                                |
| flaskblogging              | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                              |
| meteor_contest             | 77.0 ms                                                         | 77.4 ms: 1.01x slower                                               |
| xml_etree_parse            | 109 ms                                                          | 110 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 65.1 ms                                                         | 66.2 ms: 1.02x slower                                               |
| regex_v8                   | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                               |
| generators                 | 22.1 ms                                                         | 22.7 ms: 1.03x slower                                               |
| async_tree_none_tg         | 219 ms                                                          | 225 ms: 1.03x slower                                                |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                               |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 489 ms: 1.05x slower                                                |
| async_tree_io              | 537 ms                                                          | 584 ms: 1.09x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 570 ms: 1.12x slower                                                |
| coverage                   | 333 ms                                                          | 460 ms: 1.38x slower                                                |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                        |

Benchmark hidden because not significant (3): json, async_tree_memoization, async_tree_cpu_io_mixed
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown