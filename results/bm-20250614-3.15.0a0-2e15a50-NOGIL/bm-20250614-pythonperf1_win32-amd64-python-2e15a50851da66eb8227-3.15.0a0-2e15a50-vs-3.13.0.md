# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.299x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 336 ms: 1.34x slower                                                             |
| docutils       | 1.78 sec                                                        | 4.15 sec: 2.33x slower                                                           |
| html5lib       | 47.5 ms                                                         | 63.9 ms: 1.34x slower                                                            |
| sphinx         | 719 ms                                                          | 1.28 sec: 1.78x slower                                                           |
| Geometric mean | (ref)                                                           | 1.66x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets        | 363 ms                                                          | 144 ms: 2.52x faster                                                             |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 479 ms: 1.01x faster                                                             |
| async_tree_io             | 526 ms                                                          | 577 ms: 1.10x slower                                                             |
| async_tree_memoization_tg | 282 ms                                                          | 311 ms: 1.10x slower                                                             |
| async_tree_io_tg          | 494 ms                                                          | 549 ms: 1.11x slower                                                             |
| async_tree_none           | 245 ms                                                          | 274 ms: 1.12x slower                                                             |
| async_tree_memoization    | 297 ms                                                          | 334 ms: 1.12x slower                                                             |
| async_tree_none_tg        | 214 ms                                                          | 246 ms: 1.15x slower                                                             |
| async_generators          | 270 ms                                                          | 410 ms: 1.52x slower                                                             |
| coroutines                | 16.2 ms                                                         | 32.8 ms: 2.02x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 141 ms: 1.42x faster                                                             |
| float          | 54.6 ms                                                         | 97.9 ms: 1.79x slower                                                            |
| nbody          | 80.0 ms                                                         | 177 ms: 2.21x slower                                                             |
| Geometric mean | (ref)                                                           | 1.41x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.81 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 160 ms: 1.59x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.04x slower                                                             |
| json_loads           | 21.6 us                                                         | 22.7 us: 1.05x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.48 ms: 1.30x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 93.0 ms: 1.49x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 79.0 ms: 1.79x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 448 us: 1.94x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 358 us: 2.23x slower                                                             |
| tomli_loads          | 1.71 sec                                                        | 5.01 sec: 2.92x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.63x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.0 ms: 1.01x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 66.0 ms: 1.32x slower                                                            |
| django_template | 29.8 ms                                                         | 45.4 ms: 1.53x slower                                                            |
| genshi_text     | 21.5 ms                                                         | 33.2 ms: 1.55x slower                                                            |
| mako            | 7.09 ms                                                         | 16.5 ms: 2.33x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.64x slower                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 837 us: 11.93x faster                                                            |
| coverage                  | 324 ms                                                          | 83.7 ms: 3.87x faster                                                            |
| asyncio_websockets        | 363 ms                                                          | 144 ms: 2.52x faster                                                             |
| pathlib                   | 82.9 ms                                                         | 36.0 ms: 2.30x faster                                                            |
| pidigits                  | 201 ms                                                          | 141 ms: 1.42x faster                                                             |
| sqlite_synth              | 1.95 us                                                         | 1.67 us: 1.17x faster                                                            |
| json                      | 4.27 ms                                                         | 4.20 ms: 1.02x faster                                                            |
| bench_mp_pool             | 90.6 ms                                                         | 89.5 ms: 1.01x faster                                                            |
| python_startup            | 28.3 ms                                                         | 28.0 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 479 ms: 1.01x faster                                                             |
| regex_effbot              | 1.80 ms                                                         | 1.81 ms: 1.01x slower                                                            |
| gc_traversal              | 1.75 ms                                                         | 1.77 ms: 1.01x slower                                                            |
| python_startup_no_site    | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                            |
| xml_etree_parse           | 107 ms                                                          | 112 ms: 1.04x slower                                                             |
| json_loads                | 21.6 us                                                         | 22.7 us: 1.05x slower                                                            |
| deepcopy                  | 314 us                                                          | 332 us: 1.06x slower                                                             |
| create_gc_cycles          | 1.06 ms                                                         | 1.13 ms: 1.07x slower                                                            |
| async_tree_io             | 526 ms                                                          | 577 ms: 1.10x slower                                                             |
| async_tree_memoization_tg | 282 ms                                                          | 311 ms: 1.10x slower                                                             |
| async_tree_io_tg          | 494 ms                                                          | 549 ms: 1.11x slower                                                             |
| async_tree_none           | 245 ms                                                          | 274 ms: 1.12x slower                                                             |
| async_tree_memoization    | 297 ms                                                          | 334 ms: 1.12x slower                                                             |
| telco                     | 6.96 ms                                                         | 7.92 ms: 1.14x slower                                                            |
| async_tree_none_tg        | 214 ms                                                          | 246 ms: 1.15x slower                                                             |
| dulwich_log               | 48.8 ms                                                         | 56.8 ms: 1.17x slower                                                            |
| deepcopy_reduce           | 2.92 us                                                         | 3.44 us: 1.18x slower                                                            |
| bench_thread_pool         | 1.00 ms                                                         | 1.22 ms: 1.22x slower                                                            |
| pylint                    | 227 ms                                                          | 280 ms: 1.24x slower                                                             |
| json_dumps                | 7.30 ms                                                         | 9.48 ms: 1.30x slower                                                            |
| sympy_expand              | 373 ms                                                          | 490 ms: 1.31x slower                                                             |
| genshi_xml                | 50.1 ms                                                         | 66.0 ms: 1.32x slower                                                            |
| logging_format            | 8.72 us                                                         | 11.7 us: 1.34x slower                                                            |
| 2to3                      | 250 ms                                                          | 336 ms: 1.34x slower                                                             |
| html5lib                  | 47.5 ms                                                         | 63.9 ms: 1.34x slower                                                            |
| sympy_sum                 | 106 ms                                                          | 144 ms: 1.36x slower                                                             |
| mdp                       | 1.62 sec                                                        | 2.24 sec: 1.38x slower                                                           |
| sympy_str                 | 212 ms                                                          | 292 ms: 1.38x slower                                                             |
| logging_simple            | 7.99 us                                                         | 11.0 us: 1.38x slower                                                            |
| sympy_integrate           | 15.0 ms                                                         | 21.0 ms: 1.40x slower                                                            |
| typing_runtime_protocols  | 138 us                                                          | 198 us: 1.44x slower                                                             |
| many_optionals            | 436 us                                                          | 641 us: 1.47x slower                                                             |
| xml_etree_iterparse       | 62.6 ms                                                         | 93.0 ms: 1.49x slower                                                            |
| async_generators          | 270 ms                                                          | 410 ms: 1.52x slower                                                             |
| django_template           | 29.8 ms                                                         | 45.4 ms: 1.53x slower                                                            |
| genshi_text               | 21.5 ms                                                         | 33.2 ms: 1.55x slower                                                            |
| regex_compile             | 101 ms                                                          | 160 ms: 1.59x slower                                                             |
| meteor_contest            | 74.6 ms                                                         | 120 ms: 1.60x slower                                                             |
| deepcopy_memo             | 25.4 us                                                         | 43.3 us: 1.70x slower                                                            |
| xml_etree_generate        | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| go                        | 109 ms                                                          | 190 ms: 1.75x slower                                                             |
| nqueens                   | 72.1 ms                                                         | 126 ms: 1.75x slower                                                             |
| sphinx                    | 719 ms                                                          | 1.28 sec: 1.78x slower                                                           |
| xml_etree_process         | 44.2 ms                                                         | 79.0 ms: 1.79x slower                                                            |
| float                     | 54.6 ms                                                         | 97.9 ms: 1.79x slower                                                            |
| subparsers                | 14.8 ms                                                         | 27.6 ms: 1.87x slower                                                            |
| chaos                     | 50.2 ms                                                         | 95.7 ms: 1.91x slower                                                            |
| generators                | 21.8 ms                                                         | 41.5 ms: 1.91x slower                                                            |
| pycparser                 | 872 ms                                                          | 1.68 sec: 1.93x slower                                                           |
| pyflate                   | 320 ms                                                          | 619 ms: 1.93x slower                                                             |
| pickle_pure_python        | 231 us                                                          | 448 us: 1.94x slower                                                             |
| fannkuch                  | 299 ms                                                          | 580 ms: 1.94x slower                                                             |
| scimark_fft               | 205 ms                                                          | 411 ms: 2.01x slower                                                             |
| coroutines                | 16.2 ms                                                         | 32.8 ms: 2.02x slower                                                            |
| raytrace                  | 201 ms                                                          | 408 ms: 2.03x slower                                                             |
| comprehensions            | 12.5 us                                                         | 25.6 us: 2.04x slower                                                            |
| crypto_pyaes              | 56.9 ms                                                         | 118 ms: 2.07x slower                                                             |
| richards                  | 32.7 ms                                                         | 69.4 ms: 2.12x slower                                                            |
| richards_super            | 36.7 ms                                                         | 78.5 ms: 2.14x slower                                                            |
| scimark_sor               | 85.9 ms                                                         | 187 ms: 2.18x slower                                                             |
| k_core                    | 1.38 sec                                                        | 3.02 sec: 2.20x slower                                                           |
| pprint_safe_repr          | 648 ms                                                          | 1.43 sec: 2.20x slower                                                           |
| nbody                     | 80.0 ms                                                         | 177 ms: 2.21x slower                                                             |
| unpickle_pure_python      | 160 us                                                          | 358 us: 2.23x slower                                                             |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 6.37 ms: 2.24x slower                                                            |
| scimark_monte_carlo       | 47.7 ms                                                         | 107 ms: 2.25x slower                                                             |
| mako                      | 7.09 ms                                                         | 16.5 ms: 2.33x slower                                                            |
| docutils                  | 1.78 sec                                                        | 4.15 sec: 2.33x slower                                                           |
| hexiom                    | 4.44 ms                                                         | 10.6 ms: 2.38x slower                                                            |
| spectral_norm             | 69.4 ms                                                         | 166 ms: 2.39x slower                                                             |
| bpe_tokeniser             | 3.46 sec                                                        | 8.31 sec: 2.40x slower                                                           |
| deltablue                 | 2.33 ms                                                         | 5.92 ms: 2.54x slower                                                            |
| shortest_path             | 290 ms                                                          | 736 ms: 2.54x slower                                                             |
| connected_components      | 267 ms                                                          | 693 ms: 2.60x slower                                                             |
| scimark_lu                | 60.2 ms                                                         | 163 ms: 2.71x slower                                                             |
| tomli_loads               | 1.71 sec                                                        | 5.01 sec: 2.92x slower                                                           |
| pprint_pformat            | 1.33 sec                                                        | 4.07 sec: 3.06x slower                                                           |
| logging_silent            | 60.3 ns                                                         | 589 ns: 9.76x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.46x slower                                                                     |

Benchmark hidden because not significant (3): regex_dna, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.299x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown