
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.02x slower
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.72 sec                                                              | 2.71 sec: 1.01x faster                                        |
| tornado_http   | 102 ms                                                                | 98.7 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 192 ms: 1.02x faster                                          |
| nbody          | 90.3 ms                                                               | 96.3 ms: 1.07x slower                                         |
| float          | 80.0 ms                                                               | 91.2 ms: 1.14x slower                                         |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 201 ms: 1.04x faster                                          |
| regex_effbot   | 3.51 ms                                                               | 3.41 ms: 1.03x faster                                         |
| regex_compile  | 145 ms                                                                | 142 ms: 1.02x faster                                          |
| regex_v8       | 22.0 ms                                                               | 22.3 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle               | 10.9 us                                                               | 10.6 us: 1.03x faster                                         |
| unpickle_list        | 4.97 us                                                               | 4.86 us: 1.02x faster                                         |
| pickle_list          | 4.70 us                                                               | 4.62 us: 1.02x faster                                         |
| json_dumps           | 9.92 ms                                                               | 9.76 ms: 1.02x faster                                         |
| pickle_dict          | 31.4 us                                                               | 31.1 us: 1.01x faster                                         |
| xml_etree_process    | 59.3 ms                                                               | 58.8 ms: 1.01x faster                                         |
| pickle_pure_python   | 316 us                                                                | 317 us: 1.01x slower                                          |
| unpickle_pure_python | 218 us                                                                | 221 us: 1.02x slower                                          |
| unpickle             | 14.9 us                                                               | 15.2 us: 1.02x slower                                         |
| xml_etree_generate   | 84.9 ms                                                               | 86.8 ms: 1.02x slower                                         |
| tomli_loads          | 2.27 sec                                                              | 2.47 sec: 1.09x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 9.26 ms                                                               | 9.48 ms: 1.02x slower                                         |
| python_startup_no_site | 6.72 ms                                                               | 6.90 ms: 1.03x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 13.4 ms: 1.25x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 | bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 54.8 ns                                                               | 43.2 ns: 1.27x faster                                         |
| logging_format           | 7.07 us                                                               | 6.55 us: 1.08x faster                                         |
| logging_simple           | 6.37 us                                                               | 5.99 us: 1.06x faster                                         |
| generators               | 31.0 ms                                                               | 29.4 ms: 1.06x faster                                         |
| regex_dna                | 208 ms                                                                | 201 ms: 1.04x faster                                          |
| tornado_http             | 102 ms                                                                | 98.7 ms: 1.03x faster                                         |
| dulwich_log              | 67.7 ms                                                               | 65.5 ms: 1.03x faster                                         |
| regex_effbot             | 3.51 ms                                                               | 3.41 ms: 1.03x faster                                         |
| pickle                   | 10.9 us                                                               | 10.6 us: 1.03x faster                                         |
| coverage                 | 96.1 ms                                                               | 93.8 ms: 1.03x faster                                         |
| unpickle_list            | 4.97 us                                                               | 4.86 us: 1.02x faster                                         |
| pidigits                 | 196 ms                                                                | 192 ms: 1.02x faster                                          |
| pycparser                | 1.19 sec                                                              | 1.17 sec: 1.02x faster                                        |
| pickle_list              | 4.70 us                                                               | 4.62 us: 1.02x faster                                         |
| regex_compile            | 145 ms                                                                | 142 ms: 1.02x faster                                          |
| sqlglot_normalize        | 110 ms                                                                | 108 ms: 1.02x faster                                          |
| json_dumps               | 9.92 ms                                                               | 9.76 ms: 1.02x faster                                         |
| dask                     | 536 ms                                                                | 529 ms: 1.01x faster                                          |
| asyncio_tcp              | 515 ms                                                                | 509 ms: 1.01x faster                                          |
| pickle_dict              | 31.4 us                                                               | 31.1 us: 1.01x faster                                         |
| xml_etree_process        | 59.3 ms                                                               | 58.8 ms: 1.01x faster                                         |
| mdp                      | 2.58 sec                                                              | 2.57 sec: 1.01x faster                                        |
| docutils                 | 2.72 sec                                                              | 2.71 sec: 1.01x faster                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                        |
| async_generators         | 447 ms                                                                | 449 ms: 1.00x slower                                          |
| pickle_pure_python       | 316 us                                                                | 317 us: 1.01x slower                                          |
| deepcopy_reduce          | 3.17 us                                                               | 3.19 us: 1.01x slower                                         |
| scimark_monte_carlo      | 71.8 ms                                                               | 72.6 ms: 1.01x slower                                         |
| meteor_contest           | 104 ms                                                                | 106 ms: 1.01x slower                                          |
| async_tree_none          | 493 ms                                                                | 499 ms: 1.01x slower                                          |
| async_tree_memoization   | 599 ms                                                                | 606 ms: 1.01x slower                                          |
| regex_v8                 | 22.0 ms                                                               | 22.3 ms: 1.01x slower                                         |
| pprint_pformat           | 1.50 sec                                                              | 1.52 sec: 1.01x slower                                        |
| async_tree_io            | 1.22 sec                                                              | 1.24 sec: 1.01x slower                                        |
| richards_super           | 50.5 ms                                                               | 51.2 ms: 1.01x slower                                         |
| telco                    | 6.88 ms                                                               | 6.98 ms: 1.02x slower                                         |
| raytrace                 | 295 ms                                                                | 299 ms: 1.02x slower                                          |
| sqlite_synth             | 2.73 us                                                               | 2.77 us: 1.02x slower                                         |
| bench_thread_pool        | 825 us                                                                | 839 us: 1.02x slower                                          |
| unpickle_pure_python     | 218 us                                                                | 221 us: 1.02x slower                                          |
| richards                 | 44.2 ms                                                               | 45.0 ms: 1.02x slower                                         |
| coroutines               | 22.3 ms                                                               | 22.7 ms: 1.02x slower                                         |
| chaos                    | 63.4 ms                                                               | 64.6 ms: 1.02x slower                                         |
| typing_runtime_protocols | 144 us                                                                | 146 us: 1.02x slower                                          |
| scimark_sparse_mat_mult  | 5.00 ms                                                               | 5.10 ms: 1.02x slower                                         |
| pathlib                  | 18.6 ms                                                               | 18.9 ms: 1.02x slower                                         |
| sqlglot_transpile        | 1.67 ms                                                               | 1.71 ms: 1.02x slower                                         |
| unpickle                 | 14.9 us                                                               | 15.2 us: 1.02x slower                                         |
| xml_etree_generate       | 84.9 ms                                                               | 86.8 ms: 1.02x slower                                         |
| python_startup           | 9.26 ms                                                               | 9.48 ms: 1.02x slower                                         |
| python_startup_no_site   | 6.72 ms                                                               | 6.90 ms: 1.03x slower                                         |
| sqlglot_parse            | 1.34 ms                                                               | 1.38 ms: 1.03x slower                                         |
| scimark_fft              | 360 ms                                                                | 371 ms: 1.03x slower                                          |
| scimark_sor              | 123 ms                                                                | 128 ms: 1.04x slower                                          |
| spectral_norm            | 106 ms                                                                | 111 ms: 1.05x slower                                          |
| gc_traversal             | 4.07 ms                                                               | 4.32 ms: 1.06x slower                                         |
| nbody                    | 90.3 ms                                                               | 96.3 ms: 1.07x slower                                         |
| nqueens                  | 80.9 ms                                                               | 86.7 ms: 1.07x slower                                         |
| go                       | 134 ms                                                                | 144 ms: 1.07x slower                                          |
| tomli_loads              | 2.27 sec                                                              | 2.47 sec: 1.09x slower                                        |
| pyflate                  | 442 ms                                                                | 480 ms: 1.09x slower                                          |
| deltablue                | 3.46 ms                                                               | 3.79 ms: 1.09x slower                                         |
| logging_silent           | 100 ns                                                                | 110 ns: 1.09x slower                                          |
| hexiom                   | 6.11 ms                                                               | 6.82 ms: 1.12x slower                                         |
| crypto_pyaes             | 78.9 ms                                                               | 88.5 ms: 1.12x slower                                         |
| float                    | 80.0 ms                                                               | 91.2 ms: 1.14x slower                                         |
| fannkuch                 | 392 ms                                                                | 448 ms: 1.14x slower                                          |
| comprehensions           | 20.6 us                                                               | 24.7 us: 1.20x slower                                         |
| scimark_lu               | 114 ms                                                                | 142 ms: 1.25x slower                                          |
| mako                     | 10.8 ms                                                               | 13.4 ms: 1.25x slower                                         |
| deepcopy_memo            | 37.7 us                                                               | 53.6 us: 1.42x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (11): xml_etree_iterparse, create_gc_cycles, mypy2, bench_mp_pool, json_loads, sqlglot_optimize, json, pprint_safe_repr, xml_etree_parse, deepcopy, async_tree_cpu_io_mixed


# HPT report

- Reliability score: 99.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
