# Results vs. base

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: 74c8568
- commit date: 2024-03-27
- overall geometric mean: 1.00x slower
- HPT reliability: 54.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 6.92 ms                                                                | 6.82 ms: 1.01x faster                                        |
| html5lib       | 66.6 ms                                                                | 67.9 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 91.4 ms                                                                | 88.3 ms: 1.04x faster                                        |
| float          | 77.8 ms                                                                | 76.6 ms: 1.02x faster                                        |
| pidigits       | 191 ms                                                                 | 189 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 132 ms                                                                 | 133 ms: 1.00x slower                                         |
| regex_v8       | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                        |
| regex_dna      | 221 ms                                                                 | 230 ms: 1.04x slower                                         |
| regex_effbot   | 3.63 ms                                                                | 3.81 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 215 us: 1.02x faster                                         |
| unpickle_list        | 5.36 us                                                                | 5.26 us: 1.02x faster                                        |
| pickle_pure_python   | 303 us                                                                 | 297 us: 1.02x faster                                         |
| xml_etree_generate   | 86.7 ms                                                                | 85.8 ms: 1.01x faster                                        |
| xml_etree_process    | 59.3 ms                                                                | 59.8 ms: 1.01x slower                                        |
| json_dumps           | 10.3 ms                                                                | 10.4 ms: 1.01x slower                                        |
| pickle               | 11.6 us                                                                | 12.0 us: 1.04x slower                                        |
| unpickle             | 16.0 us                                                                | 16.7 us: 1.04x slower                                        |
| pickle_list          | 4.90 us                                                                | 5.40 us: 1.10x slower                                        |
| pickle_dict          | 32.2 us                                                                | 35.6 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                                | 10.6 ms: 1.01x slower                                        |
| python_startup_no_site | 8.93 ms                                                                | 9.00 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 52.3 ms                                                                | 50.8 ms: 1.03x faster                                        |
| genshi_text    | 24.6 ms                                                                | 24.0 ms: 1.03x faster                                        |
| mako           | 10.8 ms                                                                | 10.7 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5+-ce00de4 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpack_sequence          | 52.4 ns                                                                | 44.4 ns: 1.18x faster                                        |
| deepcopy_memo            | 38.5 us                                                                | 37.0 us: 1.04x faster                                        |
| scimark_monte_carlo      | 68.7 ms                                                                | 66.0 ms: 1.04x faster                                        |
| nbody                    | 91.4 ms                                                                | 88.3 ms: 1.04x faster                                        |
| genshi_xml               | 52.3 ms                                                                | 50.8 ms: 1.03x faster                                        |
| go                       | 144 ms                                                                 | 140 ms: 1.03x faster                                         |
| genshi_text              | 24.6 ms                                                                | 24.0 ms: 1.03x faster                                        |
| unpickle_pure_python     | 219 us                                                                 | 215 us: 1.02x faster                                         |
| deepcopy_reduce          | 3.16 us                                                                | 3.10 us: 1.02x faster                                        |
| unpickle_list            | 5.36 us                                                                | 5.26 us: 1.02x faster                                        |
| pickle_pure_python       | 303 us                                                                 | 297 us: 1.02x faster                                         |
| logging_simple           | 5.97 us                                                                | 5.87 us: 1.02x faster                                        |
| float                    | 77.8 ms                                                                | 76.6 ms: 1.02x faster                                        |
| chameleon                | 6.92 ms                                                                | 6.82 ms: 1.01x faster                                        |
| typing_runtime_protocols | 112 us                                                                 | 111 us: 1.01x faster                                         |
| richards_super           | 51.8 ms                                                                | 51.2 ms: 1.01x faster                                        |
| fannkuch                 | 396 ms                                                                 | 391 ms: 1.01x faster                                         |
| logging_silent           | 100 ns                                                                 | 98.9 ns: 1.01x faster                                        |
| comprehensions           | 16.6 us                                                                | 16.5 us: 1.01x faster                                        |
| scimark_fft              | 362 ms                                                                 | 358 ms: 1.01x faster                                         |
| xml_etree_generate       | 86.7 ms                                                                | 85.8 ms: 1.01x faster                                        |
| deepcopy                 | 350 us                                                                 | 347 us: 1.01x faster                                         |
| mako                     | 10.8 ms                                                                | 10.7 ms: 1.01x faster                                        |
| richards                 | 45.7 ms                                                                | 45.4 ms: 1.01x faster                                        |
| raytrace                 | 265 ms                                                                 | 263 ms: 1.01x faster                                         |
| meteor_contest           | 110 ms                                                                 | 109 ms: 1.01x faster                                         |
| pidigits                 | 191 ms                                                                 | 189 ms: 1.01x faster                                         |
| chaos                    | 60.1 ms                                                                | 59.7 ms: 1.01x faster                                        |
| sqlglot_optimize         | 55.0 ms                                                                | 54.7 ms: 1.01x faster                                        |
| pprint_pformat           | 1.51 sec                                                               | 1.50 sec: 1.00x faster                                       |
| bench_thread_pool        | 828 us                                                                 | 825 us: 1.00x faster                                         |
| sympy_integrate          | 20.1 ms                                                                | 20.0 ms: 1.00x faster                                        |
| asyncio_tcp_ssl          | 1.84 sec                                                               | 1.84 sec: 1.00x slower                                       |
| regex_compile            | 132 ms                                                                 | 133 ms: 1.00x slower                                         |
| async_generators         | 439 ms                                                                 | 441 ms: 1.01x slower                                         |
| pathlib                  | 18.4 ms                                                                | 18.5 ms: 1.01x slower                                        |
| python_startup           | 10.6 ms                                                                | 10.6 ms: 1.01x slower                                        |
| deltablue                | 3.24 ms                                                                | 3.26 ms: 1.01x slower                                        |
| logging_format           | 6.54 us                                                                | 6.59 us: 1.01x slower                                        |
| python_startup_no_site   | 8.93 ms                                                                | 9.00 ms: 1.01x slower                                        |
| xml_etree_process        | 59.3 ms                                                                | 59.8 ms: 1.01x slower                                        |
| json_dumps               | 10.3 ms                                                                | 10.4 ms: 1.01x slower                                        |
| crypto_pyaes             | 72.4 ms                                                                | 73.1 ms: 1.01x slower                                        |
| spectral_norm            | 109 ms                                                                 | 110 ms: 1.01x slower                                         |
| scimark_lu               | 112 ms                                                                 | 114 ms: 1.01x slower                                         |
| scimark_sparse_mat_mult  | 4.88 ms                                                                | 4.95 ms: 1.01x slower                                        |
| create_gc_cycles         | 1.65 ms                                                                | 1.68 ms: 1.01x slower                                        |
| html5lib                 | 66.6 ms                                                                | 67.9 ms: 1.02x slower                                        |
| asyncio_tcp              | 491 ms                                                                 | 501 ms: 1.02x slower                                         |
| regex_v8                 | 25.5 ms                                                                | 26.0 ms: 1.02x slower                                        |
| pycparser                | 1.18 sec                                                               | 1.22 sec: 1.03x slower                                       |
| pickle                   | 11.6 us                                                                | 12.0 us: 1.04x slower                                        |
| unpickle                 | 16.0 us                                                                | 16.7 us: 1.04x slower                                        |
| regex_dna                | 221 ms                                                                 | 230 ms: 1.04x slower                                         |
| mdp                      | 2.58 sec                                                               | 2.70 sec: 1.05x slower                                       |
| regex_effbot             | 3.63 ms                                                                | 3.81 ms: 1.05x slower                                        |
| gc_traversal             | 3.67 ms                                                                | 4.01 ms: 1.09x slower                                        |
| pickle_list              | 4.90 us                                                                | 5.40 us: 1.10x slower                                        |
| pickle_dict              | 32.2 us                                                                | 35.6 us: 1.10x slower                                        |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (43): sympy_str, sqlite_synth, async_tree_cpu_io_mixed, coverage, async_tree_cpu_io_mixed_tg, scimark_sor, nqueens, generators, mypy2, json_loads, sqlglot_normalize, coroutines, sympy_sum, async_tree_io, sqlglot_transpile, hexiom, asyncio_websockets, async_tree_none, xml_etree_parse, pylint, pyflate, tornado_http, tomli_loads, dulwich_log, django_template, bench_mp_pool, xml_etree_iterparse, sympy_expand, 2to3, pprint_safe_repr, docutils, dask, thrift, sqlglot_parse, json, djangocms, gunicorn, telco, async_tree_none_tg, aiohttp, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg


# HPT report

- Reliability score: 54.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x