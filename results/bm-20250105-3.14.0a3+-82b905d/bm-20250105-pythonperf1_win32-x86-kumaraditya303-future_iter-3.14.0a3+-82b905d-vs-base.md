# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: windows-x86
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.004x faster
- HPT reliability: 93.62%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.81 sec                                                                        | 1.79 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 423 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 442 ms                                                                          | 433 ms: 1.02x faster                                                           |
| async_tree_memoization     | 244 ms                                                                          | 241 ms: 1.01x faster                                                           |
| asyncio_websockets         | 375 ms                                                                          | 377 ms: 1.01x slower                                                           |
| async_tree_none_tg         | 178 ms                                                                          | 179 ms: 1.01x slower                                                           |
| async_tree_io              | 428 ms                                                                          | 434 ms: 1.01x slower                                                           |
| coroutines                 | 16.0 ms                                                                         | 16.3 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 410 ms                                                                          | 421 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_none, async_generators, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                          | 196 ms: 1.02x faster                                                           |
| float          | 54.5 ms                                                                         | 53.8 ms: 1.01x faster                                                          |
| nbody          | 84.3 ms                                                                         | 83.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.9 ms                                                                         | 16.0 ms: 1.00x slower                                                          |
| regex_effbot   | 1.55 ms                                                                         | 1.58 ms: 1.02x slower                                                          |
| regex_dna      | 114 ms                                                                          | 117 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                                          | 95.4 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 65.9 ms                                                                         | 63.6 ms: 1.04x faster                                                          |
| json_loads           | 21.0 us                                                                         | 20.7 us: 1.01x faster                                                          |
| unpickle_pure_python | 166 us                                                                          | 168 us: 1.01x slower                                                           |
| json_dumps           | 8.86 ms                                                                         | 9.09 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                         | 19.2 ms: 1.01x faster                                                          |
| python_startup         | 25.6 ms                                                                         | 25.4 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 46.1 ms                                                                         | 44.5 ms: 1.04x faster                                                          |
| django_template | 32.1 ms                                                                         | 31.2 ms: 1.03x faster                                                          |
| genshi_text     | 21.0 ms                                                                         | 20.4 ms: 1.03x faster                                                          |
| mako            | 7.54 ms                                                                         | 7.48 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse            | 107 ms                                                                          | 95.4 ms: 1.12x faster                                                          |
| pprint_safe_repr           | 651 ms                                                                          | 608 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.34 sec                                                                        | 1.25 sec: 1.07x faster                                                         |
| sqlite_synth               | 1.99 us                                                                         | 1.91 us: 1.04x faster                                                          |
| richards                   | 36.1 ms                                                                         | 34.8 ms: 1.04x faster                                                          |
| xml_etree_iterparse        | 65.9 ms                                                                         | 63.6 ms: 1.04x faster                                                          |
| genshi_xml                 | 46.1 ms                                                                         | 44.5 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 423 ms: 1.03x faster                                                           |
| typing_runtime_protocols   | 142 us                                                                          | 138 us: 1.03x faster                                                           |
| django_template            | 32.1 ms                                                                         | 31.2 ms: 1.03x faster                                                          |
| genshi_text                | 21.0 ms                                                                         | 20.4 ms: 1.03x faster                                                          |
| crypto_pyaes               | 61.4 ms                                                                         | 59.9 ms: 1.02x faster                                                          |
| pidigits                   | 201 ms                                                                          | 196 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 442 ms                                                                          | 433 ms: 1.02x faster                                                           |
| deltablue                  | 2.57 ms                                                                         | 2.52 ms: 1.02x faster                                                          |
| bpe_tokeniser              | 3.46 sec                                                                        | 3.40 sec: 1.02x faster                                                         |
| richards_super             | 41.3 ms                                                                         | 40.7 ms: 1.02x faster                                                          |
| connected_components       | 256 ms                                                                          | 253 ms: 1.01x faster                                                           |
| json_loads                 | 21.0 us                                                                         | 20.7 us: 1.01x faster                                                          |
| async_tree_memoization     | 244 ms                                                                          | 241 ms: 1.01x faster                                                           |
| json                       | 4.26 ms                                                                         | 4.21 ms: 1.01x faster                                                          |
| pyflate                    | 337 ms                                                                          | 333 ms: 1.01x faster                                                           |
| shortest_path              | 285 ms                                                                          | 282 ms: 1.01x faster                                                           |
| float                      | 54.5 ms                                                                         | 53.8 ms: 1.01x faster                                                          |
| python_startup_no_site     | 19.4 ms                                                                         | 19.2 ms: 1.01x faster                                                          |
| nbody                      | 84.3 ms                                                                         | 83.5 ms: 1.01x faster                                                          |
| docutils                   | 1.81 sec                                                                        | 1.79 sec: 1.01x faster                                                         |
| hexiom                     | 4.95 ms                                                                         | 4.91 ms: 1.01x faster                                                          |
| mypy2                      | 696 ms                                                                          | 690 ms: 1.01x faster                                                           |
| mako                       | 7.54 ms                                                                         | 7.48 ms: 1.01x faster                                                          |
| logging_format             | 8.45 us                                                                         | 8.38 us: 1.01x faster                                                          |
| python_startup             | 25.6 ms                                                                         | 25.4 ms: 1.01x faster                                                          |
| subparsers                 | 20.6 ms                                                                         | 20.4 ms: 1.01x faster                                                          |
| sympy_integrate            | 15.3 ms                                                                         | 15.3 ms: 1.01x faster                                                          |
| deepcopy_reduce            | 2.47 us                                                                         | 2.46 us: 1.01x faster                                                          |
| go                         | 94.5 ms                                                                         | 94.1 ms: 1.00x faster                                                          |
| scimark_sor                | 93.5 ms                                                                         | 93.1 ms: 1.00x faster                                                          |
| generators                 | 24.6 ms                                                                         | 24.5 ms: 1.00x faster                                                          |
| mdp                        | 1.70 sec                                                                        | 1.71 sec: 1.00x slower                                                         |
| deepcopy                   | 232 us                                                                          | 234 us: 1.00x slower                                                           |
| regex_v8                   | 15.9 ms                                                                         | 16.0 ms: 1.00x slower                                                          |
| asyncio_websockets         | 375 ms                                                                          | 377 ms: 1.01x slower                                                           |
| deepcopy_memo              | 21.4 us                                                                         | 21.5 us: 1.01x slower                                                          |
| many_optionals             | 520 us                                                                          | 523 us: 1.01x slower                                                           |
| pathlib                    | 83.7 ms                                                                         | 84.3 ms: 1.01x slower                                                          |
| scimark_lu                 | 65.6 ms                                                                         | 66.0 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 42.0 ms                                                                         | 42.3 ms: 1.01x slower                                                          |
| fannkuch                   | 290 ms                                                                          | 292 ms: 1.01x slower                                                           |
| sympy_expand               | 377 ms                                                                          | 379 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                                         | 1.03 ms: 1.01x slower                                                          |
| spectral_norm              | 67.6 ms                                                                         | 68.1 ms: 1.01x slower                                                          |
| async_tree_none_tg         | 178 ms                                                                          | 179 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 166 us                                                                          | 168 us: 1.01x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                                         | 1.27 ms: 1.01x slower                                                          |
| telco                      | 6.60 ms                                                                         | 6.68 ms: 1.01x slower                                                          |
| async_tree_io              | 428 ms                                                                          | 434 ms: 1.01x slower                                                           |
| gc_traversal               | 1.76 ms                                                                         | 1.79 ms: 1.01x slower                                                          |
| meteor_contest             | 79.5 ms                                                                         | 80.9 ms: 1.02x slower                                                          |
| logging_silent             | 68.5 ns                                                                         | 69.7 ns: 1.02x slower                                                          |
| logging_simple             | 7.67 us                                                                         | 7.80 us: 1.02x slower                                                          |
| regex_effbot               | 1.55 ms                                                                         | 1.58 ms: 1.02x slower                                                          |
| coroutines                 | 16.0 ms                                                                         | 16.3 ms: 1.02x slower                                                          |
| thrift                     | 718 us                                                                          | 735 us: 1.02x slower                                                           |
| nqueens                    | 74.9 ms                                                                         | 76.6 ms: 1.02x slower                                                          |
| pycparser                  | 798 ms                                                                          | 819 ms: 1.03x slower                                                           |
| json_dumps                 | 8.86 ms                                                                         | 9.09 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                                         | 2.98 ms: 1.03x slower                                                          |
| async_tree_io_tg           | 410 ms                                                                          | 421 ms: 1.03x slower                                                           |
| regex_dna                  | 114 ms                                                                          | 117 ms: 1.03x slower                                                           |
| scimark_fft                | 214 ms                                                                          | 222 ms: 1.03x slower                                                           |
| coverage                   | 50.5 ms                                                                         | 52.3 ms: 1.04x slower                                                          |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (24): raytrace, sphinx, k_core, 2to3, async_tree_none, pylint, tomli_loads, sqlglot_normalize, xml_etree_process, scimark_monte_carlo, async_generators, html5lib, create_gc_cycles, comprehensions, async_tree_memoization_tg, sympy_str, bench_mp_pool, dulwich_log, xml_etree_generate, sympy_sum, regex_compile, chaos, pickle_pure_python, bench_thread_pool

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 93.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown