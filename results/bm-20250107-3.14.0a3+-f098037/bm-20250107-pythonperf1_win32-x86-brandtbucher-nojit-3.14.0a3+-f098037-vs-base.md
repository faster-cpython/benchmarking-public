# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.002x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 245 ms                                                                          | 247 ms: 1.01x slower                                                   |
| docutils       | 1.82 sec                                                                        | 1.84 sec: 1.01x slower                                                 |
| sphinx         | 724 ms                                                                          | 739 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 181 ms                                                                          | 183 ms: 1.01x slower                                                   |
| coroutines                 | 16.3 ms                                                                         | 16.5 ms: 1.01x slower                                                  |
| async_generators           | 291 ms                                                                          | 295 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 226 ms                                                                          | 230 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 428 ms                                                                          | 437 ms: 1.02x slower                                                   |
| async_tree_io              | 434 ms                                                                          | 446 ms: 1.03x slower                                                   |
| asyncio_websockets         | 358 ms                                                                          | 369 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 438 ms                                                                          | 451 ms: 1.03x slower                                                   |
| async_tree_none            | 202 ms                                                                          | 208 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 418 ms                                                                          | 433 ms: 1.04x slower                                                   |
| async_tree_memoization     | 244 ms                                                                          | 254 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                                           | 1.02x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.6 ms                                                                         | 55.6 ms: 1.02x faster                                                  |
| pidigits       | 198 ms                                                                          | 197 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                                         | 1.57 ms: 1.06x faster                                                  |
| regex_dna      | 124 ms                                                                          | 124 ms: 1.00x slower                                                   |
| regex_compile  | 101 ms                                                                          | 104 ms: 1.03x slower                                                   |
| regex_v8       | 15.5 ms                                                                         | 17.4 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                                           | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.64 sec                                                                        | 1.58 sec: 1.04x faster                                                 |
| unpickle_pure_python | 171 us                                                                          | 166 us: 1.03x faster                                                   |
| json_loads           | 21.3 us                                                                         | 20.7 us: 1.03x faster                                                  |
| pickle_pure_python   | 262 us                                                                          | 258 us: 1.02x faster                                                   |
| xml_etree_process    | 49.6 ms                                                                         | 48.8 ms: 1.01x faster                                                  |
| xml_etree_generate   | 68.7 ms                                                                         | 68.0 ms: 1.01x faster                                                  |
| json_dumps           | 8.82 ms                                                                         | 8.76 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 65.9 ms                                                                         | 66.7 ms: 1.01x slower                                                  |
| xml_etree_parse      | 107 ms                                                                          | 108 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                           | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 25.8 ms                                                                         | 25.4 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.59 ms                                                                         | 7.74 ms: 1.02x slower                                                  |
| django_template | 32.2 ms                                                                         | 33.3 ms: 1.03x slower                                                  |
| genshi_text     | 20.4 ms                                                                         | 21.1 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                           | 1.02x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_monte_carlo        | 56.4 ms                                                                         | 50.5 ms: 1.12x faster                                                  |
| scimark_sor                | 99.5 ms                                                                         | 93.1 ms: 1.07x faster                                                  |
| regex_effbot               | 1.66 ms                                                                         | 1.57 ms: 1.06x faster                                                  |
| typing_runtime_protocols   | 147 us                                                                          | 140 us: 1.05x faster                                                   |
| deepcopy_memo              | 21.7 us                                                                         | 20.7 us: 1.05x faster                                                  |
| tomli_loads                | 1.64 sec                                                                        | 1.58 sec: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 3.21 ms                                                                         | 3.08 ms: 1.04x faster                                                  |
| deepcopy_reduce            | 2.47 us                                                                         | 2.38 us: 1.04x faster                                                  |
| json                       | 4.37 ms                                                                         | 4.22 ms: 1.04x faster                                                  |
| deepcopy                   | 232 us                                                                          | 225 us: 1.03x faster                                                   |
| unpickle_pure_python       | 171 us                                                                          | 166 us: 1.03x faster                                                   |
| json_loads                 | 21.3 us                                                                         | 20.7 us: 1.03x faster                                                  |
| meteor_contest             | 81.6 ms                                                                         | 79.6 ms: 1.02x faster                                                  |
| coverage                   | 53.6 ms                                                                         | 52.4 ms: 1.02x faster                                                  |
| raytrace                   | 257 ms                                                                          | 252 ms: 1.02x faster                                                   |
| float                      | 56.6 ms                                                                         | 55.6 ms: 1.02x faster                                                  |
| pickle_pure_python         | 262 us                                                                          | 258 us: 1.02x faster                                                   |
| python_startup             | 25.8 ms                                                                         | 25.4 ms: 1.02x faster                                                  |
| xml_etree_process          | 49.6 ms                                                                         | 48.8 ms: 1.01x faster                                                  |
| comprehensions             | 13.4 us                                                                         | 13.2 us: 1.01x faster                                                  |
| chaos                      | 54.8 ms                                                                         | 54.0 ms: 1.01x faster                                                  |
| thrift                     | 742 us                                                                          | 732 us: 1.01x faster                                                   |
| richards                   | 36.0 ms                                                                         | 35.6 ms: 1.01x faster                                                  |
| xml_etree_generate         | 68.7 ms                                                                         | 68.0 ms: 1.01x faster                                                  |
| json_dumps                 | 8.82 ms                                                                         | 8.76 ms: 1.01x faster                                                  |
| sympy_sum                  | 106 ms                                                                          | 105 ms: 1.01x faster                                                   |
| nqueens                    | 75.5 ms                                                                         | 75.2 ms: 1.00x faster                                                  |
| pidigits                   | 198 ms                                                                          | 197 ms: 1.00x faster                                                   |
| mdp                        | 1.72 sec                                                                        | 1.72 sec: 1.00x slower                                                 |
| regex_dna                  | 124 ms                                                                          | 124 ms: 1.00x slower                                                   |
| sympy_str                  | 214 ms                                                                          | 215 ms: 1.00x slower                                                   |
| sympy_expand               | 376 ms                                                                          | 378 ms: 1.00x slower                                                   |
| hexiom                     | 4.86 ms                                                                         | 4.88 ms: 1.00x slower                                                  |
| fannkuch                   | 308 ms                                                                          | 309 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 41.0 ms                                                                         | 41.3 ms: 1.01x slower                                                  |
| 2to3                       | 245 ms                                                                          | 247 ms: 1.01x slower                                                   |
| go                         | 96.7 ms                                                                         | 97.4 ms: 1.01x slower                                                  |
| scimark_fft                | 227 ms                                                                          | 229 ms: 1.01x slower                                                   |
| create_gc_cycles           | 1.05 ms                                                                         | 1.06 ms: 1.01x slower                                                  |
| async_tree_none_tg         | 181 ms                                                                          | 183 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.30 sec                                                                        | 1.31 sec: 1.01x slower                                                 |
| scimark_lu                 | 67.5 ms                                                                         | 68.2 ms: 1.01x slower                                                  |
| coroutines                 | 16.3 ms                                                                         | 16.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 65.9 ms                                                                         | 66.7 ms: 1.01x slower                                                  |
| docutils                   | 1.82 sec                                                                        | 1.84 sec: 1.01x slower                                                 |
| many_optionals             | 530 us                                                                          | 537 us: 1.01x slower                                                   |
| shortest_path              | 284 ms                                                                          | 288 ms: 1.01x slower                                                   |
| xml_etree_parse            | 107 ms                                                                          | 108 ms: 1.01x slower                                                   |
| dulwich_log                | 50.0 ms                                                                         | 50.7 ms: 1.01x slower                                                  |
| sqlite_synth               | 1.95 us                                                                         | 1.98 us: 1.02x slower                                                  |
| async_generators           | 291 ms                                                                          | 295 ms: 1.02x slower                                                   |
| pylint                     | 216 ms                                                                          | 219 ms: 1.02x slower                                                   |
| mypy2                      | 684 ms                                                                          | 695 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 226 ms                                                                          | 230 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 3.49 sec                                                                        | 3.56 sec: 1.02x slower                                                 |
| sympy_integrate            | 15.3 ms                                                                         | 15.6 ms: 1.02x slower                                                  |
| connected_components       | 254 ms                                                                          | 259 ms: 1.02x slower                                                   |
| mako                       | 7.59 ms                                                                         | 7.74 ms: 1.02x slower                                                  |
| telco                      | 6.58 ms                                                                         | 6.71 ms: 1.02x slower                                                  |
| sphinx                     | 724 ms                                                                          | 739 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 428 ms                                                                          | 437 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.26 ms                                                                         | 1.29 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 208 ms                                                                          | 214 ms: 1.03x slower                                                   |
| generators                 | 24.1 ms                                                                         | 24.7 ms: 1.03x slower                                                  |
| crypto_pyaes               | 61.4 ms                                                                         | 63.0 ms: 1.03x slower                                                  |
| async_tree_io              | 434 ms                                                                          | 446 ms: 1.03x slower                                                   |
| logging_silent             | 71.7 ns                                                                         | 73.6 ns: 1.03x slower                                                  |
| regex_compile              | 101 ms                                                                          | 104 ms: 1.03x slower                                                   |
| asyncio_websockets         | 358 ms                                                                          | 369 ms: 1.03x slower                                                   |
| deltablue                  | 2.60 ms                                                                         | 2.68 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed    | 438 ms                                                                          | 451 ms: 1.03x slower                                                   |
| async_tree_none            | 202 ms                                                                          | 208 ms: 1.03x slower                                                   |
| django_template            | 32.2 ms                                                                         | 33.3 ms: 1.03x slower                                                  |
| genshi_text                | 20.4 ms                                                                         | 21.1 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 418 ms                                                                          | 433 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.02 ms                                                                         | 1.06 ms: 1.04x slower                                                  |
| async_tree_memoization     | 244 ms                                                                          | 254 ms: 1.04x slower                                                   |
| pycparser                  | 843 ms                                                                          | 900 ms: 1.07x slower                                                   |
| regex_v8                   | 15.5 ms                                                                         | 17.4 ms: 1.13x slower                                                  |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                           |

Benchmark hidden because not significant (16): bench_thread_pool, pyflate, genshi_xml, bench_mp_pool, python_startup_no_site, html5lib, richards_super, nbody, pprint_safe_repr, logging_format, spectral_norm, logging_simple, k_core, subparsers, gc_traversal, pathlib

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown