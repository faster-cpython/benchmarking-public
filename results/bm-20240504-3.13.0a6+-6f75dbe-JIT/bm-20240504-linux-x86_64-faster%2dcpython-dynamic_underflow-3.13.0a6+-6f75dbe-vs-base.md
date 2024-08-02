# Results vs. base

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.01x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 285 ms: 1.02x slower                                                          |
| chameleon      | 7.24 ms                                                                | 7.31 ms: 1.01x slower                                                         |
| html5lib       | 70.1 ms                                                                | 70.6 ms: 1.01x slower                                                         |
| tornado_http   | 97.5 ms                                                                | 105 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 81.7 ms                                                                | 79.6 ms: 1.03x faster                                                         |
| float          | 72.8 ms                                                                | 73.2 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                                | 3.71 ms: 1.03x faster                                                         |
| regex_dna      | 231 ms                                                                 | 227 ms: 1.02x faster                                                          |
| regex_v8       | 25.5 ms                                                                | 25.2 ms: 1.01x faster                                                         |
| regex_compile  | 140 ms                                                                 | 143 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list          | 5.23 us                                                                | 4.92 us: 1.06x faster                                                         |
| unpickle_pure_python | 222 us                                                                 | 209 us: 1.06x faster                                                          |
| pickle_dict          | 36.6 us                                                                | 35.0 us: 1.04x faster                                                         |
| unpickle_list        | 5.39 us                                                                | 5.26 us: 1.03x faster                                                         |
| pickle               | 12.1 us                                                                | 11.9 us: 1.01x faster                                                         |
| pickle_pure_python   | 302 us                                                                 | 299 us: 1.01x faster                                                          |
| xml_etree_generate   | 84.6 ms                                                                | 83.9 ms: 1.01x faster                                                         |
| xml_etree_process    | 58.9 ms                                                                | 58.4 ms: 1.01x faster                                                         |
| json_dumps           | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                         |
| tomli_loads          | 1.98 sec                                                               | 2.02 sec: 1.02x slower                                                        |
| unpickle             | 15.1 us                                                                | 15.5 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                  |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.64 ms                                                                | 7.65 ms: 1.00x slower                                                         |
| python_startup         | 11.1 ms                                                                | 11.1 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text    | 25.1 ms                                                                | 23.5 ms: 1.07x faster                                                         |
| genshi_xml     | 57.9 ms                                                                | 62.7 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                | bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| logging_silent           | 106 ns                                                                 | 98.0 ns: 1.08x faster                                                         |
| mdp                      | 2.80 sec                                                               | 2.59 sec: 1.08x faster                                                        |
| genshi_text              | 25.1 ms                                                                | 23.5 ms: 1.07x faster                                                         |
| pickle_list              | 5.23 us                                                                | 4.92 us: 1.06x faster                                                         |
| unpickle_pure_python     | 222 us                                                                 | 209 us: 1.06x faster                                                          |
| scimark_monte_carlo      | 64.5 ms                                                                | 61.6 ms: 1.05x faster                                                         |
| pickle_dict              | 36.6 us                                                                | 35.0 us: 1.04x faster                                                         |
| nqueens                  | 87.8 ms                                                                | 84.7 ms: 1.04x faster                                                         |
| gc_traversal             | 3.99 ms                                                                | 3.86 ms: 1.03x faster                                                         |
| regex_effbot             | 3.83 ms                                                                | 3.71 ms: 1.03x faster                                                         |
| deepcopy_reduce          | 3.34 us                                                                | 3.24 us: 1.03x faster                                                         |
| nbody                    | 81.7 ms                                                                | 79.6 ms: 1.03x faster                                                         |
| unpickle_list            | 5.39 us                                                                | 5.26 us: 1.03x faster                                                         |
| typing_runtime_protocols | 178 us                                                                 | 174 us: 1.02x faster                                                          |
| deepcopy                 | 375 us                                                                 | 367 us: 1.02x faster                                                          |
| chaos                    | 58.8 ms                                                                | 57.5 ms: 1.02x faster                                                         |
| async_generators         | 473 ms                                                                 | 463 ms: 1.02x faster                                                          |
| go                       | 149 ms                                                                 | 146 ms: 1.02x faster                                                          |
| pycparser                | 1.21 sec                                                               | 1.18 sec: 1.02x faster                                                        |
| regex_dna                | 231 ms                                                                 | 227 ms: 1.02x faster                                                          |
| raytrace                 | 277 ms                                                                 | 273 ms: 1.02x faster                                                          |
| comprehensions           | 16.8 us                                                                | 16.6 us: 1.01x faster                                                         |
| regex_v8                 | 25.5 ms                                                                | 25.2 ms: 1.01x faster                                                         |
| pickle                   | 12.1 us                                                                | 11.9 us: 1.01x faster                                                         |
| json                     | 5.17 ms                                                                | 5.11 ms: 1.01x faster                                                         |
| create_gc_cycles         | 1.87 ms                                                                | 1.85 ms: 1.01x faster                                                         |
| pickle_pure_python       | 302 us                                                                 | 299 us: 1.01x faster                                                          |
| xml_etree_generate       | 84.6 ms                                                                | 83.9 ms: 1.01x faster                                                         |
| xml_etree_process        | 58.9 ms                                                                | 58.4 ms: 1.01x faster                                                         |
| json_dumps               | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                         |
| pyflate                  | 450 ms                                                                 | 447 ms: 1.01x faster                                                          |
| meteor_contest           | 108 ms                                                                 | 108 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl          | 1.87 sec                                                               | 1.86 sec: 1.00x faster                                                        |
| python_startup_no_site   | 7.64 ms                                                                | 7.65 ms: 1.00x slower                                                         |
| python_startup           | 11.1 ms                                                                | 11.1 ms: 1.00x slower                                                         |
| float                    | 72.8 ms                                                                | 73.2 ms: 1.01x slower                                                         |
| html5lib                 | 70.1 ms                                                                | 70.6 ms: 1.01x slower                                                         |
| coroutines               | 24.3 ms                                                                | 24.5 ms: 1.01x slower                                                         |
| generators               | 30.1 ms                                                                | 30.3 ms: 1.01x slower                                                         |
| chameleon                | 7.24 ms                                                                | 7.31 ms: 1.01x slower                                                         |
| pathlib                  | 17.6 ms                                                                | 17.8 ms: 1.01x slower                                                         |
| bench_thread_pool        | 872 us                                                                 | 882 us: 1.01x slower                                                          |
| deepcopy_memo            | 37.6 us                                                                | 38.1 us: 1.01x slower                                                         |
| dask                     | 378 ms                                                                 | 383 ms: 1.01x slower                                                          |
| scimark_fft              | 317 ms                                                                 | 322 ms: 1.02x slower                                                          |
| regex_compile            | 140 ms                                                                 | 143 ms: 1.02x slower                                                          |
| tomli_loads              | 1.98 sec                                                               | 2.02 sec: 1.02x slower                                                        |
| 2to3                     | 279 ms                                                                 | 285 ms: 1.02x slower                                                          |
| flaskblogging            | 9.34 ms                                                                | 9.55 ms: 1.02x slower                                                         |
| logging_simple           | 5.79 us                                                                | 5.92 us: 1.02x slower                                                         |
| sqlglot_optimize         | 56.9 ms                                                                | 58.2 ms: 1.02x slower                                                         |
| logging_format           | 6.42 us                                                                | 6.58 us: 1.02x slower                                                         |
| unpickle                 | 15.1 us                                                                | 15.5 us: 1.03x slower                                                         |
| fannkuch                 | 360 ms                                                                 | 371 ms: 1.03x slower                                                          |
| scimark_lu               | 125 ms                                                                 | 129 ms: 1.03x slower                                                          |
| sqlglot_transpile        | 1.65 ms                                                                | 1.70 ms: 1.03x slower                                                         |
| asyncio_tcp              | 511 ms                                                                 | 530 ms: 1.04x slower                                                          |
| scimark_sparse_mat_mult  | 4.55 ms                                                                | 4.71 ms: 1.04x slower                                                         |
| sympy_expand             | 509 ms                                                                 | 528 ms: 1.04x slower                                                          |
| sqlglot_normalize        | 114 ms                                                                 | 119 ms: 1.04x slower                                                          |
| richards_super           | 49.2 ms                                                                | 51.5 ms: 1.05x slower                                                         |
| sympy_integrate          | 22.5 ms                                                                | 23.6 ms: 1.05x slower                                                         |
| aiohttp                  | 1.25 ms                                                                | 1.31 ms: 1.05x slower                                                         |
| spectral_norm            | 95.8 ms                                                                | 101 ms: 1.05x slower                                                          |
| sympy_str                | 301 ms                                                                 | 317 ms: 1.05x slower                                                          |
| gunicorn                 | 1.35 ms                                                                | 1.43 ms: 1.06x slower                                                         |
| pprint_pformat           | 1.46 sec                                                               | 1.55 sec: 1.06x slower                                                        |
| pprint_safe_repr         | 709 ms                                                                 | 751 ms: 1.06x slower                                                          |
| richards                 | 43.1 ms                                                                | 45.9 ms: 1.06x slower                                                         |
| sympy_sum                | 173 ms                                                                 | 184 ms: 1.07x slower                                                          |
| dulwich_log              | 69.8 ms                                                                | 74.4 ms: 1.07x slower                                                         |
| tornado_http             | 97.5 ms                                                                | 105 ms: 1.07x slower                                                          |
| scimark_sor              | 131 ms                                                                 | 142 ms: 1.08x slower                                                          |
| genshi_xml               | 57.9 ms                                                                | 62.7 ms: 1.08x slower                                                         |
| deltablue                | 3.76 ms                                                                | 4.21 ms: 1.12x slower                                                         |
| mypy2                    | 821 ms                                                                 | 926 ms: 1.13x slower                                                          |
| pylint                   | 356 ms                                                                 | 409 ms: 1.15x slower                                                          |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (24): asyncio_websockets, django_template, telco, coverage, crypto_pyaes, thrift, json_loads, async_tree_cpu_io_mixed, bench_mp_pool, pidigits, async_tree_none, xml_etree_iterparse, mako, hexiom, sqlite_synth, async_tree_cpu_io_mixed_tg, async_tree_none_tg, sqlglot_parse, async_tree_memoization_tg, xml_etree_parse, async_tree_io, djangocms, async_tree_memoization, async_tree_io_tg

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x