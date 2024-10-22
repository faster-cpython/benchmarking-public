# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.04 sec                                                                        | 2.05 sec: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (4): 2to3, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 223 ms                                                                          | 215 ms: 1.04x faster                                                           |
| async_tree_memoization     | 282 ms                                                                          | 273 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 477 ms                                                                          | 465 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 464 ms: 1.02x faster                                                           |
| async_tree_io              | 522 ms                                                                          | 510 ms: 1.02x faster                                                           |
| coroutines                 | 17.9 ms                                                                         | 17.5 ms: 1.02x faster                                                          |
| async_tree_memoization_tg  | 257 ms                                                                          | 251 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 204 ms                                                                          | 201 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 553 ms                                                                          | 547 ms: 1.01x faster                                                           |
| async_generators           | 320 ms                                                                          | 322 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 64.8 ms                                                                         | 59.6 ms: 1.09x faster                                                          |
| float          | 46.3 ms                                                                         | 45.7 ms: 1.01x faster                                                          |
| pidigits       | 201 ms                                                                          | 199 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                                         | 1.76 ms: 1.03x faster                                                          |
| regex_v8       | 15.7 ms                                                                         | 15.6 ms: 1.00x faster                                                          |
| regex_compile  | 105 ms                                                                          | 106 ms: 1.01x slower                                                           |
| regex_dna      | 113 ms                                                                          | 118 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.1 us                                                                         | 20.5 us: 1.03x faster                                                          |
| pickle_list          | 3.50 us                                                                         | 3.44 us: 1.02x faster                                                          |
| pickle               | 8.54 us                                                                         | 8.39 us: 1.02x faster                                                          |
| pickle_dict          | 21.6 us                                                                         | 21.2 us: 1.02x faster                                                          |
| xml_etree_parse      | 111 ms                                                                          | 110 ms: 1.01x faster                                                           |
| unpickle             | 10.4 us                                                                         | 10.3 us: 1.01x faster                                                          |
| tomli_loads          | 1.52 sec                                                                        | 1.51 sec: 1.01x faster                                                         |
| unpickle_pure_python | 163 us                                                                          | 164 us: 1.01x slower                                                           |
| xml_etree_generate   | 55.6 ms                                                                         | 56.1 ms: 1.01x slower                                                          |
| xml_etree_process    | 41.7 ms                                                                         | 42.3 ms: 1.01x slower                                                          |
| pickle_pure_python   | 245 us                                                                          | 251 us: 1.02x slower                                                           |
| json_dumps           | 8.14 ms                                                                         | 8.74 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 21.1 ms                                                                         | 20.3 ms: 1.04x faster                                                          |
| python_startup         | 27.7 ms                                                                         | 26.9 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.4 ms                                                                         | 22.9 ms: 1.02x faster                                                          |
| genshi_xml      | 54.4 ms                                                                         | 53.7 ms: 1.01x faster                                                          |
| mako            | 5.75 ms                                                                         | 5.78 ms: 1.01x slower                                                          |
| django_template | 32.8 ms                                                                         | 33.1 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                                           | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 64.8 ms                                                                         | 59.6 ms: 1.09x faster                                                          |
| bench_mp_pool              | 99.8 ms                                                                         | 94.1 ms: 1.06x faster                                                          |
| spectral_norm              | 60.1 ms                                                                         | 57.8 ms: 1.04x faster                                                          |
| python_startup_no_site     | 21.1 ms                                                                         | 20.3 ms: 1.04x faster                                                          |
| async_tree_none            | 223 ms                                                                          | 215 ms: 1.04x faster                                                           |
| async_tree_memoization     | 282 ms                                                                          | 273 ms: 1.03x faster                                                           |
| python_startup             | 27.7 ms                                                                         | 26.9 ms: 1.03x faster                                                          |
| regex_effbot               | 1.81 ms                                                                         | 1.76 ms: 1.03x faster                                                          |
| json_loads                 | 21.1 us                                                                         | 20.5 us: 1.03x faster                                                          |
| typing_runtime_protocols   | 146 us                                                                          | 142 us: 1.03x faster                                                           |
| crypto_pyaes               | 51.7 ms                                                                         | 50.3 ms: 1.03x faster                                                          |
| logging_silent             | 57.2 ns                                                                         | 55.7 ns: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 477 ms                                                                          | 465 ms: 1.03x faster                                                           |
| raytrace                   | 279 ms                                                                          | 272 ms: 1.03x faster                                                           |
| meteor_contest             | 73.9 ms                                                                         | 72.1 ms: 1.03x faster                                                          |
| go                         | 98.4 ms                                                                         | 96.0 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 464 ms: 1.02x faster                                                           |
| async_tree_io              | 522 ms                                                                          | 510 ms: 1.02x faster                                                           |
| coroutines                 | 17.9 ms                                                                         | 17.5 ms: 1.02x faster                                                          |
| genshi_text                | 23.4 ms                                                                         | 22.9 ms: 1.02x faster                                                          |
| async_tree_memoization_tg  | 257 ms                                                                          | 251 ms: 1.02x faster                                                           |
| pickle_list                | 3.50 us                                                                         | 3.44 us: 1.02x faster                                                          |
| scimark_monte_carlo        | 40.3 ms                                                                         | 39.6 ms: 1.02x faster                                                          |
| dulwich_log                | 50.4 ms                                                                         | 49.5 ms: 1.02x faster                                                          |
| richards                   | 39.5 ms                                                                         | 38.8 ms: 1.02x faster                                                          |
| pickle                     | 8.54 us                                                                         | 8.39 us: 1.02x faster                                                          |
| pickle_dict                | 21.6 us                                                                         | 21.2 us: 1.02x faster                                                          |
| sympy_str                  | 229 ms                                                                          | 226 ms: 1.02x faster                                                           |
| scimark_sor                | 70.2 ms                                                                         | 69.2 ms: 1.02x faster                                                          |
| async_tree_none_tg         | 204 ms                                                                          | 201 ms: 1.01x faster                                                           |
| float                      | 46.3 ms                                                                         | 45.7 ms: 1.01x faster                                                          |
| genshi_xml                 | 54.4 ms                                                                         | 53.7 ms: 1.01x faster                                                          |
| generators                 | 24.6 ms                                                                         | 24.3 ms: 1.01x faster                                                          |
| async_tree_io_tg           | 553 ms                                                                          | 547 ms: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                                          | 199 ms: 1.01x faster                                                           |
| logging_format             | 8.32 us                                                                         | 8.24 us: 1.01x faster                                                          |
| xml_etree_parse            | 111 ms                                                                          | 110 ms: 1.01x faster                                                           |
| sympy_expand               | 396 ms                                                                          | 392 ms: 1.01x faster                                                           |
| unpickle                   | 10.4 us                                                                         | 10.3 us: 1.01x faster                                                          |
| tomli_loads                | 1.52 sec                                                                        | 1.51 sec: 1.01x faster                                                         |
| regex_v8                   | 15.7 ms                                                                         | 15.6 ms: 1.00x faster                                                          |
| docutils                   | 2.04 sec                                                                        | 2.05 sec: 1.00x slower                                                         |
| deltablue                  | 2.57 ms                                                                         | 2.58 ms: 1.00x slower                                                          |
| mako                       | 5.75 ms                                                                         | 5.78 ms: 1.01x slower                                                          |
| async_generators           | 320 ms                                                                          | 322 ms: 1.01x slower                                                           |
| pyflate                    | 315 ms                                                                          | 317 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 572 ms                                                                          | 577 ms: 1.01x slower                                                           |
| deepcopy_reduce            | 2.36 us                                                                         | 2.38 us: 1.01x slower                                                          |
| unpickle_pure_python       | 163 us                                                                          | 164 us: 1.01x slower                                                           |
| xml_etree_generate         | 55.6 ms                                                                         | 56.1 ms: 1.01x slower                                                          |
| django_template            | 32.8 ms                                                                         | 33.1 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 49.8 ms                                                                         | 50.3 ms: 1.01x slower                                                          |
| logging_simple             | 7.53 us                                                                         | 7.62 us: 1.01x slower                                                          |
| scimark_sparse_mat_mult    | 2.52 ms                                                                         | 2.55 ms: 1.01x slower                                                          |
| regex_compile              | 105 ms                                                                          | 106 ms: 1.01x slower                                                           |
| pathlib                    | 87.9 ms                                                                         | 89.1 ms: 1.01x slower                                                          |
| xml_etree_process          | 41.7 ms                                                                         | 42.3 ms: 1.01x slower                                                          |
| gc_traversal               | 1.80 ms                                                                         | 1.83 ms: 1.02x slower                                                          |
| richards_super             | 44.5 ms                                                                         | 45.2 ms: 1.02x slower                                                          |
| pickle_pure_python         | 245 us                                                                          | 251 us: 1.02x slower                                                           |
| sqlite_synth               | 1.92 us                                                                         | 1.96 us: 1.02x slower                                                          |
| deepcopy_memo              | 16.3 us                                                                         | 16.7 us: 1.02x slower                                                          |
| fannkuch                   | 248 ms                                                                          | 254 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.17 sec                                                                        | 1.20 sec: 1.02x slower                                                         |
| mdp                        | 1.70 sec                                                                        | 1.75 sec: 1.03x slower                                                         |
| unpack_sequence            | 39.7 ns                                                                         | 41.2 ns: 1.04x slower                                                          |
| thrift                     | 757 us                                                                          | 790 us: 1.04x slower                                                           |
| regex_dna                  | 113 ms                                                                          | 118 ms: 1.04x slower                                                           |
| telco                      | 5.79 ms                                                                         | 6.10 ms: 1.05x slower                                                          |
| json_dumps                 | 8.14 ms                                                                         | 8.74 ms: 1.07x slower                                                          |
| sqlglot_normalize          | 102 ms                                                                          | 244 ms: 2.39x slower                                                           |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (25): json, asyncio_tcp, comprehensions, sphinx, coverage, 2to3, hexiom, xml_etree_iterparse, pylint, sqlglot_transpile, scimark_lu, tornado_http, nqueens, sympy_integrate, scimark_fft, bench_thread_pool, html5lib, deepcopy, sympy_sum, chaos, pycparser, sqlglot_parse, asyncio_tcp_ssl, unpickle_list, create_gc_cycles

# HPT report

- Reliability score: 98.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown