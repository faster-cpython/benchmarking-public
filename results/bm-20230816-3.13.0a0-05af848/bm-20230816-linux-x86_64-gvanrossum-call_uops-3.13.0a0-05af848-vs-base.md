
# Results vs. base

- fork: gvanrossum
- ref: call_uops
- machine: linux-x86_64
- commit hash: 05af848
- commit date: 2023-08-16
- overall geometric mean: 1.00x faster
- HPT reliability: 93.20%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.62 sec                                                              | 2.63 sec: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                           |
| nbody          | 89.9 ms                                                               | 88.3 ms: 1.02x faster                                          |
| float          | 79.1 ms                                                               | 79.8 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 217 ms: 1.03x faster                                           |
| regex_effbot   | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                          |
| regex_v8       | 23.2 ms                                                               | 23.5 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.0 us                                                               | 14.3 us: 1.05x faster                                          |
| pickle_dict          | 33.0 us                                                               | 32.0 us: 1.03x faster                                          |
| unpickle_pure_python | 215 us                                                                | 211 us: 1.02x faster                                           |
| pickle_pure_python   | 298 us                                                                | 295 us: 1.01x faster                                           |
| xml_etree_parse      | 153 ms                                                                | 152 ms: 1.01x faster                                           |
| json_loads           | 25.4 us                                                               | 25.2 us: 1.01x faster                                          |
| xml_etree_process    | 57.2 ms                                                               | 57.6 ms: 1.01x slower                                          |
| pickle_list          | 4.62 us                                                               | 4.72 us: 1.02x slower                                          |
| unpickle_list        | 4.95 us                                                               | 5.12 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_iterparse, pickle, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.36 ms: 1.00x slower                                          |
| python_startup_no_site | 6.82 ms                                                               | 6.86 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230815-linux-x86_64-python-e28b0dc86dd1d058788b-3.13.0a0-e28b0dc | bm-20230816-linux-x86_64-gvanrossum-call_uops-3.13.0a0-05af848 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpack_sequence          | 48.9 ns                                                               | 42.7 ns: 1.14x faster                                          |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                           |
| unpickle                 | 15.0 us                                                               | 14.3 us: 1.05x faster                                          |
| mdp                      | 2.66 sec                                                              | 2.54 sec: 1.04x faster                                         |
| logging_simple           | 6.02 us                                                               | 5.81 us: 1.04x faster                                          |
| logging_format           | 6.63 us                                                               | 6.41 us: 1.03x faster                                          |
| regex_dna                | 223 ms                                                                | 217 ms: 1.03x faster                                           |
| nqueens                  | 81.4 ms                                                               | 78.9 ms: 1.03x faster                                          |
| pickle_dict              | 33.0 us                                                               | 32.0 us: 1.03x faster                                          |
| coverage                 | 86.2 ms                                                               | 84.6 ms: 1.02x faster                                          |
| scimark_monte_carlo      | 67.2 ms                                                               | 66.0 ms: 1.02x faster                                          |
| nbody                    | 89.9 ms                                                               | 88.3 ms: 1.02x faster                                          |
| unpickle_pure_python     | 215 us                                                                | 211 us: 1.02x faster                                           |
| sqlglot_parse            | 1.30 ms                                                               | 1.28 ms: 1.01x faster                                          |
| comprehensions           | 20.6 us                                                               | 20.4 us: 1.01x faster                                          |
| async_generators         | 457 ms                                                                | 452 ms: 1.01x faster                                           |
| typing_runtime_protocols | 144 us                                                                | 142 us: 1.01x faster                                           |
| pickle_pure_python       | 298 us                                                                | 295 us: 1.01x faster                                           |
| deepcopy_reduce          | 3.17 us                                                               | 3.14 us: 1.01x faster                                          |
| xml_etree_parse          | 153 ms                                                                | 152 ms: 1.01x faster                                           |
| json_loads               | 25.4 us                                                               | 25.2 us: 1.01x faster                                          |
| sqlglot_normalize        | 105 ms                                                                | 105 ms: 1.01x faster                                           |
| deepcopy                 | 351 us                                                                | 349 us: 1.01x faster                                           |
| sqlglot_optimize         | 52.7 ms                                                               | 52.6 ms: 1.00x faster                                          |
| dulwich_log              | 65.7 ms                                                               | 65.8 ms: 1.00x slower                                          |
| docutils                 | 2.62 sec                                                              | 2.63 sec: 1.00x slower                                         |
| python_startup           | 9.33 ms                                                               | 9.36 ms: 1.00x slower                                          |
| fannkuch                 | 388 ms                                                                | 390 ms: 1.00x slower                                           |
| go                       | 139 ms                                                                | 140 ms: 1.00x slower                                           |
| python_startup_no_site   | 6.82 ms                                                               | 6.86 ms: 1.00x slower                                          |
| pprint_pformat           | 1.47 sec                                                              | 1.48 sec: 1.01x slower                                         |
| pycparser                | 1.20 sec                                                              | 1.21 sec: 1.01x slower                                         |
| hexiom                   | 5.99 ms                                                               | 6.03 ms: 1.01x slower                                          |
| xml_etree_process        | 57.2 ms                                                               | 57.6 ms: 1.01x slower                                          |
| async_tree_io            | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                         |
| deepcopy_memo            | 36.7 us                                                               | 37.0 us: 1.01x slower                                          |
| float                    | 79.1 ms                                                               | 79.8 ms: 1.01x slower                                          |
| telco                    | 8.00 ms                                                               | 8.08 ms: 1.01x slower                                          |
| create_gc_cycles         | 1.47 ms                                                               | 1.48 ms: 1.01x slower                                          |
| scimark_fft              | 350 ms                                                                | 355 ms: 1.01x slower                                           |
| crypto_pyaes             | 68.7 ms                                                               | 69.6 ms: 1.01x slower                                          |
| regex_effbot             | 3.69 ms                                                               | 3.74 ms: 1.01x slower                                          |
| regex_v8                 | 23.2 ms                                                               | 23.5 ms: 1.02x slower                                          |
| spectral_norm            | 105 ms                                                                | 107 ms: 1.02x slower                                           |
| deltablue                | 3.24 ms                                                               | 3.29 ms: 1.02x slower                                          |
| json                     | 4.84 ms                                                               | 4.92 ms: 1.02x slower                                          |
| pickle_list              | 4.62 us                                                               | 4.72 us: 1.02x slower                                          |
| scimark_lu               | 108 ms                                                                | 112 ms: 1.03x slower                                           |
| logging_silent           | 100 ns                                                                | 104 ns: 1.03x slower                                           |
| unpickle_list            | 4.95 us                                                               | 5.12 us: 1.04x slower                                          |
| scimark_sparse_mat_mult  | 4.51 ms                                                               | 4.94 ms: 1.09x slower                                          |
| gc_traversal             | 3.65 ms                                                               | 4.06 ms: 1.11x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (30): sqlglot_transpile, tornado_http, tomli_loads, asyncio_tcp, generators, bench_thread_pool, richards, scimark_sor, xml_etree_iterparse, sqlite_synth, mako, bench_mp_pool, chaos, asyncio_tcp_ssl, pickle, xml_etree_generate, pathlib, async_tree_memoization, json_dumps, pyflate, dask, raytrace, regex_compile, pprint_safe_repr, mypy2, meteor_contest, async_tree_none, richards_super, async_tree_cpu_io_mixed, coroutines


# HPT report

- Reliability score: 93.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
