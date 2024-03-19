# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-x86
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.00x faster
- HPT reliability: 61.67%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                          | 255 ms: 1.01x faster                                                                  |
| chameleon      | 5.67 ms                                                                         | 5.84 ms: 1.03x slower                                                                 |
| docutils       | 1.83 sec                                                                        | 1.81 sec: 1.01x faster                                                                |
| html5lib       | 46.0 ms                                                                         | 44.9 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 241 ms                                                                          | 242 ms: 1.01x slower                                                                  |
| async_tree_memoization_tg  | 302 ms                                                                          | 306 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed    | 507 ms                                                                          | 519 ms: 1.02x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                          | 505 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                                           | 1.01x slower                                                                          |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                          | 199 ms: 1.01x slower                                                                  |
| nbody          | 95.1 ms                                                                         | 95.9 ms: 1.01x slower                                                                 |
| float          | 53.9 ms                                                                         | 55.4 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                          | 121 ms: 1.01x faster                                                                  |
| regex_compile  | 109 ms                                                                          | 108 ms: 1.01x faster                                                                  |
| regex_v8       | 16.0 ms                                                                         | 16.2 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle             | 10.2 us                                                                         | 9.96 us: 1.02x faster                                                                 |
| tomli_loads          | 1.71 sec                                                                        | 1.68 sec: 1.02x faster                                                                |
| unpickle_pure_python | 167 us                                                                          | 164 us: 1.01x faster                                                                  |
| pickle_dict          | 20.0 us                                                                         | 19.8 us: 1.01x faster                                                                 |
| xml_etree_iterparse  | 67.4 ms                                                                         | 67.0 ms: 1.01x faster                                                                 |
| pickle_pure_python   | 210 us                                                                          | 209 us: 1.01x faster                                                                  |
| xml_etree_process    | 42.7 ms                                                                         | 42.8 ms: 1.00x slower                                                                 |
| json_loads           | 19.8 us                                                                         | 19.8 us: 1.00x slower                                                                 |
| xml_etree_generate   | 61.7 ms                                                                         | 62.0 ms: 1.01x slower                                                                 |
| unpickle_list        | 2.88 us                                                                         | 2.93 us: 1.02x slower                                                                 |
| pickle               | 7.89 us                                                                         | 8.03 us: 1.02x slower                                                                 |
| json_dumps           | 6.91 ms                                                                         | 7.07 ms: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 26.4 ms                                                                         | 25.1 ms: 1.05x faster                                                                 |
| python_startup_no_site | 23.9 ms                                                                         | 23.0 ms: 1.04x faster                                                                 |
| Geometric mean         | (ref)                                                                           | 1.04x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                                         | 21.8 ms: 1.04x faster                                                                 |
| django_template | 30.0 ms                                                                         | 29.1 ms: 1.03x faster                                                                 |
| genshi_xml      | 49.7 ms                                                                         | 48.5 ms: 1.03x faster                                                                 |
| mako            | 6.94 ms                                                                         | 7.00 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                                           | 1.02x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup             | 26.4 ms                                                                         | 25.1 ms: 1.05x faster                                                                 |
| genshi_text                | 22.7 ms                                                                         | 21.8 ms: 1.04x faster                                                                 |
| go                         | 123 ms                                                                          | 118 ms: 1.04x faster                                                                  |
| python_startup_no_site     | 23.9 ms                                                                         | 23.0 ms: 1.04x faster                                                                 |
| richards_super             | 39.0 ms                                                                         | 37.7 ms: 1.04x faster                                                                 |
| django_template            | 30.0 ms                                                                         | 29.1 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult    | 3.20 ms                                                                         | 3.11 ms: 1.03x faster                                                                 |
| logging_simple             | 8.21 us                                                                         | 7.98 us: 1.03x faster                                                                 |
| richards                   | 34.7 ms                                                                         | 33.8 ms: 1.03x faster                                                                 |
| scimark_lu                 | 84.3 ms                                                                         | 82.1 ms: 1.03x faster                                                                 |
| genshi_xml                 | 49.7 ms                                                                         | 48.5 ms: 1.03x faster                                                                 |
| html5lib                   | 46.0 ms                                                                         | 44.9 ms: 1.02x faster                                                                 |
| deltablue                  | 2.55 ms                                                                         | 2.49 ms: 1.02x faster                                                                 |
| logging_format             | 8.82 us                                                                         | 8.62 us: 1.02x faster                                                                 |
| pycparser                  | 860 ms                                                                          | 841 ms: 1.02x faster                                                                  |
| unpickle                   | 10.2 us                                                                         | 9.96 us: 1.02x faster                                                                 |
| tomli_loads                | 1.71 sec                                                                        | 1.68 sec: 1.02x faster                                                                |
| bench_mp_pool              | 74.6 ms                                                                         | 73.2 ms: 1.02x faster                                                                 |
| logging_silent             | 61.1 ns                                                                         | 60.0 ns: 1.02x faster                                                                 |
| unpickle_pure_python       | 167 us                                                                          | 164 us: 1.01x faster                                                                  |
| coroutines                 | 14.2 ms                                                                         | 14.0 ms: 1.01x faster                                                                 |
| 2to3                       | 258 ms                                                                          | 255 ms: 1.01x faster                                                                  |
| scimark_fft                | 239 ms                                                                          | 236 ms: 1.01x faster                                                                  |
| docutils                   | 1.83 sec                                                                        | 1.81 sec: 1.01x faster                                                                |
| sympy_integrate            | 15.4 ms                                                                         | 15.3 ms: 1.01x faster                                                                 |
| pickle_dict                | 20.0 us                                                                         | 19.8 us: 1.01x faster                                                                 |
| regex_dna                  | 122 ms                                                                          | 121 ms: 1.01x faster                                                                  |
| regex_compile              | 109 ms                                                                          | 108 ms: 1.01x faster                                                                  |
| comprehensions             | 14.7 us                                                                         | 14.6 us: 1.01x faster                                                                 |
| spectral_norm              | 72.2 ms                                                                         | 71.7 ms: 1.01x faster                                                                 |
| hexiom                     | 6.04 ms                                                                         | 5.99 ms: 1.01x faster                                                                 |
| sympy_sum                  | 108 ms                                                                          | 107 ms: 1.01x faster                                                                  |
| xml_etree_iterparse        | 67.4 ms                                                                         | 67.0 ms: 1.01x faster                                                                 |
| pickle_pure_python         | 210 us                                                                          | 209 us: 1.01x faster                                                                  |
| sympy_str                  | 212 ms                                                                          | 211 ms: 1.01x faster                                                                  |
| sqlglot_normalize          | 227 ms                                                                          | 226 ms: 1.00x faster                                                                  |
| sympy_expand               | 370 ms                                                                          | 370 ms: 1.00x faster                                                                  |
| xml_etree_process          | 42.7 ms                                                                         | 42.8 ms: 1.00x slower                                                                 |
| json_loads                 | 19.8 us                                                                         | 19.8 us: 1.00x slower                                                                 |
| meteor_contest             | 82.2 ms                                                                         | 82.7 ms: 1.01x slower                                                                 |
| xml_etree_generate         | 61.7 ms                                                                         | 62.0 ms: 1.01x slower                                                                 |
| async_tree_none_tg         | 241 ms                                                                          | 242 ms: 1.01x slower                                                                  |
| sqlglot_optimize           | 46.4 ms                                                                         | 46.7 ms: 1.01x slower                                                                 |
| pidigits                   | 198 ms                                                                          | 199 ms: 1.01x slower                                                                  |
| sqlite_synth               | 1.93 us                                                                         | 1.94 us: 1.01x slower                                                                 |
| scimark_monte_carlo        | 63.0 ms                                                                         | 63.4 ms: 1.01x slower                                                                 |
| regex_v8                   | 16.0 ms                                                                         | 16.2 ms: 1.01x slower                                                                 |
| mako                       | 6.94 ms                                                                         | 7.00 ms: 1.01x slower                                                                 |
| pprint_safe_repr           | 722 ms                                                                          | 728 ms: 1.01x slower                                                                  |
| nbody                      | 95.1 ms                                                                         | 95.9 ms: 1.01x slower                                                                 |
| async_generators           | 297 ms                                                                          | 300 ms: 1.01x slower                                                                  |
| deepcopy_memo              | 24.2 us                                                                         | 24.4 us: 1.01x slower                                                                 |
| mdp                        | 1.71 sec                                                                        | 1.73 sec: 1.01x slower                                                                |
| raytrace                   | 266 ms                                                                          | 269 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.21 ms                                                                         | 1.22 ms: 1.01x slower                                                                 |
| coverage                   | 495 ms                                                                          | 501 ms: 1.01x slower                                                                  |
| sqlglot_parse              | 960 us                                                                          | 972 us: 1.01x slower                                                                  |
| typing_runtime_protocols   | 96.4 us                                                                         | 97.7 us: 1.01x slower                                                                 |
| async_tree_memoization_tg  | 302 ms                                                                          | 306 ms: 1.01x slower                                                                  |
| unpickle_list              | 2.88 us                                                                         | 2.93 us: 1.02x slower                                                                 |
| pickle                     | 7.89 us                                                                         | 8.03 us: 1.02x slower                                                                 |
| chaos                      | 58.8 ms                                                                         | 60.1 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed    | 507 ms                                                                          | 519 ms: 1.02x slower                                                                  |
| json_dumps                 | 6.91 ms                                                                         | 7.07 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                          | 505 ms: 1.02x slower                                                                  |
| json                       | 4.08 ms                                                                         | 4.19 ms: 1.03x slower                                                                 |
| float                      | 53.9 ms                                                                         | 55.4 ms: 1.03x slower                                                                 |
| chameleon                  | 5.67 ms                                                                         | 5.84 ms: 1.03x slower                                                                 |
| scimark_sor                | 94.8 ms                                                                         | 97.7 ms: 1.03x slower                                                                 |
| unpack_sequence            | 43.7 ns                                                                         | 45.2 ns: 1.03x slower                                                                 |
| telco                      | 6.33 ms                                                                         | 6.57 ms: 1.04x slower                                                                 |
| nqueens                    | 90.0 ms                                                                         | 94.1 ms: 1.05x slower                                                                 |
| fannkuch                   | 324 ms                                                                          | 342 ms: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                          |

Benchmark hidden because not significant (22): deepcopy_reduce, create_gc_cycles, tornado_http, pylint, async_tree_io_tg, async_tree_io, gc_traversal, pprint_pformat, generators, xml_etree_parse, crypto_pyaes, pickle_list, asyncio_tcp_ssl, async_tree_memoization, regex_effbot, pathlib, thrift, pyflate, deepcopy, async_tree_none, asyncio_tcp, bench_thread_pool


# HPT report

- Reliability score: 61.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown