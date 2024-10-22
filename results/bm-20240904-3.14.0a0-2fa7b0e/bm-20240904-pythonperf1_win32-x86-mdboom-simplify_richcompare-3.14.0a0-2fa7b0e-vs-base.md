# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.01x faster
- HPT reliability: 82.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.86 sec                                                                       | 1.86 sec: 1.01x faster                                                         |
| html5lib       | 46.8 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators | 304 ms                                                                         | 299 ms: 1.02x faster                                                           |
| coroutines       | 17.7 ms                                                                        | 17.5 ms: 1.01x faster                                                          |
| async_tree_none  | 213 ms                                                                         | 217 ms: 1.02x slower                                                           |
| Geometric mean   | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (9): asyncio_tcp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 62.3 ms                                                                        | 60.8 ms: 1.03x faster                                                          |
| pidigits       | 198 ms                                                                         | 201 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                         | 123 ms: 1.01x faster                                                           |
| regex_v8       | 16.1 ms                                                                        | 16.3 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 262 us                                                                         | 254 us: 1.03x faster                                                           |
| xml_etree_process    | 50.6 ms                                                                        | 49.3 ms: 1.03x faster                                                          |
| json_dumps           | 7.60 ms                                                                        | 7.42 ms: 1.02x faster                                                          |
| unpickle_pure_python | 174 us                                                                         | 171 us: 1.02x faster                                                           |
| tomli_loads          | 1.92 sec                                                                       | 1.89 sec: 1.02x faster                                                         |
| xml_etree_iterparse  | 67.6 ms                                                                        | 67.9 ms: 1.00x slower                                                          |
| Geometric mean       | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.0 ms                                                                        | 24.2 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.2 ms                                                                        | 21.6 ms: 1.03x faster                                                          |
| genshi_xml      | 47.2 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| django_template | 32.8 ms                                                                        | 32.3 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 3.54 ms                                                                        | 3.12 ms: 1.14x faster                                                          |
| deepcopy_reduce          | 2.51 us                                                                        | 2.43 us: 1.03x faster                                                          |
| comprehensions           | 14.0 us                                                                        | 13.5 us: 1.03x faster                                                          |
| genshi_text              | 22.2 ms                                                                        | 21.6 ms: 1.03x faster                                                          |
| richards                 | 39.6 ms                                                                        | 38.5 ms: 1.03x faster                                                          |
| pickle_pure_python       | 262 us                                                                         | 254 us: 1.03x faster                                                           |
| richards_super           | 44.4 ms                                                                        | 43.3 ms: 1.03x faster                                                          |
| xml_etree_process        | 50.6 ms                                                                        | 49.3 ms: 1.03x faster                                                          |
| float                    | 62.3 ms                                                                        | 60.8 ms: 1.03x faster                                                          |
| json                     | 4.29 ms                                                                        | 4.19 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 43.8 ms                                                                        | 42.8 ms: 1.02x faster                                                          |
| json_dumps               | 7.60 ms                                                                        | 7.42 ms: 1.02x faster                                                          |
| gc_traversal             | 1.45 ms                                                                        | 1.42 ms: 1.02x faster                                                          |
| scimark_lu               | 71.7 ms                                                                        | 70.2 ms: 1.02x faster                                                          |
| logging_format           | 8.73 us                                                                        | 8.55 us: 1.02x faster                                                          |
| unpickle_pure_python     | 174 us                                                                         | 171 us: 1.02x faster                                                           |
| scimark_monte_carlo      | 55.9 ms                                                                        | 55.0 ms: 1.02x faster                                                          |
| tomli_loads              | 1.92 sec                                                                       | 1.89 sec: 1.02x faster                                                         |
| async_generators         | 304 ms                                                                         | 299 ms: 1.02x faster                                                           |
| logging_silent           | 76.0 ns                                                                        | 74.7 ns: 1.02x faster                                                          |
| deltablue                | 2.68 ms                                                                        | 2.64 ms: 1.02x faster                                                          |
| nqueens                  | 77.3 ms                                                                        | 76.1 ms: 1.02x faster                                                          |
| genshi_xml               | 47.2 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| mdp                      | 1.72 sec                                                                       | 1.70 sec: 1.01x faster                                                         |
| django_template          | 32.8 ms                                                                        | 32.3 ms: 1.01x faster                                                          |
| sqlglot_parse            | 1.09 ms                                                                        | 1.08 ms: 1.01x faster                                                          |
| spectral_norm            | 76.7 ms                                                                        | 75.8 ms: 1.01x faster                                                          |
| sympy_expand             | 383 ms                                                                         | 379 ms: 1.01x faster                                                           |
| scimark_sor              | 99.5 ms                                                                        | 98.5 ms: 1.01x faster                                                          |
| thrift                   | 742 us                                                                         | 735 us: 1.01x faster                                                           |
| coroutines               | 17.7 ms                                                                        | 17.5 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 225 ms                                                                         | 223 ms: 1.01x faster                                                           |
| sqlglot_transpile        | 1.34 ms                                                                        | 1.33 ms: 1.01x faster                                                          |
| telco                    | 6.97 ms                                                                        | 6.92 ms: 1.01x faster                                                          |
| crypto_pyaes             | 58.3 ms                                                                        | 57.8 ms: 1.01x faster                                                          |
| html5lib                 | 46.8 ms                                                                        | 46.5 ms: 1.01x faster                                                          |
| logging_simple           | 7.97 us                                                                        | 7.92 us: 1.01x faster                                                          |
| regex_dna                | 124 ms                                                                         | 123 ms: 1.01x faster                                                           |
| dulwich_log              | 49.9 ms                                                                        | 49.7 ms: 1.01x faster                                                          |
| docutils                 | 1.86 sec                                                                       | 1.86 sec: 1.01x faster                                                         |
| pprint_pformat           | 1.34 sec                                                                       | 1.34 sec: 1.00x faster                                                         |
| fannkuch                 | 327 ms                                                                         | 328 ms: 1.00x slower                                                           |
| xml_etree_iterparse      | 67.6 ms                                                                        | 67.9 ms: 1.00x slower                                                          |
| coverage                 | 51.2 ms                                                                        | 51.5 ms: 1.01x slower                                                          |
| python_startup           | 24.0 ms                                                                        | 24.2 ms: 1.01x slower                                                          |
| sympy_integrate          | 15.4 ms                                                                        | 15.5 ms: 1.01x slower                                                          |
| pathlib                  | 87.1 ms                                                                        | 87.8 ms: 1.01x slower                                                          |
| regex_v8                 | 16.1 ms                                                                        | 16.3 ms: 1.01x slower                                                          |
| pyflate                  | 354 ms                                                                         | 357 ms: 1.01x slower                                                           |
| sympy_str                | 214 ms                                                                         | 217 ms: 1.01x slower                                                           |
| pidigits                 | 198 ms                                                                         | 201 ms: 1.01x slower                                                           |
| pycparser                | 868 ms                                                                         | 878 ms: 1.01x slower                                                           |
| meteor_contest           | 81.3 ms                                                                        | 82.2 ms: 1.01x slower                                                          |
| hexiom                   | 5.20 ms                                                                        | 5.27 ms: 1.01x slower                                                          |
| typing_runtime_protocols | 148 us                                                                         | 151 us: 1.02x slower                                                           |
| async_tree_none          | 213 ms                                                                         | 217 ms: 1.02x slower                                                           |
| bench_mp_pool            | 73.4 ms                                                                        | 74.9 ms: 1.02x slower                                                          |
| generators               | 27.1 ms                                                                        | 27.7 ms: 1.02x slower                                                          |
| deepcopy_memo            | 21.8 us                                                                        | 22.5 us: 1.03x slower                                                          |
| scimark_fft              | 234 ms                                                                         | 241 ms: 1.03x slower                                                           |
| Geometric mean           | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (28): asyncio_tcp, async_tree_cpu_io_mixed, tornado_http, async_tree_cpu_io_mixed_tg, chaos, sympy_sum, regex_effbot, xml_etree_generate, asyncio_tcp_ssl, regex_compile, raytrace, json_loads, go, async_tree_memoization, deepcopy, pprint_safe_repr, xml_etree_parse, mako, 2to3, nbody, create_gc_cycles, async_tree_none_tg, pylint, async_tree_io_tg, python_startup_no_site, async_tree_memoization_tg, async_tree_io, bench_thread_pool

# HPT report

- Reliability score: 82.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown