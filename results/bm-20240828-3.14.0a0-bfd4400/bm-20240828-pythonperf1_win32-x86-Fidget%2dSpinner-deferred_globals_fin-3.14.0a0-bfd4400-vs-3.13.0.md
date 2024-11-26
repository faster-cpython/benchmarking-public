# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.011x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 258 ms: 1.01x slower                                                                     |
| docutils       | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                                   |
| html5lib       | 47.1 ms                                                         | 48.8 ms: 1.04x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                                     |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.08x faster                                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                                     |
| async_tree_io_tg           | 499 ms                                                          | 514 ms: 1.03x slower                                                                     |
| async_tree_io              | 530 ms                                                          | 553 ms: 1.04x slower                                                                     |
| async_generators           | 267 ms                                                          | 304 ms: 1.14x slower                                                                     |
| coroutines                 | 16.1 ms                                                         | 18.6 ms: 1.15x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                                     |
| float          | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                                    |
| nbody          | 81.4 ms                                                         | 92.7 ms: 1.14x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                                     |
| regex_v8       | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                                    |
| regex_effbot   | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                                    |
| regex_compile  | 101 ms                                                          | 109 ms: 1.08x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.3 us: 1.02x faster                                                                    |
| json_dumps           | 7.53 ms                                                         | 7.47 ms: 1.01x faster                                                                    |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.06x slower                                                                     |
| pickle_pure_python   | 239 us                                                          | 262 us: 1.10x slower                                                                     |
| tomli_loads          | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                                                   |
| xml_etree_generate   | 61.9 ms                                                         | 68.1 ms: 1.10x slower                                                                    |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                                     |
| xml_etree_iterparse  | 61.3 ms                                                         | 69.8 ms: 1.14x slower                                                                    |
| xml_etree_process    | 44.6 ms                                                         | 51.2 ms: 1.15x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 33.2 ms: 1.04x slower                                                                    |
| genshi_text     | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                                    |
| mako            | 7.02 ms                                                         | 8.27 ms: 1.18x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 749 us: 13.69x faster                                                                    |
| coverage                   | 326 ms                                                          | 54.0 ms: 6.04x faster                                                                    |
| create_gc_cycles           | 1.08 ms                                                         | 760 us: 1.42x faster                                                                     |
| bench_mp_pool              | 93.6 ms                                                         | 73.1 ms: 1.28x faster                                                                    |
| deepcopy                   | 311 us                                                          | 252 us: 1.23x faster                                                                     |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                                    |
| python_startup             | 28.3 ms                                                         | 24.0 ms: 1.18x faster                                                                    |
| deepcopy_reduce            | 2.94 us                                                         | 2.50 us: 1.18x faster                                                                    |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                                     |
| deepcopy_memo              | 26.2 us                                                         | 23.0 us: 1.14x faster                                                                    |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                                     |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.08x faster                                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 471 ms: 1.04x faster                                                                     |
| json                       | 4.40 ms                                                         | 4.25 ms: 1.03x faster                                                                    |
| pathlib                    | 89.1 ms                                                         | 86.5 ms: 1.03x faster                                                                    |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                                     |
| json_loads                 | 21.7 us                                                         | 21.3 us: 1.02x faster                                                                    |
| pycparser                  | 869 ms                                                          | 857 ms: 1.01x faster                                                                     |
| logging_format             | 8.59 us                                                         | 8.49 us: 1.01x faster                                                                    |
| json_dumps                 | 7.53 ms                                                         | 7.47 ms: 1.01x faster                                                                    |
| 2to3                       | 255 ms                                                          | 258 ms: 1.01x slower                                                                     |
| logging_simple             | 7.89 us                                                         | 7.99 us: 1.01x slower                                                                    |
| pprint_safe_repr           | 658 ms                                                          | 672 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 499 ms                                                          | 514 ms: 1.03x slower                                                                     |
| sympy_expand               | 377 ms                                                          | 389 ms: 1.03x slower                                                                     |
| sympy_integrate            | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                                    |
| telco                      | 6.27 ms                                                         | 6.49 ms: 1.03x slower                                                                    |
| django_template            | 32.0 ms                                                         | 33.2 ms: 1.04x slower                                                                    |
| html5lib                   | 47.1 ms                                                         | 48.8 ms: 1.04x slower                                                                    |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                                     |
| sympy_str                  | 214 ms                                                          | 222 ms: 1.04x slower                                                                     |
| meteor_contest             | 78.1 ms                                                         | 81.2 ms: 1.04x slower                                                                    |
| async_tree_io              | 530 ms                                                          | 553 ms: 1.04x slower                                                                     |
| sqlglot_normalize          | 223 ms                                                          | 233 ms: 1.05x slower                                                                     |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                                     |
| crypto_pyaes               | 56.6 ms                                                         | 59.5 ms: 1.05x slower                                                                    |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.05x slower                                                                     |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.06x slower                                                                     |
| regex_v8                   | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                                    |
| sqlglot_optimize           | 42.4 ms                                                         | 45.0 ms: 1.06x slower                                                                    |
| genshi_text                | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                                    |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                                    |
| regex_effbot               | 1.82 ms                                                         | 1.93 ms: 1.06x slower                                                                    |
| pprint_pformat             | 1.32 sec                                                        | 1.41 sec: 1.07x slower                                                                   |
| sqlglot_parse              | 1.02 ms                                                         | 1.10 ms: 1.07x slower                                                                    |
| docutils                   | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                                   |
| typing_runtime_protocols   | 141 us                                                          | 152 us: 1.08x slower                                                                     |
| regex_compile              | 101 ms                                                          | 109 ms: 1.08x slower                                                                     |
| nqueens                    | 75.1 ms                                                         | 81.6 ms: 1.09x slower                                                                    |
| comprehensions             | 13.1 us                                                         | 14.4 us: 1.09x slower                                                                    |
| chaos                      | 49.4 ms                                                         | 54.0 ms: 1.09x slower                                                                    |
| pickle_pure_python         | 239 us                                                          | 262 us: 1.10x slower                                                                     |
| tomli_loads                | 1.74 sec                                                        | 1.91 sec: 1.10x slower                                                                   |
| xml_etree_generate         | 61.9 ms                                                         | 68.1 ms: 1.10x slower                                                                    |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.10x slower                                                                     |
| go                         | 111 ms                                                          | 122 ms: 1.10x slower                                                                     |
| float                      | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                                    |
| spectral_norm              | 70.0 ms                                                         | 78.4 ms: 1.12x slower                                                                    |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.24 ms: 1.13x slower                                                                    |
| raytrace                   | 203 ms                                                          | 228 ms: 1.13x slower                                                                     |
| nbody                      | 81.4 ms                                                         | 92.7 ms: 1.14x slower                                                                    |
| xml_etree_iterparse        | 61.3 ms                                                         | 69.8 ms: 1.14x slower                                                                    |
| async_generators           | 267 ms                                                          | 304 ms: 1.14x slower                                                                     |
| fannkuch                   | 288 ms                                                          | 329 ms: 1.14x slower                                                                     |
| xml_etree_process          | 44.6 ms                                                         | 51.2 ms: 1.15x slower                                                                    |
| coroutines                 | 16.1 ms                                                         | 18.6 ms: 1.15x slower                                                                    |
| pyflate                    | 322 ms                                                          | 372 ms: 1.15x slower                                                                     |
| scimark_lu                 | 60.7 ms                                                         | 71.0 ms: 1.17x slower                                                                    |
| deltablue                  | 2.35 ms                                                         | 2.76 ms: 1.17x slower                                                                    |
| mako                       | 7.02 ms                                                         | 8.27 ms: 1.18x slower                                                                    |
| hexiom                     | 4.60 ms                                                         | 5.42 ms: 1.18x slower                                                                    |
| scimark_fft                | 204 ms                                                          | 241 ms: 1.18x slower                                                                     |
| richards                   | 33.4 ms                                                         | 40.0 ms: 1.20x slower                                                                    |
| scimark_sor                | 85.8 ms                                                         | 104 ms: 1.21x slower                                                                     |
| scimark_monte_carlo        | 48.7 ms                                                         | 58.9 ms: 1.21x slower                                                                    |
| logging_silent             | 62.4 ns                                                         | 75.6 ns: 1.21x slower                                                                    |
| richards_super             | 37.0 ms                                                         | 45.0 ms: 1.21x slower                                                                    |
| generators                 | 21.5 ms                                                         | 27.0 ms: 1.25x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                             |

Benchmark hidden because not significant (6): genshi_xml, python_startup_no_site, dulwich_log, mdp, bench_thread_pool, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown