# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.07x faster
- HPT reliability: 75.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 264 ms: 1.04x slower                                                            |
| docutils       | 1.82 sec                                                        | 2.06 sec: 1.13x slower                                                          |
| html5lib       | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                           |
| tornado_http   | 104 ms                                                          | 109 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 246 ms                                                          | 222 ms: 1.11x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 269 ms: 1.07x faster                                                            |
| async_tree_none_tg         | 219 ms                                                          | 206 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 476 ms: 1.04x faster                                                            |
| async_tree_io              | 537 ms                                                          | 524 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 509 ms                                                          | 551 ms: 1.08x slower                                                            |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| async_generators           | 274 ms                                                          | 314 ms: 1.15x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 64.6 ms: 1.27x faster                                                           |
| float          | 57.8 ms                                                         | 46.6 ms: 1.24x faster                                                           |
| pidigits       | 202 ms                                                          | 204 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| regex_compile  | 103 ms                                                          | 105 ms: 1.02x slower                                                            |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.05x slower                                                           |
| regex_dna      | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 62.6 ms                                                         | 55.1 ms: 1.14x faster                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 42.1 ms: 1.07x faster                                                           |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 160 us: 1.01x faster                                                            |
| xml_etree_parse      | 109 ms                                                          | 112 ms: 1.03x slower                                                            |
| pickle_pure_python   | 238 us                                                          | 246 us: 1.03x slower                                                            |
| json_dumps           | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                           |
| python_startup         | 24.3 ms                                                         | 26.7 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.69 ms: 1.28x faster                                                           |
| genshi_text    | 22.4 ms                                                         | 23.4 ms: 1.04x slower                                                           |
| genshi_xml     | 49.5 ms                                                         | 54.3 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 780 us: 13.00x faster                                                           |
| coverage                   | 333 ms                                                          | 53.5 ms: 6.23x faster                                                           |
| sqlglot_normalize          | 220 ms                                                          | 101 ms: 2.17x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 16.6 us: 1.57x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 70.2 ms: 1.31x faster                                                           |
| deepcopy                   | 307 us                                                          | 236 us: 1.30x faster                                                            |
| mako                       | 7.31 ms                                                         | 5.69 ms: 1.28x faster                                                           |
| nbody                      | 81.9 ms                                                         | 64.6 ms: 1.27x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 40.0 ms: 1.26x faster                                                           |
| float                      | 57.8 ms                                                         | 46.6 ms: 1.24x faster                                                           |
| fannkuch                   | 293 ms                                                          | 237 ms: 1.24x faster                                                            |
| spectral_norm              | 71.3 ms                                                         | 57.8 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.48 ms: 1.17x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 49.8 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.44 us: 1.17x faster                                                           |
| go                         | 111 ms                                                          | 96.7 ms: 1.15x faster                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 55.1 ms: 1.14x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 567 ms: 1.14x faster                                                            |
| tomli_loads                | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                          |
| scimark_fft                | 206 ms                                                          | 183 ms: 1.13x faster                                                            |
| pprint_pformat             | 1.30 sec                                                        | 1.16 sec: 1.12x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 55.6 ns: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 222 ms: 1.11x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                            |
| pycparser                  | 869 ms                                                          | 809 ms: 1.07x faster                                                            |
| xml_etree_process          | 45.0 ms                                                         | 42.1 ms: 1.07x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 269 ms: 1.07x faster                                                            |
| meteor_contest             | 77.0 ms                                                         | 72.3 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 206 ms: 1.06x faster                                                            |
| telco                      | 6.67 ms                                                         | 6.33 ms: 1.05x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                           |
| pyflate                    | 326 ms                                                          | 312 ms: 1.04x faster                                                            |
| logging_format             | 8.57 us                                                         | 8.23 us: 1.04x faster                                                           |
| logging_simple             | 7.87 us                                                         | 7.58 us: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 476 ms: 1.04x faster                                                            |
| bench_thread_pool          | 1.02 ms                                                         | 988 us: 1.03x faster                                                            |
| scimark_lu                 | 63.5 ms                                                         | 61.8 ms: 1.03x faster                                                           |
| async_tree_io              | 537 ms                                                          | 524 ms: 1.02x faster                                                            |
| pathlib                    | 89.4 ms                                                         | 88.0 ms: 1.02x faster                                                           |
| regex_v8                   | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.8 us: 1.01x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 160 us: 1.01x faster                                                            |
| pidigits                   | 202 ms                                                          | 204 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                            |
| nqueens                    | 75.1 ms                                                         | 76.3 ms: 1.02x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                          |
| comprehensions             | 12.7 us                                                         | 13.0 us: 1.02x slower                                                           |
| regex_compile              | 103 ms                                                          | 105 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.9 ms                                                         | 20.4 ms: 1.02x slower                                                           |
| xml_etree_parse            | 109 ms                                                          | 112 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 136 us                                                          | 141 us: 1.03x slower                                                            |
| pickle_pure_python         | 238 us                                                          | 246 us: 1.03x slower                                                            |
| genshi_text                | 22.4 ms                                                         | 23.4 ms: 1.04x slower                                                           |
| tornado_http               | 104 ms                                                          | 109 ms: 1.04x slower                                                            |
| 2to3                       | 253 ms                                                          | 264 ms: 1.04x slower                                                            |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.05x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.52 ms: 1.05x slower                                                           |
| regex_dna                  | 117 ms                                                          | 124 ms: 1.06x slower                                                            |
| chaos                      | 51.2 ms                                                         | 54.5 ms: 1.06x slower                                                           |
| sympy_expand               | 375 ms                                                          | 399 ms: 1.07x slower                                                            |
| sympy_str                  | 215 ms                                                          | 230 ms: 1.07x slower                                                            |
| sympy_sum                  | 108 ms                                                          | 116 ms: 1.07x slower                                                            |
| async_tree_io_tg           | 509 ms                                                          | 551 ms: 1.08x slower                                                            |
| generators                 | 22.1 ms                                                         | 23.9 ms: 1.08x slower                                                           |
| genshi_xml                 | 49.5 ms                                                         | 54.3 ms: 1.10x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| python_startup             | 24.3 ms                                                         | 26.7 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                           |
| docutils                   | 1.82 sec                                                        | 2.06 sec: 1.13x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 17.3 ms: 1.14x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.32 ms: 1.15x slower                                                           |
| async_generators           | 274 ms                                                          | 314 ms: 1.15x slower                                                            |
| richards                   | 33.8 ms                                                         | 39.2 ms: 1.16x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 49.9 ms: 1.18x slower                                                           |
| json                       | 4.27 ms                                                         | 5.02 ms: 1.18x slower                                                           |
| richards_super             | 38.0 ms                                                         | 45.3 ms: 1.19x slower                                                           |
| gc_traversal               | 1.45 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| pylint                     | 225 ms                                                          | 283 ms: 1.26x slower                                                            |
| bench_mp_pool              | 74.3 ms                                                         | 94.1 ms: 1.27x slower                                                           |
| raytrace                   | 205 ms                                                          | 275 ms: 1.34x slower                                                            |
| create_gc_cycles           | 713 us                                                          | 1.19 ms: 1.66x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (4): dulwich_log, xml_etree_iterparse, django_template, sqlglot_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: sphinx

# HPT report

- Reliability score: 75.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown