# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.252x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.09x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| sphinx         | 719 ms                                                          | 638 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.23x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 335 ms: 1.36x faster                                                             |
| async_tree_io              | 526 ms                                                          | 390 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 150 ms: 1.34x faster                                                             |
| nbody          | 80.0 ms                                                         | 67.0 ms: 1.19x faster                                                            |
| float          | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 81.4 ms: 1.24x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.1 ms: 1.19x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.5 us: 1.49x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.49 ms: 1.33x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.40 sec: 1.23x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 89.5 ms: 1.20x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 137 us: 1.17x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 39.9 ms: 1.11x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 57.1 ms: 1.08x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 216 us: 1.07x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.0 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.4 ms: 1.42x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                            |
| django_template | 29.8 ms                                                         | 25.0 ms: 1.19x faster                                                            |
| mako            | 7.09 ms                                                         | 6.76 ms: 1.05x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.24x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 506 us: 19.74x faster                                                            |
| coverage                   | 324 ms                                                          | 51.4 ms: 6.30x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.2 ms: 2.84x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.23x faster                                                             |
| mdp                        | 1.62 sec                                                        | 826 ms: 1.97x faster                                                             |
| deepcopy                   | 314 us                                                          | 169 us: 1.85x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.22 ms: 1.65x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.5 us: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| json                       | 4.27 ms                                                         | 2.92 ms: 1.46x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 17.9 us: 1.42x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 35.4 ms: 1.42x faster                                                            |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| go                         | 109 ms                                                          | 77.3 ms: 1.41x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 335 ms: 1.36x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.9 ms: 1.35x faster                                                            |
| async_tree_io              | 526 ms                                                          | 390 ms: 1.35x faster                                                             |
| pidigits                   | 201 ms                                                          | 150 ms: 1.34x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.49 ms: 1.33x faster                                                            |
| logging_format             | 8.72 us                                                         | 6.65 us: 1.31x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.15 us: 1.30x faster                                                            |
| sympy_expand               | 373 ms                                                          | 290 ms: 1.29x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.03 sec: 1.29x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 508 ms: 1.28x faster                                                             |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| regex_compile              | 101 ms                                                          | 81.4 ms: 1.24x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.40 sec: 1.23x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.60 us: 1.22x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.7 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.5 ms: 1.20x faster                                                            |
| pycparser                  | 872 ms                                                          | 725 ms: 1.20x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 89.5 ms: 1.20x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 88.0 ms: 1.20x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.5 ms: 1.20x faster                                                            |
| nbody                      | 80.0 ms                                                         | 67.0 ms: 1.19x faster                                                            |
| django_template            | 29.8 ms                                                         | 25.0 ms: 1.19x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.5 ms: 1.19x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.1 ms: 1.19x faster                                                            |
| scimark_fft                | 205 ms                                                          | 172 ms: 1.19x faster                                                             |
| richards_super             | 36.7 ms                                                         | 31.0 ms: 1.18x faster                                                            |
| float                      | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 48.2 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 137 us: 1.17x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.9 ms: 1.17x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 867 us: 1.16x faster                                                             |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 62.8 ms: 1.15x faster                                                            |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                             |
| pyflate                    | 320 ms                                                          | 283 ms: 1.13x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 3.06 sec: 1.13x faster                                                           |
| sphinx                     | 719 ms                                                          | 638 ms: 1.13x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.2 us: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.55 ms: 1.11x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                            |
| fannkuch                   | 299 ms                                                          | 270 ms: 1.11x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 39.9 ms: 1.11x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 63.3 ms: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.09x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.0 ms: 1.09x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 79.1 ms: 1.09x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.0 ms: 1.09x faster                                                            |
| raytrace                   | 201 ms                                                          | 186 ms: 1.08x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 57.1 ms: 1.08x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.13 ms: 1.07x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 216 us: 1.07x faster                                                             |
| mako                       | 7.09 ms                                                         | 6.76 ms: 1.05x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.24 ms: 1.04x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 58.4 ns: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 73.6 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.4 ms: 1.01x slower                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.05x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.06 ms: 1.18x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.30 ms: 1.22x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.24x slower                                                           |
| connected_components       | 267 ms                                                          | 334 ms: 1.25x slower                                                             |
| shortest_path              | 290 ms                                                          | 363 ms: 1.25x slower                                                             |
| many_optionals             | 436 us                                                          | 566 us: 1.30x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.7 ms: 2.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (3): python_startup_no_site, scimark_lu, bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.252x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown