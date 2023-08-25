
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.01x slower
- HPT reliability: 88.75%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.72 sec                                                              | 2.70 sec: 1.01x faster                                        |
| tornado_http   | 102 ms                                                                | 98.5 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 198 ms: 1.01x slower                                          |
| nbody          | 90.3 ms                                                               | 94.2 ms: 1.04x slower                                         |
| float          | 80.0 ms                                                               | 87.3 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 145 ms                                                                | 141 ms: 1.02x faster                                          |
| regex_effbot   | 3.51 ms                                                               | 3.53 ms: 1.00x slower                                         |
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                          |
| regex_v8       | 22.0 ms                                                               | 22.4 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_list          | 4.70 us                                                               | 4.44 us: 1.06x faster                                         |
| pickle               | 10.9 us                                                               | 10.5 us: 1.03x faster                                         |
| xml_etree_process    | 59.3 ms                                                               | 58.5 ms: 1.01x faster                                         |
| xml_etree_iterparse  | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| xml_etree_parse      | 153 ms                                                                | 152 ms: 1.01x faster                                          |
| pickle_pure_python   | 316 us                                                                | 313 us: 1.01x faster                                          |
| json_dumps           | 9.92 ms                                                               | 9.85 ms: 1.01x faster                                         |
| unpickle_pure_python | 218 us                                                                | 216 us: 1.01x faster                                          |
| xml_etree_generate   | 84.9 ms                                                               | 85.2 ms: 1.00x slower                                         |
| pickle_dict          | 31.4 us                                                               | 31.7 us: 1.01x slower                                         |
| json_loads           | 24.9 us                                                               | 25.3 us: 1.01x slower                                         |
| tomli_loads          | 2.27 sec                                                              | 2.37 sec: 1.04x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 9.26 ms                                                               | 9.46 ms: 1.02x slower                                         |
| python_startup_no_site | 6.72 ms                                                               | 6.88 ms: 1.02x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 12.3 ms: 1.15x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 54.8 ns                                                               | 46.1 ns: 1.19x faster                                         |
| logging_format           | 7.07 us                                                               | 6.55 us: 1.08x faster                                         |
| generators               | 31.0 ms                                                               | 28.8 ms: 1.08x faster                                         |
| pickle_list              | 4.70 us                                                               | 4.44 us: 1.06x faster                                         |
| pycparser                | 1.19 sec                                                              | 1.13 sec: 1.06x faster                                        |
| logging_simple           | 6.37 us                                                               | 6.05 us: 1.05x faster                                         |
| dulwich_log              | 67.7 ms                                                               | 65.2 ms: 1.04x faster                                         |
| tornado_http             | 102 ms                                                                | 98.5 ms: 1.04x faster                                         |
| pickle                   | 10.9 us                                                               | 10.5 us: 1.03x faster                                         |
| dask                     | 536 ms                                                                | 523 ms: 1.02x faster                                          |
| deepcopy                 | 361 us                                                                | 352 us: 1.02x faster                                          |
| regex_compile            | 145 ms                                                                | 141 ms: 1.02x faster                                          |
| sqlglot_normalize        | 110 ms                                                                | 107 ms: 1.02x faster                                          |
| asyncio_tcp              | 515 ms                                                                | 505 ms: 1.02x faster                                          |
| xml_etree_process        | 59.3 ms                                                               | 58.5 ms: 1.01x faster                                         |
| pprint_safe_repr         | 741 ms                                                                | 731 ms: 1.01x faster                                          |
| coverage                 | 96.1 ms                                                               | 94.9 ms: 1.01x faster                                         |
| sqlglot_optimize         | 54.1 ms                                                               | 53.5 ms: 1.01x faster                                         |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| deepcopy_reduce          | 3.17 us                                                               | 3.14 us: 1.01x faster                                         |
| xml_etree_parse          | 153 ms                                                                | 152 ms: 1.01x faster                                          |
| create_gc_cycles         | 1.49 ms                                                               | 1.48 ms: 1.01x faster                                         |
| pickle_pure_python       | 316 us                                                                | 313 us: 1.01x faster                                          |
| docutils                 | 2.72 sec                                                              | 2.70 sec: 1.01x faster                                        |
| async_tree_io            | 1.22 sec                                                              | 1.21 sec: 1.01x faster                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                        |
| json_dumps               | 9.92 ms                                                               | 9.85 ms: 1.01x faster                                         |
| mypy2                    | 343 ms                                                                | 341 ms: 1.01x faster                                          |
| unpickle_pure_python     | 218 us                                                                | 216 us: 1.01x faster                                          |
| pprint_pformat           | 1.50 sec                                                              | 1.49 sec: 1.00x faster                                        |
| xml_etree_generate       | 84.9 ms                                                               | 85.2 ms: 1.00x slower                                         |
| bench_thread_pool        | 825 us                                                                | 829 us: 1.00x slower                                          |
| coroutines               | 22.3 ms                                                               | 22.4 ms: 1.00x slower                                         |
| regex_effbot             | 3.51 ms                                                               | 3.53 ms: 1.00x slower                                         |
| raytrace                 | 295 ms                                                                | 296 ms: 1.01x slower                                          |
| pidigits                 | 196 ms                                                                | 198 ms: 1.01x slower                                          |
| scimark_sor              | 123 ms                                                                | 124 ms: 1.01x slower                                          |
| sqlite_synth             | 2.73 us                                                               | 2.75 us: 1.01x slower                                         |
| regex_dna                | 208 ms                                                                | 210 ms: 1.01x slower                                          |
| pickle_dict              | 31.4 us                                                               | 31.7 us: 1.01x slower                                         |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.01x slower                                          |
| scimark_monte_carlo      | 71.8 ms                                                               | 72.7 ms: 1.01x slower                                         |
| sqlglot_parse            | 1.34 ms                                                               | 1.36 ms: 1.01x slower                                         |
| json_loads               | 24.9 us                                                               | 25.3 us: 1.01x slower                                         |
| chaos                    | 63.4 ms                                                               | 64.6 ms: 1.02x slower                                         |
| regex_v8                 | 22.0 ms                                                               | 22.4 ms: 1.02x slower                                         |
| richards_super           | 50.5 ms                                                               | 51.5 ms: 1.02x slower                                         |
| typing_runtime_protocols | 144 us                                                                | 147 us: 1.02x slower                                          |
| python_startup           | 9.26 ms                                                               | 9.46 ms: 1.02x slower                                         |
| richards                 | 44.2 ms                                                               | 45.2 ms: 1.02x slower                                         |
| python_startup_no_site   | 6.72 ms                                                               | 6.88 ms: 1.02x slower                                         |
| async_generators         | 447 ms                                                                | 458 ms: 1.02x slower                                          |
| spectral_norm            | 106 ms                                                                | 108 ms: 1.03x slower                                          |
| deltablue                | 3.46 ms                                                               | 3.56 ms: 1.03x slower                                         |
| mdp                      | 2.58 sec                                                              | 2.67 sec: 1.03x slower                                        |
| scimark_fft              | 360 ms                                                                | 372 ms: 1.03x slower                                          |
| scimark_sparse_mat_mult  | 5.00 ms                                                               | 5.19 ms: 1.04x slower                                         |
| tomli_loads              | 2.27 sec                                                              | 2.37 sec: 1.04x slower                                        |
| nbody                    | 90.3 ms                                                               | 94.2 ms: 1.04x slower                                         |
| go                       | 134 ms                                                                | 141 ms: 1.05x slower                                          |
| nqueens                  | 80.9 ms                                                               | 85.0 ms: 1.05x slower                                         |
| logging_silent           | 100 ns                                                                | 106 ns: 1.05x slower                                          |
| hexiom                   | 6.11 ms                                                               | 6.58 ms: 1.08x slower                                         |
| pyflate                  | 442 ms                                                                | 476 ms: 1.08x slower                                          |
| float                    | 80.0 ms                                                               | 87.3 ms: 1.09x slower                                         |
| crypto_pyaes             | 78.9 ms                                                               | 87.2 ms: 1.11x slower                                         |
| fannkuch                 | 392 ms                                                                | 437 ms: 1.11x slower                                          |
| comprehensions           | 20.6 us                                                               | 23.2 us: 1.12x slower                                         |
| scimark_lu               | 114 ms                                                                | 131 ms: 1.14x slower                                          |
| mako                     | 10.8 ms                                                               | 12.3 ms: 1.15x slower                                         |
| deepcopy_memo            | 37.7 us                                                               | 48.6 us: 1.29x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (11): telco, async_tree_none, async_tree_memoization, bench_mp_pool, gc_traversal, unpickle_list, json, async_tree_cpu_io_mixed, pathlib, sqlglot_transpile, unpickle


# HPT report

- Reliability score: 88.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
