# Results vs. base

- fork: brandtbucher
- ref: justin_plt
- machine: windows-x86
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                          | 262 ms: 1.01x slower                                                        |
| chameleon      | 5.59 ms                                                                         | 5.91 ms: 1.06x slower                                                       |
| docutils       | 1.82 sec                                                                        | 1.87 sec: 1.03x slower                                                      |
| html5lib       | 44.8 ms                                                                         | 46.4 ms: 1.04x slower                                                       |
| tornado_http   | 96.0 ms                                                                         | 98.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                           | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 519 ms                                                                          | 498 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 532 ms                                                                          | 510 ms: 1.04x faster                                                        |
| async_tree_none_tg         | 243 ms                                                                          | 245 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 304 ms                                                                          | 307 ms: 1.01x slower                                                        |
| async_tree_io              | 616 ms                                                                          | 623 ms: 1.01x slower                                                        |
| async_tree_none            | 257 ms                                                                          | 261 ms: 1.01x slower                                                        |
| async_tree_io_tg           | 597 ms                                                                          | 608 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                          | 199 ms: 1.01x faster                                                        |
| float          | 53.8 ms                                                                         | 54.7 ms: 1.02x slower                                                       |
| nbody          | 96.2 ms                                                                         | 98.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 15.9 ms                                                                         | 16.2 ms: 1.02x slower                                                       |
| regex_compile  | 108 ms                                                                          | 112 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 2.98 us                                                                         | 2.88 us: 1.03x faster                                                       |
| pickle_list          | 3.22 us                                                                         | 3.19 us: 1.01x faster                                                       |
| json_loads           | 20.0 us                                                                         | 20.1 us: 1.01x slower                                                       |
| json_dumps           | 6.86 ms                                                                         | 6.98 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.6 ms                                                                         | 67.0 ms: 1.02x slower                                                       |
| pickle               | 7.83 us                                                                         | 8.02 us: 1.02x slower                                                       |
| unpickle             | 9.93 us                                                                         | 10.2 us: 1.03x slower                                                       |
| tomli_loads          | 1.66 sec                                                                        | 1.71 sec: 1.03x slower                                                      |
| pickle_pure_python   | 210 us                                                                          | 224 us: 1.06x slower                                                        |
| xml_etree_process    | 42.4 ms                                                                         | 45.2 ms: 1.07x slower                                                       |
| xml_etree_generate   | 59.9 ms                                                                         | 64.0 ms: 1.07x slower                                                       |
| unpickle_pure_python | 162 us                                                                          | 174 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 26.1 ms                                                                         | 25.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 22.8 ms                                                                         | 23.4 ms: 1.03x slower                                                       |
| genshi_xml      | 49.0 ms                                                                         | 50.9 ms: 1.04x slower                                                       |
| django_template | 29.1 ms                                                                         | 31.7 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240313-pythonperf1_win32-x86-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 519 ms                                                                          | 498 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 532 ms                                                                          | 510 ms: 1.04x faster                                                        |
| unpickle_list              | 2.98 us                                                                         | 2.88 us: 1.03x faster                                                       |
| sqlite_synth               | 1.94 us                                                                         | 1.89 us: 1.02x faster                                                       |
| pidigits                   | 201 ms                                                                          | 199 ms: 1.01x faster                                                        |
| python_startup             | 26.1 ms                                                                         | 25.8 ms: 1.01x faster                                                       |
| crypto_pyaes               | 60.9 ms                                                                         | 60.2 ms: 1.01x faster                                                       |
| pickle_list                | 3.22 us                                                                         | 3.19 us: 1.01x faster                                                       |
| unpack_sequence            | 44.4 ns                                                                         | 44.0 ns: 1.01x faster                                                       |
| async_generators           | 291 ms                                                                          | 292 ms: 1.00x slower                                                        |
| coverage                   | 486 ms                                                                          | 489 ms: 1.01x slower                                                        |
| pyflate                    | 375 ms                                                                          | 377 ms: 1.01x slower                                                        |
| json_loads                 | 20.0 us                                                                         | 20.1 us: 1.01x slower                                                       |
| meteor_contest             | 82.3 ms                                                                         | 82.9 ms: 1.01x slower                                                       |
| thrift                     | 10.8 ms                                                                         | 10.9 ms: 1.01x slower                                                       |
| json                       | 4.17 ms                                                                         | 4.21 ms: 1.01x slower                                                       |
| async_tree_none_tg         | 243 ms                                                                          | 245 ms: 1.01x slower                                                        |
| comprehensions             | 14.7 us                                                                         | 14.9 us: 1.01x slower                                                       |
| async_tree_memoization_tg  | 304 ms                                                                          | 307 ms: 1.01x slower                                                        |
| gc_traversal               | 1.40 ms                                                                         | 1.42 ms: 1.01x slower                                                       |
| 2to3                       | 259 ms                                                                          | 262 ms: 1.01x slower                                                        |
| fannkuch                   | 334 ms                                                                          | 338 ms: 1.01x slower                                                        |
| async_tree_io              | 616 ms                                                                          | 623 ms: 1.01x slower                                                        |
| hexiom                     | 6.04 ms                                                                         | 6.12 ms: 1.01x slower                                                       |
| logging_format             | 8.83 us                                                                         | 8.96 us: 1.01x slower                                                       |
| async_tree_none            | 257 ms                                                                          | 261 ms: 1.01x slower                                                        |
| pycparser                  | 865 ms                                                                          | 878 ms: 1.01x slower                                                        |
| regex_v8                   | 15.9 ms                                                                         | 16.2 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 734 ms                                                                          | 746 ms: 1.02x slower                                                        |
| spectral_norm              | 72.0 ms                                                                         | 73.2 ms: 1.02x slower                                                       |
| logging_simple             | 8.17 us                                                                         | 8.31 us: 1.02x slower                                                       |
| float                      | 53.8 ms                                                                         | 54.7 ms: 1.02x slower                                                       |
| json_dumps                 | 6.86 ms                                                                         | 6.98 ms: 1.02x slower                                                       |
| scimark_fft                | 233 ms                                                                          | 237 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 597 ms                                                                          | 608 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.49 sec                                                                        | 1.52 sec: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.6 ms                                                                         | 67.0 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 62.5 ms                                                                         | 64.0 ms: 1.02x slower                                                       |
| pickle                     | 7.83 us                                                                         | 8.02 us: 1.02x slower                                                       |
| tornado_http               | 96.0 ms                                                                         | 98.4 ms: 1.02x slower                                                       |
| docutils                   | 1.82 sec                                                                        | 1.87 sec: 1.03x slower                                                      |
| nbody                      | 96.2 ms                                                                         | 98.8 ms: 1.03x slower                                                       |
| unpickle                   | 9.93 us                                                                         | 10.2 us: 1.03x slower                                                       |
| tomli_loads                | 1.66 sec                                                                        | 1.71 sec: 1.03x slower                                                      |
| genshi_text                | 22.8 ms                                                                         | 23.4 ms: 1.03x slower                                                       |
| nqueens                    | 92.1 ms                                                                         | 95.0 ms: 1.03x slower                                                       |
| html5lib                   | 44.8 ms                                                                         | 46.4 ms: 1.04x slower                                                       |
| chaos                      | 57.1 ms                                                                         | 59.1 ms: 1.04x slower                                                       |
| pylint                     | 227 ms                                                                          | 235 ms: 1.04x slower                                                        |
| regex_compile              | 108 ms                                                                          | 112 ms: 1.04x slower                                                        |
| telco                      | 6.37 ms                                                                         | 6.62 ms: 1.04x slower                                                       |
| genshi_xml                 | 49.0 ms                                                                         | 50.9 ms: 1.04x slower                                                       |
| go                         | 120 ms                                                                          | 125 ms: 1.04x slower                                                        |
| deepcopy                   | 279 us                                                                          | 291 us: 1.04x slower                                                        |
| coroutines                 | 14.3 ms                                                                         | 15.0 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 2.48 us                                                                         | 2.60 us: 1.05x slower                                                       |
| sqlglot_optimize           | 45.6 ms                                                                         | 48.0 ms: 1.05x slower                                                       |
| mdp                        | 1.68 sec                                                                        | 1.76 sec: 1.05x slower                                                      |
| sympy_sum                  | 107 ms                                                                          | 112 ms: 1.05x slower                                                        |
| sympy_expand               | 369 ms                                                                          | 388 ms: 1.05x slower                                                        |
| sympy_str                  | 209 ms                                                                          | 220 ms: 1.05x slower                                                        |
| chameleon                  | 5.59 ms                                                                         | 5.91 ms: 1.06x slower                                                       |
| sympy_integrate            | 15.1 ms                                                                         | 16.0 ms: 1.06x slower                                                       |
| scimark_lu                 | 84.1 ms                                                                         | 88.9 ms: 1.06x slower                                                       |
| richards                   | 34.0 ms                                                                         | 36.0 ms: 1.06x slower                                                       |
| sqlglot_transpile          | 1.19 ms                                                                         | 1.27 ms: 1.06x slower                                                       |
| pickle_pure_python         | 210 us                                                                          | 224 us: 1.06x slower                                                        |
| richards_super             | 38.3 ms                                                                         | 40.8 ms: 1.07x slower                                                       |
| xml_etree_process          | 42.4 ms                                                                         | 45.2 ms: 1.07x slower                                                       |
| sqlglot_parse              | 944 us                                                                          | 1.01 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 93.0 us                                                                         | 99.4 us: 1.07x slower                                                       |
| xml_etree_generate         | 59.9 ms                                                                         | 64.0 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 162 us                                                                          | 174 us: 1.07x slower                                                        |
| deltablue                  | 2.51 ms                                                                         | 2.69 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 224 ms                                                                          | 241 ms: 1.07x slower                                                        |
| generators                 | 22.5 ms                                                                         | 24.3 ms: 1.08x slower                                                       |
| django_template            | 29.1 ms                                                                         | 31.7 ms: 1.09x slower                                                       |
| deepcopy_memo              | 24.6 us                                                                         | 27.1 us: 1.10x slower                                                       |
| scimark_sor                | 95.6 ms                                                                         | 106 ms: 1.11x slower                                                        |
| logging_silent             | 61.2 ns                                                                         | 67.8 ns: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                                           | 1.03x slower                                                                |

Benchmark hidden because not significant (15): raytrace, asyncio_tcp_ssl, regex_effbot, regex_dna, xml_etree_parse, pathlib, scimark_sparse_mat_mult, python_startup_no_site, pickle_dict, create_gc_cycles, mako, bench_mp_pool, async_tree_memoization, asyncio_tcp, bench_thread_pool


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: unknown