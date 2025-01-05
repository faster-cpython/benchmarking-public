# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.036x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 266 ms: 1.06x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.94 sec: 1.09x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.1 ms: 1.01x slower                                                           |
| sphinx         | 719 ms                                                          | 782 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 243 ms: 1.16x faster                                                            |
| async_tree_io              | 526 ms                                                          | 471 ms: 1.12x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 451 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 195 ms: 1.10x faster                                                            |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.09x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 275 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 350 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 471 ms: 1.03x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| async_generators           | 270 ms                                                          | 329 ms: 1.22x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 51.9 ms: 1.05x faster                                                           |
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| nbody          | 80.0 ms                                                         | 97.0 ms: 1.21x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                            |
| regex_compile  | 101 ms                                                          | 112 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.76 sec: 1.02x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.9 ms: 1.05x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 72.7 ms: 1.18x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.92 ms: 1.22x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 200 us: 1.25x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 291 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.45 ms: 1.05x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 54.7 ms: 1.09x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 25.0 ms: 1.16x slower                                                           |
| django_template | 29.8 ms                                                         | 36.8 ms: 1.23x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 757 us: 13.19x faster                                                           |
| coverage                   | 324 ms                                                          | 52.5 ms: 6.16x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 106 ms: 2.04x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 243 ms: 1.16x faster                                                            |
| deepcopy                   | 314 us                                                          | 271 us: 1.16x faster                                                            |
| async_tree_io              | 526 ms                                                          | 471 ms: 1.12x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 451 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 195 ms: 1.10x faster                                                            |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.09x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 23.5 us: 1.08x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 275 ms: 1.08x faster                                                            |
| float                      | 54.6 ms                                                         | 51.9 ms: 1.05x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.80 us: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 350 ms: 1.04x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 87.4 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 471 ms: 1.03x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| telco                      | 6.96 ms                                                         | 7.01 ms: 1.01x slower                                                           |
| html5lib                   | 47.5 ms                                                         | 48.1 ms: 1.01x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 16.6 ms: 1.02x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.76 sec: 1.02x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.42 sec: 1.03x slower                                                          |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                            |
| pylint                     | 227 ms                                                          | 234 ms: 1.03x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 50.6 ms: 1.04x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.05 ms: 1.04x slower                                                           |
| json                       | 4.27 ms                                                         | 4.46 ms: 1.04x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.10 us: 1.04x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.45 ms: 1.05x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.9 ms: 1.05x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 73.4 ms: 1.06x slower                                                           |
| 2to3                       | 250 ms                                                          | 266 ms: 1.06x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.50 us: 1.06x slower                                                           |
| pycparser                  | 872 ms                                                          | 931 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.04 ms: 1.07x slower                                                           |
| connected_components       | 267 ms                                                          | 287 ms: 1.08x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                            |
| sympy_expand               | 373 ms                                                          | 406 ms: 1.09x slower                                                            |
| sphinx                     | 719 ms                                                          | 782 ms: 1.09x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.94 sec: 1.09x slower                                                          |
| genshi_xml                 | 50.1 ms                                                         | 54.7 ms: 1.09x slower                                                           |
| shortest_path              | 290 ms                                                          | 317 ms: 1.09x slower                                                            |
| sympy_str                  | 212 ms                                                          | 234 ms: 1.11x slower                                                            |
| regex_compile              | 101 ms                                                          | 112 ms: 1.11x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 95.2 ms: 1.11x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.86 sec: 1.11x slower                                                          |
| go                         | 109 ms                                                          | 122 ms: 1.12x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.82 sec: 1.12x slower                                                          |
| sqlglot_parse              | 1.00 ms                                                         | 1.12 ms: 1.12x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 729 ms: 1.12x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.50 sec: 1.13x slower                                                          |
| sqlglot_transpile          | 1.24 ms                                                         | 1.39 ms: 1.13x slower                                                           |
| fannkuch                   | 299 ms                                                          | 337 ms: 1.13x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 17.3 ms: 1.15x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 25.0 ms: 1.16x slower                                                           |
| pyflate                    | 320 ms                                                          | 374 ms: 1.17x slower                                                            |
| scimark_fft                | 205 ms                                                          | 239 ms: 1.17x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 87.4 ms: 1.17x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 70.8 ms: 1.18x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 72.7 ms: 1.18x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 164 us: 1.19x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 53.3 ms: 1.21x slower                                                           |
| nbody                      | 80.0 ms                                                         | 97.0 ms: 1.21x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 50.4 ms: 1.22x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 69.3 ms: 1.22x slower                                                           |
| async_generators           | 270 ms                                                          | 329 ms: 1.22x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 8.92 ms: 1.22x slower                                                           |
| django_template            | 29.8 ms                                                         | 36.8 ms: 1.23x slower                                                           |
| richards                   | 32.7 ms                                                         | 40.8 ms: 1.25x slower                                                           |
| richards_super             | 36.7 ms                                                         | 45.8 ms: 1.25x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 200 us: 1.25x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 291 us: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 555 us: 1.27x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 61.2 ms: 1.28x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 78.5 ns: 1.30x slower                                                           |
| chaos                      | 50.2 ms                                                         | 66.4 ms: 1.32x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 97.3 ms: 1.35x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.17 ms: 1.36x slower                                                           |
| raytrace                   | 201 ms                                                          | 289 ms: 1.44x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 21.2 ms: 1.44x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.5 us: 1.48x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 7.02 ms: 1.58x slower                                                           |
| generators                 | 21.8 ms                                                         | 37.4 ms: 1.72x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (6): regex_v8, create_gc_cycles, xml_etree_parse, python_startup_no_site, json_loads, pathlib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: mypy2

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown