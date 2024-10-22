# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                         | 258 ms: 1.02x slower                                                                     |
| html5lib       | 48.6 ms                                                                        | 48.8 ms: 1.00x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_generators | 307 ms                                                                         | 304 ms: 1.01x faster                                                                     |
| coroutines       | 17.6 ms                                                                        | 18.6 ms: 1.05x slower                                                                    |
| Geometric mean   | (ref)                                                                          | 1.00x slower                                                                             |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_tcp_ssl, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                                        | 92.7 ms: 1.01x faster                                                                    |
| float          | 61.2 ms                                                                        | 62.8 ms: 1.03x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                         | 118 ms: 1.01x faster                                                                     |
| regex_v8       | 16.2 ms                                                                        | 16.4 ms: 1.01x slower                                                                    |
| regex_compile  | 107 ms                                                                         | 109 ms: 1.02x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|---------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps          | 7.70 ms                                                                        | 7.47 ms: 1.03x faster                                                                    |
| xml_etree_generate  | 70.0 ms                                                                        | 68.1 ms: 1.03x faster                                                                    |
| xml_etree_iterparse | 69.0 ms                                                                        | 69.8 ms: 1.01x slower                                                                    |
| tomli_loads         | 1.88 sec                                                                       | 1.91 sec: 1.02x slower                                                                   |
| pickle_pure_python  | 254 us                                                                         | 262 us: 1.04x slower                                                                     |
| json_loads          | 20.3 us                                                                        | 21.3 us: 1.05x slower                                                                    |
| Geometric mean      | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                                        | 20.1 ms: 1.01x slower                                                                    |
| Geometric mean         | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 8.13 ms                                                                        | 8.27 ms: 1.02x slower                                                                    |
| genshi_text     | 22.7 ms                                                                        | 23.1 ms: 1.02x slower                                                                    |
| genshi_xml      | 46.8 ms                                                                        | 48.6 ms: 1.04x slower                                                                    |
| django_template | 31.8 ms                                                                        | 33.2 ms: 1.04x slower                                                                    |
| Geometric mean  | (ref)                                                                          | 1.03x slower                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| fannkuch                 | 347 ms                                                                         | 329 ms: 1.05x faster                                                                     |
| json_dumps               | 7.70 ms                                                                        | 7.47 ms: 1.03x faster                                                                    |
| xml_etree_generate       | 70.0 ms                                                                        | 68.1 ms: 1.03x faster                                                                    |
| meteor_contest           | 82.9 ms                                                                        | 81.2 ms: 1.02x faster                                                                    |
| logging_silent           | 77.1 ns                                                                        | 75.6 ns: 1.02x faster                                                                    |
| deepcopy_reduce          | 2.55 us                                                                        | 2.50 us: 1.02x faster                                                                    |
| deepcopy                 | 255 us                                                                         | 252 us: 1.01x faster                                                                     |
| logging_format           | 8.57 us                                                                        | 8.49 us: 1.01x faster                                                                    |
| async_generators         | 307 ms                                                                         | 304 ms: 1.01x faster                                                                     |
| pathlib                  | 87.3 ms                                                                        | 86.5 ms: 1.01x faster                                                                    |
| regex_dna                | 119 ms                                                                         | 118 ms: 1.01x faster                                                                     |
| mdp                      | 1.71 sec                                                                       | 1.70 sec: 1.01x faster                                                                   |
| nbody                    | 93.3 ms                                                                        | 92.7 ms: 1.01x faster                                                                    |
| html5lib                 | 48.6 ms                                                                        | 48.8 ms: 1.00x slower                                                                    |
| dulwich_log              | 49.8 ms                                                                        | 50.0 ms: 1.00x slower                                                                    |
| logging_simple           | 7.95 us                                                                        | 7.99 us: 1.00x slower                                                                    |
| deepcopy_memo            | 22.8 us                                                                        | 23.0 us: 1.01x slower                                                                    |
| regex_v8                 | 16.2 ms                                                                        | 16.4 ms: 1.01x slower                                                                    |
| python_startup_no_site   | 19.9 ms                                                                        | 20.1 ms: 1.01x slower                                                                    |
| nqueens                  | 80.6 ms                                                                        | 81.6 ms: 1.01x slower                                                                    |
| xml_etree_iterparse      | 69.0 ms                                                                        | 69.8 ms: 1.01x slower                                                                    |
| sympy_str                | 220 ms                                                                         | 222 ms: 1.01x slower                                                                     |
| deltablue                | 2.72 ms                                                                        | 2.76 ms: 1.01x slower                                                                    |
| 2to3                     | 254 ms                                                                         | 258 ms: 1.02x slower                                                                     |
| tomli_loads              | 1.88 sec                                                                       | 1.91 sec: 1.02x slower                                                                   |
| sympy_sum                | 110 ms                                                                         | 112 ms: 1.02x slower                                                                     |
| mako                     | 8.13 ms                                                                        | 8.27 ms: 1.02x slower                                                                    |
| thrift                   | 737 us                                                                         | 749 us: 1.02x slower                                                                     |
| sympy_expand             | 382 ms                                                                         | 389 ms: 1.02x slower                                                                     |
| sqlglot_normalize        | 230 ms                                                                         | 233 ms: 1.02x slower                                                                     |
| hexiom                   | 5.33 ms                                                                        | 5.42 ms: 1.02x slower                                                                    |
| coverage                 | 53.0 ms                                                                        | 54.0 ms: 1.02x slower                                                                    |
| genshi_text              | 22.7 ms                                                                        | 23.1 ms: 1.02x slower                                                                    |
| create_gc_cycles         | 746 us                                                                         | 760 us: 1.02x slower                                                                     |
| scimark_lu               | 69.4 ms                                                                        | 71.0 ms: 1.02x slower                                                                    |
| regex_compile            | 107 ms                                                                         | 109 ms: 1.02x slower                                                                     |
| sqlglot_optimize         | 43.8 ms                                                                        | 45.0 ms: 1.03x slower                                                                    |
| scimark_monte_carlo      | 57.5 ms                                                                        | 58.9 ms: 1.03x slower                                                                    |
| float                    | 61.2 ms                                                                        | 62.8 ms: 1.03x slower                                                                    |
| richards                 | 38.8 ms                                                                        | 40.0 ms: 1.03x slower                                                                    |
| richards_super           | 43.6 ms                                                                        | 45.0 ms: 1.03x slower                                                                    |
| crypto_pyaes             | 57.6 ms                                                                        | 59.5 ms: 1.03x slower                                                                    |
| go                       | 118 ms                                                                         | 122 ms: 1.03x slower                                                                     |
| pickle_pure_python       | 254 us                                                                         | 262 us: 1.04x slower                                                                     |
| comprehensions           | 13.8 us                                                                        | 14.4 us: 1.04x slower                                                                    |
| genshi_xml               | 46.8 ms                                                                        | 48.6 ms: 1.04x slower                                                                    |
| pprint_pformat           | 1.36 sec                                                                       | 1.41 sec: 1.04x slower                                                                   |
| chaos                    | 52.0 ms                                                                        | 54.0 ms: 1.04x slower                                                                    |
| scimark_sparse_mat_mult  | 3.12 ms                                                                        | 3.24 ms: 1.04x slower                                                                    |
| scimark_sor              | 99.6 ms                                                                        | 104 ms: 1.04x slower                                                                     |
| django_template          | 31.8 ms                                                                        | 33.2 ms: 1.04x slower                                                                    |
| scimark_fft              | 230 ms                                                                         | 241 ms: 1.05x slower                                                                     |
| telco                    | 6.20 ms                                                                        | 6.49 ms: 1.05x slower                                                                    |
| typing_runtime_protocols | 145 us                                                                         | 152 us: 1.05x slower                                                                     |
| raytrace                 | 218 ms                                                                         | 228 ms: 1.05x slower                                                                     |
| json_loads               | 20.3 us                                                                        | 21.3 us: 1.05x slower                                                                    |
| pprint_safe_repr         | 639 ms                                                                         | 672 ms: 1.05x slower                                                                     |
| coroutines               | 17.6 ms                                                                        | 18.6 ms: 1.05x slower                                                                    |
| Geometric mean           | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (30): pyflate, asyncio_tcp, async_tree_memoization, generators, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, sqlglot_transpile, xml_etree_parse, pycparser, async_tree_cpu_io_mixed, xml_etree_process, gc_traversal, pylint, python_startup, unpickle_pure_python, pidigits, docutils, sympy_integrate, async_tree_none_tg, spectral_norm, asyncio_tcp_ssl, async_tree_io_tg, regex_effbot, async_tree_io, bench_mp_pool, sqlglot_parse, json, tornado_http, bench_thread_pool

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown