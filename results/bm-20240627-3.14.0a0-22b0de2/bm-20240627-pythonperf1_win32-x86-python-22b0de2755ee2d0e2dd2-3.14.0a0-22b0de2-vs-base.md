# Results vs. base

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-x86
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 247 ms                                                                         | 264 ms: 1.07x slower                                                           |
| docutils       | 1.88 sec                                                                       | 1.96 sec: 1.04x slower                                                         |
| html5lib       | 48.3 ms                                                                        | 49.9 ms: 1.03x slower                                                          |
| tornado_http   | 95.3 ms                                                                        | 97.6 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 461 ms                                                                         | 472 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 491 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 246 ms                                                                         | 262 ms: 1.06x slower                                                           |
| async_tree_io_tg           | 491 ms                                                                         | 534 ms: 1.09x slower                                                           |
| async_tree_io              | 532 ms                                                                         | 579 ms: 1.09x slower                                                           |
| async_tree_memoization     | 268 ms                                                                         | 295 ms: 1.10x slower                                                           |
| async_tree_none            | 217 ms                                                                         | 241 ms: 1.11x slower                                                           |
| async_tree_none_tg         | 184 ms                                                                         | 208 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.08x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                         | 199 ms: 1.01x slower                                                           |
| float          | 59.5 ms                                                                        | 64.8 ms: 1.09x slower                                                          |
| nbody          | 91.7 ms                                                                        | 103 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                         | 119 ms: 1.04x faster                                                           |
| regex_effbot   | 1.95 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| regex_compile  | 105 ms                                                                         | 115 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                                         | 107 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 67.7 ms                                                                        | 69.7 ms: 1.03x slower                                                          |
| json_loads           | 20.2 us                                                                        | 21.1 us: 1.04x slower                                                          |
| xml_etree_process    | 47.2 ms                                                                        | 51.6 ms: 1.09x slower                                                          |
| json_dumps           | 7.03 ms                                                                        | 7.82 ms: 1.11x slower                                                          |
| xml_etree_generate   | 63.0 ms                                                                        | 70.2 ms: 1.11x slower                                                          |
| unpickle_pure_python | 167 us                                                                         | 189 us: 1.14x slower                                                           |
| tomli_loads          | 1.76 sec                                                                       | 2.01 sec: 1.14x slower                                                         |
| pickle_pure_python   | 233 us                                                                         | 278 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                                          | 1.10x slower                                                                   |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                                        | 34.4 ms: 1.02x slower                                                          |
| mako            | 8.00 ms                                                                        | 8.76 ms: 1.09x slower                                                          |
| genshi_xml      | 47.4 ms                                                                        | 54.6 ms: 1.15x slower                                                          |
| genshi_text     | 21.1 ms                                                                        | 24.9 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                                          | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240626-pythonperf1_win32-x86-python-d611c4c8e9893c081696-3.14.0a0-d611c4c | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna                  | 123 ms                                                                         | 119 ms: 1.04x faster                                                           |
| regex_effbot               | 1.95 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| create_gc_cycles           | 746 us                                                                         | 739 us: 1.01x faster                                                           |
| nqueens                    | 78.0 ms                                                                        | 77.5 ms: 1.01x faster                                                          |
| bench_mp_pool              | 70.6 ms                                                                        | 71.0 ms: 1.01x slower                                                          |
| pathlib                    | 83.4 ms                                                                        | 84.0 ms: 1.01x slower                                                          |
| pycparser                  | 884 ms                                                                         | 892 ms: 1.01x slower                                                           |
| pidigits                   | 197 ms                                                                         | 199 ms: 1.01x slower                                                           |
| coverage                   | 51.4 ms                                                                        | 52.1 ms: 1.01x slower                                                          |
| bench_thread_pool          | 980 us                                                                         | 992 us: 1.01x slower                                                           |
| mdp                        | 1.73 sec                                                                       | 1.75 sec: 1.01x slower                                                         |
| django_template            | 33.8 ms                                                                        | 34.4 ms: 1.02x slower                                                          |
| tornado_http               | 95.3 ms                                                                        | 97.6 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 461 ms                                                                         | 472 ms: 1.03x slower                                                           |
| spectral_norm              | 77.5 ms                                                                        | 79.6 ms: 1.03x slower                                                          |
| xml_etree_parse            | 104 ms                                                                         | 107 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 67.7 ms                                                                        | 69.7 ms: 1.03x slower                                                          |
| pylint                     | 226 ms                                                                         | 234 ms: 1.03x slower                                                           |
| html5lib                   | 48.3 ms                                                                        | 49.9 ms: 1.03x slower                                                          |
| json_loads                 | 20.2 us                                                                        | 21.1 us: 1.04x slower                                                          |
| pprint_pformat             | 1.36 sec                                                                       | 1.42 sec: 1.04x slower                                                         |
| docutils                   | 1.88 sec                                                                       | 1.96 sec: 1.04x slower                                                         |
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 491 ms: 1.05x slower                                                           |
| pprint_safe_repr           | 663 ms                                                                         | 694 ms: 1.05x slower                                                           |
| coroutines                 | 17.3 ms                                                                        | 18.1 ms: 1.05x slower                                                          |
| logging_silent             | 73.9 ns                                                                        | 77.7 ns: 1.05x slower                                                          |
| hexiom                     | 5.15 ms                                                                        | 5.43 ms: 1.05x slower                                                          |
| sympy_integrate            | 15.3 ms                                                                        | 16.2 ms: 1.06x slower                                                          |
| async_tree_memoization_tg  | 246 ms                                                                         | 262 ms: 1.06x slower                                                           |
| sympy_str                  | 219 ms                                                                         | 233 ms: 1.06x slower                                                           |
| sympy_sum                  | 108 ms                                                                         | 116 ms: 1.07x slower                                                           |
| 2to3                       | 247 ms                                                                         | 264 ms: 1.07x slower                                                           |
| scimark_lu                 | 70.5 ms                                                                        | 75.5 ms: 1.07x slower                                                          |
| logging_format             | 8.71 us                                                                        | 9.33 us: 1.07x slower                                                          |
| thrift                     | 753 us                                                                         | 810 us: 1.08x slower                                                           |
| json                       | 4.09 ms                                                                        | 4.40 ms: 1.08x slower                                                          |
| generators                 | 26.4 ms                                                                        | 28.5 ms: 1.08x slower                                                          |
| sympy_expand               | 383 ms                                                                         | 413 ms: 1.08x slower                                                           |
| async_generators           | 291 ms                                                                         | 314 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 144 us                                                                         | 155 us: 1.08x slower                                                           |
| meteor_contest             | 76.0 ms                                                                        | 82.4 ms: 1.08x slower                                                          |
| crypto_pyaes               | 58.7 ms                                                                        | 63.7 ms: 1.09x slower                                                          |
| logging_simple             | 7.93 us                                                                        | 8.62 us: 1.09x slower                                                          |
| async_tree_io_tg           | 491 ms                                                                         | 534 ms: 1.09x slower                                                           |
| float                      | 59.5 ms                                                                        | 64.8 ms: 1.09x slower                                                          |
| async_tree_io              | 532 ms                                                                         | 579 ms: 1.09x slower                                                           |
| xml_etree_process          | 47.2 ms                                                                        | 51.6 ms: 1.09x slower                                                          |
| mako                       | 8.00 ms                                                                        | 8.76 ms: 1.09x slower                                                          |
| async_tree_memoization     | 268 ms                                                                         | 295 ms: 1.10x slower                                                           |
| regex_compile              | 105 ms                                                                         | 115 ms: 1.10x slower                                                           |
| sqlglot_normalize          | 223 ms                                                                         | 246 ms: 1.10x slower                                                           |
| deepcopy_reduce            | 2.51 us                                                                        | 2.76 us: 1.10x slower                                                          |
| sqlglot_optimize           | 42.9 ms                                                                        | 47.3 ms: 1.10x slower                                                          |
| async_tree_none            | 217 ms                                                                         | 241 ms: 1.11x slower                                                           |
| json_dumps                 | 7.03 ms                                                                        | 7.82 ms: 1.11x slower                                                          |
| deltablue                  | 2.59 ms                                                                        | 2.88 ms: 1.11x slower                                                          |
| chaos                      | 54.5 ms                                                                        | 60.7 ms: 1.11x slower                                                          |
| deepcopy                   | 243 us                                                                         | 271 us: 1.11x slower                                                           |
| xml_etree_generate         | 63.0 ms                                                                        | 70.2 ms: 1.11x slower                                                          |
| pyflate                    | 338 ms                                                                         | 378 ms: 1.12x slower                                                           |
| nbody                      | 91.7 ms                                                                        | 103 ms: 1.12x slower                                                           |
| telco                      | 6.03 ms                                                                        | 6.79 ms: 1.13x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                                        | 1.45 ms: 1.13x slower                                                          |
| async_tree_none_tg         | 184 ms                                                                         | 208 ms: 1.13x slower                                                           |
| go                         | 112 ms                                                                         | 127 ms: 1.14x slower                                                           |
| comprehensions             | 13.1 us                                                                        | 14.8 us: 1.14x slower                                                          |
| unpickle_pure_python       | 167 us                                                                         | 189 us: 1.14x slower                                                           |
| tomli_loads                | 1.76 sec                                                                       | 2.01 sec: 1.14x slower                                                         |
| scimark_fft                | 224 ms                                                                         | 257 ms: 1.15x slower                                                           |
| genshi_xml                 | 47.4 ms                                                                        | 54.6 ms: 1.15x slower                                                          |
| scimark_sparse_mat_mult    | 3.13 ms                                                                        | 3.61 ms: 1.15x slower                                                          |
| deepcopy_memo              | 21.7 us                                                                        | 25.1 us: 1.15x slower                                                          |
| richards_super             | 39.6 ms                                                                        | 45.8 ms: 1.16x slower                                                          |
| sqlglot_parse              | 1.04 ms                                                                        | 1.21 ms: 1.16x slower                                                          |
| raytrace                   | 209 ms                                                                         | 247 ms: 1.18x slower                                                           |
| genshi_text                | 21.1 ms                                                                        | 24.9 ms: 1.18x slower                                                          |
| richards                   | 34.8 ms                                                                        | 41.2 ms: 1.19x slower                                                          |
| scimark_sor                | 89.3 ms                                                                        | 106 ms: 1.19x slower                                                           |
| pickle_pure_python         | 233 us                                                                         | 278 us: 1.19x slower                                                           |
| fannkuch                   | 288 ms                                                                         | 347 ms: 1.21x slower                                                           |
| scimark_monte_carlo        | 48.6 ms                                                                        | 60.9 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.08x slower                                                                   |

Benchmark hidden because not significant (6): python_startup, asyncio_tcp_ssl, asyncio_tcp, python_startup_no_site, regex_v8, gc_traversal

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown