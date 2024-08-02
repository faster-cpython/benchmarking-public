# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 97.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib       | 48.5 ms                                                                        | 48.6 ms: 1.00x slower                                                          |
| tornado_http   | 98.9 ms                                                                        | 97.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 488 ms                                                                         | 498 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                                         | 481 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 53.9 ms                                                                        | 54.4 ms: 1.01x slower                                                          |
| float          | 42.4 ms                                                                        | 43.1 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 95.1 ms                                                                        | 93.6 ms: 1.02x faster                                                          |
| regex_dna      | 124 ms                                                                         | 129 ms: 1.04x slower                                                           |
| regex_effbot   | 1.99 ms                                                                        | 2.07 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle           | 10.6 us                                                                        | 10.3 us: 1.02x faster                                                          |
| xml_etree_process  | 43.6 ms                                                                        | 42.8 ms: 1.02x faster                                                          |
| json_dumps         | 6.83 ms                                                                        | 6.87 ms: 1.01x slower                                                          |
| pickle_pure_python | 208 us                                                                         | 211 us: 1.01x slower                                                           |
| unpickle_list      | 2.65 us                                                                        | 2.78 us: 1.05x slower                                                          |
| pickle_list        | 3.81 us                                                                        | 4.10 us: 1.08x slower                                                          |
| Geometric mean     | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_parse, tomli_loads, pickle_dict, json_loads, pickle, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.8 ms                                                                        | 25.1 ms: 1.01x slower                                                          |
| python_startup_no_site | 20.7 ms                                                                        | 21.0 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                          | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 54.5 ms                                                                        | 51.0 ms: 1.07x faster                                                          |
| genshi_text     | 22.4 ms                                                                        | 21.4 ms: 1.04x faster                                                          |
| mako            | 5.47 ms                                                                        | 5.34 ms: 1.02x faster                                                          |
| django_template | 33.9 ms                                                                        | 34.1 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                                          | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| hexiom                     | 4.70 ms                                                                        | 4.32 ms: 1.09x faster                                                          |
| genshi_xml                 | 54.5 ms                                                                        | 51.0 ms: 1.07x faster                                                          |
| genshi_text                | 22.4 ms                                                                        | 21.4 ms: 1.04x faster                                                          |
| coverage                   | 51.5 ms                                                                        | 49.6 ms: 1.04x faster                                                          |
| nqueens                    | 74.0 ms                                                                        | 71.2 ms: 1.04x faster                                                          |
| mako                       | 5.47 ms                                                                        | 5.34 ms: 1.02x faster                                                          |
| unpickle                   | 10.6 us                                                                        | 10.3 us: 1.02x faster                                                          |
| sqlglot_optimize           | 44.0 ms                                                                        | 43.2 ms: 1.02x faster                                                          |
| pycparser                  | 847 ms                                                                         | 831 ms: 1.02x faster                                                           |
| fannkuch                   | 217 ms                                                                         | 213 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 41.9 ms                                                                        | 41.2 ms: 1.02x faster                                                          |
| xml_etree_process          | 43.6 ms                                                                        | 42.8 ms: 1.02x faster                                                          |
| regex_compile              | 95.1 ms                                                                        | 93.6 ms: 1.02x faster                                                          |
| sqlglot_parse              | 936 us                                                                         | 922 us: 1.02x faster                                                           |
| sqlglot_normalize          | 237 ms                                                                         | 233 ms: 1.02x faster                                                           |
| coroutines                 | 17.7 ms                                                                        | 17.5 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.94 us                                                                        | 1.92 us: 1.01x faster                                                          |
| tornado_http               | 98.9 ms                                                                        | 97.8 ms: 1.01x faster                                                          |
| mdp                        | 1.65 sec                                                                       | 1.64 sec: 1.01x faster                                                         |
| deepcopy_reduce            | 2.37 us                                                                        | 2.35 us: 1.01x faster                                                          |
| sqlglot_transpile          | 1.19 ms                                                                        | 1.19 ms: 1.00x faster                                                          |
| sympy_expand               | 391 ms                                                                         | 389 ms: 1.00x faster                                                           |
| html5lib                   | 48.5 ms                                                                        | 48.6 ms: 1.00x slower                                                          |
| generators                 | 27.6 ms                                                                        | 27.7 ms: 1.00x slower                                                          |
| deepcopy                   | 237 us                                                                         | 238 us: 1.00x slower                                                           |
| sympy_integrate            | 15.9 ms                                                                        | 16.0 ms: 1.00x slower                                                          |
| logging_format             | 8.26 us                                                                        | 8.31 us: 1.01x slower                                                          |
| json_dumps                 | 6.83 ms                                                                        | 6.87 ms: 1.01x slower                                                          |
| django_template            | 33.9 ms                                                                        | 34.1 ms: 1.01x slower                                                          |
| deltablue                  | 2.75 ms                                                                        | 2.78 ms: 1.01x slower                                                          |
| nbody                      | 53.9 ms                                                                        | 54.4 ms: 1.01x slower                                                          |
| python_startup             | 24.8 ms                                                                        | 25.1 ms: 1.01x slower                                                          |
| thrift                     | 748 us                                                                         | 756 us: 1.01x slower                                                           |
| deepcopy_memo              | 15.6 us                                                                        | 15.8 us: 1.01x slower                                                          |
| pickle_pure_python         | 208 us                                                                         | 211 us: 1.01x slower                                                           |
| python_startup_no_site     | 20.7 ms                                                                        | 21.0 ms: 1.01x slower                                                          |
| logging_simple             | 7.54 us                                                                        | 7.65 us: 1.01x slower                                                          |
| pprint_safe_repr           | 575 ms                                                                         | 584 ms: 1.01x slower                                                           |
| logging_silent             | 57.5 ns                                                                        | 58.3 ns: 1.02x slower                                                          |
| pprint_pformat             | 1.18 sec                                                                       | 1.20 sec: 1.02x slower                                                         |
| float                      | 42.4 ms                                                                        | 43.1 ms: 1.02x slower                                                          |
| chaos                      | 55.0 ms                                                                        | 56.1 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 488 ms                                                                         | 498 ms: 1.02x slower                                                           |
| raytrace                   | 236 ms                                                                         | 241 ms: 1.02x slower                                                           |
| scimark_lu                 | 74.3 ms                                                                        | 75.9 ms: 1.02x slower                                                          |
| gc_traversal               | 1.43 ms                                                                        | 1.46 ms: 1.02x slower                                                          |
| scimark_fft                | 167 ms                                                                         | 170 ms: 1.02x slower                                                           |
| bench_mp_pool              | 74.5 ms                                                                        | 76.1 ms: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 2.42 ms                                                                        | 2.48 ms: 1.02x slower                                                          |
| scimark_sor                | 97.1 ms                                                                        | 99.5 ms: 1.02x slower                                                          |
| richards_super             | 38.3 ms                                                                        | 39.3 ms: 1.03x slower                                                          |
| spectral_norm              | 47.5 ms                                                                        | 49.0 ms: 1.03x slower                                                          |
| richards                   | 33.9 ms                                                                        | 35.2 ms: 1.04x slower                                                          |
| regex_dna                  | 124 ms                                                                         | 129 ms: 1.04x slower                                                           |
| asyncio_tcp                | 605 ms                                                                         | 629 ms: 1.04x slower                                                           |
| regex_effbot               | 1.99 ms                                                                        | 2.07 ms: 1.04x slower                                                          |
| unpickle_list              | 2.65 us                                                                        | 2.78 us: 1.05x slower                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                                         | 481 ms: 1.06x slower                                                           |
| json                       | 4.22 ms                                                                        | 4.52 ms: 1.07x slower                                                          |
| pickle_list                | 3.81 us                                                                        | 4.10 us: 1.08x slower                                                          |
| telco                      | 5.55 ms                                                                        | 6.04 ms: 1.09x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (32): pyflate, bench_thread_pool, async_generators, xml_etree_generate, create_gc_cycles, typing_runtime_protocols, 2to3, xml_etree_parse, tomli_loads, pickle_dict, meteor_contest, pidigits, json_loads, async_tree_io_tg, async_tree_memoization, sympy_sum, async_tree_io, sympy_str, docutils, asyncio_tcp_ssl, go, comprehensions, pickle, xml_etree_iterparse, pathlib, crypto_pyaes, regex_v8, pylint, async_tree_none, unpickle_pure_python, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 97.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown