# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.101x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 276 ms: 1.10x slower                                                           |
| docutils       | 1.78 sec                                                        | 3.19 sec: 1.80x slower                                                         |
| html5lib       | 47.5 ms                                                         | 52.8 ms: 1.11x slower                                                          |
| sphinx         | 719 ms                                                          | 979 ms: 1.36x slower                                                           |
| Geometric mean | (ref)                                                           | 1.32x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets        | 363 ms                                                          | 167 ms: 2.18x faster                                                           |
| async_tree_io             | 526 ms                                                          | 428 ms: 1.23x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 230 ms: 1.23x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 405 ms: 1.22x faster                                                           |
| async_tree_none           | 245 ms                                                          | 207 ms: 1.18x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 254 ms: 1.17x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 184 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 477 ms: 1.01x faster                                                           |
| async_generators          | 270 ms                                                          | 321 ms: 1.19x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.17x faster                                                                   |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 190 ms: 1.06x faster                                                           |
| float          | 54.6 ms                                                         | 59.3 ms: 1.09x slower                                                          |
| nbody          | 80.0 ms                                                         | 114 ms: 1.43x slower                                                           |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                          |
| regex_effbot   | 1.80 ms                                                         | 1.76 ms: 1.02x faster                                                          |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                           |
| regex_compile  | 101 ms                                                          | 123 ms: 1.22x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 111 ms: 1.04x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 69.7 ms: 1.11x slower                                                          |
| json_loads           | 21.6 us                                                         | 25.7 us: 1.19x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 77.9 ms: 1.27x slower                                                          |
| xml_etree_process    | 44.2 ms                                                         | 56.5 ms: 1.28x slower                                                          |
| unpickle_pure_python | 160 us                                                          | 206 us: 1.29x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.42 ms: 1.29x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 318 us: 1.38x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 3.32 sec: 1.94x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.29x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.4 ms: 1.04x slower                                                          |
| python_startup_no_site | 19.7 ms                                                         | 21.9 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 59.9 ms: 1.19x slower                                                          |
| django_template | 29.8 ms                                                         | 38.2 ms: 1.28x slower                                                          |
| genshi_text     | 21.5 ms                                                         | 28.7 ms: 1.33x slower                                                          |
| mako            | 7.09 ms                                                         | 12.0 ms: 1.69x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.36x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 827 us: 12.06x faster                                                          |
| coverage                  | 324 ms                                                          | 76.7 ms: 4.23x faster                                                          |
| pathlib                   | 82.9 ms                                                         | 37.4 ms: 2.21x faster                                                          |
| asyncio_websockets        | 363 ms                                                          | 167 ms: 2.18x faster                                                           |
| gc_traversal              | 1.75 ms                                                         | 1.12 ms: 1.56x faster                                                          |
| regex_v8                  | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                          |
| async_tree_io             | 526 ms                                                          | 428 ms: 1.23x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 230 ms: 1.23x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 405 ms: 1.22x faster                                                           |
| async_tree_none           | 245 ms                                                          | 207 ms: 1.18x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 254 ms: 1.17x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 184 ms: 1.17x faster                                                           |
| sqlite_synth              | 1.95 us                                                         | 1.68 us: 1.16x faster                                                          |
| deepcopy                  | 314 us                                                          | 273 us: 1.15x faster                                                           |
| mdp                       | 1.62 sec                                                        | 1.51 sec: 1.08x faster                                                         |
| pidigits                  | 201 ms                                                          | 190 ms: 1.06x faster                                                           |
| bench_mp_pool             | 90.6 ms                                                         | 86.6 ms: 1.05x faster                                                          |
| regex_effbot              | 1.80 ms                                                         | 1.76 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 477 ms: 1.01x faster                                                           |
| deepcopy_memo             | 25.4 us                                                         | 25.7 us: 1.01x slower                                                          |
| deepcopy_reduce           | 2.92 us                                                         | 2.95 us: 1.01x slower                                                          |
| telco                     | 6.96 ms                                                         | 7.13 ms: 1.02x slower                                                          |
| xml_etree_parse           | 107 ms                                                          | 111 ms: 1.04x slower                                                           |
| python_startup            | 28.3 ms                                                         | 29.4 ms: 1.04x slower                                                          |
| regex_dna                 | 114 ms                                                          | 120 ms: 1.06x slower                                                           |
| float                     | 54.6 ms                                                         | 59.3 ms: 1.09x slower                                                          |
| dulwich_log               | 48.8 ms                                                         | 53.5 ms: 1.10x slower                                                          |
| 2to3                      | 250 ms                                                          | 276 ms: 1.10x slower                                                           |
| html5lib                  | 47.5 ms                                                         | 52.8 ms: 1.11x slower                                                          |
| xml_etree_iterparse       | 62.6 ms                                                         | 69.7 ms: 1.11x slower                                                          |
| python_startup_no_site    | 19.7 ms                                                         | 21.9 ms: 1.12x slower                                                          |
| pylint                    | 227 ms                                                          | 254 ms: 1.12x slower                                                           |
| go                        | 109 ms                                                          | 122 ms: 1.12x slower                                                           |
| json                      | 4.27 ms                                                         | 4.82 ms: 1.13x slower                                                          |
| sympy_expand              | 373 ms                                                          | 423 ms: 1.13x slower                                                           |
| sympy_str                 | 212 ms                                                          | 244 ms: 1.15x slower                                                           |
| sympy_integrate           | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                          |
| sympy_sum                 | 106 ms                                                          | 122 ms: 1.16x slower                                                           |
| logging_format            | 8.72 us                                                         | 10.2 us: 1.17x slower                                                          |
| json_loads                | 21.6 us                                                         | 25.7 us: 1.19x slower                                                          |
| async_generators          | 270 ms                                                          | 321 ms: 1.19x slower                                                           |
| genshi_xml                | 50.1 ms                                                         | 59.9 ms: 1.19x slower                                                          |
| logging_simple            | 7.99 us                                                         | 9.58 us: 1.20x slower                                                          |
| chaos                     | 50.2 ms                                                         | 60.6 ms: 1.21x slower                                                          |
| spectral_norm             | 69.4 ms                                                         | 83.8 ms: 1.21x slower                                                          |
| regex_compile             | 101 ms                                                          | 123 ms: 1.22x slower                                                           |
| pprint_safe_repr          | 648 ms                                                          | 794 ms: 1.22x slower                                                           |
| xml_etree_generate        | 61.4 ms                                                         | 77.9 ms: 1.27x slower                                                          |
| pyflate                   | 320 ms                                                          | 407 ms: 1.27x slower                                                           |
| scimark_monte_carlo       | 47.7 ms                                                         | 60.8 ms: 1.27x slower                                                          |
| deltablue                 | 2.33 ms                                                         | 2.98 ms: 1.28x slower                                                          |
| xml_etree_process         | 44.2 ms                                                         | 56.5 ms: 1.28x slower                                                          |
| django_template           | 29.8 ms                                                         | 38.2 ms: 1.28x slower                                                          |
| bench_thread_pool         | 1.00 ms                                                         | 1.28 ms: 1.28x slower                                                          |
| scimark_sor               | 85.9 ms                                                         | 110 ms: 1.28x slower                                                           |
| unpickle_pure_python      | 160 us                                                          | 206 us: 1.29x slower                                                           |
| typing_runtime_protocols  | 138 us                                                          | 177 us: 1.29x slower                                                           |
| json_dumps                | 7.30 ms                                                         | 9.42 ms: 1.29x slower                                                          |
| meteor_contest            | 74.6 ms                                                         | 96.4 ms: 1.29x slower                                                          |
| fannkuch                  | 299 ms                                                          | 387 ms: 1.29x slower                                                           |
| crypto_pyaes              | 56.9 ms                                                         | 74.1 ms: 1.30x slower                                                          |
| generators                | 21.8 ms                                                         | 28.5 ms: 1.31x slower                                                          |
| scimark_fft               | 205 ms                                                          | 269 ms: 1.31x slower                                                           |
| nqueens                   | 72.1 ms                                                         | 95.4 ms: 1.32x slower                                                          |
| pycparser                 | 872 ms                                                          | 1.16 sec: 1.33x slower                                                         |
| genshi_text               | 21.5 ms                                                         | 28.7 ms: 1.33x slower                                                          |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 3.79 ms: 1.33x slower                                                          |
| hexiom                    | 4.44 ms                                                         | 6.01 ms: 1.35x slower                                                          |
| comprehensions            | 12.5 us                                                         | 17.0 us: 1.36x slower                                                          |
| sphinx                    | 719 ms                                                          | 979 ms: 1.36x slower                                                           |
| richards                  | 32.7 ms                                                         | 44.7 ms: 1.37x slower                                                          |
| pickle_pure_python        | 231 us                                                          | 318 us: 1.38x slower                                                           |
| scimark_lu                | 60.2 ms                                                         | 83.5 ms: 1.39x slower                                                          |
| richards_super            | 36.7 ms                                                         | 50.9 ms: 1.39x slower                                                          |
| raytrace                  | 201 ms                                                          | 281 ms: 1.39x slower                                                           |
| many_optionals            | 436 us                                                          | 615 us: 1.41x slower                                                           |
| nbody                     | 80.0 ms                                                         | 114 ms: 1.43x slower                                                           |
| subparsers                | 14.8 ms                                                         | 24.7 ms: 1.67x slower                                                          |
| mako                      | 7.09 ms                                                         | 12.0 ms: 1.69x slower                                                          |
| pprint_pformat            | 1.33 sec                                                        | 2.30 sec: 1.73x slower                                                         |
| bpe_tokeniser             | 3.46 sec                                                        | 6.08 sec: 1.76x slower                                                         |
| docutils                  | 1.78 sec                                                        | 3.19 sec: 1.80x slower                                                         |
| k_core                    | 1.38 sec                                                        | 2.48 sec: 1.80x slower                                                         |
| tomli_loads               | 1.71 sec                                                        | 3.32 sec: 1.94x slower                                                         |
| shortest_path             | 290 ms                                                          | 617 ms: 2.13x slower                                                           |
| connected_components      | 267 ms                                                          | 585 ms: 2.20x slower                                                           |
| logging_silent            | 60.3 ns                                                         | 425 ns: 7.05x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.14x slower                                                                   |

Benchmark hidden because not significant (3): coroutines, async_tree_cpu_io_mixed_tg, create_gc_cycles
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.101x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown