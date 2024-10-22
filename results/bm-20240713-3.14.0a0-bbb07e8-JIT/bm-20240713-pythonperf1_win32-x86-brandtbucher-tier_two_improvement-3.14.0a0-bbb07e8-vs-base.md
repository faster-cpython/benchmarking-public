# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-x86
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 95.47%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.93 sec                                                                       | 1.91 sec: 1.01x faster                                                               |
| html5lib       | 46.8 ms                                                                        | 47.5 ms: 1.01x slower                                                                |
| tornado_http   | 98.3 ms                                                                        | 97.0 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 470 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 482 ms: 1.02x slower                                                                 |
| Geometric mean             | (ref)                                                                          | 1.00x slower                                                                         |

Benchmark hidden because not significant (6): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 44.1 ms                                                                        | 43.0 ms: 1.03x faster                                                                |
| nbody          | 55.7 ms                                                                        | 61.2 ms: 1.10x slower                                                                |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                         | 118 ms: 1.04x faster                                                                 |
| regex_compile  | 95.0 ms                                                                        | 94.4 ms: 1.01x faster                                                                |
| regex_v8       | 15.8 ms                                                                        | 15.7 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_generate   | 60.9 ms                                                                        | 58.1 ms: 1.05x faster                                                                |
| unpickle_pure_python | 148 us                                                                         | 146 us: 1.01x faster                                                                 |
| xml_etree_process    | 44.0 ms                                                                        | 43.4 ms: 1.01x faster                                                                |
| tomli_loads          | 1.48 sec                                                                       | 1.49 sec: 1.01x slower                                                               |
| json_loads           | 21.3 us                                                                        | 21.7 us: 1.02x slower                                                                |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                                         |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 5.44 ms                                                                        | 5.39 ms: 1.01x faster                                                                |
| genshi_xml      | 53.2 ms                                                                        | 52.9 ms: 1.01x faster                                                                |
| genshi_text     | 22.8 ms                                                                        | 22.9 ms: 1.01x slower                                                                |
| django_template | 32.6 ms                                                                        | 33.6 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                                          | 1.01x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| generators                 | 27.7 ms                                                                        | 25.5 ms: 1.09x faster                                                                |
| meteor_contest             | 74.6 ms                                                                        | 70.1 ms: 1.06x faster                                                                |
| pyflate                    | 278 ms                                                                         | 263 ms: 1.06x faster                                                                 |
| telco                      | 5.92 ms                                                                        | 5.60 ms: 1.06x faster                                                                |
| crypto_pyaes               | 49.2 ms                                                                        | 46.8 ms: 1.05x faster                                                                |
| xml_etree_generate         | 60.9 ms                                                                        | 58.1 ms: 1.05x faster                                                                |
| coroutines                 | 17.9 ms                                                                        | 17.1 ms: 1.05x faster                                                                |
| regex_dna                  | 123 ms                                                                         | 118 ms: 1.04x faster                                                                 |
| sqlglot_normalize          | 241 ms                                                                         | 232 ms: 1.04x faster                                                                 |
| sympy_expand               | 392 ms                                                                         | 379 ms: 1.04x faster                                                                 |
| float                      | 44.1 ms                                                                        | 43.0 ms: 1.03x faster                                                                |
| deltablue                  | 2.73 ms                                                                        | 2.67 ms: 1.03x faster                                                                |
| raytrace                   | 235 ms                                                                         | 229 ms: 1.02x faster                                                                 |
| pycparser                  | 844 ms                                                                         | 826 ms: 1.02x faster                                                                 |
| sympy_str                  | 219 ms                                                                         | 214 ms: 1.02x faster                                                                 |
| sqlglot_optimize           | 44.1 ms                                                                        | 43.1 ms: 1.02x faster                                                                |
| logging_silent             | 58.6 ns                                                                        | 57.4 ns: 1.02x faster                                                                |
| scimark_sor                | 102 ms                                                                         | 99.9 ms: 1.02x faster                                                                |
| richards_super             | 38.9 ms                                                                        | 38.2 ms: 1.02x faster                                                                |
| sqlglot_parse              | 958 us                                                                         | 942 us: 1.02x faster                                                                 |
| logging_simple             | 7.55 us                                                                        | 7.44 us: 1.02x faster                                                                |
| sympy_sum                  | 109 ms                                                                         | 108 ms: 1.02x faster                                                                 |
| unpickle_pure_python       | 148 us                                                                         | 146 us: 1.01x faster                                                                 |
| comprehensions             | 11.4 us                                                                        | 11.2 us: 1.01x faster                                                                |
| mdp                        | 1.66 sec                                                                       | 1.64 sec: 1.01x faster                                                               |
| tornado_http               | 98.3 ms                                                                        | 97.0 ms: 1.01x faster                                                                |
| xml_etree_process          | 44.0 ms                                                                        | 43.4 ms: 1.01x faster                                                                |
| chaos                      | 54.0 ms                                                                        | 53.3 ms: 1.01x faster                                                                |
| docutils                   | 1.93 sec                                                                       | 1.91 sec: 1.01x faster                                                               |
| mako                       | 5.44 ms                                                                        | 5.39 ms: 1.01x faster                                                                |
| logging_format             | 8.13 us                                                                        | 8.06 us: 1.01x faster                                                                |
| sqlglot_transpile          | 1.22 ms                                                                        | 1.21 ms: 1.01x faster                                                                |
| regex_compile              | 95.0 ms                                                                        | 94.4 ms: 1.01x faster                                                                |
| genshi_xml                 | 53.2 ms                                                                        | 52.9 ms: 1.01x faster                                                                |
| regex_v8                   | 15.8 ms                                                                        | 15.7 ms: 1.01x faster                                                                |
| fannkuch                   | 226 ms                                                                         | 225 ms: 1.00x faster                                                                 |
| scimark_sparse_mat_mult    | 2.36 ms                                                                        | 2.37 ms: 1.00x slower                                                                |
| gc_traversal               | 1.45 ms                                                                        | 1.46 ms: 1.01x slower                                                                |
| go                         | 112 ms                                                                         | 113 ms: 1.01x slower                                                                 |
| scimark_fft                | 165 ms                                                                         | 166 ms: 1.01x slower                                                                 |
| nqueens                    | 73.2 ms                                                                        | 73.7 ms: 1.01x slower                                                                |
| genshi_text                | 22.8 ms                                                                        | 22.9 ms: 1.01x slower                                                                |
| tomli_loads                | 1.48 sec                                                                       | 1.49 sec: 1.01x slower                                                               |
| coverage                   | 51.3 ms                                                                        | 51.9 ms: 1.01x slower                                                                |
| async_generators           | 317 ms                                                                         | 321 ms: 1.01x slower                                                                 |
| html5lib                   | 46.8 ms                                                                        | 47.5 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 462 ms                                                                         | 470 ms: 1.02x slower                                                                 |
| json_loads                 | 21.3 us                                                                        | 21.7 us: 1.02x slower                                                                |
| thrift                     | 747 us                                                                         | 760 us: 1.02x slower                                                                 |
| hexiom                     | 4.60 ms                                                                        | 4.68 ms: 1.02x slower                                                                |
| deepcopy_reduce            | 2.37 us                                                                        | 2.42 us: 1.02x slower                                                                |
| pprint_safe_repr           | 552 ms                                                                         | 563 ms: 1.02x slower                                                                 |
| pprint_pformat             | 1.14 sec                                                                       | 1.16 sec: 1.02x slower                                                               |
| deepcopy_memo              | 15.5 us                                                                        | 15.8 us: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 470 ms                                                                         | 482 ms: 1.02x slower                                                                 |
| django_template            | 32.6 ms                                                                        | 33.6 ms: 1.03x slower                                                                |
| spectral_norm              | 47.3 ms                                                                        | 48.7 ms: 1.03x slower                                                                |
| scimark_lu                 | 77.9 ms                                                                        | 80.4 ms: 1.03x slower                                                                |
| richards                   | 32.4 ms                                                                        | 33.7 ms: 1.04x slower                                                                |
| scimark_monte_carlo        | 41.2 ms                                                                        | 42.8 ms: 1.04x slower                                                                |
| nbody                      | 55.7 ms                                                                        | 61.2 ms: 1.10x slower                                                                |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                         |

Benchmark hidden because not significant (26): async_tree_io, async_tree_io_tg, pylint, bench_mp_pool, 2to3, async_tree_none_tg, typing_runtime_protocols, sympy_integrate, asyncio_tcp_ssl, pathlib, python_startup, regex_effbot, pickle_pure_python, async_tree_memoization, pidigits, python_startup_no_site, bench_thread_pool, xml_etree_iterparse, deepcopy, async_tree_none, json_dumps, xml_etree_parse, async_tree_memoization_tg, create_gc_cycles, asyncio_tcp, json

# HPT report

- Reliability score: 95.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown