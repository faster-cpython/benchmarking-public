# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-x86
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.96 sec: 1.10x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 794 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 256 ms: 1.10x faster                                                            |
| async_tree_io              | 526 ms                                                          | 495 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 468 ms: 1.06x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 206 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 237 ms: 1.03x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 289 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.00x slower                                                            |
| async_generators           | 270 ms                                                          | 336 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 196 ms: 1.02x faster                                                            |
| float          | 54.6 ms                                                         | 55.5 ms: 1.02x slower                                                           |
| nbody          | 80.0 ms                                                         | 98.7 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| regex_dna      | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| regex_compile  | 101 ms                                                          | 113 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.2 us: 1.07x faster                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.76 sec: 1.03x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 72.9 ms: 1.19x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 54.3 ms: 1.23x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.07 ms: 1.24x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 204 us: 1.28x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 298 us: 1.29x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 19.5 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.40 ms: 1.04x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 55.9 ms: 1.11x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 26.5 ms: 1.23x slower                                                           |
| django_template | 29.8 ms                                                         | 38.2 ms: 1.28x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 792 us: 12.60x faster                                                           |
| coverage                   | 324 ms                                                          | 52.2 ms: 6.20x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 107 ms: 2.01x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| deepcopy                   | 314 us                                                          | 275 us: 1.14x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 256 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.9 ms: 1.09x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| json_loads                 | 21.6 us                                                         | 20.2 us: 1.07x faster                                                           |
| async_tree_io              | 526 ms                                                          | 495 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 468 ms: 1.06x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 24.2 us: 1.05x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 206 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 87.3 ms: 1.04x faster                                                           |
| async_tree_none            | 245 ms                                                          | 237 ms: 1.03x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.84 us: 1.03x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 289 ms: 1.03x faster                                                            |
| pidigits                   | 201 ms                                                          | 196 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.5 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.00x slower                                                            |
| regex_dna                  | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| pathlib                    | 82.9 ms                                                         | 83.7 ms: 1.01x slower                                                           |
| float                      | 54.6 ms                                                         | 55.5 ms: 1.02x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.03x slower                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.76 sec: 1.03x slower                                                          |
| html5lib                   | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.40 ms: 1.04x slower                                                           |
| pylint                     | 227 ms                                                          | 237 ms: 1.04x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.11 us: 1.04x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 51.2 ms: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.99 ms: 1.05x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.43 us: 1.06x slower                                                           |
| 2to3                       | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.06 ms: 1.06x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.44 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| connected_components       | 267 ms                                                          | 286 ms: 1.07x slower                                                            |
| pycparser                  | 872 ms                                                          | 945 ms: 1.08x slower                                                            |
| sympy_expand               | 373 ms                                                          | 406 ms: 1.09x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                            |
| shortest_path              | 290 ms                                                          | 316 ms: 1.09x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.96 sec: 1.10x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 76.4 ms: 1.10x slower                                                           |
| sphinx                     | 719 ms                                                          | 794 ms: 1.10x slower                                                            |
| fannkuch                   | 299 ms                                                          | 331 ms: 1.11x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 55.9 ms: 1.11x slower                                                           |
| sympy_str                  | 212 ms                                                          | 236 ms: 1.11x slower                                                            |
| go                         | 109 ms                                                          | 122 ms: 1.12x slower                                                            |
| regex_compile              | 101 ms                                                          | 113 ms: 1.12x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.89 sec: 1.12x slower                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.52 sec: 1.15x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 744 ms: 1.15x slower                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.15 ms: 1.15x slower                                                           |
| scimark_fft                | 205 ms                                                          | 236 ms: 1.15x slower                                                            |
| sqlglot_transpile          | 1.24 ms                                                         | 1.43 ms: 1.15x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.88 sec: 1.16x slower                                                          |
| sympy_integrate            | 15.0 ms                                                         | 17.5 ms: 1.17x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 72.9 ms: 1.19x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 102 ms: 1.19x slower                                                            |
| pyflate                    | 320 ms                                                          | 385 ms: 1.20x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 166 us: 1.21x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 90.5 ms: 1.21x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 73.7 ms: 1.22x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 54.3 ms: 1.23x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 26.5 ms: 1.23x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 51.1 ms: 1.23x slower                                                           |
| nbody                      | 80.0 ms                                                         | 98.7 ms: 1.23x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 70.5 ms: 1.24x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.07 ms: 1.24x slower                                                           |
| async_generators           | 270 ms                                                          | 336 ms: 1.24x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 204 us: 1.28x slower                                                            |
| django_template            | 29.8 ms                                                         | 38.2 ms: 1.28x slower                                                           |
| many_optionals             | 436 us                                                          | 560 us: 1.28x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 298 us: 1.29x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 61.7 ms: 1.29x slower                                                           |
| chaos                      | 50.2 ms                                                         | 65.0 ms: 1.29x slower                                                           |
| richards_super             | 36.7 ms                                                         | 49.5 ms: 1.35x slower                                                           |
| richards                   | 32.7 ms                                                         | 44.5 ms: 1.36x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.19 ms: 1.37x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 98.9 ms: 1.37x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 86.3 ns: 1.43x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.4 ms: 1.45x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.7 us: 1.49x slower                                                           |
| raytrace                   | 201 ms                                                          | 313 ms: 1.56x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.34 ms: 1.65x slower                                                           |
| generators                 | 21.8 ms                                                         | 36.9 ms: 1.70x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (5): json, sqlite_synth, xml_etree_parse, create_gc_cycles, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown