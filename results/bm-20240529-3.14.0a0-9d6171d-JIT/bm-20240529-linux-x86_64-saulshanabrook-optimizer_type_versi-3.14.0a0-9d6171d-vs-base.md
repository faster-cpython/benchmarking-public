# Results vs. base

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: 9d6171d
- commit date: 2024-05-29
- overall geometric mean: 1.00x faster
- HPT reliability: 61.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.6 ms                                                               | 71.6 ms: 1.01x faster                                                         |
| nbody          | 80.2 ms                                                               | 82.0 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                               | 3.72 ms: 1.01x faster                                                         |
| regex_compile  | 140 ms                                                                | 139 ms: 1.01x faster                                                          |
| regex_dna      | 227 ms                                                                | 226 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_dict          | 36.2 us                                                               | 34.6 us: 1.05x faster                                                         |
| pickle_pure_python   | 301 us                                                                | 297 us: 1.01x faster                                                          |
| json_loads           | 29.1 us                                                               | 28.8 us: 1.01x faster                                                         |
| unpickle_pure_python | 223 us                                                                | 221 us: 1.01x faster                                                          |
| xml_etree_generate   | 82.1 ms                                                               | 82.8 ms: 1.01x slower                                                         |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                         |
| pickle               | 11.7 us                                                               | 11.8 us: 1.01x slower                                                         |
| tomli_loads          | 1.95 sec                                                              | 1.98 sec: 1.01x slower                                                        |
| unpickle             | 15.0 us                                                               | 15.2 us: 1.01x slower                                                         |
| xml_etree_process    | 57.7 ms                                                               | 58.7 ms: 1.02x slower                                                         |
| unpickle_list        | 5.39 us                                                               | 5.60 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 11.0 ms                                                               | 11.0 ms: 1.00x slower                                                         |
| python_startup_no_site | 7.56 ms                                                               | 7.60 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml     | 59.1 ms                                                               | 57.4 ms: 1.03x faster                                                         |
| genshi_text    | 25.1 ms                                                               | 24.7 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_sor              | 137 ms                                                                | 128 ms: 1.08x faster                                                          |
| pickle_dict              | 36.2 us                                                               | 34.6 us: 1.05x faster                                                         |
| coroutines               | 23.4 ms                                                               | 22.6 ms: 1.03x faster                                                         |
| genshi_xml               | 59.1 ms                                                               | 57.4 ms: 1.03x faster                                                         |
| deepcopy_memo            | 39.1 us                                                               | 38.1 us: 1.03x faster                                                         |
| sqlglot_parse            | 1.32 ms                                                               | 1.30 ms: 1.02x faster                                                         |
| richards                 | 42.5 ms                                                               | 41.7 ms: 1.02x faster                                                         |
| coverage                 | 94.2 ms                                                               | 92.5 ms: 1.02x faster                                                         |
| genshi_text              | 25.1 ms                                                               | 24.7 ms: 1.02x faster                                                         |
| regex_effbot             | 3.77 ms                                                               | 3.72 ms: 1.01x faster                                                         |
| float                    | 72.6 ms                                                               | 71.6 ms: 1.01x faster                                                         |
| json                     | 5.29 ms                                                               | 5.22 ms: 1.01x faster                                                         |
| pickle_pure_python       | 301 us                                                                | 297 us: 1.01x faster                                                          |
| meteor_contest           | 110 ms                                                                | 108 ms: 1.01x faster                                                          |
| json_loads               | 29.1 us                                                               | 28.8 us: 1.01x faster                                                         |
| unpickle_pure_python     | 223 us                                                                | 221 us: 1.01x faster                                                          |
| chaos                    | 60.2 ms                                                               | 59.8 ms: 1.01x faster                                                         |
| regex_compile            | 140 ms                                                                | 139 ms: 1.01x faster                                                          |
| mdp                      | 2.60 sec                                                              | 2.58 sec: 1.01x faster                                                        |
| pathlib                  | 16.4 ms                                                               | 16.3 ms: 1.01x faster                                                         |
| regex_dna                | 227 ms                                                                | 226 ms: 1.01x faster                                                          |
| spectral_norm            | 103 ms                                                                | 103 ms: 1.00x faster                                                          |
| go                       | 148 ms                                                                | 148 ms: 1.00x faster                                                          |
| logging_silent           | 106 ns                                                                | 106 ns: 1.00x faster                                                          |
| bench_thread_pool        | 865 us                                                                | 863 us: 1.00x faster                                                          |
| asyncio_tcp_ssl          | 1.86 sec                                                              | 1.86 sec: 1.00x slower                                                        |
| create_gc_cycles         | 1.81 ms                                                               | 1.82 ms: 1.00x slower                                                         |
| python_startup           | 11.0 ms                                                               | 11.0 ms: 1.00x slower                                                         |
| sympy_expand             | 506 ms                                                                | 508 ms: 1.00x slower                                                          |
| deepcopy_reduce          | 3.29 us                                                               | 3.31 us: 1.00x slower                                                         |
| python_startup_no_site   | 7.56 ms                                                               | 7.60 ms: 1.01x slower                                                         |
| dulwich_log              | 68.8 ms                                                               | 69.2 ms: 1.01x slower                                                         |
| scimark_lu               | 124 ms                                                                | 124 ms: 1.01x slower                                                          |
| sqlite_synth             | 2.87 us                                                               | 2.89 us: 1.01x slower                                                         |
| docutils                 | 2.93 sec                                                              | 2.95 sec: 1.01x slower                                                        |
| async_generators         | 465 ms                                                                | 468 ms: 1.01x slower                                                          |
| xml_etree_generate       | 82.1 ms                                                               | 82.8 ms: 1.01x slower                                                         |
| thrift                   | 806 us                                                                | 813 us: 1.01x slower                                                          |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                         |
| crypto_pyaes             | 67.5 ms                                                               | 68.1 ms: 1.01x slower                                                         |
| hexiom                   | 6.62 ms                                                               | 6.68 ms: 1.01x slower                                                         |
| logging_format           | 6.37 us                                                               | 6.44 us: 1.01x slower                                                         |
| pickle                   | 11.7 us                                                               | 11.8 us: 1.01x slower                                                         |
| tomli_loads              | 1.95 sec                                                              | 1.98 sec: 1.01x slower                                                        |
| raytrace                 | 281 ms                                                                | 284 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 4.54 ms                                                               | 4.60 ms: 1.01x slower                                                         |
| unpickle                 | 15.0 us                                                               | 15.2 us: 1.01x slower                                                         |
| xml_etree_process        | 57.7 ms                                                               | 58.7 ms: 1.02x slower                                                         |
| deepcopy                 | 366 us                                                                | 372 us: 1.02x slower                                                          |
| gc_traversal             | 3.92 ms                                                               | 3.99 ms: 1.02x slower                                                         |
| typing_runtime_protocols | 170 us                                                                | 174 us: 1.02x slower                                                          |
| nbody                    | 80.2 ms                                                               | 82.0 ms: 1.02x slower                                                         |
| pycparser                | 1.17 sec                                                              | 1.20 sec: 1.02x slower                                                        |
| asyncio_tcp              | 509 ms                                                                | 523 ms: 1.03x slower                                                          |
| unpickle_list            | 5.39 us                                                               | 5.60 us: 1.04x slower                                                         |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (41): pprint_pformat, deltablue, mako, async_tree_memoization, xml_etree_parse, telco, richards_super, async_tree_cpu_io_mixed, sqlglot_normalize, scimark_fft, dask, bench_mp_pool, sympy_sum, pyflate, sqlglot_transpile, django_template, tornado_http, html5lib, async_tree_none, pidigits, generators, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, xml_etree_iterparse, sympy_integrate, sympy_str, nqueens, pylint, regex_v8, sqlglot_optimize, 2to3, pickle_list, fannkuch, async_tree_none_tg, logging_simple, comprehensions, async_tree_io_tg, pprint_safe_repr, async_tree_memoization_tg, scimark_monte_carlo

# HPT report

- Reliability score: 61.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x