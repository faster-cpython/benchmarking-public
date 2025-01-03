# Results vs. 3.13.0

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-x86
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.056x faster
- HPT reliability: 97.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 240 ms: 1.04x faster                                                          |
| docutils       | 1.78 sec                                                        | 1.75 sec: 1.01x faster                                                        |
| html5lib       | 47.5 ms                                                         | 42.4 ms: 1.12x faster                                                         |
| sphinx         | 719 ms                                                          | 712 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 218 ms: 1.29x faster                                                          |
| async_tree_none            | 245 ms                                                          | 196 ms: 1.25x faster                                                          |
| async_tree_memoization     | 297 ms                                                          | 237 ms: 1.25x faster                                                          |
| async_tree_io              | 526 ms                                                          | 424 ms: 1.24x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 175 ms: 1.23x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 407 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 435 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 424 ms: 1.07x faster                                                          |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                          |
| async_generators           | 270 ms                                                          | 295 ms: 1.09x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                  |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 196 ms: 1.03x faster                                                          |
| float          | 54.6 ms                                                         | 56.4 ms: 1.03x slower                                                         |
| nbody          | 80.0 ms                                                         | 85.1 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.17x faster                                                         |
| regex_dna      | 114 ms                                                          | 111 ms: 1.03x faster                                                          |
| regex_compile  | 101 ms                                                          | 98.6 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.61 sec: 1.07x faster                                                        |
| json_loads           | 21.6 us                                                         | 20.6 us: 1.05x faster                                                         |
| unpickle_pure_python | 160 us                                                          | 167 us: 1.05x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 64.7 ms: 1.05x slower                                                         |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.5 ms: 1.06x slower                                                         |
| xml_etree_process    | 44.2 ms                                                         | 47.2 ms: 1.07x slower                                                         |
| pickle_pure_python   | 231 us                                                          | 263 us: 1.14x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.72 ms: 1.19x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.3 ms: 1.11x faster                                                         |
| genshi_text     | 21.5 ms                                                         | 20.7 ms: 1.04x faster                                                         |
| mako            | 7.09 ms                                                         | 7.64 ms: 1.08x slower                                                         |
| django_template | 29.8 ms                                                         | 32.5 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 725 us: 13.76x faster                                                         |
| coverage                   | 324 ms                                                          | 53.1 ms: 6.10x faster                                                         |
| deepcopy                   | 314 us                                                          | 223 us: 1.41x faster                                                          |
| async_tree_memoization_tg  | 282 ms                                                          | 218 ms: 1.29x faster                                                          |
| deepcopy_reduce            | 2.92 us                                                         | 2.33 us: 1.25x faster                                                         |
| async_tree_none            | 245 ms                                                          | 196 ms: 1.25x faster                                                          |
| async_tree_memoization     | 297 ms                                                          | 237 ms: 1.25x faster                                                          |
| async_tree_io              | 526 ms                                                          | 424 ms: 1.24x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 175 ms: 1.23x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 407 ms: 1.21x faster                                                          |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.17x faster                                                         |
| deepcopy_memo              | 25.4 us                                                         | 22.1 us: 1.15x faster                                                         |
| go                         | 109 ms                                                          | 95.7 ms: 1.14x faster                                                         |
| html5lib                   | 47.5 ms                                                         | 42.4 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 435 ms: 1.11x faster                                                          |
| genshi_xml                 | 50.1 ms                                                         | 45.3 ms: 1.11x faster                                                         |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                         |
| telco                      | 6.96 ms                                                         | 6.36 ms: 1.09x faster                                                         |
| pycparser                  | 872 ms                                                          | 803 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 424 ms: 1.07x faster                                                          |
| pylint                     | 227 ms                                                          | 212 ms: 1.07x faster                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.61 sec: 1.07x faster                                                        |
| pprint_safe_repr           | 648 ms                                                          | 616 ms: 1.05x faster                                                          |
| connected_components       | 267 ms                                                          | 254 ms: 1.05x faster                                                          |
| json_loads                 | 21.6 us                                                         | 20.6 us: 1.05x faster                                                         |
| bench_mp_pool              | 90.6 ms                                                         | 86.8 ms: 1.04x faster                                                         |
| 2to3                       | 250 ms                                                          | 240 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.27 sec: 1.04x faster                                                        |
| k_core                     | 1.38 sec                                                        | 1.32 sec: 1.04x faster                                                        |
| genshi_text                | 21.5 ms                                                         | 20.7 ms: 1.04x faster                                                         |
| sympy_expand               | 373 ms                                                          | 360 ms: 1.04x faster                                                          |
| logging_format             | 8.72 us                                                         | 8.44 us: 1.03x faster                                                         |
| logging_simple             | 7.99 us                                                         | 7.76 us: 1.03x faster                                                         |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 216 ms                                                          | 211 ms: 1.03x faster                                                          |
| pidigits                   | 201 ms                                                          | 196 ms: 1.03x faster                                                          |
| regex_dna                  | 114 ms                                                          | 111 ms: 1.03x faster                                                          |
| regex_compile              | 101 ms                                                          | 98.6 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 41.4 ms                                                         | 40.4 ms: 1.02x faster                                                         |
| sympy_str                  | 212 ms                                                          | 207 ms: 1.02x faster                                                          |
| shortest_path              | 290 ms                                                          | 283 ms: 1.02x faster                                                          |
| sympy_sum                  | 106 ms                                                          | 103 ms: 1.02x faster                                                          |
| bpe_tokeniser              | 3.46 sec                                                        | 3.40 sec: 1.02x faster                                                        |
| docutils                   | 1.78 sec                                                        | 1.75 sec: 1.01x faster                                                        |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                         |
| json                       | 4.27 ms                                                         | 4.23 ms: 1.01x faster                                                         |
| sphinx                     | 719 ms                                                          | 712 ms: 1.01x faster                                                          |
| sympy_integrate            | 15.0 ms                                                         | 14.9 ms: 1.01x faster                                                         |
| nqueens                    | 72.1 ms                                                         | 72.4 ms: 1.00x slower                                                         |
| pathlib                    | 82.9 ms                                                         | 83.5 ms: 1.01x slower                                                         |
| gc_traversal               | 1.75 ms                                                         | 1.77 ms: 1.01x slower                                                         |
| spectral_norm              | 69.4 ms                                                         | 70.1 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 138 us                                                          | 139 us: 1.01x slower                                                          |
| dulwich_log                | 48.8 ms                                                         | 49.6 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.24 ms                                                         | 1.27 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.00 ms                                                         | 1.03 ms: 1.03x slower                                                         |
| fannkuch                   | 299 ms                                                          | 308 ms: 1.03x slower                                                          |
| float                      | 54.6 ms                                                         | 56.4 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.94 ms: 1.04x slower                                                         |
| mdp                        | 1.62 sec                                                        | 1.69 sec: 1.04x slower                                                        |
| scimark_fft                | 205 ms                                                          | 214 ms: 1.04x slower                                                          |
| unpickle_pure_python       | 160 us                                                          | 167 us: 1.05x slower                                                          |
| xml_etree_generate         | 61.4 ms                                                         | 64.7 ms: 1.05x slower                                                         |
| pyflate                    | 320 ms                                                          | 339 ms: 1.06x slower                                                          |
| chaos                      | 50.2 ms                                                         | 53.3 ms: 1.06x slower                                                         |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.5 ms: 1.06x slower                                                         |
| nbody                      | 80.0 ms                                                         | 85.1 ms: 1.06x slower                                                         |
| comprehensions             | 12.5 us                                                         | 13.3 us: 1.07x slower                                                         |
| xml_etree_process          | 44.2 ms                                                         | 47.2 ms: 1.07x slower                                                         |
| meteor_contest             | 74.6 ms                                                         | 80.3 ms: 1.08x slower                                                         |
| mako                       | 7.09 ms                                                         | 7.64 ms: 1.08x slower                                                         |
| crypto_pyaes               | 56.9 ms                                                         | 61.7 ms: 1.08x slower                                                         |
| richards                   | 32.7 ms                                                         | 35.5 ms: 1.09x slower                                                         |
| django_template            | 29.8 ms                                                         | 32.5 ms: 1.09x slower                                                         |
| deltablue                  | 2.33 ms                                                         | 2.54 ms: 1.09x slower                                                         |
| async_generators           | 270 ms                                                          | 295 ms: 1.09x slower                                                          |
| hexiom                     | 4.44 ms                                                         | 4.93 ms: 1.11x slower                                                         |
| richards_super             | 36.7 ms                                                         | 40.7 ms: 1.11x slower                                                         |
| generators                 | 21.8 ms                                                         | 24.3 ms: 1.12x slower                                                         |
| scimark_monte_carlo        | 47.7 ms                                                         | 53.7 ms: 1.13x slower                                                         |
| pickle_pure_python         | 231 us                                                          | 263 us: 1.14x slower                                                          |
| scimark_lu                 | 60.2 ms                                                         | 68.9 ms: 1.14x slower                                                         |
| many_optionals             | 436 us                                                          | 505 us: 1.16x slower                                                          |
| scimark_sor                | 85.9 ms                                                         | 101 ms: 1.18x slower                                                          |
| logging_silent             | 60.3 ns                                                         | 71.4 ns: 1.18x slower                                                         |
| json_dumps                 | 7.30 ms                                                         | 8.72 ms: 1.19x slower                                                         |
| raytrace                   | 201 ms                                                          | 255 ms: 1.27x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 20.0 ms: 1.36x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                  |

Benchmark hidden because not significant (6): regex_v8, create_gc_cycles, xml_etree_parse, bench_thread_pool, python_startup_no_site, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: mypy2

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 97.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown