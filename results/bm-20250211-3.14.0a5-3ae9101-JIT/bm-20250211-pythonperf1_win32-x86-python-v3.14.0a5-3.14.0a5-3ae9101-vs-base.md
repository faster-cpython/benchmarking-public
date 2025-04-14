# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: windows-x86
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.014x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.01 sec                                                                        | 2.03 sec: 1.01x slower                                              |
| html5lib       | 47.5 ms                                                                         | 49.0 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 15.7 ms                                                                         | 15.8 ms: 1.01x slower                                               |
| async_tree_none            | 231 ms                                                                          | 233 ms: 1.01x slower                                                |
| async_tree_io              | 483 ms                                                                          | 489 ms: 1.01x slower                                                |
| async_tree_memoization     | 281 ms                                                                          | 285 ms: 1.01x slower                                                |
| async_tree_io_tg           | 477 ms                                                                          | 491 ms: 1.03x slower                                                |
| async_tree_memoization_tg  | 266 ms                                                                          | 273 ms: 1.03x slower                                                |
| async_generators           | 322 ms                                                                          | 334 ms: 1.04x slower                                                |
| async_tree_none_tg         | 209 ms                                                                          | 217 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed    | 467 ms                                                                          | 506 ms: 1.08x slower                                                |
| async_tree_cpu_io_mixed_tg | 451 ms                                                                          | 494 ms: 1.09x slower                                                |
| Geometric mean             | (ref)                                                                           | 1.03x slower                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 113 ms                                                                          | 110 ms: 1.03x faster                                                |
| pidigits       | 200 ms                                                                          | 201 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                          | 119 ms: 1.00x slower                                                |
| regex_compile  | 118 ms                                                                          | 119 ms: 1.01x slower                                                |
| regex_effbot   | 1.52 ms                                                                         | 1.54 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 23.1 us                                                                         | 22.8 us: 1.01x faster                                               |
| xml_etree_parse      | 109 ms                                                                          | 108 ms: 1.01x faster                                                |
| unpickle_pure_python | 226 us                                                                          | 227 us: 1.01x slower                                                |
| xml_etree_iterparse  | 68.1 ms                                                                         | 68.8 ms: 1.01x slower                                               |
| json_dumps           | 9.02 ms                                                                         | 9.18 ms: 1.02x slower                                               |
| tomli_loads          | 1.81 sec                                                                        | 1.85 sec: 1.02x slower                                              |
| pickle_pure_python   | 319 us                                                                          | 327 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 24.7 ms                                                                         | 24.3 ms: 1.02x faster                                               |
| genshi_xml      | 51.3 ms                                                                         | 50.7 ms: 1.01x faster                                               |
| mako            | 7.69 ms                                                                         | 7.91 ms: 1.03x slower                                               |
| django_template | 35.6 ms                                                                         | 36.8 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                           | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody                      | 113 ms                                                                          | 110 ms: 1.03x faster                                                |
| meteor_contest             | 95.1 ms                                                                         | 93.2 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult    | 3.17 ms                                                                         | 3.12 ms: 1.02x faster                                               |
| genshi_text                | 24.7 ms                                                                         | 24.3 ms: 1.02x faster                                               |
| create_gc_cycles           | 1.06 ms                                                                         | 1.04 ms: 1.02x faster                                               |
| telco                      | 7.68 ms                                                                         | 7.55 ms: 1.02x faster                                               |
| generators                 | 23.7 ms                                                                         | 23.3 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 174 us                                                                          | 171 us: 1.01x faster                                                |
| scimark_fft                | 261 ms                                                                          | 257 ms: 1.01x faster                                                |
| json_loads                 | 23.1 us                                                                         | 22.8 us: 1.01x faster                                               |
| thrift                     | 779 us                                                                          | 768 us: 1.01x faster                                                |
| genshi_xml                 | 51.3 ms                                                                         | 50.7 ms: 1.01x faster                                               |
| mdp                        | 1.89 sec                                                                        | 1.87 sec: 1.01x faster                                              |
| spectral_norm              | 66.2 ms                                                                         | 65.5 ms: 1.01x faster                                               |
| xml_etree_parse            | 109 ms                                                                          | 108 ms: 1.01x faster                                                |
| deepcopy_memo              | 21.4 us                                                                         | 21.3 us: 1.00x faster                                               |
| regex_dna                  | 118 ms                                                                          | 119 ms: 1.00x slower                                                |
| sqlglot_parse              | 1.21 ms                                                                         | 1.21 ms: 1.01x slower                                               |
| pprint_pformat             | 1.59 sec                                                                        | 1.60 sec: 1.01x slower                                              |
| deepcopy                   | 256 us                                                                          | 258 us: 1.01x slower                                                |
| unpickle_pure_python       | 226 us                                                                          | 227 us: 1.01x slower                                                |
| regex_compile              | 118 ms                                                                          | 119 ms: 1.01x slower                                                |
| coroutines                 | 15.7 ms                                                                         | 15.8 ms: 1.01x slower                                               |
| dulwich_log                | 52.4 ms                                                                         | 52.8 ms: 1.01x slower                                               |
| logging_format             | 9.17 us                                                                         | 9.24 us: 1.01x slower                                               |
| sympy_sum                  | 116 ms                                                                          | 117 ms: 1.01x slower                                                |
| pidigits                   | 200 ms                                                                          | 201 ms: 1.01x slower                                                |
| docutils                   | 2.01 sec                                                                        | 2.03 sec: 1.01x slower                                              |
| json                       | 4.63 ms                                                                         | 4.68 ms: 1.01x slower                                               |
| xml_etree_iterparse        | 68.1 ms                                                                         | 68.8 ms: 1.01x slower                                               |
| regex_effbot               | 1.52 ms                                                                         | 1.54 ms: 1.01x slower                                               |
| async_tree_none            | 231 ms                                                                          | 233 ms: 1.01x slower                                                |
| async_tree_io              | 483 ms                                                                          | 489 ms: 1.01x slower                                                |
| many_optionals             | 568 us                                                                          | 576 us: 1.01x slower                                                |
| async_tree_memoization     | 281 ms                                                                          | 285 ms: 1.01x slower                                                |
| comprehensions             | 16.6 us                                                                         | 16.9 us: 1.02x slower                                               |
| sympy_integrate            | 16.9 ms                                                                         | 17.2 ms: 1.02x slower                                               |
| json_dumps                 | 9.02 ms                                                                         | 9.18 ms: 1.02x slower                                               |
| fannkuch                   | 373 ms                                                                          | 380 ms: 1.02x slower                                                |
| sqlglot_normalize          | 105 ms                                                                          | 108 ms: 1.02x slower                                                |
| sqlglot_optimize           | 50.8 ms                                                                         | 51.8 ms: 1.02x slower                                               |
| sympy_str                  | 233 ms                                                                          | 238 ms: 1.02x slower                                                |
| hexiom                     | 6.13 ms                                                                         | 6.27 ms: 1.02x slower                                               |
| tomli_loads                | 1.81 sec                                                                        | 1.85 sec: 1.02x slower                                              |
| scimark_sor                | 101 ms                                                                          | 103 ms: 1.02x slower                                                |
| shortest_path              | 327 ms                                                                          | 336 ms: 1.02x slower                                                |
| pickle_pure_python         | 319 us                                                                          | 327 us: 1.03x slower                                                |
| async_tree_io_tg           | 477 ms                                                                          | 491 ms: 1.03x slower                                                |
| async_tree_memoization_tg  | 266 ms                                                                          | 273 ms: 1.03x slower                                                |
| pathlib                    | 34.0 ms                                                                         | 35.0 ms: 1.03x slower                                               |
| mako                       | 7.69 ms                                                                         | 7.91 ms: 1.03x slower                                               |
| connected_components       | 291 ms                                                                          | 300 ms: 1.03x slower                                                |
| django_template            | 35.6 ms                                                                         | 36.8 ms: 1.03x slower                                               |
| html5lib                   | 47.5 ms                                                                         | 49.0 ms: 1.03x slower                                               |
| sympy_expand               | 407 ms                                                                          | 422 ms: 1.04x slower                                                |
| async_generators           | 322 ms                                                                          | 334 ms: 1.04x slower                                                |
| async_tree_none_tg         | 209 ms                                                                          | 217 ms: 1.04x slower                                                |
| bpe_tokeniser              | 3.83 sec                                                                        | 4.00 sec: 1.04x slower                                              |
| pyflate                    | 333 ms                                                                          | 348 ms: 1.04x slower                                                |
| crypto_pyaes               | 73.5 ms                                                                         | 76.8 ms: 1.05x slower                                               |
| coverage                   | 53.4 ms                                                                         | 55.9 ms: 1.05x slower                                               |
| scimark_monte_carlo        | 50.5 ms                                                                         | 52.8 ms: 1.05x slower                                               |
| deepcopy_reduce            | 2.61 us                                                                         | 2.74 us: 1.05x slower                                               |
| chaos                      | 58.5 ms                                                                         | 61.3 ms: 1.05x slower                                               |
| deltablue                  | 2.75 ms                                                                         | 2.89 ms: 1.05x slower                                               |
| raytrace                   | 254 ms                                                                          | 268 ms: 1.05x slower                                                |
| go                         | 110 ms                                                                          | 117 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed    | 467 ms                                                                          | 506 ms: 1.08x slower                                                |
| async_tree_cpu_io_mixed_tg | 451 ms                                                                          | 494 ms: 1.09x slower                                                |
| richards_super             | 42.9 ms                                                                         | 47.0 ms: 1.10x slower                                               |
| richards                   | 37.2 ms                                                                         | 41.3 ms: 1.11x slower                                               |
| Geometric mean             | (ref)                                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (23): python_startup_no_site, gc_traversal, regex_v8, sqlite_synth, python_startup, logging_silent, bench_mp_pool, asyncio_websockets, nqueens, logging_simple, sqlglot_transpile, xml_etree_generate, pprint_safe_repr, subparsers, scimark_lu, pycparser, 2to3, xml_etree_process, k_core, sphinx, float, pylint, bench_thread_pool

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown