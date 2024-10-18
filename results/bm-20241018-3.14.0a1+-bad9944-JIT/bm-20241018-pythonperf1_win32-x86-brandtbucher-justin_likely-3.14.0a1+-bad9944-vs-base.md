# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.01x slower
- HPT reliability: 60.24%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                          | 266 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): docutils, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none           | 225 ms                                                                          | 215 ms: 1.05x faster                                                           |
| async_tree_memoization    | 281 ms                                                                          | 273 ms: 1.03x faster                                                           |
| async_tree_memoization_tg | 258 ms                                                                          | 251 ms: 1.03x faster                                                           |
| async_tree_io             | 522 ms                                                                          | 510 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed   | 471 ms                                                                          | 465 ms: 1.01x faster                                                           |
| async_tree_none_tg        | 203 ms                                                                          | 201 ms: 1.01x faster                                                           |
| coroutines                | 17.3 ms                                                                         | 17.5 ms: 1.01x slower                                                          |
| async_generators          | 311 ms                                                                          | 322 ms: 1.03x slower                                                           |
| Geometric mean            | (ref)                                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                         | 59.6 ms: 1.10x faster                                                          |
| float          | 46.5 ms                                                                         | 45.7 ms: 1.02x faster                                                          |
| pidigits       | 200 ms                                                                          | 199 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.85 ms                                                                         | 1.76 ms: 1.05x faster                                                          |
| regex_v8       | 15.4 ms                                                                         | 15.6 ms: 1.01x slower                                                          |
| regex_dna      | 116 ms                                                                          | 118 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_list        | 2.94 us                                                                         | 2.81 us: 1.05x faster                                                          |
| unpickle             | 10.6 us                                                                         | 10.3 us: 1.03x faster                                                          |
| json_loads           | 20.6 us                                                                         | 20.5 us: 1.01x faster                                                          |
| unpickle_pure_python | 163 us                                                                          | 164 us: 1.01x slower                                                           |
| pickle_list          | 3.41 us                                                                         | 3.44 us: 1.01x slower                                                          |
| pickle               | 8.27 us                                                                         | 8.39 us: 1.02x slower                                                          |
| xml_etree_generate   | 53.8 ms                                                                         | 56.1 ms: 1.04x slower                                                          |
| pickle_pure_python   | 239 us                                                                          | 251 us: 1.05x slower                                                           |
| xml_etree_process    | 40.3 ms                                                                         | 42.3 ms: 1.05x slower                                                          |
| json_dumps           | 8.12 ms                                                                         | 8.74 ms: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 27.1 ms                                                                         | 26.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 54.5 ms                                                                         | 53.7 ms: 1.01x faster                                                          |
| mako            | 5.75 ms                                                                         | 5.78 ms: 1.01x slower                                                          |
| django_template | 32.3 ms                                                                         | 33.1 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                     | 65.5 ms                                                                         | 59.6 ms: 1.10x faster                                                          |
| coverage                  | 55.7 ms                                                                         | 52.7 ms: 1.06x faster                                                          |
| regex_effbot              | 1.85 ms                                                                         | 1.76 ms: 1.05x faster                                                          |
| unpickle_list             | 2.94 us                                                                         | 2.81 us: 1.05x faster                                                          |
| async_tree_none           | 225 ms                                                                          | 215 ms: 1.05x faster                                                           |
| unpack_sequence           | 42.9 ns                                                                         | 41.2 ns: 1.04x faster                                                          |
| async_tree_memoization    | 281 ms                                                                          | 273 ms: 1.03x faster                                                           |
| nqueens                   | 78.3 ms                                                                         | 76.0 ms: 1.03x faster                                                          |
| scimark_monte_carlo       | 40.8 ms                                                                         | 39.6 ms: 1.03x faster                                                          |
| async_tree_memoization_tg | 258 ms                                                                          | 251 ms: 1.03x faster                                                           |
| unpickle                  | 10.6 us                                                                         | 10.3 us: 1.03x faster                                                          |
| deepcopy_reduce           | 2.44 us                                                                         | 2.38 us: 1.03x faster                                                          |
| sympy_expand              | 401 ms                                                                          | 392 ms: 1.02x faster                                                           |
| async_tree_io             | 522 ms                                                                          | 510 ms: 1.02x faster                                                           |
| sympy_str                 | 231 ms                                                                          | 226 ms: 1.02x faster                                                           |
| logging_format            | 8.39 us                                                                         | 8.24 us: 1.02x faster                                                          |
| float                     | 46.5 ms                                                                         | 45.7 ms: 1.02x faster                                                          |
| scimark_lu                | 60.8 ms                                                                         | 59.9 ms: 1.02x faster                                                          |
| genshi_xml                | 54.5 ms                                                                         | 53.7 ms: 1.01x faster                                                          |
| sqlglot_transpile         | 1.36 ms                                                                         | 1.34 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed   | 471 ms                                                                          | 465 ms: 1.01x faster                                                           |
| meteor_contest            | 72.9 ms                                                                         | 72.1 ms: 1.01x faster                                                          |
| async_tree_none_tg        | 203 ms                                                                          | 201 ms: 1.01x faster                                                           |
| sympy_integrate           | 17.5 ms                                                                         | 17.4 ms: 1.01x faster                                                          |
| typing_runtime_protocols  | 143 us                                                                          | 142 us: 1.01x faster                                                           |
| python_startup            | 27.1 ms                                                                         | 26.9 ms: 1.01x faster                                                          |
| json_loads                | 20.6 us                                                                         | 20.5 us: 1.01x faster                                                          |
| hexiom                    | 5.47 ms                                                                         | 5.42 ms: 1.01x faster                                                          |
| logging_silent            | 56.1 ns                                                                         | 55.7 ns: 1.01x faster                                                          |
| go                        | 96.7 ms                                                                         | 96.0 ms: 1.01x faster                                                          |
| deepcopy                  | 232 us                                                                          | 231 us: 1.01x faster                                                           |
| pidigits                  | 200 ms                                                                          | 199 ms: 1.00x faster                                                           |
| mako                      | 5.75 ms                                                                         | 5.78 ms: 1.01x slower                                                          |
| unpickle_pure_python      | 163 us                                                                          | 164 us: 1.01x slower                                                           |
| 2to3                      | 264 ms                                                                          | 266 ms: 1.01x slower                                                           |
| pickle_list               | 3.41 us                                                                         | 3.44 us: 1.01x slower                                                          |
| sqlite_synth              | 1.94 us                                                                         | 1.96 us: 1.01x slower                                                          |
| generators                | 24.1 ms                                                                         | 24.3 ms: 1.01x slower                                                          |
| coroutines                | 17.3 ms                                                                         | 17.5 ms: 1.01x slower                                                          |
| telco                     | 6.03 ms                                                                         | 6.10 ms: 1.01x slower                                                          |
| pprint_safe_repr          | 569 ms                                                                          | 577 ms: 1.01x slower                                                           |
| regex_v8                  | 15.4 ms                                                                         | 15.6 ms: 1.01x slower                                                          |
| pickle                    | 8.27 us                                                                         | 8.39 us: 1.02x slower                                                          |
| thrift                    | 778 us                                                                          | 790 us: 1.02x slower                                                           |
| pprint_pformat            | 1.18 sec                                                                        | 1.20 sec: 1.02x slower                                                         |
| pathlib                   | 87.7 ms                                                                         | 89.1 ms: 1.02x slower                                                          |
| scimark_fft               | 181 ms                                                                          | 184 ms: 1.02x slower                                                           |
| gc_traversal              | 1.79 ms                                                                         | 1.83 ms: 1.02x slower                                                          |
| sqlglot_optimize          | 49.2 ms                                                                         | 50.3 ms: 1.02x slower                                                          |
| regex_dna                 | 116 ms                                                                          | 118 ms: 1.02x slower                                                           |
| django_template           | 32.3 ms                                                                         | 33.1 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult   | 2.48 ms                                                                         | 2.55 ms: 1.03x slower                                                          |
| richards_super            | 44.0 ms                                                                         | 45.2 ms: 1.03x slower                                                          |
| async_generators          | 311 ms                                                                          | 322 ms: 1.03x slower                                                           |
| deepcopy_memo             | 16.1 us                                                                         | 16.7 us: 1.04x slower                                                          |
| mdp                       | 1.68 sec                                                                        | 1.75 sec: 1.04x slower                                                         |
| fannkuch                  | 244 ms                                                                          | 254 ms: 1.04x slower                                                           |
| xml_etree_generate        | 53.8 ms                                                                         | 56.1 ms: 1.04x slower                                                          |
| chaos                     | 52.8 ms                                                                         | 55.3 ms: 1.05x slower                                                          |
| pickle_pure_python        | 239 us                                                                          | 251 us: 1.05x slower                                                           |
| xml_etree_process         | 40.3 ms                                                                         | 42.3 ms: 1.05x slower                                                          |
| raytrace                  | 256 ms                                                                          | 272 ms: 1.06x slower                                                           |
| json_dumps                | 8.12 ms                                                                         | 8.74 ms: 1.08x slower                                                          |
| sqlglot_normalize         | 100 ms                                                                          | 244 ms: 2.43x slower                                                           |
| Geometric mean            | (ref)                                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (32): json, async_tree_io_tg, bench_thread_pool, async_tree_cpu_io_mixed_tg, python_startup_no_site, spectral_norm, logging_simple, crypto_pyaes, pyflate, sphinx, deltablue, bench_mp_pool, xml_etree_parse, docutils, richards, genshi_text, tomli_loads, scimark_sor, pickle_dict, sqlglot_parse, pycparser, comprehensions, html5lib, asyncio_tcp_ssl, regex_compile, pylint, sympy_sum, xml_etree_iterparse, tornado_http, dulwich_log, create_gc_cycles, asyncio_tcp

# HPT report

- Reliability score: 60.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown