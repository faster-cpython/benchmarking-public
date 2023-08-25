
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 97f762a
- commit date: 2023-08-12
- overall geometric mean: 1.02x faster
- HPT reliability: 96.19%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.44 sec: 1.09x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 92.7 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 89.6 ms: 1.03x faster                                                     |
| float          | 79.2 ms                                                               | 77.8 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                               | 21.8 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_dict          | 31.7 us                                                               | 31.1 us: 1.02x faster                                                     |
| pickle_pure_python   | 299 us                                                                | 294 us: 1.02x faster                                                      |
| pickle               | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| xml_etree_process    | 58.1 ms                                                               | 57.6 ms: 1.01x faster                                                     |
| json_loads           | 25.7 us                                                               | 25.5 us: 1.00x faster                                                     |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                      |
| json_dumps           | 9.71 ms                                                               | 9.82 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 103 ms                                                                | 105 ms: 1.01x slower                                                      |
| pickle_list          | 4.51 us                                                               | 4.62 us: 1.02x slower                                                     |
| xml_etree_parse      | 152 ms                                                                | 166 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (4): unpickle, xml_etree_generate, unpickle_list, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.75 ms: 1.01x faster                                                     |
| python_startup         | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 730 ms: 1.63x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 406 ms: 1.44x faster                                                      |
| async_tree_none          | 478 ms                                                                | 342 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 577 ms: 1.25x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.61 ms: 1.19x faster                                                     |
| docutils                 | 2.65 sec                                                              | 2.44 sec: 1.09x faster                                                    |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| logging_silent           | 106 ns                                                                | 99.7 ns: 1.06x faster                                                     |
| dask                     | 520 ms                                                                | 495 ms: 1.05x faster                                                      |
| richards                 | 47.8 ms                                                               | 46.2 ms: 1.04x faster                                                     |
| tornado_http             | 95.7 ms                                                               | 92.7 ms: 1.03x faster                                                     |
| nbody                    | 92.4 ms                                                               | 89.6 ms: 1.03x faster                                                     |
| async_generators         | 447 ms                                                                | 434 ms: 1.03x faster                                                      |
| create_gc_cycles         | 1.49 ms                                                               | 1.45 ms: 1.03x faster                                                     |
| crypto_pyaes             | 70.0 ms                                                               | 68.3 ms: 1.03x faster                                                     |
| richards_super           | 54.2 ms                                                               | 52.8 ms: 1.02x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 37.5 us: 1.02x faster                                                     |
| coverage                 | 95.0 ms                                                               | 92.8 ms: 1.02x faster                                                     |
| deltablue                | 3.20 ms                                                               | 3.13 ms: 1.02x faster                                                     |
| deepcopy_reduce          | 3.21 us                                                               | 3.14 us: 1.02x faster                                                     |
| scimark_sor              | 121 ms                                                                | 118 ms: 1.02x faster                                                      |
| pickle_dict              | 31.7 us                                                               | 31.1 us: 1.02x faster                                                     |
| pickle_pure_python       | 299 us                                                                | 294 us: 1.02x faster                                                      |
| float                    | 79.2 ms                                                               | 77.8 ms: 1.02x faster                                                     |
| scimark_monte_carlo      | 68.0 ms                                                               | 66.9 ms: 1.02x faster                                                     |
| pickle                   | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| scimark_fft              | 358 ms                                                                | 354 ms: 1.01x faster                                                      |
| python_startup_no_site   | 6.83 ms                                                               | 6.75 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.61 ms                                                               | 1.59 ms: 1.01x faster                                                     |
| spectral_norm            | 107 ms                                                                | 106 ms: 1.01x faster                                                      |
| pyflate                  | 446 ms                                                                | 441 ms: 1.01x faster                                                      |
| mako                     | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                     |
| xml_etree_process        | 58.1 ms                                                               | 57.6 ms: 1.01x faster                                                     |
| comprehensions           | 20.4 us                                                               | 20.2 us: 1.01x faster                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                     |
| python_startup           | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| dulwich_log              | 66.4 ms                                                               | 66.0 ms: 1.01x faster                                                     |
| deepcopy                 | 356 us                                                                | 354 us: 1.01x faster                                                      |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                                      |
| json_loads               | 25.7 us                                                               | 25.5 us: 1.00x faster                                                     |
| regex_v8                 | 21.9 ms                                                               | 21.8 ms: 1.00x faster                                                     |
| fannkuch                 | 394 ms                                                                | 392 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                    |
| bench_thread_pool        | 824 us                                                                | 826 us: 1.00x slower                                                      |
| hexiom                   | 6.02 ms                                                               | 6.05 ms: 1.00x slower                                                     |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.00x slower                                                      |
| logging_simple           | 5.88 us                                                               | 5.91 us: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                    |
| nqueens                  | 80.8 ms                                                               | 81.3 ms: 1.01x slower                                                     |
| asyncio_tcp              | 483 ms                                                                | 486 ms: 1.01x slower                                                      |
| pathlib                  | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| unpickle_pure_python     | 212 us                                                                | 214 us: 1.01x slower                                                      |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                      |
| sqlglot_optimize         | 52.8 ms                                                               | 53.3 ms: 1.01x slower                                                     |
| json_dumps               | 9.71 ms                                                               | 9.82 ms: 1.01x slower                                                     |
| json                     | 4.82 ms                                                               | 4.87 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 145 us                                                                | 147 us: 1.01x slower                                                      |
| unpack_sequence          | 42.2 ns                                                               | 42.7 ns: 1.01x slower                                                     |
| xml_etree_iterparse      | 103 ms                                                                | 105 ms: 1.01x slower                                                      |
| go                       | 137 ms                                                                | 139 ms: 1.02x slower                                                      |
| sqlite_synth             | 2.73 us                                                               | 2.78 us: 1.02x slower                                                     |
| raytrace                 | 266 ms                                                                | 271 ms: 1.02x slower                                                      |
| telco                    | 7.80 ms                                                               | 7.98 ms: 1.02x slower                                                     |
| pickle_list              | 4.51 us                                                               | 4.62 us: 1.02x slower                                                     |
| coroutines               | 21.6 ms                                                               | 22.1 ms: 1.03x slower                                                     |
| pycparser                | 1.15 sec                                                              | 1.18 sec: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.74 ms: 1.04x slower                                                     |
| mypy2                    | 337 ms                                                                | 359 ms: 1.07x slower                                                      |
| xml_etree_parse          | 152 ms                                                                | 166 ms: 1.09x slower                                                      |
| generators               | 27.8 ms                                                               | 30.9 ms: 1.11x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (12): unpickle, regex_dna, regex_effbot, chaos, xml_etree_generate, mdp, bench_mp_pool, regex_compile, pprint_safe_repr, unpickle_list, logging_format, tomli_loads


# HPT report

- Reliability score: 96.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
