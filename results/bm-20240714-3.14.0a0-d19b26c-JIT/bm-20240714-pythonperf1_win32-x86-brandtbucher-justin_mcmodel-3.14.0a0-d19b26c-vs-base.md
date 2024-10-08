# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 59.78%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib       | 46.5 ms                                                                        | 47.7 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 469 ms                                                                         | 475 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 458 ms                                                                         | 469 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 203 ms                                                                         | 196 ms: 1.04x faster                                                           |
| float          | 43.0 ms                                                                        | 43.2 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                                         | 117 ms: 1.09x faster                                                           |
| regex_v8       | 16.1 ms                                                                        | 16.0 ms: 1.01x faster                                                          |
| regex_compile  | 95.5 ms                                                                        | 96.0 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 150 us                                                                         | 147 us: 1.02x faster                                                           |
| json_dumps           | 7.25 ms                                                                        | 7.15 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 61.8 ms                                                                        | 61.4 ms: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                                         | 104 ms: 1.01x slower                                                           |
| tomli_loads          | 1.48 sec                                                                       | 1.51 sec: 1.02x slower                                                         |
| xml_etree_process    | 43.6 ms                                                                        | 44.4 ms: 1.02x slower                                                          |
| xml_etree_generate   | 59.8 ms                                                                        | 62.1 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 20.0 ms                                                                        | 19.1 ms: 1.05x faster                                                          |
| python_startup         | 23.7 ms                                                                        | 22.9 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                                          | 1.04x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.4 ms                                                                        | 22.6 ms: 1.03x faster                                                          |
| django_template | 33.7 ms                                                                        | 32.6 ms: 1.03x faster                                                          |
| genshi_xml      | 53.6 ms                                                                        | 53.2 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna                  | 127 ms                                                                         | 117 ms: 1.09x faster                                                           |
| richards_super             | 40.7 ms                                                                        | 38.6 ms: 1.06x faster                                                          |
| python_startup_no_site     | 20.0 ms                                                                        | 19.1 ms: 1.05x faster                                                          |
| bench_mp_pool              | 77.1 ms                                                                        | 73.6 ms: 1.05x faster                                                          |
| deepcopy_memo              | 15.8 us                                                                        | 15.2 us: 1.04x faster                                                          |
| pidigits                   | 203 ms                                                                         | 196 ms: 1.04x faster                                                           |
| async_generators           | 320 ms                                                                         | 308 ms: 1.04x faster                                                           |
| genshi_text                | 23.4 ms                                                                        | 22.6 ms: 1.03x faster                                                          |
| django_template            | 33.7 ms                                                                        | 32.6 ms: 1.03x faster                                                          |
| python_startup             | 23.7 ms                                                                        | 22.9 ms: 1.03x faster                                                          |
| hexiom                     | 4.69 ms                                                                        | 4.56 ms: 1.03x faster                                                          |
| comprehensions             | 11.5 us                                                                        | 11.2 us: 1.03x faster                                                          |
| thrift                     | 772 us                                                                         | 753 us: 1.03x faster                                                           |
| nqueens                    | 74.0 ms                                                                        | 72.2 ms: 1.02x faster                                                          |
| scimark_lu                 | 79.7 ms                                                                        | 77.8 ms: 1.02x faster                                                          |
| unpickle_pure_python       | 150 us                                                                         | 147 us: 1.02x faster                                                           |
| logging_silent             | 58.5 ns                                                                        | 57.3 ns: 1.02x faster                                                          |
| meteor_contest             | 76.3 ms                                                                        | 74.6 ms: 1.02x faster                                                          |
| coverage                   | 52.1 ms                                                                        | 51.1 ms: 1.02x faster                                                          |
| richards                   | 33.4 ms                                                                        | 32.9 ms: 1.01x faster                                                          |
| json_dumps                 | 7.25 ms                                                                        | 7.15 ms: 1.01x faster                                                          |
| crypto_pyaes               | 48.9 ms                                                                        | 48.3 ms: 1.01x faster                                                          |
| generators                 | 27.9 ms                                                                        | 27.6 ms: 1.01x faster                                                          |
| telco                      | 5.70 ms                                                                        | 5.64 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 565 ms                                                                         | 560 ms: 1.01x faster                                                           |
| genshi_xml                 | 53.6 ms                                                                        | 53.2 ms: 1.01x faster                                                          |
| sqlglot_parse              | 949 us                                                                         | 941 us: 1.01x faster                                                           |
| sympy_integrate            | 16.0 ms                                                                        | 15.9 ms: 1.01x faster                                                          |
| regex_v8                   | 16.1 ms                                                                        | 16.0 ms: 1.01x faster                                                          |
| gc_traversal               | 1.44 ms                                                                        | 1.43 ms: 1.01x faster                                                          |
| xml_etree_iterparse        | 61.8 ms                                                                        | 61.4 ms: 1.01x faster                                                          |
| deltablue                  | 2.76 ms                                                                        | 2.74 ms: 1.01x faster                                                          |
| coroutines                 | 17.7 ms                                                                        | 17.8 ms: 1.00x slower                                                          |
| sqlglot_normalize          | 235 ms                                                                         | 236 ms: 1.00x slower                                                           |
| regex_compile              | 95.5 ms                                                                        | 96.0 ms: 1.00x slower                                                          |
| xml_etree_parse            | 104 ms                                                                         | 104 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 43.5 ms                                                                        | 43.7 ms: 1.01x slower                                                          |
| float                      | 43.0 ms                                                                        | 43.2 ms: 1.01x slower                                                          |
| scimark_fft                | 167 ms                                                                         | 168 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.21 ms                                                                        | 1.21 ms: 1.01x slower                                                          |
| logging_format             | 7.99 us                                                                        | 8.05 us: 1.01x slower                                                          |
| sympy_sum                  | 109 ms                                                                         | 109 ms: 1.01x slower                                                           |
| spectral_norm              | 47.7 ms                                                                        | 48.2 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 151 us                                                                         | 153 us: 1.01x slower                                                           |
| logging_simple             | 7.31 us                                                                        | 7.40 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 469 ms                                                                         | 475 ms: 1.01x slower                                                           |
| tomli_loads                | 1.48 sec                                                                       | 1.51 sec: 1.02x slower                                                         |
| xml_etree_process          | 43.6 ms                                                                        | 44.4 ms: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 2.41 ms                                                                        | 2.45 ms: 1.02x slower                                                          |
| chaos                      | 52.4 ms                                                                        | 53.5 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 458 ms                                                                         | 469 ms: 1.02x slower                                                           |
| html5lib                   | 46.5 ms                                                                        | 47.7 ms: 1.03x slower                                                          |
| raytrace                   | 227 ms                                                                         | 233 ms: 1.03x slower                                                           |
| mdp                        | 1.66 sec                                                                       | 1.72 sec: 1.04x slower                                                         |
| xml_etree_generate         | 59.8 ms                                                                        | 62.1 ms: 1.04x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (32): asyncio_tcp, docutils, pickle_pure_python, pyflate, regex_effbot, tornado_http, nbody, 2to3, async_tree_io_tg, scimark_sor, mako, pprint_pformat, deepcopy, pycparser, async_tree_io, sympy_expand, scimark_monte_carlo, json_loads, pylint, pathlib, create_gc_cycles, sympy_str, go, asyncio_tcp_ssl, deepcopy_reduce, bench_thread_pool, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, fannkuch, json

# HPT report

- Reliability score: 59.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown