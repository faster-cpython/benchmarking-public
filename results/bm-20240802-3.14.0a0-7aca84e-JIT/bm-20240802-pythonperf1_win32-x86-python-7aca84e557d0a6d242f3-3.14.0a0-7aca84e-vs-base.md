# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x faster
- HPT reliability: 98.68%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.97 sec                                                                       | 1.98 sec: 1.01x slower                                                         |
| html5lib       | 49.1 ms                                                                        | 47.7 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 485 ms                                                                         | 458 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 499 ms                                                                         | 479 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 205 ms                                                                         | 197 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 522 ms                                                                         | 506 ms: 1.03x faster                                                           |
| async_tree_io              | 563 ms                                                                         | 546 ms: 1.03x faster                                                           |
| async_tree_none            | 234 ms                                                                         | 229 ms: 1.02x faster                                                           |
| async_tree_memoization_tg  | 258 ms                                                                         | 253 ms: 1.02x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.8 ms: 1.00x slower                                                          |
| async_generators           | 311 ms                                                                         | 320 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_tcp_ssl, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 54.0 ms                                                                        | 52.6 ms: 1.03x faster                                                          |
| pidigits       | 197 ms                                                                         | 196 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                        | 16.1 ms: 1.01x faster                                                          |
| regex_compile  | 95.0 ms                                                                        | 96.1 ms: 1.01x slower                                                          |
| regex_effbot   | 1.95 ms                                                                        | 2.00 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 216 us                                                                         | 213 us: 1.02x faster                                                           |
| unpickle_pure_python | 149 us                                                                         | 147 us: 1.02x faster                                                           |
| tomli_loads          | 1.56 sec                                                                       | 1.54 sec: 1.01x faster                                                         |
| json_loads           | 21.3 us                                                                        | 21.1 us: 1.01x faster                                                          |
| xml_etree_generate   | 58.5 ms                                                                        | 59.6 ms: 1.02x slower                                                          |
| xml_etree_process    | 43.9 ms                                                                        | 44.9 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.1 ms                                                                        | 24.8 ms: 1.03x slower                                                          |
| python_startup_no_site | 19.9 ms                                                                        | 20.8 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                                          | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 34.0 ms                                                                        | 32.8 ms: 1.04x faster                                                          |
| genshi_text     | 25.1 ms                                                                        | 24.5 ms: 1.03x faster                                                          |
| mako            | 5.34 ms                                                                        | 5.43 ms: 1.02x slower                                                          |
| genshi_xml      | 51.9 ms                                                                        | 53.5 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                                          | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240802-pythonperf1_win32-x86-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| chaos                      | 54.9 ms                                                                        | 51.6 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                         | 458 ms: 1.06x faster                                                           |
| scimark_sor                | 70.7 ms                                                                        | 67.0 ms: 1.06x faster                                                          |
| logging_simple             | 7.99 us                                                                        | 7.62 us: 1.05x faster                                                          |
| pprint_pformat             | 1.25 sec                                                                       | 1.20 sec: 1.04x faster                                                         |
| logging_format             | 8.72 us                                                                        | 8.36 us: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 499 ms                                                                         | 479 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 205 ms                                                                         | 197 ms: 1.04x faster                                                           |
| django_template            | 34.0 ms                                                                        | 32.8 ms: 1.04x faster                                                          |
| crypto_pyaes               | 48.7 ms                                                                        | 46.9 ms: 1.04x faster                                                          |
| pprint_safe_repr           | 607 ms                                                                         | 586 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 522 ms                                                                         | 506 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.00 ms                                                                        | 973 us: 1.03x faster                                                           |
| async_tree_io              | 563 ms                                                                         | 546 ms: 1.03x faster                                                           |
| html5lib                   | 49.1 ms                                                                        | 47.7 ms: 1.03x faster                                                          |
| go                         | 119 ms                                                                         | 115 ms: 1.03x faster                                                           |
| genshi_text                | 25.1 ms                                                                        | 24.5 ms: 1.03x faster                                                          |
| nbody                      | 54.0 ms                                                                        | 52.6 ms: 1.03x faster                                                          |
| deltablue                  | 2.82 ms                                                                        | 2.75 ms: 1.02x faster                                                          |
| sqlglot_transpile          | 1.28 ms                                                                        | 1.25 ms: 1.02x faster                                                          |
| async_tree_none            | 234 ms                                                                         | 229 ms: 1.02x faster                                                           |
| mdp                        | 1.73 sec                                                                       | 1.69 sec: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 2.37 ms                                                                        | 2.32 ms: 1.02x faster                                                          |
| async_tree_memoization_tg  | 258 ms                                                                         | 253 ms: 1.02x faster                                                           |
| raytrace                   | 231 ms                                                                         | 227 ms: 1.02x faster                                                           |
| fannkuch                   | 231 ms                                                                         | 227 ms: 1.02x faster                                                           |
| meteor_contest             | 70.3 ms                                                                        | 69.0 ms: 1.02x faster                                                          |
| pickle_pure_python         | 216 us                                                                         | 213 us: 1.02x faster                                                           |
| unpickle_pure_python       | 149 us                                                                         | 147 us: 1.02x faster                                                           |
| tomli_loads                | 1.56 sec                                                                       | 1.54 sec: 1.01x faster                                                         |
| spectral_norm              | 48.4 ms                                                                        | 47.9 ms: 1.01x faster                                                          |
| pycparser                  | 800 ms                                                                         | 793 ms: 1.01x faster                                                           |
| json_loads                 | 21.3 us                                                                        | 21.1 us: 1.01x faster                                                          |
| regex_v8                   | 16.2 ms                                                                        | 16.1 ms: 1.01x faster                                                          |
| sympy_expand               | 396 ms                                                                         | 394 ms: 1.01x faster                                                           |
| pidigits                   | 197 ms                                                                         | 196 ms: 1.01x faster                                                           |
| sympy_str                  | 223 ms                                                                         | 222 ms: 1.00x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.8 ms: 1.00x slower                                                          |
| gc_traversal               | 1.45 ms                                                                        | 1.46 ms: 1.01x slower                                                          |
| docutils                   | 1.97 sec                                                                       | 1.98 sec: 1.01x slower                                                         |
| hexiom                     | 4.80 ms                                                                        | 4.84 ms: 1.01x slower                                                          |
| sympy_integrate            | 16.4 ms                                                                        | 16.6 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 152 us                                                                         | 153 us: 1.01x slower                                                           |
| scimark_monte_carlo        | 41.3 ms                                                                        | 41.8 ms: 1.01x slower                                                          |
| regex_compile              | 95.0 ms                                                                        | 96.1 ms: 1.01x slower                                                          |
| create_gc_cycles           | 761 us                                                                         | 771 us: 1.01x slower                                                           |
| pyflate                    | 265 ms                                                                         | 269 ms: 1.01x slower                                                           |
| comprehensions             | 11.3 us                                                                        | 11.5 us: 1.02x slower                                                          |
| mako                       | 5.34 ms                                                                        | 5.43 ms: 1.02x slower                                                          |
| scimark_fft                | 166 ms                                                                         | 168 ms: 1.02x slower                                                           |
| scimark_lu                 | 58.6 ms                                                                        | 59.7 ms: 1.02x slower                                                          |
| xml_etree_generate         | 58.5 ms                                                                        | 59.6 ms: 1.02x slower                                                          |
| richards                   | 34.3 ms                                                                        | 35.1 ms: 1.02x slower                                                          |
| xml_etree_process          | 43.9 ms                                                                        | 44.9 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.49 us                                                                        | 2.54 us: 1.02x slower                                                          |
| async_generators           | 311 ms                                                                         | 320 ms: 1.03x slower                                                           |
| deepcopy                   | 247 us                                                                         | 254 us: 1.03x slower                                                           |
| regex_effbot               | 1.95 ms                                                                        | 2.00 ms: 1.03x slower                                                          |
| python_startup             | 24.1 ms                                                                        | 24.8 ms: 1.03x slower                                                          |
| genshi_xml                 | 51.9 ms                                                                        | 53.5 ms: 1.03x slower                                                          |
| thrift                     | 750 us                                                                         | 774 us: 1.03x slower                                                           |
| generators                 | 23.7 ms                                                                        | 24.7 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                                        | 20.8 ms: 1.04x slower                                                          |
| deepcopy_memo              | 15.5 us                                                                        | 16.4 us: 1.06x slower                                                          |
| telco                      | 5.66 ms                                                                        | 6.01 ms: 1.06x slower                                                          |
| richards_super             | 38.9 ms                                                                        | 41.7 ms: 1.07x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (22): json, asyncio_tcp, xml_etree_iterparse, xml_etree_parse, float, tornado_http, logging_silent, 2to3, pathlib, bench_mp_pool, nqueens, asyncio_tcp_ssl, bench_thread_pool, pylint, regex_dna, dulwich_log, sqlglot_normalize, sqlglot_optimize, coverage, sympy_sum, json_dumps, async_tree_memoization

# HPT report

- Reliability score: 98.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown