# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: windows-x86
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.000x faster
- HPT reliability: 74.21%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                          | 273 ms: 1.02x slower                                                                  |
| docutils       | 1.96 sec                                                                        | 1.97 sec: 1.01x slower                                                                |
| html5lib       | 47.3 ms                                                                         | 47.6 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 483 ms                                                                          | 477 ms: 1.01x faster                                                                  |
| coroutines                 | 16.0 ms                                                                         | 15.9 ms: 1.01x faster                                                                 |
| async_tree_memoization     | 280 ms                                                                          | 278 ms: 1.01x faster                                                                  |
| async_tree_io              | 481 ms                                                                          | 479 ms: 1.00x faster                                                                  |
| asyncio_websockets         | 351 ms                                                                          | 353 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed    | 474 ms                                                                          | 490 ms: 1.03x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                          | 478 ms: 1.04x slower                                                                  |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                                          | 203 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 125 ms                                                                          | 117 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.54 ms                                                                         | 1.53 ms: 1.01x faster                                                                 |
| regex_v8       | 15.8 ms                                                                         | 15.7 ms: 1.01x faster                                                                 |
| regex_compile  | 116 ms                                                                          | 118 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|---------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads          | 23.1 us                                                                         | 22.2 us: 1.04x faster                                                                 |
| pickle_pure_python  | 329 us                                                                          | 325 us: 1.01x faster                                                                  |
| xml_etree_iterparse | 66.3 ms                                                                         | 67.0 ms: 1.01x slower                                                                 |
| xml_etree_process   | 55.3 ms                                                                         | 56.2 ms: 1.02x slower                                                                 |
| xml_etree_generate  | 74.2 ms                                                                         | 75.8 ms: 1.02x slower                                                                 |
| json_dumps          | 8.96 ms                                                                         | 9.38 ms: 1.05x slower                                                                 |
| Geometric mean      | (ref)                                                                           | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 37.8 ms                                                                         | 36.4 ms: 1.04x faster                                                                 |
| mako            | 7.61 ms                                                                         | 7.47 ms: 1.02x faster                                                                 |
| genshi_text     | 24.2 ms                                                                         | 24.5 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                           | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna                  | 125 ms                                                                          | 117 ms: 1.07x faster                                                                  |
| json_loads                 | 23.1 us                                                                         | 22.2 us: 1.04x faster                                                                 |
| django_template            | 37.8 ms                                                                         | 36.4 ms: 1.04x faster                                                                 |
| scimark_monte_carlo        | 51.2 ms                                                                         | 49.4 ms: 1.04x faster                                                                 |
| richards                   | 38.2 ms                                                                         | 36.9 ms: 1.04x faster                                                                 |
| fannkuch                   | 388 ms                                                                          | 375 ms: 1.03x faster                                                                  |
| json                       | 4.64 ms                                                                         | 4.51 ms: 1.03x faster                                                                 |
| typing_runtime_protocols   | 173 us                                                                          | 168 us: 1.03x faster                                                                  |
| chaos                      | 58.2 ms                                                                         | 57.1 ms: 1.02x faster                                                                 |
| mako                       | 7.61 ms                                                                         | 7.47 ms: 1.02x faster                                                                 |
| sqlglot_optimize           | 51.4 ms                                                                         | 50.5 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult    | 3.23 ms                                                                         | 3.18 ms: 1.02x faster                                                                 |
| coverage                   | 52.5 ms                                                                         | 51.6 ms: 1.02x faster                                                                 |
| hexiom                     | 6.07 ms                                                                         | 5.98 ms: 1.02x faster                                                                 |
| pprint_safe_repr           | 768 ms                                                                          | 756 ms: 1.02x faster                                                                  |
| go                         | 111 ms                                                                          | 109 ms: 1.01x faster                                                                  |
| pickle_pure_python         | 329 us                                                                          | 325 us: 1.01x faster                                                                  |
| crypto_pyaes               | 74.2 ms                                                                         | 73.2 ms: 1.01x faster                                                                 |
| async_tree_io_tg           | 483 ms                                                                          | 477 ms: 1.01x faster                                                                  |
| pprint_pformat             | 1.58 sec                                                                        | 1.56 sec: 1.01x faster                                                                |
| coroutines                 | 16.0 ms                                                                         | 15.9 ms: 1.01x faster                                                                 |
| regex_effbot               | 1.54 ms                                                                         | 1.53 ms: 1.01x faster                                                                 |
| async_tree_memoization     | 280 ms                                                                          | 278 ms: 1.01x faster                                                                  |
| regex_v8                   | 15.8 ms                                                                         | 15.7 ms: 1.01x faster                                                                 |
| sqlglot_parse              | 1.20 ms                                                                         | 1.20 ms: 1.01x faster                                                                 |
| scimark_fft                | 256 ms                                                                          | 255 ms: 1.00x faster                                                                  |
| async_tree_io              | 481 ms                                                                          | 479 ms: 1.00x faster                                                                  |
| sympy_str                  | 234 ms                                                                          | 235 ms: 1.00x slower                                                                  |
| sympy_integrate            | 17.0 ms                                                                         | 17.0 ms: 1.00x slower                                                                 |
| logging_format             | 8.98 us                                                                         | 9.03 us: 1.01x slower                                                                 |
| pyflate                    | 337 ms                                                                          | 339 ms: 1.01x slower                                                                  |
| pidigits                   | 202 ms                                                                          | 203 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 351 ms                                                                          | 353 ms: 1.01x slower                                                                  |
| html5lib                   | 47.3 ms                                                                         | 47.6 ms: 1.01x slower                                                                 |
| meteor_contest             | 89.7 ms                                                                         | 90.3 ms: 1.01x slower                                                                 |
| nqueens                    | 105 ms                                                                          | 106 ms: 1.01x slower                                                                  |
| scimark_lu                 | 66.7 ms                                                                         | 67.2 ms: 1.01x slower                                                                 |
| docutils                   | 1.96 sec                                                                        | 1.97 sec: 1.01x slower                                                                |
| dulwich_log                | 52.0 ms                                                                         | 52.5 ms: 1.01x slower                                                                 |
| sympy_expand               | 408 ms                                                                          | 412 ms: 1.01x slower                                                                  |
| subparsers                 | 22.4 ms                                                                         | 22.6 ms: 1.01x slower                                                                 |
| xml_etree_iterparse        | 66.3 ms                                                                         | 67.0 ms: 1.01x slower                                                                 |
| comprehensions             | 16.3 us                                                                         | 16.5 us: 1.01x slower                                                                 |
| deepcopy                   | 256 us                                                                          | 259 us: 1.01x slower                                                                  |
| pycparser                  | 971 ms                                                                          | 983 ms: 1.01x slower                                                                  |
| richards_super             | 43.0 ms                                                                         | 43.5 ms: 1.01x slower                                                                 |
| genshi_text                | 24.2 ms                                                                         | 24.5 ms: 1.01x slower                                                                 |
| spectral_norm              | 64.8 ms                                                                         | 65.7 ms: 1.01x slower                                                                 |
| logging_simple             | 8.18 us                                                                         | 8.30 us: 1.01x slower                                                                 |
| raytrace                   | 251 ms                                                                          | 254 ms: 1.01x slower                                                                  |
| regex_compile              | 116 ms                                                                          | 118 ms: 1.02x slower                                                                  |
| xml_etree_process          | 55.3 ms                                                                         | 56.2 ms: 1.02x slower                                                                 |
| many_optionals             | 564 us                                                                          | 574 us: 1.02x slower                                                                  |
| 2to3                       | 268 ms                                                                          | 273 ms: 1.02x slower                                                                  |
| xml_etree_generate         | 74.2 ms                                                                         | 75.8 ms: 1.02x slower                                                                 |
| thrift                     | 757 us                                                                          | 775 us: 1.02x slower                                                                  |
| logging_silent             | 69.3 ns                                                                         | 71.1 ns: 1.03x slower                                                                 |
| deepcopy_memo              | 21.6 us                                                                         | 22.3 us: 1.03x slower                                                                 |
| async_tree_cpu_io_mixed    | 474 ms                                                                          | 490 ms: 1.03x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 460 ms                                                                          | 478 ms: 1.04x slower                                                                  |
| bpe_tokeniser              | 3.88 sec                                                                        | 4.05 sec: 1.04x slower                                                                |
| json_dumps                 | 8.96 ms                                                                         | 9.38 ms: 1.05x slower                                                                 |
| deepcopy_reduce            | 2.60 us                                                                         | 2.75 us: 1.06x slower                                                                 |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                                          |

Benchmark hidden because not significant (31): nbody, pathlib, k_core, sqlite_synth, create_gc_cycles, gc_traversal, pylint, telco, async_tree_memoization_tg, python_startup, async_tree_none_tg, sqlglot_transpile, genshi_xml, generators, async_tree_none, scimark_sor, bench_thread_pool, connected_components, tomli_loads, python_startup_no_site, sqlglot_normalize, mdp, sphinx, xml_etree_parse, shortest_path, sympy_sum, async_generators, unpickle_pure_python, bench_mp_pool, deltablue, float

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 74.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown