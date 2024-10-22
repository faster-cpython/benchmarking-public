# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.01x faster
- HPT reliability: 78.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                         | 248 ms: 1.01x faster                                                           |
| html5lib       | 46.8 ms                                                                        | 45.8 ms: 1.02x faster                                                          |
| tornado_http   | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp      | 756 ms                                                                         | 722 ms: 1.05x faster                                                           |
| async_generators | 304 ms                                                                         | 292 ms: 1.04x faster                                                           |
| coroutines       | 17.7 ms                                                                        | 17.4 ms: 1.01x faster                                                          |
| Geometric mean   | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (9): asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 96.4 ms                                                                        | 94.3 ms: 1.02x faster                                                          |
| pidigits       | 198 ms                                                                         | 201 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                         | 118 ms: 1.05x faster                                                           |
| regex_effbot   | 1.94 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.92 sec                                                                       | 1.84 sec: 1.04x faster                                                         |
| json_dumps           | 7.60 ms                                                                        | 7.39 ms: 1.03x faster                                                          |
| xml_etree_process    | 50.6 ms                                                                        | 49.9 ms: 1.01x faster                                                          |
| xml_etree_generate   | 68.1 ms                                                                        | 67.5 ms: 1.01x faster                                                          |
| xml_etree_parse      | 108 ms                                                                         | 109 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 67.6 ms                                                                        | 68.8 ms: 1.02x slower                                                          |
| unpickle_pure_python | 174 us                                                                         | 183 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                                          | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                                        | 20.1 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                          | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 32.8 ms                                                                        | 31.9 ms: 1.03x faster                                                          |
| genshi_xml      | 47.2 ms                                                                        | 46.1 ms: 1.03x faster                                                          |
| mako            | 8.35 ms                                                                        | 8.24 ms: 1.01x faster                                                          |
| genshi_text     | 22.2 ms                                                                        | 22.0 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                                          | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 3.54 ms                                                                        | 3.14 ms: 1.13x faster                                                          |
| asyncio_tcp              | 756 ms                                                                         | 722 ms: 1.05x faster                                                           |
| regex_dna                | 124 ms                                                                         | 118 ms: 1.05x faster                                                           |
| scimark_lu               | 71.7 ms                                                                        | 68.7 ms: 1.04x faster                                                          |
| tomli_loads              | 1.92 sec                                                                       | 1.84 sec: 1.04x faster                                                         |
| telco                    | 6.97 ms                                                                        | 6.69 ms: 1.04x faster                                                          |
| async_generators         | 304 ms                                                                         | 292 ms: 1.04x faster                                                           |
| deepcopy_reduce          | 2.51 us                                                                        | 2.42 us: 1.04x faster                                                          |
| chaos                    | 54.9 ms                                                                        | 52.8 ms: 1.04x faster                                                          |
| logging_silent           | 76.0 ns                                                                        | 73.1 ns: 1.04x faster                                                          |
| typing_runtime_protocols | 148 us                                                                         | 143 us: 1.04x faster                                                           |
| thrift                   | 742 us                                                                         | 719 us: 1.03x faster                                                           |
| raytrace                 | 236 ms                                                                         | 229 ms: 1.03x faster                                                           |
| crypto_pyaes             | 58.3 ms                                                                        | 56.7 ms: 1.03x faster                                                          |
| json_dumps               | 7.60 ms                                                                        | 7.39 ms: 1.03x faster                                                          |
| nqueens                  | 77.3 ms                                                                        | 75.3 ms: 1.03x faster                                                          |
| django_template          | 32.8 ms                                                                        | 31.9 ms: 1.03x faster                                                          |
| genshi_xml               | 47.2 ms                                                                        | 46.1 ms: 1.03x faster                                                          |
| nbody                    | 96.4 ms                                                                        | 94.3 ms: 1.02x faster                                                          |
| html5lib                 | 46.8 ms                                                                        | 45.8 ms: 1.02x faster                                                          |
| comprehensions           | 14.0 us                                                                        | 13.7 us: 1.02x faster                                                          |
| deepcopy                 | 247 us                                                                         | 242 us: 1.02x faster                                                           |
| sqlglot_parse            | 1.09 ms                                                                        | 1.07 ms: 1.02x faster                                                          |
| tornado_http             | 106 ms                                                                         | 104 ms: 1.02x faster                                                           |
| coroutines               | 17.7 ms                                                                        | 17.4 ms: 1.01x faster                                                          |
| xml_etree_process        | 50.6 ms                                                                        | 49.9 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 650 ms                                                                         | 642 ms: 1.01x faster                                                           |
| logging_format           | 8.73 us                                                                        | 8.61 us: 1.01x faster                                                          |
| mako                     | 8.35 ms                                                                        | 8.24 ms: 1.01x faster                                                          |
| pprint_pformat           | 1.34 sec                                                                       | 1.33 sec: 1.01x faster                                                         |
| sqlglot_transpile        | 1.34 ms                                                                        | 1.32 ms: 1.01x faster                                                          |
| regex_effbot             | 1.94 ms                                                                        | 1.92 ms: 1.01x faster                                                          |
| generators               | 27.1 ms                                                                        | 26.8 ms: 1.01x faster                                                          |
| genshi_text              | 22.2 ms                                                                        | 22.0 ms: 1.01x faster                                                          |
| xml_etree_generate       | 68.1 ms                                                                        | 67.5 ms: 1.01x faster                                                          |
| 2to3                     | 250 ms                                                                         | 248 ms: 1.01x faster                                                           |
| richards                 | 39.6 ms                                                                        | 39.4 ms: 1.01x faster                                                          |
| pycparser                | 868 ms                                                                         | 862 ms: 1.01x faster                                                           |
| logging_simple           | 7.97 us                                                                        | 7.94 us: 1.00x faster                                                          |
| sympy_integrate          | 15.4 ms                                                                        | 15.5 ms: 1.01x slower                                                          |
| python_startup_no_site   | 19.9 ms                                                                        | 20.1 ms: 1.01x slower                                                          |
| deltablue                | 2.68 ms                                                                        | 2.71 ms: 1.01x slower                                                          |
| xml_etree_parse          | 108 ms                                                                         | 109 ms: 1.01x slower                                                           |
| spectral_norm            | 76.7 ms                                                                        | 77.6 ms: 1.01x slower                                                          |
| pidigits                 | 198 ms                                                                         | 201 ms: 1.01x slower                                                           |
| scimark_fft              | 234 ms                                                                         | 237 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 67.6 ms                                                                        | 68.8 ms: 1.02x slower                                                          |
| meteor_contest           | 81.3 ms                                                                        | 82.8 ms: 1.02x slower                                                          |
| deepcopy_memo            | 21.8 us                                                                        | 22.2 us: 1.02x slower                                                          |
| go                       | 102 ms                                                                         | 104 ms: 1.02x slower                                                           |
| scimark_monte_carlo      | 55.9 ms                                                                        | 57.4 ms: 1.03x slower                                                          |
| fannkuch                 | 327 ms                                                                         | 336 ms: 1.03x slower                                                           |
| scimark_sor              | 99.5 ms                                                                        | 103 ms: 1.03x slower                                                           |
| coverage                 | 51.2 ms                                                                        | 53.6 ms: 1.05x slower                                                          |
| unpickle_pure_python     | 174 us                                                                         | 183 us: 1.05x slower                                                           |
| Geometric mean           | (ref)                                                                          | 1.01x faster                                                                   |

Benchmark hidden because not significant (33): richards_super, gc_traversal, create_gc_cycles, json_loads, bench_mp_pool, asyncio_tcp_ssl, sympy_sum, float, docutils, regex_compile, dulwich_log, sympy_expand, async_tree_cpu_io_mixed, mdp, hexiom, async_tree_none, python_startup, pyflate, sqlglot_normalize, sqlglot_optimize, sympy_str, async_tree_memoization, async_tree_cpu_io_mixed_tg, regex_v8, pickle_pure_python, pathlib, pylint, async_tree_io, json, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bench_thread_pool

# HPT report

- Reliability score: 78.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown