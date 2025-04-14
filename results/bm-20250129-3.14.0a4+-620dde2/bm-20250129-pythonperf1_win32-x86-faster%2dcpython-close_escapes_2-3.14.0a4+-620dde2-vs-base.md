# Results vs. base

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-x86
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                          | 258 ms: 1.03x slower                                                                 |
| docutils       | 1.83 sec                                                                        | 1.86 sec: 1.01x slower                                                               |
| html5lib       | 45.1 ms                                                                         | 45.3 ms: 1.01x slower                                                                |
| sphinx         | 743 ms                                                                          | 758 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators           | 311 ms                                                                          | 309 ms: 1.01x faster                                                                 |
| coroutines                 | 17.6 ms                                                                         | 17.8 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 441 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed    | 449 ms                                                                          | 460 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 456 ms                                                                          | 471 ms: 1.03x slower                                                                 |
| async_tree_memoization_tg  | 245 ms                                                                          | 253 ms: 1.04x slower                                                                 |
| async_tree_io              | 455 ms                                                                          | 475 ms: 1.04x slower                                                                 |
| async_tree_none_tg         | 196 ms                                                                          | 205 ms: 1.04x slower                                                                 |
| async_tree_memoization     | 256 ms                                                                          | 269 ms: 1.05x slower                                                                 |
| async_tree_none            | 211 ms                                                                          | 225 ms: 1.06x slower                                                                 |
| Geometric mean             | (ref)                                                                           | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                          | 202 ms: 1.01x slower                                                                 |
| nbody          | 83.4 ms                                                                         | 87.2 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                          | 116 ms: 1.01x faster                                                                 |
| regex_v8       | 15.7 ms                                                                         | 15.8 ms: 1.01x slower                                                                |
| regex_compile  | 105 ms                                                                          | 110 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.41 ms                                                                         | 9.24 ms: 1.02x faster                                                                |
| xml_etree_iterparse  | 67.7 ms                                                                         | 67.1 ms: 1.01x faster                                                                |
| xml_etree_parse      | 109 ms                                                                          | 110 ms: 1.01x slower                                                                 |
| xml_etree_generate   | 68.7 ms                                                                         | 70.5 ms: 1.03x slower                                                                |
| json_loads           | 22.7 us                                                                         | 23.2 us: 1.03x slower                                                                |
| unpickle_pure_python | 177 us                                                                          | 183 us: 1.03x slower                                                                 |
| xml_etree_process    | 50.1 ms                                                                         | 51.7 ms: 1.03x slower                                                                |
| tomli_loads          | 1.68 sec                                                                        | 1.76 sec: 1.05x slower                                                               |
| pickle_pure_python   | 273 us                                                                          | 289 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                                           | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                                         | 21.3 ms: 1.02x faster                                                                |
| mako            | 7.52 ms                                                                         | 7.68 ms: 1.02x slower                                                                |
| genshi_xml      | 45.7 ms                                                                         | 46.9 ms: 1.03x slower                                                                |
| django_template | 32.6 ms                                                                         | 35.1 ms: 1.08x slower                                                                |
| Geometric mean  | (ref)                                                                           | 1.02x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| telco                      | 7.14 ms                                                                         | 6.91 ms: 1.03x faster                                                                |
| connected_components       | 265 ms                                                                          | 258 ms: 1.03x faster                                                                 |
| shortest_path              | 294 ms                                                                          | 287 ms: 1.02x faster                                                                 |
| genshi_text                | 21.8 ms                                                                         | 21.3 ms: 1.02x faster                                                                |
| json_dumps                 | 9.41 ms                                                                         | 9.24 ms: 1.02x faster                                                                |
| spectral_norm              | 72.7 ms                                                                         | 72.1 ms: 1.01x faster                                                                |
| xml_etree_iterparse        | 67.7 ms                                                                         | 67.1 ms: 1.01x faster                                                                |
| pathlib                    | 86.5 ms                                                                         | 85.9 ms: 1.01x faster                                                                |
| async_generators           | 311 ms                                                                          | 309 ms: 1.01x faster                                                                 |
| regex_dna                  | 116 ms                                                                          | 116 ms: 1.01x faster                                                                 |
| nqueens                    | 78.1 ms                                                                         | 78.4 ms: 1.00x slower                                                                |
| mdp                        | 1.76 sec                                                                        | 1.77 sec: 1.00x slower                                                               |
| pidigits                   | 201 ms                                                                          | 202 ms: 1.01x slower                                                                 |
| regex_v8                   | 15.7 ms                                                                         | 15.8 ms: 1.01x slower                                                                |
| html5lib                   | 45.1 ms                                                                         | 45.3 ms: 1.01x slower                                                                |
| richards                   | 39.5 ms                                                                         | 39.8 ms: 1.01x slower                                                                |
| sqlglot_parse              | 1.08 ms                                                                         | 1.09 ms: 1.01x slower                                                                |
| fannkuch                   | 313 ms                                                                          | 316 ms: 1.01x slower                                                                 |
| coroutines                 | 17.6 ms                                                                         | 17.8 ms: 1.01x slower                                                                |
| sqlglot_transpile          | 1.33 ms                                                                         | 1.34 ms: 1.01x slower                                                                |
| gc_traversal               | 1.77 ms                                                                         | 1.78 ms: 1.01x slower                                                                |
| deepcopy_reduce            | 2.58 us                                                                         | 2.60 us: 1.01x slower                                                                |
| xml_etree_parse            | 109 ms                                                                          | 110 ms: 1.01x slower                                                                 |
| meteor_contest             | 80.1 ms                                                                         | 81.0 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 441 ms: 1.01x slower                                                                 |
| docutils                   | 1.83 sec                                                                        | 1.86 sec: 1.01x slower                                                               |
| create_gc_cycles           | 1.04 ms                                                                         | 1.06 ms: 1.01x slower                                                                |
| deltablue                  | 2.77 ms                                                                         | 2.82 ms: 1.02x slower                                                                |
| deepcopy_memo              | 21.3 us                                                                         | 21.7 us: 1.02x slower                                                                |
| sympy_integrate            | 15.6 ms                                                                         | 15.9 ms: 1.02x slower                                                                |
| comprehensions             | 14.3 us                                                                         | 14.6 us: 1.02x slower                                                                |
| sphinx                     | 743 ms                                                                          | 758 ms: 1.02x slower                                                                 |
| sympy_sum                  | 108 ms                                                                          | 110 ms: 1.02x slower                                                                 |
| logging_silent             | 75.9 ns                                                                         | 77.5 ns: 1.02x slower                                                                |
| mako                       | 7.52 ms                                                                         | 7.68 ms: 1.02x slower                                                                |
| richards_super             | 44.2 ms                                                                         | 45.4 ms: 1.03x slower                                                                |
| async_tree_cpu_io_mixed    | 449 ms                                                                          | 460 ms: 1.03x slower                                                                 |
| json                       | 4.59 ms                                                                         | 4.71 ms: 1.03x slower                                                                |
| xml_etree_generate         | 68.7 ms                                                                         | 70.5 ms: 1.03x slower                                                                |
| genshi_xml                 | 45.7 ms                                                                         | 46.9 ms: 1.03x slower                                                                |
| json_loads                 | 22.7 us                                                                         | 23.2 us: 1.03x slower                                                                |
| generators                 | 26.4 ms                                                                         | 27.1 ms: 1.03x slower                                                                |
| 2to3                       | 251 ms                                                                          | 258 ms: 1.03x slower                                                                 |
| subparsers                 | 21.0 ms                                                                         | 21.6 ms: 1.03x slower                                                                |
| sympy_str                  | 217 ms                                                                          | 224 ms: 1.03x slower                                                                 |
| unpickle_pure_python       | 177 us                                                                          | 183 us: 1.03x slower                                                                 |
| xml_etree_process          | 50.1 ms                                                                         | 51.7 ms: 1.03x slower                                                                |
| pyflate                    | 343 ms                                                                          | 354 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 456 ms                                                                          | 471 ms: 1.03x slower                                                                 |
| dulwich_log                | 50.6 ms                                                                         | 52.3 ms: 1.03x slower                                                                |
| hexiom                     | 5.26 ms                                                                         | 5.43 ms: 1.03x slower                                                                |
| bpe_tokeniser              | 3.41 sec                                                                        | 3.53 sec: 1.03x slower                                                               |
| scimark_monte_carlo        | 52.9 ms                                                                         | 54.7 ms: 1.03x slower                                                                |
| async_tree_memoization_tg  | 245 ms                                                                          | 253 ms: 1.04x slower                                                                 |
| sympy_expand               | 384 ms                                                                          | 398 ms: 1.04x slower                                                                 |
| crypto_pyaes               | 62.6 ms                                                                         | 65.1 ms: 1.04x slower                                                                |
| raytrace                   | 276 ms                                                                          | 287 ms: 1.04x slower                                                                 |
| pprint_pformat             | 1.33 sec                                                                        | 1.38 sec: 1.04x slower                                                               |
| async_tree_io              | 455 ms                                                                          | 475 ms: 1.04x slower                                                                 |
| pprint_safe_repr           | 642 ms                                                                          | 670 ms: 1.04x slower                                                                 |
| regex_compile              | 105 ms                                                                          | 110 ms: 1.04x slower                                                                 |
| coverage                   | 50.6 ms                                                                         | 52.8 ms: 1.04x slower                                                                |
| async_tree_none_tg         | 196 ms                                                                          | 205 ms: 1.04x slower                                                                 |
| nbody                      | 83.4 ms                                                                         | 87.2 ms: 1.05x slower                                                                |
| deepcopy                   | 236 us                                                                          | 247 us: 1.05x slower                                                                 |
| sqlglot_normalize          | 222 ms                                                                          | 232 ms: 1.05x slower                                                                 |
| tomli_loads                | 1.68 sec                                                                        | 1.76 sec: 1.05x slower                                                               |
| scimark_fft                | 223 ms                                                                          | 235 ms: 1.05x slower                                                                 |
| async_tree_memoization     | 256 ms                                                                          | 269 ms: 1.05x slower                                                                 |
| sqlglot_optimize           | 42.7 ms                                                                         | 45.0 ms: 1.05x slower                                                                |
| pycparser                  | 854 ms                                                                          | 900 ms: 1.05x slower                                                                 |
| logging_simple             | 7.99 us                                                                         | 8.43 us: 1.06x slower                                                                |
| pickle_pure_python         | 273 us                                                                          | 289 us: 1.06x slower                                                                 |
| logging_format             | 8.65 us                                                                         | 9.15 us: 1.06x slower                                                                |
| go                         | 101 ms                                                                          | 107 ms: 1.06x slower                                                                 |
| scimark_sparse_mat_mult    | 2.93 ms                                                                         | 3.11 ms: 1.06x slower                                                                |
| async_tree_none            | 211 ms                                                                          | 225 ms: 1.06x slower                                                                 |
| chaos                      | 55.0 ms                                                                         | 58.6 ms: 1.07x slower                                                                |
| scimark_lu                 | 73.3 ms                                                                         | 78.3 ms: 1.07x slower                                                                |
| django_template            | 32.6 ms                                                                         | 35.1 ms: 1.08x slower                                                                |
| typing_runtime_protocols   | 150 us                                                                          | 164 us: 1.09x slower                                                                 |
| Geometric mean             | (ref)                                                                           | 1.02x slower                                                                         |

Benchmark hidden because not significant (13): bench_thread_pool, thrift, k_core, float, bench_mp_pool, scimark_sor, sqlite_synth, python_startup_no_site, asyncio_websockets, regex_effbot, many_optionals, python_startup, pylint

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown