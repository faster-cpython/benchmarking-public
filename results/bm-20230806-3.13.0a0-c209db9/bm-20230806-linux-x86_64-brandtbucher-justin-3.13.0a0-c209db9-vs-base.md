
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.75 sec: 1.04x slower                                        |
| tornado_http   | 95.2 ms                                                               | 97.3 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 200 ms: 1.00x faster                                          |
| float          | 79.3 ms                                                               | 84.4 ms: 1.07x slower                                         |
| nbody          | 88.0 ms                                                               | 102 ms: 1.15x slower                                          |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                               | 3.39 ms: 1.04x faster                                         |
| regex_v8       | 22.6 ms                                                               | 22.0 ms: 1.03x faster                                         |
| regex_dna      | 204 ms                                                                | 200 ms: 1.02x faster                                          |
| regex_compile  | 136 ms                                                                | 150 ms: 1.11x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_parse      | 155 ms                                                                | 152 ms: 1.02x faster                                          |
| pickle_pure_python   | 297 us                                                                | 300 us: 1.01x slower                                          |
| pickle               | 10.3 us                                                               | 10.5 us: 1.02x slower                                         |
| xml_etree_process    | 57.8 ms                                                               | 59.0 ms: 1.02x slower                                         |
| json_dumps           | 9.64 ms                                                               | 9.89 ms: 1.03x slower                                         |
| xml_etree_iterparse  | 103 ms                                                                | 106 ms: 1.03x slower                                          |
| xml_etree_generate   | 83.6 ms                                                               | 86.1 ms: 1.03x slower                                         |
| unpickle_pure_python | 212 us                                                                | 222 us: 1.04x slower                                          |
| tomli_loads          | 2.29 sec                                                              | 2.58 sec: 1.13x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (5): unpickle, unpickle_list, pickle_dict, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 9.38 ms                                                               | 9.39 ms: 1.00x slower                                         |
| python_startup_no_site | 6.87 ms                                                               | 6.88 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 12.1 ms: 1.12x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot             | 3.52 ms                                                               | 3.39 ms: 1.04x faster                                         |
| regex_v8                 | 22.6 ms                                                               | 22.0 ms: 1.03x faster                                         |
| regex_dna                | 204 ms                                                                | 200 ms: 1.02x faster                                          |
| xml_etree_parse          | 155 ms                                                                | 152 ms: 1.02x faster                                          |
| coverage                 | 95.2 ms                                                               | 93.8 ms: 1.01x faster                                         |
| create_gc_cycles         | 1.52 ms                                                               | 1.51 ms: 1.01x faster                                         |
| pidigits                 | 201 ms                                                                | 200 ms: 1.00x faster                                          |
| python_startup           | 9.38 ms                                                               | 9.39 ms: 1.00x slower                                         |
| python_startup_no_site   | 6.87 ms                                                               | 6.88 ms: 1.00x slower                                         |
| richards                 | 48.4 ms                                                               | 48.7 ms: 1.01x slower                                         |
| async_tree_io            | 1.19 sec                                                              | 1.19 sec: 1.01x slower                                        |
| generators               | 28.9 ms                                                               | 29.1 ms: 1.01x slower                                         |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                        |
| pickle_pure_python       | 297 us                                                                | 300 us: 1.01x slower                                          |
| logging_format           | 6.48 us                                                               | 6.56 us: 1.01x slower                                         |
| logging_simple           | 5.94 us                                                               | 6.01 us: 1.01x slower                                         |
| async_tree_cpu_io_mixed  | 721 ms                                                                | 732 ms: 1.01x slower                                          |
| deepcopy                 | 357 us                                                                | 362 us: 1.01x slower                                          |
| scimark_monte_carlo      | 67.8 ms                                                               | 68.9 ms: 1.02x slower                                         |
| json                     | 4.77 ms                                                               | 4.86 ms: 1.02x slower                                         |
| async_tree_memoization   | 584 ms                                                                | 594 ms: 1.02x slower                                          |
| pickle                   | 10.3 us                                                               | 10.5 us: 1.02x slower                                         |
| sqlite_synth             | 2.75 us                                                               | 2.80 us: 1.02x slower                                         |
| xml_etree_process        | 57.8 ms                                                               | 59.0 ms: 1.02x slower                                         |
| tornado_http             | 95.2 ms                                                               | 97.3 ms: 1.02x slower                                         |
| dulwich_log              | 65.5 ms                                                               | 67.2 ms: 1.03x slower                                         |
| json_dumps               | 9.64 ms                                                               | 9.89 ms: 1.03x slower                                         |
| dask                     | 518 ms                                                                | 532 ms: 1.03x slower                                          |
| pycparser                | 1.16 sec                                                              | 1.19 sec: 1.03x slower                                        |
| sqlglot_normalize        | 105 ms                                                                | 108 ms: 1.03x slower                                          |
| asyncio_tcp              | 476 ms                                                                | 490 ms: 1.03x slower                                          |
| async_tree_none          | 479 ms                                                                | 493 ms: 1.03x slower                                          |
| xml_etree_iterparse      | 103 ms                                                                | 106 ms: 1.03x slower                                          |
| sqlglot_transpile        | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                         |
| sqlglot_parse            | 1.28 ms                                                               | 1.32 ms: 1.03x slower                                         |
| xml_etree_generate       | 83.6 ms                                                               | 86.1 ms: 1.03x slower                                         |
| richards_super           | 54.2 ms                                                               | 55.9 ms: 1.03x slower                                         |
| telco                    | 7.79 ms                                                               | 8.05 ms: 1.03x slower                                         |
| coroutines               | 21.7 ms                                                               | 22.4 ms: 1.03x slower                                         |
| raytrace                 | 271 ms                                                                | 280 ms: 1.03x slower                                          |
| spectral_norm            | 105 ms                                                                | 109 ms: 1.03x slower                                          |
| pathlib                  | 18.4 ms                                                               | 19.1 ms: 1.04x slower                                         |
| scimark_sor              | 120 ms                                                                | 125 ms: 1.04x slower                                          |
| sqlglot_optimize         | 52.7 ms                                                               | 54.6 ms: 1.04x slower                                         |
| gc_traversal             | 3.84 ms                                                               | 3.99 ms: 1.04x slower                                         |
| pprint_safe_repr         | 713 ms                                                                | 741 ms: 1.04x slower                                          |
| pprint_pformat           | 1.46 sec                                                              | 1.52 sec: 1.04x slower                                        |
| unpickle_pure_python     | 212 us                                                                | 222 us: 1.04x slower                                          |
| docutils                 | 2.64 sec                                                              | 2.75 sec: 1.04x slower                                        |
| scimark_lu               | 113 ms                                                                | 118 ms: 1.04x slower                                          |
| mypy2                    | 334 ms                                                                | 350 ms: 1.05x slower                                          |
| bench_thread_pool        | 823 us                                                                | 864 us: 1.05x slower                                          |
| crypto_pyaes             | 70.2 ms                                                               | 73.8 ms: 1.05x slower                                         |
| async_generators         | 443 ms                                                                | 466 ms: 1.05x slower                                          |
| go                       | 139 ms                                                                | 147 ms: 1.06x slower                                          |
| typing_runtime_protocols | 143 us                                                                | 152 us: 1.06x slower                                          |
| float                    | 79.3 ms                                                               | 84.4 ms: 1.07x slower                                         |
| deltablue                | 3.19 ms                                                               | 3.42 ms: 1.07x slower                                         |
| pyflate                  | 450 ms                                                                | 485 ms: 1.08x slower                                          |
| mdp                      | 2.63 sec                                                              | 2.83 sec: 1.08x slower                                        |
| meteor_contest           | 107 ms                                                                | 115 ms: 1.08x slower                                          |
| deepcopy_memo            | 38.6 us                                                               | 41.9 us: 1.09x slower                                         |
| scimark_fft              | 353 ms                                                                | 385 ms: 1.09x slower                                          |
| unpack_sequence          | 45.5 ns                                                               | 49.8 ns: 1.10x slower                                         |
| chaos                    | 59.3 ms                                                               | 65.5 ms: 1.11x slower                                         |
| regex_compile            | 136 ms                                                                | 150 ms: 1.11x slower                                          |
| mako                     | 10.8 ms                                                               | 12.1 ms: 1.12x slower                                         |
| tomli_loads              | 2.29 sec                                                              | 2.58 sec: 1.13x slower                                        |
| nbody                    | 88.0 ms                                                               | 102 ms: 1.15x slower                                          |
| fannkuch                 | 388 ms                                                                | 468 ms: 1.21x slower                                          |
| scimark_sparse_mat_mult  | 4.62 ms                                                               | 5.70 ms: 1.23x slower                                         |
| comprehensions           | 20.2 us                                                               | 25.0 us: 1.24x slower                                         |
| nqueens                  | 79.6 ms                                                               | 98.9 ms: 1.24x slower                                         |
| hexiom                   | 6.07 ms                                                               | 7.61 ms: 1.25x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.04x slower                                                  |

Benchmark hidden because not significant (8): logging_silent, unpickle, unpickle_list, pickle_dict, deepcopy_reduce, json_loads, bench_mp_pool, pickle_list


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x
