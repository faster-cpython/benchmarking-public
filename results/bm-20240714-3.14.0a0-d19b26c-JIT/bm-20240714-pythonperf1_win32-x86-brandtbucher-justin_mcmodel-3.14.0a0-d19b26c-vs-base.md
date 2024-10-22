# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.00x faster
- HPT reliability: 77.79%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                         | 254 ms: 1.01x slower                                                           |
| docutils       | 1.93 sec                                                                       | 1.92 sec: 1.01x faster                                                         |
| html5lib       | 46.8 ms                                                                        | 47.7 ms: 1.02x slower                                                          |
| tornado_http   | 98.3 ms                                                                        | 97.7 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 475 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 469 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 44.1 ms                                                                        | 43.2 ms: 1.02x faster                                                          |
| nbody          | 55.7 ms                                                                        | 54.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                         | 117 ms: 1.05x faster                                                           |
| regex_compile  | 95.0 ms                                                                        | 96.0 ms: 1.01x slower                                                          |
| regex_v8       | 15.8 ms                                                                        | 16.0 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 148 us                                                                         | 147 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 61.8 ms                                                                        | 61.4 ms: 1.01x faster                                                          |
| xml_etree_process    | 44.0 ms                                                                        | 44.4 ms: 1.01x slower                                                          |
| json_loads           | 21.3 us                                                                        | 21.6 us: 1.01x slower                                                          |
| tomli_loads          | 1.48 sec                                                                       | 1.51 sec: 1.02x slower                                                         |
| xml_etree_generate   | 60.9 ms                                                                        | 62.1 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 23.2 ms                                                                        | 22.9 ms: 1.01x faster                                                          |
| python_startup_no_site | 19.3 ms                                                                        | 19.1 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                                          | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 22.8 ms                                                                        | 22.6 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| telco                      | 5.92 ms                                                                        | 5.64 ms: 1.05x faster                                                          |
| regex_dna                  | 123 ms                                                                         | 117 ms: 1.05x faster                                                           |
| async_generators           | 317 ms                                                                         | 308 ms: 1.03x faster                                                           |
| logging_silent             | 58.6 ns                                                                        | 57.3 ns: 1.02x faster                                                          |
| logging_simple             | 7.55 us                                                                        | 7.40 us: 1.02x faster                                                          |
| float                      | 44.1 ms                                                                        | 43.2 ms: 1.02x faster                                                          |
| crypto_pyaes               | 49.2 ms                                                                        | 48.3 ms: 1.02x faster                                                          |
| sqlglot_normalize          | 241 ms                                                                         | 236 ms: 1.02x faster                                                           |
| deepcopy_memo              | 15.5 us                                                                        | 15.2 us: 1.02x faster                                                          |
| sympy_expand               | 392 ms                                                                         | 385 ms: 1.02x faster                                                           |
| sqlglot_parse              | 958 us                                                                         | 941 us: 1.02x faster                                                           |
| scimark_sor                | 102 ms                                                                         | 100 ms: 1.02x faster                                                           |
| nbody                      | 55.7 ms                                                                        | 54.9 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                                        | 1.43 ms: 1.01x faster                                                          |
| comprehensions             | 11.4 us                                                                        | 11.2 us: 1.01x faster                                                          |
| nqueens                    | 73.2 ms                                                                        | 72.2 ms: 1.01x faster                                                          |
| pathlib                    | 83.3 ms                                                                        | 82.3 ms: 1.01x faster                                                          |
| pycparser                  | 844 ms                                                                         | 834 ms: 1.01x faster                                                           |
| logging_format             | 8.13 us                                                                        | 8.05 us: 1.01x faster                                                          |
| python_startup             | 23.2 ms                                                                        | 22.9 ms: 1.01x faster                                                          |
| python_startup_no_site     | 19.3 ms                                                                        | 19.1 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 148 us                                                                         | 147 us: 1.01x faster                                                           |
| chaos                      | 54.0 ms                                                                        | 53.5 ms: 1.01x faster                                                          |
| deepcopy                   | 239 us                                                                         | 237 us: 1.01x faster                                                           |
| raytrace                   | 235 ms                                                                         | 233 ms: 1.01x faster                                                           |
| richards_super             | 38.9 ms                                                                        | 38.6 ms: 1.01x faster                                                          |
| sqlglot_optimize           | 44.1 ms                                                                        | 43.7 ms: 1.01x faster                                                          |
| coroutines                 | 17.9 ms                                                                        | 17.8 ms: 1.01x faster                                                          |
| hexiom                     | 4.60 ms                                                                        | 4.56 ms: 1.01x faster                                                          |
| xml_etree_iterparse        | 61.8 ms                                                                        | 61.4 ms: 1.01x faster                                                          |
| generators                 | 27.7 ms                                                                        | 27.6 ms: 1.01x faster                                                          |
| sympy_str                  | 219 ms                                                                         | 217 ms: 1.01x faster                                                           |
| docutils                   | 1.93 sec                                                                       | 1.92 sec: 1.01x faster                                                         |
| genshi_text                | 22.8 ms                                                                        | 22.6 ms: 1.01x faster                                                          |
| tornado_http               | 98.3 ms                                                                        | 97.7 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 1.22 ms                                                                        | 1.21 ms: 1.00x faster                                                          |
| coverage                   | 51.3 ms                                                                        | 51.1 ms: 1.00x faster                                                          |
| sympy_integrate            | 15.9 ms                                                                        | 15.9 ms: 1.00x faster                                                          |
| go                         | 112 ms                                                                         | 113 ms: 1.00x slower                                                           |
| 2to3                       | 252 ms                                                                         | 254 ms: 1.01x slower                                                           |
| thrift                     | 747 us                                                                         | 753 us: 1.01x slower                                                           |
| xml_etree_process          | 44.0 ms                                                                        | 44.4 ms: 1.01x slower                                                          |
| regex_compile              | 95.0 ms                                                                        | 96.0 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 475 ms: 1.01x slower                                                           |
| regex_v8                   | 15.8 ms                                                                        | 16.0 ms: 1.01x slower                                                          |
| json_loads                 | 21.3 us                                                                        | 21.6 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 469 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 552 ms                                                                         | 560 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.14 sec                                                                       | 1.15 sec: 1.02x slower                                                         |
| richards                   | 32.4 ms                                                                        | 32.9 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 41.2 ms                                                                        | 41.9 ms: 1.02x slower                                                          |
| tomli_loads                | 1.48 sec                                                                       | 1.51 sec: 1.02x slower                                                         |
| html5lib                   | 46.8 ms                                                                        | 47.7 ms: 1.02x slower                                                          |
| xml_etree_generate         | 60.9 ms                                                                        | 62.1 ms: 1.02x slower                                                          |
| spectral_norm              | 47.3 ms                                                                        | 48.2 ms: 1.02x slower                                                          |
| scimark_fft                | 165 ms                                                                         | 168 ms: 1.02x slower                                                           |
| mdp                        | 1.66 sec                                                                       | 1.72 sec: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 2.36 ms                                                                        | 2.45 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 145 us                                                                         | 153 us: 1.06x slower                                                           |
| json                       | 4.20 ms                                                                        | 4.56 ms: 1.08x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (27): asyncio_tcp, async_tree_io_tg, async_tree_memoization, pylint, bench_thread_pool, async_tree_io, deepcopy_reduce, bench_mp_pool, scimark_lu, django_template, async_tree_none, regex_effbot, genshi_xml, meteor_contest, json_dumps, asyncio_tcp_ssl, mako, pidigits, async_tree_none_tg, deltablue, sympy_sum, xml_etree_parse, async_tree_memoization_tg, create_gc_cycles, pickle_pure_python, pyflate, fannkuch

# HPT report

- Reliability score: 77.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown