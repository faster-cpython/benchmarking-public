# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.8 ms: 1.22x faster                                                            |
| sphinx         | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 338 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.27x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 57.3 ms: 1.40x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 43.2 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.6 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.11 sec: 1.54x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads           | 21.6 us                                                         | 14.4 us: 1.50x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.3 ms: 1.23x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 51.0 ms: 1.20x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.18 ms: 1.18x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 203 us: 1.14x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.2 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.8 ms: 1.44x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| mako            | 7.09 ms                                                         | 5.42 ms: 1.31x faster                                                            |
| django_template | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 488 us: 20.45x faster                                                            |
| coverage                   | 324 ms                                                          | 49.7 ms: 6.52x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.2 ms: 2.74x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 796 ms: 2.04x faster                                                             |
| deepcopy                   | 314 us                                                          | 170 us: 1.85x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.29 ms: 1.62x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.58x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.11 sec: 1.54x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.4 us: 1.50x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 897 ms: 1.48x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 443 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 332 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.46x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.8 ms: 1.44x faster                                                            |
| json                       | 4.27 ms                                                         | 3.01 ms: 1.42x faster                                                            |
| go                         | 109 ms                                                          | 76.7 ms: 1.42x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.0 us: 1.41x faster                                                            |
| fannkuch                   | 299 ms                                                          | 213 ms: 1.40x faster                                                             |
| nbody                      | 80.0 ms                                                         | 57.3 ms: 1.40x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.37x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 338 ms: 1.35x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.58 sec: 1.34x faster                                                           |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.57 us: 1.33x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.42 ms: 1.31x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.14 us: 1.30x faster                                                            |
| regex_compile              | 101 ms                                                          | 78.6 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| pyflate                    | 320 ms                                                          | 251 ms: 1.28x faster                                                             |
| sympy_expand               | 373 ms                                                          | 293 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.27x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.23 ms: 1.27x faster                                                            |
| pycparser                  | 872 ms                                                          | 689 ms: 1.26x faster                                                             |
| float                      | 54.6 ms                                                         | 43.2 ms: 1.26x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 45.6 ms: 1.25x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.58 us: 1.24x faster                                                            |
| sympy_str                  | 212 ms                                                          | 171 ms: 1.24x faster                                                             |
| chaos                      | 50.2 ms                                                         | 40.6 ms: 1.24x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.3 ms: 1.23x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.8 ms: 1.22x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.8 ms: 1.22x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.8 ms: 1.22x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.3 ms: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.7 ms: 1.20x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 51.0 ms: 1.20x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.19x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.8 ms: 1.19x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 847 us: 1.18x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.18 ms: 1.18x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 61.1 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.5 ms: 1.15x faster                                                            |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 203 us: 1.14x faster                                                             |
| sphinx                     | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 54.1 ns: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 78.0 ms: 1.10x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 63.1 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.08 ms: 1.09x faster                                                            |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 69.1 ms: 1.08x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.65 sec: 1.08x faster                                                           |
| deltablue                  | 2.33 ms                                                         | 2.19 ms: 1.07x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.2 ms: 1.01x slower                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| many_optionals             | 436 us                                                          | 446 us: 1.02x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 94.5 ms: 1.04x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 63.8 ms: 1.06x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 17.2 ms: 1.16x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.61 sec: 1.17x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.21x slower                                                            |
| connected_components       | 267 ms                                                          | 321 ms: 1.21x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.29 ms: 1.22x slower                                                            |
| shortest_path              | 290 ms                                                          | 354 ms: 1.22x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown