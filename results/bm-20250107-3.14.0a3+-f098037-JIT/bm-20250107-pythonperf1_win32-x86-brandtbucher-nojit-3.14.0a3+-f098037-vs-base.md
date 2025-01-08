# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.005x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators           | 346 ms                                                                          | 326 ms: 1.06x faster                                                   |
| async_tree_none            | 229 ms                                                                          | 223 ms: 1.03x faster                                                   |
| async_tree_none_tg         | 194 ms                                                                          | 189 ms: 1.03x faster                                                   |
| async_tree_memoization     | 279 ms                                                                          | 273 ms: 1.02x faster                                                   |
| async_tree_io              | 481 ms                                                                          | 470 ms: 1.02x faster                                                   |
| async_tree_io_tg           | 451 ms                                                                          | 444 ms: 1.02x faster                                                   |
| async_tree_memoization_tg  | 244 ms                                                                          | 241 ms: 1.01x faster                                                   |
| asyncio_websockets         | 353 ms                                                                          | 349 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 471 ms                                                                          | 473 ms: 1.00x slower                                                   |
| coroutines                 | 16.6 ms                                                                         | 16.8 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 440 ms                                                                          | 453 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                                         | 52.2 ms: 1.01x faster                                                  |
| pidigits       | 200 ms                                                                          | 201 ms: 1.01x slower                                                   |
| nbody          | 99.3 ms                                                                         | 102 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 114 ms                                                                          | 112 ms: 1.01x faster                                                   |
| regex_v8       | 15.4 ms                                                                         | 15.7 ms: 1.02x slower                                                  |
| regex_effbot   | 1.52 ms                                                                         | 1.65 ms: 1.08x slower                                                  |
| regex_dna      | 113 ms                                                                          | 124 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                           | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                                         | 20.6 us: 1.02x faster                                                  |
| unpickle_pure_python | 205 us                                                                          | 203 us: 1.01x faster                                                   |
| xml_etree_parse      | 108 ms                                                                          | 107 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 66.0 ms                                                                         | 66.6 ms: 1.01x slower                                                  |
| pickle_pure_python   | 291 us                                                                          | 294 us: 1.01x slower                                                   |
| json_dumps           | 9.02 ms                                                                         | 9.18 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                           | 1.00x slower                                                           |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                         | 19.1 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                                           | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                                         | 26.0 ms: 1.04x faster                                                  |
| genshi_xml     | 56.6 ms                                                                         | 55.1 ms: 1.03x faster                                                  |
| mako           | 7.39 ms                                                                         | 7.59 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 1.97 sec                                                                        | 1.84 sec: 1.07x faster                                                 |
| scimark_sor                | 98.7 ms                                                                         | 92.7 ms: 1.07x faster                                                  |
| async_generators           | 346 ms                                                                          | 326 ms: 1.06x faster                                                   |
| genshi_text                | 27.2 ms                                                                         | 26.0 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 64.4 ms                                                                         | 61.7 ms: 1.04x faster                                                  |
| logging_silent             | 87.9 ns                                                                         | 84.3 ns: 1.04x faster                                                  |
| telco                      | 7.43 ms                                                                         | 7.18 ms: 1.03x faster                                                  |
| richards_super             | 49.7 ms                                                                         | 48.1 ms: 1.03x faster                                                  |
| coverage                   | 53.5 ms                                                                         | 51.9 ms: 1.03x faster                                                  |
| async_tree_none            | 229 ms                                                                          | 223 ms: 1.03x faster                                                   |
| genshi_xml                 | 56.6 ms                                                                         | 55.1 ms: 1.03x faster                                                  |
| deepcopy_memo              | 23.4 us                                                                         | 22.8 us: 1.03x faster                                                  |
| async_tree_none_tg         | 194 ms                                                                          | 189 ms: 1.03x faster                                                   |
| async_tree_memoization     | 279 ms                                                                          | 273 ms: 1.02x faster                                                   |
| async_tree_io              | 481 ms                                                                          | 470 ms: 1.02x faster                                                   |
| nqueens                    | 98.7 ms                                                                         | 96.5 ms: 1.02x faster                                                  |
| thrift                     | 797 us                                                                          | 780 us: 1.02x faster                                                   |
| spectral_norm              | 76.2 ms                                                                         | 74.7 ms: 1.02x faster                                                  |
| deepcopy                   | 278 us                                                                          | 273 us: 1.02x faster                                                   |
| json_loads                 | 21.0 us                                                                         | 20.6 us: 1.02x faster                                                  |
| shortest_path              | 320 ms                                                                          | 314 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 2.84 us                                                                         | 2.79 us: 1.02x faster                                                  |
| async_tree_io_tg           | 451 ms                                                                          | 444 ms: 1.02x faster                                                   |
| deltablue                  | 3.22 ms                                                                         | 3.17 ms: 1.02x faster                                                  |
| python_startup_no_site     | 19.4 ms                                                                         | 19.1 ms: 1.02x faster                                                  |
| connected_components       | 290 ms                                                                          | 285 ms: 1.01x faster                                                   |
| float                      | 53.0 ms                                                                         | 52.2 ms: 1.01x faster                                                  |
| regex_compile              | 114 ms                                                                          | 112 ms: 1.01x faster                                                   |
| async_tree_memoization_tg  | 244 ms                                                                          | 241 ms: 1.01x faster                                                   |
| crypto_pyaes               | 69.8 ms                                                                         | 68.9 ms: 1.01x faster                                                  |
| meteor_contest             | 89.3 ms                                                                         | 88.3 ms: 1.01x faster                                                  |
| asyncio_websockets         | 353 ms                                                                          | 349 ms: 1.01x faster                                                   |
| subparsers                 | 21.4 ms                                                                         | 21.2 ms: 1.01x faster                                                  |
| sympy_integrate            | 17.5 ms                                                                         | 17.3 ms: 1.01x faster                                                  |
| pathlib                    | 83.7 ms                                                                         | 82.9 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 50.6 ms                                                                         | 50.1 ms: 1.01x faster                                                  |
| richards                   | 43.9 ms                                                                         | 43.5 ms: 1.01x faster                                                  |
| sqlglot_normalize          | 106 ms                                                                          | 105 ms: 1.01x faster                                                   |
| sqlite_synth               | 1.94 us                                                                         | 1.92 us: 1.01x faster                                                  |
| fannkuch                   | 336 ms                                                                          | 334 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 205 us                                                                          | 203 us: 1.01x faster                                                   |
| sympy_sum                  | 115 ms                                                                          | 114 ms: 1.01x faster                                                   |
| logging_simple             | 8.59 us                                                                         | 8.54 us: 1.01x faster                                                  |
| many_optionals             | 563 us                                                                          | 560 us: 1.01x faster                                                   |
| hexiom                     | 7.14 ms                                                                         | 7.10 ms: 1.01x faster                                                  |
| sympy_str                  | 235 ms                                                                          | 233 ms: 1.01x faster                                                   |
| xml_etree_parse            | 108 ms                                                                          | 107 ms: 1.01x faster                                                   |
| sympy_expand               | 408 ms                                                                          | 406 ms: 1.00x faster                                                   |
| scimark_lu                 | 72.7 ms                                                                         | 72.5 ms: 1.00x faster                                                  |
| mypy2                      | 729 ms                                                                          | 727 ms: 1.00x faster                                                   |
| go                         | 123 ms                                                                          | 124 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 731 ms                                                                          | 733 ms: 1.00x slower                                                   |
| raytrace                   | 306 ms                                                                          | 307 ms: 1.00x slower                                                   |
| async_tree_cpu_io_mixed    | 471 ms                                                                          | 473 ms: 1.00x slower                                                   |
| sqlglot_transpile          | 1.42 ms                                                                         | 1.42 ms: 1.00x slower                                                  |
| pidigits                   | 200 ms                                                                          | 201 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 66.0 ms                                                                         | 66.6 ms: 1.01x slower                                                  |
| create_gc_cycles           | 1.05 ms                                                                         | 1.06 ms: 1.01x slower                                                  |
| coroutines                 | 16.6 ms                                                                         | 16.8 ms: 1.01x slower                                                  |
| pickle_pure_python         | 291 us                                                                          | 294 us: 1.01x slower                                                   |
| generators                 | 37.2 ms                                                                         | 37.6 ms: 1.01x slower                                                  |
| dulwich_log                | 49.7 ms                                                                         | 50.5 ms: 1.02x slower                                                  |
| regex_v8                   | 15.4 ms                                                                         | 15.7 ms: 1.02x slower                                                  |
| json_dumps                 | 9.02 ms                                                                         | 9.18 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult    | 3.02 ms                                                                         | 3.08 ms: 1.02x slower                                                  |
| pycparser                  | 922 ms                                                                          | 943 ms: 1.02x slower                                                   |
| mako                       | 7.39 ms                                                                         | 7.59 ms: 1.03x slower                                                  |
| nbody                      | 99.3 ms                                                                         | 102 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 440 ms                                                                          | 453 ms: 1.03x slower                                                   |
| regex_effbot               | 1.52 ms                                                                         | 1.65 ms: 1.08x slower                                                  |
| regex_dna                  | 113 ms                                                                          | 124 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                                           | 1.01x faster                                                           |

Benchmark hidden because not significant (24): bench_thread_pool, typing_runtime_protocols, pylint, python_startup, gc_traversal, xml_etree_generate, k_core, bpe_tokeniser, json, pprint_pformat, html5lib, chaos, sphinx, docutils, comprehensions, logging_format, sqlglot_parse, bench_mp_pool, 2to3, xml_etree_process, scimark_fft, django_template, tomli_loads, pyflate

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown