
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 13cce66
- commit date: 2023-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 86.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.40 sec: 1.11x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 94.4 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 72.7 ms: 1.09x faster                                                     |
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 89.9 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 137 ms: 1.00x slower                                                      |
| regex_dna      | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| regex_v8       | 21.9 ms                                                               | 22.5 ms: 1.03x slower                                                     |
| regex_effbot   | 3.54 ms                                                               | 3.72 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                | 94.5 ms: 1.09x faster                                                     |
| xml_etree_parse      | 152 ms                                                                | 140 ms: 1.09x faster                                                      |
| xml_etree_process    | 58.1 ms                                                               | 56.7 ms: 1.02x faster                                                     |
| pickle               | 10.7 us                                                               | 10.5 us: 1.02x faster                                                     |
| xml_etree_generate   | 83.4 ms                                                               | 81.8 ms: 1.02x faster                                                     |
| pickle_dict          | 31.7 us                                                               | 31.8 us: 1.00x slower                                                     |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                      |
| json_dumps           | 9.71 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| pickle_list          | 4.51 us                                                               | 4.58 us: 1.02x slower                                                     |
| json_loads           | 25.7 us                                                               | 26.1 us: 1.02x slower                                                     |
| tomli_loads          | 2.29 sec                                                              | 2.34 sec: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.84 ms: 1.00x slower                                                     |
| python_startup         | 9.33 ms                                                               | 9.36 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.00x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 563 ms: 2.12x faster                                                      |
| async_tree_none          | 478 ms                                                                | 276 ms: 1.73x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 342 ms: 1.72x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 500 ms: 1.44x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.51 ms: 1.22x faster                                                     |
| docutils                 | 2.65 sec                                                              | 2.40 sec: 1.11x faster                                                    |
| xml_etree_iterparse      | 103 ms                                                                | 94.5 ms: 1.09x faster                                                     |
| float                    | 79.2 ms                                                               | 72.7 ms: 1.09x faster                                                     |
| xml_etree_parse          | 152 ms                                                                | 140 ms: 1.09x faster                                                      |
| dask                     | 520 ms                                                                | 485 ms: 1.07x faster                                                      |
| pycparser                | 1.15 sec                                                              | 1.08 sec: 1.07x faster                                                    |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| create_gc_cycles         | 1.49 ms                                                               | 1.42 ms: 1.05x faster                                                     |
| richards                 | 47.8 ms                                                               | 46.2 ms: 1.03x faster                                                     |
| async_generators         | 447 ms                                                                | 433 ms: 1.03x faster                                                      |
| richards_super           | 54.2 ms                                                               | 52.7 ms: 1.03x faster                                                     |
| nbody                    | 92.4 ms                                                               | 89.9 ms: 1.03x faster                                                     |
| xml_etree_process        | 58.1 ms                                                               | 56.7 ms: 1.02x faster                                                     |
| crypto_pyaes             | 70.0 ms                                                               | 68.4 ms: 1.02x faster                                                     |
| pickle                   | 10.7 us                                                               | 10.5 us: 1.02x faster                                                     |
| xml_etree_generate       | 83.4 ms                                                               | 81.8 ms: 1.02x faster                                                     |
| deltablue                | 3.20 ms                                                               | 3.14 ms: 1.02x faster                                                     |
| deepcopy_reduce          | 3.21 us                                                               | 3.15 us: 1.02x faster                                                     |
| coverage                 | 95.0 ms                                                               | 93.4 ms: 1.02x faster                                                     |
| deepcopy                 | 356 us                                                                | 351 us: 1.01x faster                                                      |
| tornado_http             | 95.7 ms                                                               | 94.4 ms: 1.01x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 37.9 us: 1.01x faster                                                     |
| scimark_monte_carlo      | 68.0 ms                                                               | 67.2 ms: 1.01x faster                                                     |
| scimark_fft              | 358 ms                                                                | 355 ms: 1.01x faster                                                      |
| sqlglot_parse            | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.61 ms                                                               | 1.59 ms: 1.01x faster                                                     |
| mako                     | 11.0 ms                                                               | 10.9 ms: 1.00x faster                                                     |
| pyflate                  | 446 ms                                                                | 444 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| python_startup_no_site   | 6.83 ms                                                               | 6.84 ms: 1.00x slower                                                     |
| pickle_dict              | 31.7 us                                                               | 31.8 us: 1.00x slower                                                     |
| comprehensions           | 20.4 us                                                               | 20.5 us: 1.00x slower                                                     |
| python_startup           | 9.33 ms                                                               | 9.36 ms: 1.00x slower                                                     |
| regex_compile            | 137 ms                                                                | 137 ms: 1.00x slower                                                      |
| dulwich_log              | 66.4 ms                                                               | 66.8 ms: 1.01x slower                                                     |
| bench_thread_pool        | 824 us                                                                | 829 us: 1.01x slower                                                      |
| chaos                    | 58.9 ms                                                               | 59.3 ms: 1.01x slower                                                     |
| regex_dna                | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 145 us                                                                | 146 us: 1.01x slower                                                      |
| pprint_safe_repr         | 716 ms                                                                | 723 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 212 us                                                                | 214 us: 1.01x slower                                                      |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| logging_format           | 6.45 us                                                               | 6.52 us: 1.01x slower                                                     |
| mypy2                    | 337 ms                                                                | 340 ms: 1.01x slower                                                      |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                      |
| hexiom                   | 6.02 ms                                                               | 6.09 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                                              | 1.48 sec: 1.01x slower                                                    |
| telco                    | 7.80 ms                                                               | 7.89 ms: 1.01x slower                                                     |
| raytrace                 | 266 ms                                                                | 269 ms: 1.01x slower                                                      |
| json_dumps               | 9.71 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| pickle_list              | 4.51 us                                                               | 4.58 us: 1.02x slower                                                     |
| json_loads               | 25.7 us                                                               | 26.1 us: 1.02x slower                                                     |
| tomli_loads              | 2.29 sec                                                              | 2.34 sec: 1.02x slower                                                    |
| coroutines               | 21.6 ms                                                               | 22.0 ms: 1.02x slower                                                     |
| generators               | 27.8 ms                                                               | 28.5 ms: 1.02x slower                                                     |
| scimark_lu               | 110 ms                                                                | 113 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.69 ms: 1.03x slower                                                     |
| regex_v8                 | 21.9 ms                                                               | 22.5 ms: 1.03x slower                                                     |
| unpack_sequence          | 42.2 ns                                                               | 44.0 ns: 1.04x slower                                                     |
| regex_effbot             | 3.54 ms                                                               | 3.72 ms: 1.05x slower                                                     |
| mdp                      | 2.53 sec                                                              | 2.69 sec: 1.06x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (16): spectral_norm, logging_silent, pickle_pure_python, asyncio_tcp, bench_mp_pool, go, unpickle_list, fannkuch, scimark_sor, sqlglot_optimize, pathlib, nqueens, logging_simple, sqlite_synth, json, unpickle


# HPT report

- Reliability score: 86.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
