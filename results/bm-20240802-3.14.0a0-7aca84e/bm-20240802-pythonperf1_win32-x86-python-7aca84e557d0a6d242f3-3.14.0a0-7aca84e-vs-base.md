# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                                       | 1.96 sec: 1.00x slower                                                         |
| html5lib       | 49.3 ms                                                                        | 51.4 ms: 1.04x slower                                                          |
| tornado_http   | 105 ms                                                                         | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 845 ms                                                                         | 785 ms: 1.08x faster                                                           |
| async_generators           | 303 ms                                                                         | 306 ms: 1.01x slower                                                           |
| async_tree_io              | 563 ms                                                                         | 570 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 520 ms                                                                         | 528 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 476 ms                                                                         | 484 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 472 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none, asyncio_tcp_ssl, coroutines, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 108 ms                                                                         | 102 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.3 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| regex_dna      | 121 ms                                                                         | 129 ms: 1.06x slower                                                           |
| regex_effbot   | 1.92 ms                                                                        | 2.05 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.95 sec                                                                       | 1.91 sec: 1.02x faster                                                         |
| xml_etree_parse      | 107 ms                                                                         | 105 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 68.7 ms                                                                        | 67.7 ms: 1.01x faster                                                          |
| pickle_pure_python   | 263 us                                                                         | 266 us: 1.01x slower                                                           |
| xml_etree_generate   | 64.6 ms                                                                        | 65.8 ms: 1.02x slower                                                          |
| unpickle_pure_python | 170 us                                                                         | 174 us: 1.02x slower                                                           |
| json_dumps           | 7.49 ms                                                                        | 7.71 ms: 1.03x slower                                                          |
| xml_etree_process    | 47.7 ms                                                                        | 49.1 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.0 ms                                                                        | 23.7 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 51.2 ms                                                                        | 50.4 ms: 1.02x faster                                                          |
| mako            | 8.24 ms                                                                        | 8.31 ms: 1.01x slower                                                          |
| django_template | 34.5 ms                                                                        | 34.9 ms: 1.01x slower                                                          |
| genshi_text     | 23.6 ms                                                                        | 24.4 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                                          | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 845 ms                                                                         | 785 ms: 1.08x faster                                                           |
| nbody                      | 108 ms                                                                         | 102 ms: 1.06x faster                                                           |
| thrift                     | 772 us                                                                         | 751 us: 1.03x faster                                                           |
| spectral_norm              | 80.0 ms                                                                        | 78.0 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 234 ms                                                                         | 229 ms: 1.02x faster                                                           |
| tomli_loads                | 1.95 sec                                                                       | 1.91 sec: 1.02x faster                                                         |
| genshi_xml                 | 51.2 ms                                                                        | 50.4 ms: 1.02x faster                                                          |
| create_gc_cycles           | 765 us                                                                         | 753 us: 1.01x faster                                                           |
| xml_etree_parse            | 107 ms                                                                         | 105 ms: 1.01x faster                                                           |
| crypto_pyaes               | 60.7 ms                                                                        | 59.8 ms: 1.01x faster                                                          |
| xml_etree_iterparse        | 68.7 ms                                                                        | 67.7 ms: 1.01x faster                                                          |
| python_startup             | 24.0 ms                                                                        | 23.7 ms: 1.01x faster                                                          |
| sqlglot_optimize           | 45.1 ms                                                                        | 44.6 ms: 1.01x faster                                                          |
| sympy_expand               | 396 ms                                                                         | 392 ms: 1.01x faster                                                           |
| raytrace                   | 243 ms                                                                         | 241 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.40 sec                                                                       | 1.39 sec: 1.01x faster                                                         |
| deepcopy_reduce            | 2.68 us                                                                        | 2.66 us: 1.00x faster                                                          |
| scimark_fft                | 234 ms                                                                         | 235 ms: 1.00x slower                                                           |
| docutils                   | 1.95 sec                                                                       | 1.96 sec: 1.00x slower                                                         |
| regex_v8                   | 16.3 ms                                                                        | 16.4 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 3.14 ms                                                                        | 3.17 ms: 1.01x slower                                                          |
| mako                       | 8.24 ms                                                                        | 8.31 ms: 1.01x slower                                                          |
| hexiom                     | 5.36 ms                                                                        | 5.40 ms: 1.01x slower                                                          |
| logging_format             | 8.90 us                                                                        | 8.98 us: 1.01x slower                                                          |
| dulwich_log                | 51.1 ms                                                                        | 51.6 ms: 1.01x slower                                                          |
| mdp                        | 1.74 sec                                                                       | 1.76 sec: 1.01x slower                                                         |
| async_generators           | 303 ms                                                                         | 306 ms: 1.01x slower                                                           |
| pickle_pure_python         | 263 us                                                                         | 266 us: 1.01x slower                                                           |
| generators                 | 27.6 ms                                                                        | 27.9 ms: 1.01x slower                                                          |
| django_template            | 34.5 ms                                                                        | 34.9 ms: 1.01x slower                                                          |
| async_tree_io              | 563 ms                                                                         | 570 ms: 1.01x slower                                                           |
| deepcopy                   | 261 us                                                                         | 264 us: 1.01x slower                                                           |
| async_tree_io_tg           | 520 ms                                                                         | 528 ms: 1.01x slower                                                           |
| coverage                   | 51.4 ms                                                                        | 52.2 ms: 1.02x slower                                                          |
| tornado_http               | 105 ms                                                                         | 107 ms: 1.02x slower                                                           |
| comprehensions             | 13.9 us                                                                        | 14.1 us: 1.02x slower                                                          |
| typing_runtime_protocols   | 150 us                                                                         | 152 us: 1.02x slower                                                           |
| sqlglot_parse              | 1.10 ms                                                                        | 1.12 ms: 1.02x slower                                                          |
| nqueens                    | 77.7 ms                                                                        | 79.0 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 476 ms                                                                         | 484 ms: 1.02x slower                                                           |
| fannkuch                   | 320 ms                                                                         | 325 ms: 1.02x slower                                                           |
| xml_etree_generate         | 64.6 ms                                                                        | 65.8 ms: 1.02x slower                                                          |
| unpickle_pure_python       | 170 us                                                                         | 174 us: 1.02x slower                                                           |
| sqlglot_transpile          | 1.36 ms                                                                        | 1.38 ms: 1.02x slower                                                          |
| pycparser                  | 898 ms                                                                         | 918 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 472 ms: 1.02x slower                                                           |
| meteor_contest             | 82.1 ms                                                                        | 83.9 ms: 1.02x slower                                                          |
| deepcopy_memo              | 22.4 us                                                                        | 23.0 us: 1.03x slower                                                          |
| pyflate                    | 350 ms                                                                         | 360 ms: 1.03x slower                                                           |
| logging_silent             | 73.2 ns                                                                        | 75.3 ns: 1.03x slower                                                          |
| json_dumps                 | 7.49 ms                                                                        | 7.71 ms: 1.03x slower                                                          |
| xml_etree_process          | 47.7 ms                                                                        | 49.1 ms: 1.03x slower                                                          |
| richards_super             | 45.9 ms                                                                        | 47.4 ms: 1.03x slower                                                          |
| richards                   | 42.3 ms                                                                        | 43.7 ms: 1.03x slower                                                          |
| genshi_text                | 23.6 ms                                                                        | 24.4 ms: 1.03x slower                                                          |
| deltablue                  | 2.74 ms                                                                        | 2.84 ms: 1.04x slower                                                          |
| scimark_sor                | 97.0 ms                                                                        | 101 ms: 1.04x slower                                                           |
| html5lib                   | 49.3 ms                                                                        | 51.4 ms: 1.04x slower                                                          |
| go                         | 119 ms                                                                         | 124 ms: 1.05x slower                                                           |
| scimark_lu                 | 69.0 ms                                                                        | 72.4 ms: 1.05x slower                                                          |
| scimark_monte_carlo        | 55.0 ms                                                                        | 58.2 ms: 1.06x slower                                                          |
| telco                      | 6.23 ms                                                                        | 6.60 ms: 1.06x slower                                                          |
| regex_dna                  | 121 ms                                                                         | 129 ms: 1.06x slower                                                           |
| regex_effbot               | 1.92 ms                                                                        | 2.05 ms: 1.07x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (24): bench_thread_pool, async_tree_none, json, json_loads, pprint_safe_repr, chaos, float, asyncio_tcp_ssl, gc_traversal, pidigits, python_startup_no_site, bench_mp_pool, sympy_integrate, sympy_str, 2to3, pylint, regex_compile, pathlib, logging_simple, sympy_sum, coroutines, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown