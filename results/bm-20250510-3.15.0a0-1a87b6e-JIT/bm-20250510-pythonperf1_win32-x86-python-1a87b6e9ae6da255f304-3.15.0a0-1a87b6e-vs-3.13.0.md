# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.036x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 285 ms: 1.14x slower                                                           |
| docutils       | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                         |
| html5lib       | 47.5 ms                                                         | 46.5 ms: 1.02x faster                                                          |
| sphinx         | 719 ms                                                          | 781 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets        | 363 ms                                                          | 202 ms: 1.79x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 244 ms: 1.16x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 258 ms: 1.15x faster                                                           |
| async_tree_none           | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_io             | 526 ms                                                          | 469 ms: 1.12x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 202 ms: 1.06x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 467 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 470 ms: 1.03x faster                                                           |
| coroutines                | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                          |
| async_generators          | 270 ms                                                          | 324 ms: 1.20x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 204 ms: 1.02x slower                                                           |
| float          | 54.6 ms                                                         | 56.9 ms: 1.04x slower                                                          |
| nbody          | 80.0 ms                                                         | 119 ms: 1.49x slower                                                           |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 14.9 ms: 1.13x faster                                                          |
| regex_effbot   | 1.80 ms                                                         | 1.73 ms: 1.04x faster                                                          |
| regex_dna      | 114 ms                                                          | 122 ms: 1.07x slower                                                           |
| regex_compile  | 101 ms                                                          | 111 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.4 us: 1.03x slower                                                          |
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.05x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.81 sec: 1.05x slower                                                         |
| xml_etree_iterparse  | 62.6 ms                                                         | 69.6 ms: 1.11x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.36 ms: 1.15x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 74.3 ms: 1.21x slower                                                          |
| xml_etree_process    | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 321 us: 1.39x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 241 us: 1.51x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.9 ms: 1.02x slower                                                          |
| python_startup_no_site | 19.7 ms                                                         | 22.2 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 23.2 ms: 1.08x slower                                                          |
| django_template | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                          |
| mako            | 7.09 ms                                                         | 8.30 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 741 us: 13.46x faster                                                          |
| coverage                  | 324 ms                                                          | 56.7 ms: 5.71x faster                                                          |
| pathlib                   | 82.9 ms                                                         | 37.2 ms: 2.23x faster                                                          |
| asyncio_websockets        | 363 ms                                                          | 202 ms: 1.79x faster                                                           |
| mdp                       | 1.62 sec                                                        | 1.07 sec: 1.52x faster                                                         |
| deepcopy                  | 314 us                                                          | 254 us: 1.24x faster                                                           |
| async_tree_memoization_tg | 282 ms                                                          | 244 ms: 1.16x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 258 ms: 1.15x faster                                                           |
| async_tree_none           | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| deepcopy_memo             | 25.4 us                                                         | 22.6 us: 1.13x faster                                                          |
| regex_v8                  | 16.8 ms                                                         | 14.9 ms: 1.13x faster                                                          |
| deepcopy_reduce           | 2.92 us                                                         | 2.59 us: 1.12x faster                                                          |
| async_tree_io             | 526 ms                                                          | 469 ms: 1.12x faster                                                           |
| async_tree_none_tg        | 214 ms                                                          | 202 ms: 1.06x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 467 ms: 1.06x faster                                                           |
| regex_effbot              | 1.80 ms                                                         | 1.73 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 470 ms: 1.03x faster                                                           |
| html5lib                  | 47.5 ms                                                         | 46.5 ms: 1.02x faster                                                          |
| pidigits                  | 201 ms                                                          | 204 ms: 1.02x slower                                                           |
| go                        | 109 ms                                                          | 111 ms: 1.02x slower                                                           |
| python_startup            | 28.3 ms                                                         | 28.9 ms: 1.02x slower                                                          |
| pylint                    | 227 ms                                                          | 234 ms: 1.03x slower                                                           |
| json_loads                | 21.6 us                                                         | 22.4 us: 1.03x slower                                                          |
| float                     | 54.6 ms                                                         | 56.9 ms: 1.04x slower                                                          |
| telco                     | 6.96 ms                                                         | 7.28 ms: 1.05x slower                                                          |
| xml_etree_parse           | 107 ms                                                          | 112 ms: 1.05x slower                                                           |
| sympy_sum                 | 106 ms                                                          | 111 ms: 1.05x slower                                                           |
| json                      | 4.27 ms                                                         | 4.50 ms: 1.05x slower                                                          |
| tomli_loads               | 1.71 sec                                                        | 1.81 sec: 1.05x slower                                                         |
| sympy_str                 | 212 ms                                                          | 224 ms: 1.06x slower                                                           |
| dulwich_log               | 48.8 ms                                                         | 51.7 ms: 1.06x slower                                                          |
| sympy_expand              | 373 ms                                                          | 396 ms: 1.06x slower                                                           |
| sympy_integrate           | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                          |
| k_core                    | 1.38 sec                                                        | 1.47 sec: 1.07x slower                                                         |
| create_gc_cycles          | 1.06 ms                                                         | 1.13 ms: 1.07x slower                                                          |
| regex_dna                 | 114 ms                                                          | 122 ms: 1.07x slower                                                           |
| genshi_text               | 21.5 ms                                                         | 23.2 ms: 1.08x slower                                                          |
| sphinx                    | 719 ms                                                          | 781 ms: 1.09x slower                                                           |
| regex_compile             | 101 ms                                                          | 111 ms: 1.10x slower                                                           |
| pyflate                   | 320 ms                                                          | 353 ms: 1.10x slower                                                           |
| docutils                  | 1.78 sec                                                        | 1.97 sec: 1.11x slower                                                         |
| gc_traversal              | 1.75 ms                                                         | 1.94 ms: 1.11x slower                                                          |
| logging_format            | 8.72 us                                                         | 9.67 us: 1.11x slower                                                          |
| xml_etree_iterparse       | 62.6 ms                                                         | 69.6 ms: 1.11x slower                                                          |
| pycparser                 | 872 ms                                                          | 971 ms: 1.11x slower                                                           |
| django_template           | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                          |
| coroutines                | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                          |
| chaos                     | 50.2 ms                                                         | 56.2 ms: 1.12x slower                                                          |
| logging_simple            | 7.99 us                                                         | 9.00 us: 1.13x slower                                                          |
| python_startup_no_site    | 19.7 ms                                                         | 22.2 ms: 1.13x slower                                                          |
| 2to3                      | 250 ms                                                          | 285 ms: 1.14x slower                                                           |
| json_dumps                | 7.30 ms                                                         | 8.36 ms: 1.15x slower                                                          |
| bench_mp_pool             | 90.6 ms                                                         | 104 ms: 1.15x slower                                                           |
| shortest_path             | 290 ms                                                          | 333 ms: 1.15x slower                                                           |
| bpe_tokeniser             | 3.46 sec                                                        | 3.98 sec: 1.15x slower                                                         |
| scimark_monte_carlo       | 47.7 ms                                                         | 55.0 ms: 1.15x slower                                                          |
| spectral_norm             | 69.4 ms                                                         | 80.9 ms: 1.17x slower                                                          |
| mako                      | 7.09 ms                                                         | 8.30 ms: 1.17x slower                                                          |
| connected_components      | 267 ms                                                          | 312 ms: 1.17x slower                                                           |
| async_generators          | 270 ms                                                          | 324 ms: 1.20x slower                                                           |
| xml_etree_generate        | 61.4 ms                                                         | 74.3 ms: 1.21x slower                                                          |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 3.44 ms: 1.21x slower                                                          |
| raytrace                  | 201 ms                                                          | 246 ms: 1.22x slower                                                           |
| scimark_sor               | 85.9 ms                                                         | 105 ms: 1.22x slower                                                           |
| pprint_pformat            | 1.33 sec                                                        | 1.63 sec: 1.23x slower                                                         |
| richards                  | 32.7 ms                                                         | 40.1 ms: 1.23x slower                                                          |
| pprint_safe_repr          | 648 ms                                                          | 799 ms: 1.23x slower                                                           |
| deltablue                 | 2.33 ms                                                         | 2.90 ms: 1.25x slower                                                          |
| richards_super            | 36.7 ms                                                         | 46.0 ms: 1.25x slower                                                          |
| xml_etree_process         | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                                          |
| meteor_contest            | 74.6 ms                                                         | 94.5 ms: 1.27x slower                                                          |
| nqueens                   | 72.1 ms                                                         | 91.7 ms: 1.27x slower                                                          |
| typing_runtime_protocols  | 138 us                                                          | 177 us: 1.29x slower                                                           |
| scimark_lu                | 60.2 ms                                                         | 78.7 ms: 1.31x slower                                                          |
| scimark_fft               | 205 ms                                                          | 268 ms: 1.31x slower                                                           |
| many_optionals            | 436 us                                                          | 572 us: 1.31x slower                                                           |
| hexiom                    | 4.44 ms                                                         | 5.86 ms: 1.32x slower                                                          |
| generators                | 21.8 ms                                                         | 28.8 ms: 1.32x slower                                                          |
| fannkuch                  | 299 ms                                                          | 400 ms: 1.34x slower                                                           |
| bench_thread_pool         | 1.00 ms                                                         | 1.34 ms: 1.34x slower                                                          |
| pickle_pure_python        | 231 us                                                          | 321 us: 1.39x slower                                                           |
| crypto_pyaes              | 56.9 ms                                                         | 81.2 ms: 1.43x slower                                                          |
| comprehensions            | 12.5 us                                                         | 18.1 us: 1.45x slower                                                          |
| nbody                     | 80.0 ms                                                         | 119 ms: 1.49x slower                                                           |
| unpickle_pure_python      | 160 us                                                          | 241 us: 1.51x slower                                                           |
| subparsers                | 14.8 ms                                                         | 23.0 ms: 1.55x slower                                                          |
| logging_silent            | 60.3 ns                                                         | 375 ns: 6.22x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, sqlite_synth, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown