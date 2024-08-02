# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: windows-x86
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.00x slower
- HPT reliability: 90.11%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                         | 249 ms: 1.01x slower                                                         |
| chameleon      | 6.12 ms                                                                        | 6.18 ms: 1.01x slower                                                        |
| docutils       | 1.87 sec                                                                       | 1.90 sec: 1.02x slower                                                       |
| html5lib       | 45.0 ms                                                                        | 46.0 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 472 ms                                                                         | 478 ms: 1.01x slower                                                         |
| async_tree_memoization  | 280 ms                                                                         | 284 ms: 1.02x slower                                                         |
| async_tree_none         | 228 ms                                                                         | 232 ms: 1.02x slower                                                         |
| Geometric mean          | (ref)                                                                          | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 41.5 ms                                                                        | 40.9 ms: 1.01x faster                                                        |
| pidigits       | 194 ms                                                                         | 198 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 1.94 ms                                                                        | 1.88 ms: 1.03x faster                                                        |
| regex_v8       | 16.0 ms                                                                        | 15.7 ms: 1.02x faster                                                        |
| regex_dna      | 120 ms                                                                         | 119 ms: 1.01x faster                                                         |
| regex_compile  | 96.8 ms                                                                        | 96.3 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 3.06 us                                                                        | 2.85 us: 1.07x faster                                                        |
| json_dumps           | 6.74 ms                                                                        | 6.63 ms: 1.02x faster                                                        |
| unpickle             | 10.2 us                                                                        | 10.0 us: 1.01x faster                                                        |
| tomli_loads          | 1.38 sec                                                                       | 1.37 sec: 1.01x faster                                                       |
| unpickle_pure_python | 138 us                                                                         | 137 us: 1.01x faster                                                         |
| pickle_list          | 3.53 us                                                                        | 3.60 us: 1.02x slower                                                        |
| xml_etree_process    | 41.2 ms                                                                        | 42.6 ms: 1.03x slower                                                        |
| pickle_pure_python   | 196 us                                                                         | 204 us: 1.04x slower                                                         |
| xml_etree_generate   | 55.3 ms                                                                        | 58.0 ms: 1.05x slower                                                        |
| pickle               | 8.51 us                                                                        | 9.05 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                                          | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): pickle_dict, xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 24.2 ms                                                                        | 24.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.1 ms                                                                        | 50.5 ms: 1.01x faster                                                        |
| genshi_text     | 21.6 ms                                                                        | 21.4 ms: 1.01x faster                                                        |
| django_template | 31.2 ms                                                                        | 31.7 ms: 1.02x slower                                                        |
| mako            | 5.25 ms                                                                        | 5.38 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                          | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 147 us                                                                         | 137 us: 1.08x faster                                                         |
| unpickle_list            | 3.06 us                                                                        | 2.85 us: 1.07x faster                                                        |
| pyflate                  | 292 ms                                                                         | 278 ms: 1.05x faster                                                         |
| nqueens                  | 71.0 ms                                                                        | 67.5 ms: 1.05x faster                                                        |
| chaos                    | 52.0 ms                                                                        | 49.8 ms: 1.04x faster                                                        |
| fannkuch                 | 224 ms                                                                         | 215 ms: 1.04x faster                                                         |
| regex_effbot             | 1.94 ms                                                                        | 1.88 ms: 1.03x faster                                                        |
| raytrace                 | 208 ms                                                                         | 202 ms: 1.03x faster                                                         |
| go                       | 111 ms                                                                         | 108 ms: 1.03x faster                                                         |
| scimark_fft              | 171 ms                                                                         | 167 ms: 1.02x faster                                                         |
| comprehensions           | 11.2 us                                                                        | 11.0 us: 1.02x faster                                                        |
| regex_v8                 | 16.0 ms                                                                        | 15.7 ms: 1.02x faster                                                        |
| json_dumps               | 6.74 ms                                                                        | 6.63 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 551 ms                                                                         | 542 ms: 1.02x faster                                                         |
| coroutines               | 16.5 ms                                                                        | 16.2 ms: 1.02x faster                                                        |
| unpickle                 | 10.2 us                                                                        | 10.0 us: 1.01x faster                                                        |
| sqlite_synth             | 1.88 us                                                                        | 1.85 us: 1.01x faster                                                        |
| float                    | 41.5 ms                                                                        | 40.9 ms: 1.01x faster                                                        |
| tomli_loads              | 1.38 sec                                                                       | 1.37 sec: 1.01x faster                                                       |
| gc_traversal             | 1.47 ms                                                                        | 1.45 ms: 1.01x faster                                                        |
| genshi_xml               | 51.1 ms                                                                        | 50.5 ms: 1.01x faster                                                        |
| generators               | 23.6 ms                                                                        | 23.4 ms: 1.01x faster                                                        |
| scimark_monte_carlo      | 41.6 ms                                                                        | 41.2 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 138 us                                                                         | 137 us: 1.01x faster                                                         |
| genshi_text              | 21.6 ms                                                                        | 21.4 ms: 1.01x faster                                                        |
| regex_dna                | 120 ms                                                                         | 119 ms: 1.01x faster                                                         |
| richards                 | 30.9 ms                                                                        | 30.7 ms: 1.01x faster                                                        |
| pprint_pformat           | 1.14 sec                                                                       | 1.13 sec: 1.01x faster                                                       |
| regex_compile            | 96.8 ms                                                                        | 96.3 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 220 ms                                                                         | 221 ms: 1.00x slower                                                         |
| logging_silent           | 54.8 ns                                                                        | 55.0 ns: 1.00x slower                                                        |
| deltablue                | 2.54 ms                                                                        | 2.55 ms: 1.00x slower                                                        |
| sympy_expand             | 374 ms                                                                         | 376 ms: 1.00x slower                                                         |
| hexiom                   | 4.43 ms                                                                        | 4.45 ms: 1.00x slower                                                        |
| richards_super           | 35.3 ms                                                                        | 35.5 ms: 1.00x slower                                                        |
| python_startup           | 24.2 ms                                                                        | 24.3 ms: 1.01x slower                                                        |
| 2to3                     | 248 ms                                                                         | 249 ms: 1.01x slower                                                         |
| deepcopy_memo            | 20.5 us                                                                        | 20.6 us: 1.01x slower                                                        |
| sqlglot_optimize         | 42.0 ms                                                                        | 42.3 ms: 1.01x slower                                                        |
| pathlib                  | 85.8 ms                                                                        | 86.4 ms: 1.01x slower                                                        |
| deepcopy                 | 298 us                                                                         | 300 us: 1.01x slower                                                         |
| chameleon                | 6.12 ms                                                                        | 6.18 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed  | 472 ms                                                                         | 478 ms: 1.01x slower                                                         |
| sympy_integrate          | 15.5 ms                                                                        | 15.7 ms: 1.01x slower                                                        |
| thrift                   | 705 us                                                                         | 714 us: 1.01x slower                                                         |
| pycparser                | 794 ms                                                                         | 804 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult  | 2.34 ms                                                                        | 2.37 ms: 1.01x slower                                                        |
| spectral_norm            | 47.3 ms                                                                        | 47.9 ms: 1.01x slower                                                        |
| logging_simple           | 7.44 us                                                                        | 7.54 us: 1.01x slower                                                        |
| sympy_str                | 209 ms                                                                         | 212 ms: 1.01x slower                                                         |
| django_template          | 31.2 ms                                                                        | 31.7 ms: 1.02x slower                                                        |
| async_tree_memoization   | 280 ms                                                                         | 284 ms: 1.02x slower                                                         |
| meteor_contest           | 72.2 ms                                                                        | 73.5 ms: 1.02x slower                                                        |
| pickle_list              | 3.53 us                                                                        | 3.60 us: 1.02x slower                                                        |
| docutils                 | 1.87 sec                                                                       | 1.90 sec: 1.02x slower                                                       |
| create_gc_cycles         | 749 us                                                                         | 764 us: 1.02x slower                                                         |
| async_tree_none          | 228 ms                                                                         | 232 ms: 1.02x slower                                                         |
| pidigits                 | 194 ms                                                                         | 198 ms: 1.02x slower                                                         |
| deepcopy_reduce          | 2.69 us                                                                        | 2.75 us: 1.02x slower                                                        |
| html5lib                 | 45.0 ms                                                                        | 46.0 ms: 1.02x slower                                                        |
| crypto_pyaes             | 48.5 ms                                                                        | 49.6 ms: 1.02x slower                                                        |
| mako                     | 5.25 ms                                                                        | 5.38 ms: 1.02x slower                                                        |
| sympy_sum                | 105 ms                                                                         | 108 ms: 1.03x slower                                                         |
| xml_etree_process        | 41.2 ms                                                                        | 42.6 ms: 1.03x slower                                                        |
| telco                    | 5.45 ms                                                                        | 5.63 ms: 1.03x slower                                                        |
| sqlglot_transpile        | 1.15 ms                                                                        | 1.19 ms: 1.03x slower                                                        |
| sqlglot_parse            | 891 us                                                                         | 922 us: 1.04x slower                                                         |
| pickle_pure_python       | 196 us                                                                         | 204 us: 1.04x slower                                                         |
| xml_etree_generate       | 55.3 ms                                                                        | 58.0 ms: 1.05x slower                                                        |
| asyncio_tcp              | 599 ms                                                                         | 634 ms: 1.06x slower                                                         |
| pickle                   | 8.51 us                                                                        | 9.05 us: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                          | 1.00x slower                                                                 |

Benchmark hidden because not significant (24): json, async_tree_io_tg, nbody, scimark_sor, logging_format, pickle_dict, async_generators, bench_mp_pool, xml_etree_parse, xml_etree_iterparse, flaskblogging, asyncio_tcp_ssl, scimark_lu, mdp, json_loads, coverage, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, tornado_http, python_startup_no_site, async_tree_io, pylint, bench_thread_pool

# HPT report

- Reliability score: 90.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown