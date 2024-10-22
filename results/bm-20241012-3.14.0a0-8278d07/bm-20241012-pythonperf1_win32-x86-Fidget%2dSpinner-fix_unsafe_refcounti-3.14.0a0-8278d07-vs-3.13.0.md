# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.03x faster
- HPT reliability: 98.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                                     |
| docutils       | 1.82 sec                                                        | 1.84 sec: 1.01x slower                                                                   |
| html5lib       | 48.3 ms                                                         | 44.7 ms: 1.08x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 737 ms: 1.14x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 470 ms: 1.05x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                                   |
| async_tree_io_tg           | 509 ms                                                          | 520 ms: 1.02x slower                                                                     |
| async_generators           | 274 ms                                                          | 303 ms: 1.11x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 201 ms: 1.01x faster                                                                     |
| float          | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                                    |
| nbody          | 81.9 ms                                                         | 89.4 ms: 1.09x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 113 ms: 1.04x faster                                                                     |
| regex_v8       | 15.6 ms                                                         | 15.3 ms: 1.02x faster                                                                    |
| regex_effbot   | 1.81 ms                                                         | 1.79 ms: 1.01x faster                                                                    |
| regex_compile  | 103 ms                                                          | 106 ms: 1.03x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| unpickle_list        | 3.09 us                                                         | 2.99 us: 1.04x faster                                                                    |
| json_loads           | 21.0 us                                                         | 20.7 us: 1.01x faster                                                                    |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.01x faster                                                                    |
| pickle               | 8.42 us                                                         | 8.48 us: 1.01x slower                                                                    |
| tomli_loads          | 1.73 sec                                                        | 1.77 sec: 1.02x slower                                                                   |
| pickle_list          | 3.40 us                                                         | 3.50 us: 1.03x slower                                                                    |
| xml_etree_parse      | 109 ms                                                          | 113 ms: 1.04x slower                                                                     |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.1 ms: 1.05x slower                                                                    |
| xml_etree_process    | 45.0 ms                                                         | 47.4 ms: 1.05x slower                                                                    |
| xml_etree_generate   | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                                    |
| unpickle_pure_python | 162 us                                                          | 180 us: 1.11x slower                                                                     |
| pickle_pure_python   | 238 us                                                          | 272 us: 1.14x slower                                                                     |
| json_dumps           | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_text    | 22.4 ms                                                         | 20.6 ms: 1.09x faster                                                                    |
| genshi_xml     | 49.5 ms                                                         | 45.6 ms: 1.09x faster                                                                    |
| mako           | 7.31 ms                                                         | 7.86 ms: 1.08x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 739 us: 13.73x faster                                                                    |
| coverage                   | 333 ms                                                          | 52.6 ms: 6.33x faster                                                                    |
| deepcopy                   | 307 us                                                          | 241 us: 1.27x faster                                                                     |
| deepcopy_memo              | 26.2 us                                                         | 22.1 us: 1.18x faster                                                                    |
| asyncio_tcp                | 842 ms                                                          | 737 ms: 1.14x faster                                                                     |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                                     |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                                     |
| deepcopy_reduce            | 2.85 us                                                         | 2.53 us: 1.13x faster                                                                    |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                                     |
| async_tree_none_tg         | 219 ms                                                          | 200 ms: 1.09x faster                                                                     |
| genshi_text                | 22.4 ms                                                         | 20.6 ms: 1.09x faster                                                                    |
| go                         | 111 ms                                                          | 103 ms: 1.09x faster                                                                     |
| genshi_xml                 | 49.5 ms                                                         | 45.6 ms: 1.09x faster                                                                    |
| html5lib                   | 48.3 ms                                                         | 44.7 ms: 1.08x faster                                                                    |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 470 ms: 1.05x faster                                                                     |
| pycparser                  | 869 ms                                                          | 835 ms: 1.04x faster                                                                     |
| regex_dna                  | 117 ms                                                          | 113 ms: 1.04x faster                                                                     |
| unpickle_list              | 3.09 us                                                         | 2.99 us: 1.04x faster                                                                    |
| nqueens                    | 75.1 ms                                                         | 73.5 ms: 1.02x faster                                                                    |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                                     |
| regex_v8                   | 15.6 ms                                                         | 15.3 ms: 1.02x faster                                                                    |
| pathlib                    | 89.4 ms                                                         | 87.8 ms: 1.02x faster                                                                    |
| 2to3                       | 253 ms                                                          | 249 ms: 1.02x faster                                                                     |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                                     |
| json_loads                 | 21.0 us                                                         | 20.7 us: 1.01x faster                                                                    |
| logging_simple             | 7.87 us                                                         | 7.77 us: 1.01x faster                                                                    |
| sqlite_synth               | 1.97 us                                                         | 1.94 us: 1.01x faster                                                                    |
| regex_effbot               | 1.81 ms                                                         | 1.79 ms: 1.01x faster                                                                    |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.01x faster                                                                    |
| bench_mp_pool              | 74.3 ms                                                         | 73.6 ms: 1.01x faster                                                                    |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                                    |
| pidigits                   | 202 ms                                                          | 201 ms: 1.01x faster                                                                     |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                                   |
| pickle                     | 8.42 us                                                         | 8.48 us: 1.01x slower                                                                    |
| pprint_pformat             | 1.30 sec                                                        | 1.31 sec: 1.01x slower                                                                   |
| docutils                   | 1.82 sec                                                        | 1.84 sec: 1.01x slower                                                                   |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.02x slower                                                                    |
| crypto_pyaes               | 58.2 ms                                                         | 59.2 ms: 1.02x slower                                                                    |
| sqlglot_normalize          | 220 ms                                                          | 224 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 509 ms                                                          | 520 ms: 1.02x slower                                                                     |
| tomli_loads                | 1.73 sec                                                        | 1.77 sec: 1.02x slower                                                                   |
| sympy_expand               | 375 ms                                                          | 384 ms: 1.02x slower                                                                     |
| sqlglot_optimize           | 42.5 ms                                                         | 43.5 ms: 1.02x slower                                                                    |
| telco                      | 6.67 ms                                                         | 6.86 ms: 1.03x slower                                                                    |
| regex_compile              | 103 ms                                                          | 106 ms: 1.03x slower                                                                     |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                                   |
| dulwich_log                | 49.7 ms                                                         | 51.2 ms: 1.03x slower                                                                    |
| pickle_list                | 3.40 us                                                         | 3.50 us: 1.03x slower                                                                    |
| sqlglot_transpile          | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                                    |
| meteor_contest             | 77.0 ms                                                         | 79.8 ms: 1.04x slower                                                                    |
| xml_etree_parse            | 109 ms                                                          | 113 ms: 1.04x slower                                                                     |
| pylint                     | 225 ms                                                          | 234 ms: 1.04x slower                                                                     |
| sqlglot_parse              | 1.05 ms                                                         | 1.09 ms: 1.04x slower                                                                    |
| comprehensions             | 12.7 us                                                         | 13.3 us: 1.04x slower                                                                    |
| xml_etree_iterparse        | 65.1 ms                                                         | 68.1 ms: 1.05x slower                                                                    |
| xml_etree_process          | 45.0 ms                                                         | 47.4 ms: 1.05x slower                                                                    |
| float                      | 57.8 ms                                                         | 61.2 ms: 1.06x slower                                                                    |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.08 ms: 1.06x slower                                                                    |
| spectral_norm              | 71.3 ms                                                         | 75.9 ms: 1.06x slower                                                                    |
| xml_etree_generate         | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                                    |
| typing_runtime_protocols   | 136 us                                                          | 145 us: 1.06x slower                                                                     |
| hexiom                     | 4.64 ms                                                         | 4.94 ms: 1.07x slower                                                                    |
| scimark_lu                 | 63.5 ms                                                         | 67.8 ms: 1.07x slower                                                                    |
| generators                 | 22.1 ms                                                         | 23.6 ms: 1.07x slower                                                                    |
| mako                       | 7.31 ms                                                         | 7.86 ms: 1.08x slower                                                                    |
| create_gc_cycles           | 713 us                                                          | 774 us: 1.09x slower                                                                     |
| chaos                      | 51.2 ms                                                         | 55.9 ms: 1.09x slower                                                                    |
| nbody                      | 81.9 ms                                                         | 89.4 ms: 1.09x slower                                                                    |
| async_generators           | 274 ms                                                          | 303 ms: 1.11x slower                                                                     |
| fannkuch                   | 293 ms                                                          | 324 ms: 1.11x slower                                                                     |
| scimark_fft                | 206 ms                                                          | 229 ms: 1.11x slower                                                                     |
| scimark_sor                | 91.8 ms                                                         | 102 ms: 1.11x slower                                                                     |
| pyflate                    | 326 ms                                                          | 362 ms: 1.11x slower                                                                     |
| unpickle_pure_python       | 162 us                                                          | 180 us: 1.11x slower                                                                     |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                                    |
| scimark_monte_carlo        | 50.3 ms                                                         | 56.7 ms: 1.13x slower                                                                    |
| deltablue                  | 2.41 ms                                                         | 2.72 ms: 1.13x slower                                                                    |
| pickle_pure_python         | 238 us                                                          | 272 us: 1.14x slower                                                                     |
| logging_silent             | 61.6 ns                                                         | 73.2 ns: 1.19x slower                                                                    |
| raytrace                   | 205 ms                                                          | 249 ms: 1.21x slower                                                                     |
| richards_super             | 38.0 ms                                                         | 46.0 ms: 1.21x slower                                                                    |
| unpack_sequence            | 42.9 ns                                                         | 52.3 ns: 1.22x slower                                                                    |
| json_dumps                 | 7.40 ms                                                         | 9.02 ms: 1.22x slower                                                                    |
| richards                   | 33.8 ms                                                         | 41.3 ms: 1.22x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                             |

Benchmark hidden because not significant (11): bench_thread_pool, tornado_http, pickle_dict, async_tree_io, logging_format, django_template, python_startup, python_startup_no_site, sympy_str, pprint_safe_repr, json
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 98.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown