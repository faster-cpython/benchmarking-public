# Results vs. base

- fork: eendebakpt
- ref: iterator_freelists
- machine: linux-x86_64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.006x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                       | 279 ms: 1.01x faster                                                           |
| docutils       | 2.87 sec                                                                     | 2.85 sec: 1.01x faster                                                         |
| html5lib       | 66.1 ms                                                                      | 65.0 ms: 1.02x faster                                                          |
| sphinx         | 1.11 sec                                                                     | 1.10 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|---------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators          | 413 ms                                                                       | 410 ms: 1.01x faster                                                           |
| async_tree_memoization_tg | 333 ms                                                                       | 334 ms: 1.00x slower                                                           |
| coroutines                | 20.7 ms                                                                      | 20.8 ms: 1.00x slower                                                          |
| async_tree_none_tg        | 275 ms                                                                       | 279 ms: 1.01x slower                                                           |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 89.1 ms                                                                      | 86.9 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                       | 231 ms: 1.03x faster                                                           |
| regex_effbot   | 3.07 ms                                                                      | 3.10 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 26.8 us                                                                      | 26.0 us: 1.03x faster                                                          |
| xml_etree_generate   | 84.7 ms                                                                      | 82.7 ms: 1.02x faster                                                          |
| json_dumps           | 11.7 ms                                                                      | 11.4 ms: 1.02x faster                                                          |
| xml_etree_parse      | 139 ms                                                                       | 136 ms: 1.02x faster                                                           |
| tomli_loads          | 2.08 sec                                                                     | 2.05 sec: 1.02x faster                                                         |
| xml_etree_process    | 59.5 ms                                                                      | 58.5 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 97.2 ms                                                                      | 96.1 ms: 1.01x faster                                                          |
| pickle_pure_python   | 327 us                                                                       | 324 us: 1.01x faster                                                           |
| unpickle_pure_python | 207 us                                                                       | 207 us: 1.00x faster                                                           |
| Geometric mean       | (ref)                                                                        | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                                      | 8.93 ms: 1.00x faster                                                          |
| python_startup         | 16.0 ms                                                                      | 15.9 ms: 1.00x faster                                                          |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                                      | 35.0 ms: 1.03x faster                                                          |
| genshi_xml      | 52.2 ms                                                                      | 51.7 ms: 1.01x faster                                                          |
| genshi_text     | 23.2 ms                                                                      | 23.0 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|---------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols  | 176 us                                                                       | 164 us: 1.07x faster                                                           |
| comprehensions            | 17.8 us                                                                      | 16.7 us: 1.06x faster                                                          |
| gc_traversal              | 6.59 ms                                                                      | 6.32 ms: 1.04x faster                                                          |
| sqlglot_optimize          | 57.8 ms                                                                      | 55.7 ms: 1.04x faster                                                          |
| sqlglot_normalize         | 117 ms                                                                       | 113 ms: 1.04x faster                                                           |
| bpe_tokeniser             | 4.70 sec                                                                     | 4.55 sec: 1.03x faster                                                         |
| deepcopy_memo             | 30.2 us                                                                      | 29.2 us: 1.03x faster                                                          |
| django_template           | 36.0 ms                                                                      | 35.0 ms: 1.03x faster                                                          |
| json_loads                | 26.8 us                                                                      | 26.0 us: 1.03x faster                                                          |
| regex_dna                 | 237 ms                                                                       | 231 ms: 1.03x faster                                                           |
| json                      | 5.56 ms                                                                      | 5.41 ms: 1.03x faster                                                          |
| mdp                       | 2.49 sec                                                                     | 2.42 sec: 1.03x faster                                                         |
| xml_etree_generate        | 84.7 ms                                                                      | 82.7 ms: 1.02x faster                                                          |
| nbody                     | 89.1 ms                                                                      | 86.9 ms: 1.02x faster                                                          |
| json_dumps                | 11.7 ms                                                                      | 11.4 ms: 1.02x faster                                                          |
| telco                     | 8.16 ms                                                                      | 7.97 ms: 1.02x faster                                                          |
| create_gc_cycles          | 2.78 ms                                                                      | 2.72 ms: 1.02x faster                                                          |
| xml_etree_parse           | 139 ms                                                                       | 136 ms: 1.02x faster                                                           |
| go                        | 125 ms                                                                       | 122 ms: 1.02x faster                                                           |
| bench_thread_pool         | 927 us                                                                       | 911 us: 1.02x faster                                                           |
| html5lib                  | 66.1 ms                                                                      | 65.0 ms: 1.02x faster                                                          |
| tomli_loads               | 2.08 sec                                                                     | 2.05 sec: 1.02x faster                                                         |
| logging_format            | 6.76 us                                                                      | 6.66 us: 1.02x faster                                                          |
| xml_etree_process         | 59.5 ms                                                                      | 58.5 ms: 1.02x faster                                                          |
| spectral_norm             | 84.9 ms                                                                      | 83.6 ms: 1.02x faster                                                          |
| many_optionals            | 1.01 ms                                                                      | 995 us: 1.01x faster                                                           |
| meteor_contest            | 127 ms                                                                       | 125 ms: 1.01x faster                                                           |
| sqlalchemy_imperative     | 17.8 ms                                                                      | 17.5 ms: 1.01x faster                                                          |
| shortest_path             | 445 ms                                                                       | 440 ms: 1.01x faster                                                           |
| xml_etree_iterparse       | 97.2 ms                                                                      | 96.1 ms: 1.01x faster                                                          |
| logging_simple            | 6.12 us                                                                      | 6.06 us: 1.01x faster                                                          |
| pickle_pure_python        | 327 us                                                                       | 324 us: 1.01x faster                                                           |
| sqlite_synth              | 2.83 us                                                                      | 2.80 us: 1.01x faster                                                          |
| dulwich_log               | 66.7 ms                                                                      | 66.0 ms: 1.01x faster                                                          |
| 2to3                      | 282 ms                                                                       | 279 ms: 1.01x faster                                                           |
| genshi_xml                | 52.2 ms                                                                      | 51.7 ms: 1.01x faster                                                          |
| docutils                  | 2.87 sec                                                                     | 2.85 sec: 1.01x faster                                                         |
| sympy_expand              | 489 ms                                                                       | 485 ms: 1.01x faster                                                           |
| sphinx                    | 1.11 sec                                                                     | 1.10 sec: 1.01x faster                                                         |
| genshi_text               | 23.2 ms                                                                      | 23.0 ms: 1.01x faster                                                          |
| sympy_str                 | 287 ms                                                                       | 285 ms: 1.01x faster                                                           |
| connected_components      | 418 ms                                                                       | 415 ms: 1.01x faster                                                           |
| async_generators          | 413 ms                                                                       | 410 ms: 1.01x faster                                                           |
| deltablue                 | 3.27 ms                                                                      | 3.25 ms: 1.01x faster                                                          |
| thrift                    | 848 us                                                                       | 843 us: 1.01x faster                                                           |
| sympy_integrate           | 23.0 ms                                                                      | 22.8 ms: 1.00x faster                                                          |
| pprint_safe_repr          | 773 ms                                                                       | 770 ms: 1.00x faster                                                           |
| python_startup_no_site    | 8.96 ms                                                                      | 8.93 ms: 1.00x faster                                                          |
| python_startup            | 16.0 ms                                                                      | 15.9 ms: 1.00x faster                                                          |
| sqlalchemy_declarative    | 142 ms                                                                       | 142 ms: 1.00x faster                                                           |
| sympy_sum                 | 150 ms                                                                       | 149 ms: 1.00x faster                                                           |
| deepcopy                  | 279 us                                                                       | 278 us: 1.00x faster                                                           |
| unpickle_pure_python      | 207 us                                                                       | 207 us: 1.00x faster                                                           |
| async_tree_memoization_tg | 333 ms                                                                       | 334 ms: 1.00x slower                                                           |
| sqlglot_parse             | 1.31 ms                                                                      | 1.32 ms: 1.00x slower                                                          |
| coroutines                | 20.7 ms                                                                      | 20.8 ms: 1.00x slower                                                          |
| chaos                     | 59.2 ms                                                                      | 59.5 ms: 1.01x slower                                                          |
| pprint_pformat            | 1.56 sec                                                                     | 1.57 sec: 1.01x slower                                                         |
| richards_super            | 51.4 ms                                                                      | 51.7 ms: 1.01x slower                                                          |
| deepcopy_reduce           | 2.91 us                                                                      | 2.93 us: 1.01x slower                                                          |
| crypto_pyaes              | 72.7 ms                                                                      | 73.3 ms: 1.01x slower                                                          |
| fannkuch                  | 364 ms                                                                       | 368 ms: 1.01x slower                                                           |
| regex_effbot              | 3.07 ms                                                                      | 3.10 ms: 1.01x slower                                                          |
| async_tree_none_tg        | 275 ms                                                                       | 279 ms: 1.01x slower                                                           |
| scimark_fft               | 305 ms                                                                       | 309 ms: 1.01x slower                                                           |
| scimark_lu                | 92.1 ms                                                                      | 93.2 ms: 1.01x slower                                                          |
| richards                  | 45.5 ms                                                                      | 46.2 ms: 1.02x slower                                                          |
| pycparser                 | 1.21 sec                                                                     | 1.23 sec: 1.02x slower                                                         |
| nqueens                   | 89.9 ms                                                                      | 91.4 ms: 1.02x slower                                                          |
| raytrace                  | 271 ms                                                                       | 277 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult   | 4.53 ms                                                                      | 4.69 ms: 1.03x slower                                                          |
| coverage                  | 77.8 ms                                                                      | 81.3 ms: 1.05x slower                                                          |
| scimark_sor               | 108 ms                                                                       | 114 ms: 1.05x slower                                                           |
| scimark_monte_carlo       | 60.5 ms                                                                      | 66.1 ms: 1.09x slower                                                          |
| Geometric mean            | (ref)                                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (22): pylint, float, k_core, async_tree_cpu_io_mixed, asyncio_websockets, mako, regex_compile, hexiom, async_tree_io, pathlib, sqlglot_transpile, async_tree_cpu_io_mixed_tg, subparsers, pidigits, generators, logging_silent, async_tree_memoization, pyflate, async_tree_io_tg, async_tree_none, regex_v8, bench_mp_pool

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x