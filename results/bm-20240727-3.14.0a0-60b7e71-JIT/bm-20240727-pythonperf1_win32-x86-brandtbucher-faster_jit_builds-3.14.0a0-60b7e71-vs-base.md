# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-x86
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 1.96 sec                                                                       | 1.95 sec: 1.01x faster                                                            |
| html5lib       | 47.9 ms                                                                        | 46.4 ms: 1.03x faster                                                             |
| tornado_http   | 108 ms                                                                         | 106 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 480 ms                                                                         | 463 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 488 ms                                                                         | 471 ms: 1.04x faster                                                              |
| async_tree_memoization     | 277 ms                                                                         | 271 ms: 1.02x faster                                                              |
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                      |

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, coroutines, async_tree_io, async_generators, async_tree_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 42.6 ms                                                                        | 42.9 ms: 1.01x slower                                                             |
| nbody          | 50.5 ms                                                                        | 53.1 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                         | 116 ms: 1.02x faster                                                              |
| regex_compile  | 96.3 ms                                                                        | 95.3 ms: 1.01x faster                                                             |
| regex_effbot   | 1.99 ms                                                                        | 2.00 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.50 sec                                                                       | 1.46 sec: 1.03x faster                                                            |
| json_loads           | 21.7 us                                                                        | 21.2 us: 1.02x faster                                                             |
| unpickle_pure_python | 151 us                                                                         | 149 us: 1.02x faster                                                              |
| xml_etree_generate   | 60.0 ms                                                                        | 59.6 ms: 1.01x faster                                                             |
| xml_etree_process    | 44.1 ms                                                                        | 44.7 ms: 1.01x slower                                                             |
| json_dumps           | 6.88 ms                                                                        | 7.00 ms: 1.02x slower                                                             |
| xml_etree_parse      | 105 ms                                                                         | 108 ms: 1.03x slower                                                              |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.6 ms                                                                        | 23.9 ms: 1.03x faster                                                             |
| python_startup_no_site | 20.5 ms                                                                        | 20.1 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                                          | 1.02x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                        | 32.2 ms: 1.04x faster                                                             |
| genshi_text     | 23.6 ms                                                                        | 22.8 ms: 1.04x faster                                                             |
| genshi_xml      | 51.9 ms                                                                        | 51.4 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                                          | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| telco                      | 6.22 ms                                                                        | 5.77 ms: 1.08x faster                                                             |
| thrift                     | 762 us                                                                         | 725 us: 1.05x faster                                                              |
| django_template            | 33.5 ms                                                                        | 32.2 ms: 1.04x faster                                                             |
| genshi_text                | 23.6 ms                                                                        | 22.8 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed_tg | 480 ms                                                                         | 463 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 488 ms                                                                         | 471 ms: 1.04x faster                                                              |
| sqlglot_optimize           | 45.1 ms                                                                        | 43.6 ms: 1.03x faster                                                             |
| html5lib                   | 47.9 ms                                                                        | 46.4 ms: 1.03x faster                                                             |
| comprehensions             | 11.7 us                                                                        | 11.4 us: 1.03x faster                                                             |
| tomli_loads                | 1.50 sec                                                                       | 1.46 sec: 1.03x faster                                                            |
| python_startup             | 24.6 ms                                                                        | 23.9 ms: 1.03x faster                                                             |
| logging_format             | 8.34 us                                                                        | 8.13 us: 1.03x faster                                                             |
| typing_runtime_protocols   | 150 us                                                                         | 146 us: 1.03x faster                                                              |
| deepcopy                   | 243 us                                                                         | 237 us: 1.03x faster                                                              |
| scimark_sparse_mat_mult    | 2.43 ms                                                                        | 2.37 ms: 1.02x faster                                                             |
| async_tree_memoization     | 277 ms                                                                         | 271 ms: 1.02x faster                                                              |
| generators                 | 28.9 ms                                                                        | 28.2 ms: 1.02x faster                                                             |
| sympy_sum                  | 110 ms                                                                         | 108 ms: 1.02x faster                                                              |
| sympy_expand               | 388 ms                                                                         | 380 ms: 1.02x faster                                                              |
| json_loads                 | 21.7 us                                                                        | 21.2 us: 1.02x faster                                                             |
| tornado_http               | 108 ms                                                                         | 106 ms: 1.02x faster                                                              |
| chaos                      | 52.6 ms                                                                        | 51.6 ms: 1.02x faster                                                             |
| regex_dna                  | 119 ms                                                                         | 116 ms: 1.02x faster                                                              |
| sqlglot_normalize          | 240 ms                                                                         | 236 ms: 1.02x faster                                                              |
| spectral_norm              | 48.2 ms                                                                        | 47.3 ms: 1.02x faster                                                             |
| logging_simple             | 7.60 us                                                                        | 7.47 us: 1.02x faster                                                             |
| deltablue                  | 2.76 ms                                                                        | 2.71 ms: 1.02x faster                                                             |
| json                       | 4.38 ms                                                                        | 4.31 ms: 1.02x faster                                                             |
| unpickle_pure_python       | 151 us                                                                         | 149 us: 1.02x faster                                                              |
| python_startup_no_site     | 20.5 ms                                                                        | 20.1 ms: 1.02x faster                                                             |
| nqueens                    | 75.4 ms                                                                        | 74.3 ms: 1.01x faster                                                             |
| sqlglot_parse              | 946 us                                                                         | 936 us: 1.01x faster                                                              |
| regex_compile              | 96.3 ms                                                                        | 95.3 ms: 1.01x faster                                                             |
| go                         | 117 ms                                                                         | 115 ms: 1.01x faster                                                              |
| genshi_xml                 | 51.9 ms                                                                        | 51.4 ms: 1.01x faster                                                             |
| pathlib                    | 89.5 ms                                                                        | 88.8 ms: 1.01x faster                                                             |
| xml_etree_generate         | 60.0 ms                                                                        | 59.6 ms: 1.01x faster                                                             |
| docutils                   | 1.96 sec                                                                       | 1.95 sec: 1.01x faster                                                            |
| mdp                        | 1.67 sec                                                                       | 1.66 sec: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                            |
| sympy_str                  | 217 ms                                                                         | 215 ms: 1.01x faster                                                              |
| meteor_contest             | 71.0 ms                                                                        | 70.8 ms: 1.00x faster                                                             |
| regex_effbot               | 1.99 ms                                                                        | 2.00 ms: 1.00x slower                                                             |
| float                      | 42.6 ms                                                                        | 42.9 ms: 1.01x slower                                                             |
| xml_etree_process          | 44.1 ms                                                                        | 44.7 ms: 1.01x slower                                                             |
| raytrace                   | 223 ms                                                                         | 226 ms: 1.01x slower                                                              |
| pycparser                  | 784 ms                                                                         | 796 ms: 1.01x slower                                                              |
| logging_silent             | 58.0 ns                                                                        | 59.0 ns: 1.02x slower                                                             |
| json_dumps                 | 6.88 ms                                                                        | 7.00 ms: 1.02x slower                                                             |
| richards_super             | 38.9 ms                                                                        | 39.5 ms: 1.02x slower                                                             |
| dulwich_log                | 48.8 ms                                                                        | 49.8 ms: 1.02x slower                                                             |
| fannkuch                   | 232 ms                                                                         | 238 ms: 1.03x slower                                                              |
| scimark_sor                | 104 ms                                                                         | 107 ms: 1.03x slower                                                              |
| xml_etree_parse            | 105 ms                                                                         | 108 ms: 1.03x slower                                                              |
| crypto_pyaes               | 47.1 ms                                                                        | 48.7 ms: 1.03x slower                                                             |
| pprint_safe_repr           | 561 ms                                                                         | 582 ms: 1.04x slower                                                              |
| pprint_pformat             | 1.14 sec                                                                       | 1.20 sec: 1.05x slower                                                            |
| nbody                      | 50.5 ms                                                                        | 53.1 ms: 1.05x slower                                                             |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                      |

Benchmark hidden because not significant (30): async_tree_none, pylint, async_tree_none_tg, async_tree_memoization_tg, scimark_lu, deepcopy_memo, coroutines, sympy_integrate, 2to3, async_tree_io, pickle_pure_python, gc_traversal, richards, mako, create_gc_cycles, deepcopy_reduce, scimark_monte_carlo, pidigits, pyflate, bench_mp_pool, regex_v8, scimark_fft, async_generators, sqlglot_transpile, xml_etree_iterparse, hexiom, coverage, async_tree_io_tg, asyncio_tcp, bench_thread_pool

# HPT report

- Reliability score: 99.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown