# Results vs. 3.13.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.298x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 220 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.9 ms: 1.22x faster                                                            |
| sphinx         | 719 ms                                                          | 641 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 396 ms: 1.33x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 389 ms: 1.27x faster                                                             |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.2 ms: 1.07x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 52.7 ms: 1.52x faster                                                            |
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 44.7 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.3 ms: 1.27x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.60 ms: 1.12x faster                                                            |
| regex_dna      | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 107 us: 1.49x faster                                                             |
| json_loads           | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.5 ms: 1.24x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 88.4 ms: 1.21x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.25 ms: 1.17x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 203 us: 1.14x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.8 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.8 ms: 1.44x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.8 ms: 1.36x faster                                                            |
| mako            | 7.09 ms                                                         | 5.43 ms: 1.31x faster                                                            |
| django_template | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 497 us: 20.08x faster                                                            |
| coverage                   | 324 ms                                                          | 49.8 ms: 6.51x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 31.9 ms: 2.60x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| mdp                        | 1.62 sec                                                        | 804 ms: 2.02x faster                                                             |
| deepcopy                   | 314 us                                                          | 170 us: 1.85x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.19 ms: 1.66x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.59x faster                                                            |
| nbody                      | 80.0 ms                                                         | 52.7 ms: 1.52x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 107 us: 1.49x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 918 ms: 1.45x faster                                                             |
| json                       | 4.27 ms                                                         | 2.96 ms: 1.44x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 449 ms: 1.44x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.8 ms: 1.44x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 18.3 us: 1.39x faster                                                            |
| go                         | 109 ms                                                          | 78.4 ms: 1.39x faster                                                            |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| fannkuch                   | 299 ms                                                          | 219 ms: 1.36x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.8 ms: 1.36x faster                                                            |
| scimark_fft                | 205 ms                                                          | 151 ms: 1.36x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.36x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.60 sec: 1.33x faster                                                           |
| async_tree_io              | 526 ms                                                          | 396 ms: 1.33x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.61 us: 1.32x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.43 ms: 1.31x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.16 us: 1.30x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| regex_compile              | 101 ms                                                          | 79.3 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.23 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 389 ms: 1.27x faster                                                             |
| sympy_expand               | 373 ms                                                          | 294 ms: 1.27x faster                                                             |
| pyflate                    | 320 ms                                                          | 254 ms: 1.26x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| pycparser                  | 872 ms                                                          | 699 ms: 1.25x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.5 ms: 1.24x faster                                                            |
| sympy_str                  | 212 ms                                                          | 171 ms: 1.24x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 46.1 ms: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 58.9 ms: 1.22x faster                                                            |
| float                      | 54.6 ms                                                         | 44.7 ms: 1.22x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.9 ms: 1.22x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.3 ms: 1.22x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 88.4 ms: 1.21x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.9 ms: 1.21x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.4 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.9 ms: 1.19x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.6 ms: 1.19x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.6 us: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 850 us: 1.18x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.7 ms: 1.18x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.25 ms: 1.17x faster                                                            |
| richards_super             | 36.7 ms                                                         | 31.5 ms: 1.16x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.0 ms: 1.16x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 203 us: 1.14x faster                                                             |
| 2to3                       | 250 ms                                                          | 220 ms: 1.14x faster                                                             |
| pylint                     | 227 ms                                                          | 200 ms: 1.13x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.60 ms: 1.12x faster                                                            |
| sphinx                     | 719 ms                                                          | 641 ms: 1.12x faster                                                             |
| raytrace                   | 201 ms                                                          | 180 ms: 1.12x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.5 ms: 1.12x faster                                                            |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.09x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.9 ns: 1.08x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 79.9 ms: 1.08x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 15.2 ms: 1.07x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.16 ms: 1.07x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 70.9 ms: 1.05x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.26 ms: 1.03x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 68.3 ms: 1.02x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 61.0 ms: 1.01x slower                                                            |
| many_optionals             | 436 us                                                          | 445 us: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 118 ms: 1.04x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 95.3 ms: 1.05x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 17.0 ms: 1.15x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.62 sec: 1.18x slower                                                           |
| connected_components       | 267 ms                                                          | 316 ms: 1.19x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.12 ms: 1.21x slower                                                            |
| shortest_path              | 290 ms                                                          | 360 ms: 1.24x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.33 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): python_startup_no_site, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.298x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown