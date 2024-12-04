# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: windows-x86
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.012x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 246 ms: 1.04x faster                                            |
| chameleon      | 6.24 ms                                                         | 6.19 ms: 1.01x faster                                           |
| docutils       | 1.80 sec                                                        | 1.77 sec: 1.02x faster                                          |
| sphinx         | 729 ms                                                          | 712 ms: 1.02x faster                                            |
| tornado_http   | 105 ms                                                          | 94.1 ms: 1.11x faster                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 490 ms                                                          | 484 ms: 1.01x faster                                            |
| asyncio_websockets      | 352 ms                                                          | 348 ms: 1.01x faster                                            |
| coroutines              | 16.1 ms                                                         | 15.9 ms: 1.01x faster                                           |
| async_tree_none         | 245 ms                                                          | 247 ms: 1.01x slower                                            |
| async_tree_none_tg      | 216 ms                                                          | 218 ms: 1.01x slower                                            |
| async_tree_io_tg        | 499 ms                                                          | 510 ms: 1.02x slower                                            |
| Geometric mean          | (ref)                                                           | 1.00x faster                                                    |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization, async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                            |
| float          | 56.4 ms                                                         | 55.6 ms: 1.01x faster                                           |
| nbody          | 81.4 ms                                                         | 82.6 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                           |
| regex_compile  | 101 ms                                                          | 101 ms: 1.00x faster                                            |
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                           |
| regex_dna      | 112 ms                                                          | 114 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                         | 7.27 ms: 1.04x faster                                           |
| tomli_loads          | 1.74 sec                                                        | 1.70 sec: 1.02x faster                                          |
| unpickle_pure_python | 162 us                                                          | 159 us: 1.02x faster                                            |
| pickle_pure_python   | 239 us                                                          | 235 us: 1.02x faster                                            |
| xml_etree_generate   | 61.9 ms                                                         | 62.6 ms: 1.01x slower                                           |
| json_loads           | 21.7 us                                                         | 22.1 us: 1.02x slower                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 63.0 ms: 1.03x slower                                           |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                            |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 20.2 ms                                                         | 19.3 ms: 1.04x faster                                           |
| python_startup         | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                           |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 29.9 ms: 1.07x faster                                           |
| genshi_text     | 21.7 ms                                                         | 20.7 ms: 1.05x faster                                           |
| genshi_xml      | 49.0 ms                                                         | 47.6 ms: 1.03x faster                                           |
| mako            | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                           |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot            | 1.82 ms                                                         | 1.55 ms: 1.17x faster                                           |
| tornado_http            | 105 ms                                                          | 94.1 ms: 1.11x faster                                           |
| deepcopy_reduce         | 2.94 us                                                         | 2.67 us: 1.10x faster                                           |
| pathlib                 | 89.1 ms                                                         | 83.0 ms: 1.07x faster                                           |
| django_template         | 32.0 ms                                                         | 29.9 ms: 1.07x faster                                           |
| deepcopy                | 311 us                                                          | 294 us: 1.06x faster                                            |
| deepcopy_memo           | 26.2 us                                                         | 24.9 us: 1.05x faster                                           |
| genshi_text             | 21.7 ms                                                         | 20.7 ms: 1.05x faster                                           |
| python_startup_no_site  | 20.2 ms                                                         | 19.3 ms: 1.04x faster                                           |
| bench_mp_pool           | 93.6 ms                                                         | 89.7 ms: 1.04x faster                                           |
| nqueens                 | 75.1 ms                                                         | 72.0 ms: 1.04x faster                                           |
| shortest_path           | 298 ms                                                          | 286 ms: 1.04x faster                                            |
| python_startup          | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                           |
| k_core                  | 1.43 sec                                                        | 1.38 sec: 1.04x faster                                          |
| 2to3                    | 255 ms                                                          | 246 ms: 1.04x faster                                            |
| json_dumps              | 7.53 ms                                                         | 7.27 ms: 1.04x faster                                           |
| bpe_tokeniser           | 3.49 sec                                                        | 3.37 sec: 1.04x faster                                          |
| logging_silent          | 62.4 ns                                                         | 60.3 ns: 1.04x faster                                           |
| dulwich_log             | 50.2 ms                                                         | 48.5 ms: 1.03x faster                                           |
| comprehensions          | 13.1 us                                                         | 12.7 us: 1.03x faster                                           |
| genshi_xml              | 49.0 ms                                                         | 47.6 ms: 1.03x faster                                           |
| pprint_safe_repr        | 658 ms                                                          | 639 ms: 1.03x faster                                            |
| mdp                     | 1.70 sec                                                        | 1.65 sec: 1.03x faster                                          |
| pidigits                | 204 ms                                                          | 198 ms: 1.03x faster                                            |
| meteor_contest          | 78.1 ms                                                         | 76.0 ms: 1.03x faster                                           |
| pycparser               | 869 ms                                                          | 846 ms: 1.03x faster                                            |
| connected_components    | 266 ms                                                          | 259 ms: 1.03x faster                                            |
| pyflate                 | 322 ms                                                          | 314 ms: 1.03x faster                                            |
| tomli_loads             | 1.74 sec                                                        | 1.70 sec: 1.02x faster                                          |
| sphinx                  | 729 ms                                                          | 712 ms: 1.02x faster                                            |
| thrift                  | 10.3 ms                                                         | 10.0 ms: 1.02x faster                                           |
| sympy_sum               | 108 ms                                                          | 106 ms: 1.02x faster                                            |
| sqlalchemy_imperative   | 11.3 ms                                                         | 11.1 ms: 1.02x faster                                           |
| richards                | 33.4 ms                                                         | 32.7 ms: 1.02x faster                                           |
| unpickle_pure_python    | 162 us                                                          | 159 us: 1.02x faster                                            |
| sympy_integrate         | 15.2 ms                                                         | 15.0 ms: 1.02x faster                                           |
| pickle_pure_python      | 239 us                                                          | 235 us: 1.02x faster                                            |
| docutils                | 1.80 sec                                                        | 1.77 sec: 1.02x faster                                          |
| sqlglot_optimize        | 42.4 ms                                                         | 41.8 ms: 1.02x faster                                           |
| sqlalchemy_declarative  | 94.8 ms                                                         | 93.5 ms: 1.01x faster                                           |
| float                   | 56.4 ms                                                         | 55.6 ms: 1.01x faster                                           |
| sqlglot_normalize       | 223 ms                                                          | 220 ms: 1.01x faster                                            |
| gc_traversal            | 1.76 ms                                                         | 1.74 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed | 490 ms                                                          | 484 ms: 1.01x faster                                            |
| sympy_str               | 214 ms                                                          | 212 ms: 1.01x faster                                            |
| asyncio_websockets      | 352 ms                                                          | 348 ms: 1.01x faster                                            |
| sympy_expand            | 377 ms                                                          | 373 ms: 1.01x faster                                            |
| coroutines              | 16.1 ms                                                         | 15.9 ms: 1.01x faster                                           |
| richards_super          | 37.0 ms                                                         | 36.7 ms: 1.01x faster                                           |
| chameleon               | 6.24 ms                                                         | 6.19 ms: 1.01x faster                                           |
| pprint_pformat          | 1.32 sec                                                        | 1.31 sec: 1.01x faster                                          |
| hexiom                  | 4.60 ms                                                         | 4.56 ms: 1.01x faster                                           |
| fannkuch                | 288 ms                                                          | 286 ms: 1.01x faster                                            |
| scimark_monte_carlo     | 48.7 ms                                                         | 48.3 ms: 1.01x faster                                           |
| regex_compile           | 101 ms                                                          | 101 ms: 1.00x faster                                            |
| scimark_fft             | 204 ms                                                          | 205 ms: 1.00x slower                                            |
| regex_v8                | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                           |
| async_tree_none         | 245 ms                                                          | 247 ms: 1.01x slower                                            |
| async_tree_none_tg      | 216 ms                                                          | 218 ms: 1.01x slower                                            |
| xml_etree_generate      | 61.9 ms                                                         | 62.6 ms: 1.01x slower                                           |
| go                      | 111 ms                                                          | 112 ms: 1.01x slower                                            |
| logging_simple          | 7.89 us                                                         | 8.01 us: 1.01x slower                                           |
| nbody                   | 81.4 ms                                                         | 82.6 ms: 1.01x slower                                           |
| crypto_pyaes            | 56.6 ms                                                         | 57.5 ms: 1.02x slower                                           |
| regex_dna               | 112 ms                                                          | 114 ms: 1.02x slower                                            |
| json_loads              | 21.7 us                                                         | 22.1 us: 1.02x slower                                           |
| async_tree_io_tg        | 499 ms                                                          | 510 ms: 1.02x slower                                            |
| chaos                   | 49.4 ms                                                         | 50.5 ms: 1.02x slower                                           |
| raytrace                | 203 ms                                                          | 208 ms: 1.02x slower                                            |
| json                    | 4.40 ms                                                         | 4.51 ms: 1.03x slower                                           |
| scimark_lu              | 60.7 ms                                                         | 62.3 ms: 1.03x slower                                           |
| xml_etree_iterparse     | 61.3 ms                                                         | 63.0 ms: 1.03x slower                                           |
| mako                    | 7.02 ms                                                         | 7.33 ms: 1.04x slower                                           |
| xml_etree_parse         | 102 ms                                                          | 108 ms: 1.05x slower                                            |
| telco                   | 6.27 ms                                                         | 6.60 ms: 1.05x slower                                           |
| Geometric mean          | (ref)                                                           | 1.01x faster                                                    |

Benchmark hidden because not significant (21): bench_thread_pool, async_tree_io, spectral_norm, async_tree_memoization, create_gc_cycles, typing_runtime_protocols, pylint, async_generators, scimark_sparse_mat_mult, generators, xml_etree_process, sqlglot_transpile, sqlglot_parse, coverage, scimark_sor, gevent_hub, async_tree_memoization_tg, deltablue, logging_format, html5lib, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown