# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| html5lib       | 72.9 ms                                                      | 73.8 ms: 1.01x slower                                                                 |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.21x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 300 ms: 1.14x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 771 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                                  |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                                  |
| async_generators           | 364 ms                                                       | 356 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 86.9 ms: 1.06x faster                                                                 |
| float          | 81.6 ms                                                      | 82.4 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                                  |
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                                 |
| regex_v8       | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.30 sec: 1.06x faster                                                                |
| pickle_pure_python   | 322 us                                                       | 311 us: 1.03x faster                                                                  |
| xml_etree_process    | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                                 |
| unpickle_pure_python | 216 us                                                       | 211 us: 1.02x faster                                                                  |
| xml_etree_generate   | 85.2 ms                                                      | 84.6 ms: 1.01x faster                                                                 |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                                 |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                                  |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                                 |
| python_startup_no_site | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| genshi_xml      | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.99 ms: 1.33x faster                                                                 |
| deepcopy                   | 388 us                                                       | 292 us: 1.33x faster                                                                  |
| deepcopy_memo              | 38.9 us                                                      | 29.4 us: 1.32x faster                                                                 |
| async_tree_memoization_tg  | 458 ms                                                       | 380 ms: 1.21x faster                                                                  |
| deepcopy_reduce            | 3.49 us                                                      | 2.96 us: 1.18x faster                                                                 |
| generators                 | 33.9 ms                                                      | 28.9 ms: 1.17x faster                                                                 |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                                 |
| scimark_sor                | 125 ms                                                       | 107 ms: 1.17x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 300 ms: 1.14x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                                  |
| telco                      | 8.77 ms                                                      | 7.98 ms: 1.10x faster                                                                 |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                                 |
| genshi_text                | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| fannkuch                   | 384 ms                                                       | 358 ms: 1.07x faster                                                                  |
| richards_super             | 60.2 ms                                                      | 56.2 ms: 1.07x faster                                                                 |
| bench_thread_pool          | 929 us                                                       | 869 us: 1.07x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 771 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                                  |
| nbody                      | 92.1 ms                                                      | 86.9 ms: 1.06x faster                                                                 |
| tomli_loads                | 2.43 sec                                                     | 2.30 sec: 1.06x faster                                                                |
| genshi_xml                 | 58.0 ms                                                      | 54.9 ms: 1.06x faster                                                                 |
| thrift                     | 918 us                                                       | 872 us: 1.05x faster                                                                  |
| json                       | 5.62 ms                                                      | 5.37 ms: 1.05x faster                                                                 |
| richards                   | 52.5 ms                                                      | 50.2 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.92 sec: 1.03x faster                                                                |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                                  |
| pickle_pure_python         | 322 us                                                       | 311 us: 1.03x faster                                                                  |
| bench_mp_pool              | 4.82 ms                                                      | 4.67 ms: 1.03x faster                                                                 |
| go                         | 167 ms                                                       | 162 ms: 1.03x faster                                                                  |
| pyflate                    | 493 ms                                                       | 478 ms: 1.03x faster                                                                  |
| nqueens                    | 92.3 ms                                                      | 89.7 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 73.5 ms                                                      | 71.5 ms: 1.03x faster                                                                 |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                                  |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                                  |
| xml_etree_process          | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.4 ms                                                      | 94.8 ms: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 216 us                                                       | 211 us: 1.02x faster                                                                  |
| logging_format             | 6.95 us                                                      | 6.81 us: 1.02x faster                                                                 |
| async_generators           | 364 ms                                                       | 356 ms: 1.02x faster                                                                  |
| hexiom                     | 6.47 ms                                                      | 6.34 ms: 1.02x faster                                                                 |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                                  |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                                  |
| mdp                        | 2.53 sec                                                     | 2.48 sec: 1.02x faster                                                                |
| pycparser                  | 1.28 sec                                                     | 1.26 sec: 1.02x faster                                                                |
| spectral_norm              | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                                 |
| regex_effbot               | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                                 |
| logging_simple             | 6.28 us                                                      | 6.19 us: 1.01x faster                                                                 |
| coverage                   | 84.5 ms                                                      | 83.6 ms: 1.01x faster                                                                 |
| pprint_safe_repr           | 835 ms                                                       | 827 ms: 1.01x faster                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.18 ms: 1.01x faster                                                                 |
| raytrace                   | 267 ms                                                       | 265 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.2 ms                                                      | 84.6 ms: 1.01x faster                                                                 |
| sympy_expand               | 506 ms                                                       | 503 ms: 1.01x faster                                                                  |
| gc_traversal               | 4.48 ms                                                      | 4.45 ms: 1.01x faster                                                                 |
| sympy_str                  | 297 ms                                                       | 296 ms: 1.00x faster                                                                  |
| sqlglot_optimize           | 58.7 ms                                                      | 58.9 ms: 1.00x slower                                                                 |
| sqlglot_normalize          | 119 ms                                                       | 120 ms: 1.01x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                                  |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                                 |
| float                      | 81.6 ms                                                      | 82.4 ms: 1.01x slower                                                                 |
| django_template            | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| scimark_fft                | 298 ms                                                       | 301 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                                 |
| deltablue                  | 3.38 ms                                                      | 3.43 ms: 1.01x slower                                                                 |
| html5lib                   | 72.9 ms                                                      | 73.8 ms: 1.01x slower                                                                 |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                                 |
| regex_v8                   | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                                 |
| chaos                      | 60.6 ms                                                      | 62.0 ms: 1.02x slower                                                                 |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                                 |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.1 ms: 1.03x slower                                                                 |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.04x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (9): asyncio_websockets, typing_runtime_protocols, mako, logging_silent, xml_etree_parse, pprint_pformat, pidigits, sympy_integrate, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x