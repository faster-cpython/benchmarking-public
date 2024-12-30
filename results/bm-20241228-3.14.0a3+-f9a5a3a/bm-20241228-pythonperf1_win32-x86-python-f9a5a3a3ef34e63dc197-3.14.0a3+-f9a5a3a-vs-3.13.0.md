# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.048x faster
- HPT reliability: 67.46%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 245 ms: 1.02x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.78 sec: 1.00x slower                                                          |
| html5lib       | 47.5 ms                                                         | 44.0 ms: 1.08x faster                                                           |
| sphinx         | 719 ms                                                          | 726 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 229 ms: 1.23x faster                                                            |
| async_tree_none            | 245 ms                                                          | 202 ms: 1.21x faster                                                            |
| async_tree_io              | 526 ms                                                          | 442 ms: 1.19x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 250 ms: 1.19x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 183 ms: 1.17x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 427 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| async_generators           | 270 ms                                                          | 298 ms: 1.10x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 197 ms: 1.02x faster                                                            |
| nbody          | 80.0 ms                                                         | 86.5 ms: 1.08x slower                                                           |
| float          | 54.6 ms                                                         | 59.1 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.4 ms: 1.09x faster                                                           |
| regex_compile  | 101 ms                                                          | 101 ms: 1.00x slower                                                            |
| regex_dna      | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.60 sec: 1.07x faster                                                          |
| json_loads           | 21.6 us                                                         | 20.6 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.3 ms: 1.04x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 169 us: 1.05x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 66.5 ms: 1.08x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 48.5 ms: 1.10x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 262 us: 1.13x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.64 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 46.4 ms: 1.08x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 20.4 ms: 1.05x faster                                                           |
| mako            | 7.09 ms                                                         | 7.53 ms: 1.06x slower                                                           |
| django_template | 29.8 ms                                                         | 32.2 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 722 us: 13.82x faster                                                           |
| coverage                   | 324 ms                                                          | 51.2 ms: 6.33x faster                                                           |
| deepcopy                   | 314 us                                                          | 231 us: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 229 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.39 us: 1.22x faster                                                           |
| async_tree_none            | 245 ms                                                          | 202 ms: 1.21x faster                                                            |
| async_tree_io              | 526 ms                                                          | 442 ms: 1.19x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 250 ms: 1.19x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 183 ms: 1.17x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 427 ms: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 22.1 us: 1.15x faster                                                           |
| go                         | 109 ms                                                          | 95.8 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.09x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.4 ms: 1.09x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 44.0 ms: 1.08x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 46.4 ms: 1.08x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.47 ms: 1.08x faster                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.60 sec: 1.07x faster                                                          |
| connected_components       | 267 ms                                                          | 253 ms: 1.05x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 20.4 ms: 1.05x faster                                                           |
| pycparser                  | 872 ms                                                          | 828 ms: 1.05x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.6 us: 1.05x faster                                                           |
| pylint                     | 227 ms                                                          | 216 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 624 ms: 1.04x faster                                                            |
| logging_simple             | 7.99 us                                                         | 7.69 us: 1.04x faster                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 87.3 ms: 1.04x faster                                                           |
| logging_format             | 8.72 us                                                         | 8.44 us: 1.03x faster                                                           |
| shortest_path              | 290 ms                                                          | 281 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.29 sec: 1.03x faster                                                          |
| 2to3                       | 250 ms                                                          | 245 ms: 1.02x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| fannkuch                   | 299 ms                                                          | 293 ms: 1.02x faster                                                            |
| pidigits                   | 201 ms                                                          | 197 ms: 1.02x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.35 sec: 1.02x faster                                                          |
| json                       | 4.27 ms                                                         | 4.21 ms: 1.01x faster                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 105 ms: 1.00x faster                                                            |
| sympy_expand               | 373 ms                                                          | 372 ms: 1.00x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.78 sec: 1.00x slower                                                          |
| regex_compile              | 101 ms                                                          | 101 ms: 1.00x slower                                                            |
| regex_dna                  | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 69.9 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 41.8 ms: 1.01x slower                                                           |
| sphinx                     | 719 ms                                                          | 726 ms: 1.01x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 15.2 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 139 us: 1.01x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 73.1 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.26 ms: 1.02x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.65 sec: 1.02x slower                                                          |
| sqlglot_normalize          | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.79 ms: 1.02x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 49.8 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.55 sec: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.92 ms: 1.03x slower                                                           |
| pyflate                    | 320 ms                                                          | 334 ms: 1.04x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.3 ms: 1.04x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 59.9 ms: 1.05x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 169 us: 1.05x slower                                                            |
| scimark_fft                | 205 ms                                                          | 217 ms: 1.06x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.53 ms: 1.06x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 79.9 ms: 1.07x slower                                                           |
| richards                   | 32.7 ms                                                         | 35.2 ms: 1.08x slower                                                           |
| chaos                      | 50.2 ms                                                         | 54.2 ms: 1.08x slower                                                           |
| django_template            | 29.8 ms                                                         | 32.2 ms: 1.08x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.5 ms: 1.08x slower                                                           |
| nbody                      | 80.0 ms                                                         | 86.5 ms: 1.08x slower                                                           |
| float                      | 54.6 ms                                                         | 59.1 ms: 1.08x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 66.5 ms: 1.08x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.6 us: 1.09x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 4.87 ms: 1.10x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 48.5 ms: 1.10x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.56 ms: 1.10x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 94.6 ms: 1.10x slower                                                           |
| richards_super             | 36.7 ms                                                         | 40.4 ms: 1.10x slower                                                           |
| async_generators           | 270 ms                                                          | 298 ms: 1.10x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 262 us: 1.13x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 68.4 ms: 1.14x slower                                                           |
| generators                 | 21.8 ms                                                         | 25.0 ms: 1.15x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 70.2 ns: 1.16x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.64 ms: 1.18x slower                                                           |
| many_optionals             | 436 us                                                          | 532 us: 1.22x slower                                                            |
| raytrace                   | 201 ms                                                          | 247 ms: 1.23x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 20.3 ms: 1.37x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (6): create_gc_cycles, coroutines, sympy_str, xml_etree_parse, pathlib, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 67.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown