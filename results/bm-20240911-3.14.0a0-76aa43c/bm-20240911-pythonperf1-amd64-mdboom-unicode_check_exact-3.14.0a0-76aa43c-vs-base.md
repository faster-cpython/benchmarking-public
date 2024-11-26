# Results vs. base

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.001x faster
- HPT reliability: 52.71%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                   | 1.68 sec: 1.01x faster                                                    |
| html5lib       | 39.4 ms                                                                    | 40.0 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators           | 238 ms                                                                     | 241 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 396 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, coroutines, async_tree_io, async_tree_io_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                     | 150 ms: 1.00x faster                                                      |
| nbody          | 79.8 ms                                                                    | 82.1 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 14.6 ms                                                                    | 14.4 ms: 1.01x faster                                                     |
| regex_compile  | 89.6 ms                                                                    | 89.2 ms: 1.00x faster                                                     |
| regex_effbot   | 1.55 ms                                                                    | 1.54 ms: 1.00x faster                                                     |
| regex_dna      | 114 ms                                                                     | 114 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_dict          | 19.7 us                                                                    | 19.2 us: 1.03x faster                                                     |
| pickle               | 7.28 us                                                                    | 7.15 us: 1.02x faster                                                     |
| unpickle_list        | 2.77 us                                                                    | 2.73 us: 1.02x faster                                                     |
| xml_etree_parse      | 93.6 ms                                                                    | 92.5 ms: 1.01x faster                                                     |
| pickle_pure_python   | 209 us                                                                     | 207 us: 1.01x faster                                                      |
| json_dumps           | 6.18 ms                                                                    | 6.14 ms: 1.01x faster                                                     |
| unpickle_pure_python | 145 us                                                                     | 147 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (7): pickle_list, xml_etree_iterparse, xml_etree_process, tomli_loads, json_loads, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 35.9 ms                                                                    | 36.7 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (3): django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 1.50 sec                                                                   | 1.40 sec: 1.07x faster                                                    |
| coverage                   | 48.1 ms                                                                    | 46.6 ms: 1.03x faster                                                     |
| scimark_lu                 | 61.8 ms                                                                    | 59.9 ms: 1.03x faster                                                     |
| pickle_dict                | 19.7 us                                                                    | 19.2 us: 1.03x faster                                                     |
| scimark_fft                | 204 ms                                                                     | 199 ms: 1.03x faster                                                      |
| raytrace                   | 187 ms                                                                     | 184 ms: 1.02x faster                                                      |
| pickle                     | 7.28 us                                                                    | 7.15 us: 1.02x faster                                                     |
| scimark_sor                | 87.5 ms                                                                    | 86.1 ms: 1.02x faster                                                     |
| unpickle_list              | 2.77 us                                                                    | 2.73 us: 1.02x faster                                                     |
| xml_etree_parse            | 93.6 ms                                                                    | 92.5 ms: 1.01x faster                                                     |
| regex_v8                   | 14.6 ms                                                                    | 14.4 ms: 1.01x faster                                                     |
| richards_super             | 35.8 ms                                                                    | 35.5 ms: 1.01x faster                                                     |
| pickle_pure_python         | 209 us                                                                     | 207 us: 1.01x faster                                                      |
| typing_runtime_protocols   | 111 us                                                                     | 110 us: 1.01x faster                                                      |
| sqlglot_parse              | 875 us                                                                     | 868 us: 1.01x faster                                                      |
| json_dumps                 | 6.18 ms                                                                    | 6.14 ms: 1.01x faster                                                     |
| docutils                   | 1.69 sec                                                                   | 1.68 sec: 1.01x faster                                                    |
| sympy_str                  | 176 ms                                                                     | 175 ms: 1.01x faster                                                      |
| sympy_expand               | 306 ms                                                                     | 304 ms: 1.01x faster                                                      |
| richards                   | 31.7 ms                                                                    | 31.5 ms: 1.01x faster                                                     |
| deltablue                  | 2.24 ms                                                                    | 2.23 ms: 1.00x faster                                                     |
| logging_silent             | 61.9 ns                                                                    | 61.7 ns: 1.00x faster                                                     |
| regex_compile              | 89.6 ms                                                                    | 89.2 ms: 1.00x faster                                                     |
| regex_effbot               | 1.55 ms                                                                    | 1.54 ms: 1.00x faster                                                     |
| pidigits                   | 151 ms                                                                     | 150 ms: 1.00x faster                                                      |
| regex_dna                  | 114 ms                                                                     | 114 ms: 1.00x faster                                                      |
| sympy_integrate            | 13.0 ms                                                                    | 13.0 ms: 1.00x slower                                                     |
| dulwich_log                | 41.9 ms                                                                    | 42.1 ms: 1.00x slower                                                     |
| gc_traversal               | 1.52 ms                                                                    | 1.53 ms: 1.01x slower                                                     |
| meteor_contest             | 77.6 ms                                                                    | 78.1 ms: 1.01x slower                                                     |
| hexiom                     | 4.30 ms                                                                    | 4.33 ms: 1.01x slower                                                     |
| crypto_pyaes               | 46.9 ms                                                                    | 47.2 ms: 1.01x slower                                                     |
| comprehensions             | 11.4 us                                                                    | 11.5 us: 1.01x slower                                                     |
| deepcopy_memo              | 20.0 us                                                                    | 20.2 us: 1.01x slower                                                     |
| spectral_norm              | 64.7 ms                                                                    | 65.3 ms: 1.01x slower                                                     |
| generators                 | 20.9 ms                                                                    | 21.1 ms: 1.01x slower                                                     |
| thrift                     | 507 us                                                                     | 512 us: 1.01x slower                                                      |
| deepcopy                   | 188 us                                                                     | 190 us: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 2.64 ms                                                                    | 2.67 ms: 1.01x slower                                                     |
| async_generators           | 238 ms                                                                     | 241 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 48.5 ms                                                                    | 49.1 ms: 1.01x slower                                                     |
| nqueens                    | 62.9 ms                                                                    | 63.7 ms: 1.01x slower                                                     |
| chaos                      | 42.3 ms                                                                    | 42.9 ms: 1.01x slower                                                     |
| html5lib                   | 39.4 ms                                                                    | 40.0 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 390 ms                                                                     | 396 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 145 us                                                                     | 147 us: 1.02x slower                                                      |
| genshi_xml                 | 35.9 ms                                                                    | 36.7 ms: 1.02x slower                                                     |
| bench_mp_pool              | 65.8 ms                                                                    | 67.4 ms: 1.02x slower                                                     |
| nbody                      | 79.8 ms                                                                    | 82.1 ms: 1.03x slower                                                     |
| fannkuch                   | 280 ms                                                                     | 289 ms: 1.03x slower                                                      |
| unpack_sequence            | 41.3 ns                                                                    | 43.2 ns: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (44): json, pickle_list, asyncio_tcp, django_template, bench_thread_pool, async_tree_none, telco, xml_etree_iterparse, xml_etree_process, tomli_loads, python_startup, float, logging_simple, 2to3, json_loads, pprint_pformat, sqlglot_transpile, sympy_sum, sqlglot_normalize, sqlite_synth, pprint_safe_repr, xml_etree_generate, go, mako, logging_format, python_startup_no_site, sqlglot_optimize, deepcopy_reduce, create_gc_cycles, genshi_text, tornado_http, pyflate, async_tree_memoization_tg, pathlib, async_tree_cpu_io_mixed, async_tree_memoization, unpickle, pycparser, pylint, async_tree_none_tg, coroutines, async_tree_io, async_tree_io_tg, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 52.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown