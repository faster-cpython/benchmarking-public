
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: f286c3d
- commit date: 2023-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.37 sec: 1.12x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 93.4 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 71.7 ms: 1.10x faster                                                     |
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 88.1 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                               | 3.42 ms: 1.04x faster                                                     |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| regex_v8       | 21.9 ms                                                               | 21.8 ms: 1.00x faster                                                     |
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                | 94.2 ms: 1.10x faster                                                     |
| xml_etree_parse      | 152 ms                                                                | 141 ms: 1.08x faster                                                      |
| xml_etree_generate   | 83.4 ms                                                               | 81.3 ms: 1.03x faster                                                     |
| xml_etree_process    | 58.1 ms                                                               | 56.9 ms: 1.02x faster                                                     |
| pickle_pure_python   | 299 us                                                                | 295 us: 1.01x faster                                                      |
| json_loads           | 25.7 us                                                               | 25.7 us: 1.00x slower                                                     |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.01x slower                                                      |
| json_dumps           | 9.71 ms                                                               | 9.88 ms: 1.02x slower                                                     |
| tomli_loads          | 2.29 sec                                                              | 2.34 sec: 1.02x slower                                                    |
| pickle_dict          | 31.7 us                                                               | 32.6 us: 1.03x slower                                                     |
| pickle_list          | 4.51 us                                                               | 4.64 us: 1.03x slower                                                     |
| unpickle             | 14.9 us                                                               | 15.4 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.83 ms                                                               | 6.79 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 565 ms: 2.11x faster                                                      |
| async_tree_none          | 478 ms                                                                | 278 ms: 1.72x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 344 ms: 1.70x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 506 ms: 1.42x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.40 ms: 1.26x faster                                                     |
| docutils                 | 2.65 sec                                                              | 2.37 sec: 1.12x faster                                                    |
| float                    | 79.2 ms                                                               | 71.7 ms: 1.10x faster                                                     |
| xml_etree_iterparse      | 103 ms                                                                | 94.2 ms: 1.10x faster                                                     |
| xml_etree_parse          | 152 ms                                                                | 141 ms: 1.08x faster                                                      |
| dask                     | 520 ms                                                                | 485 ms: 1.07x faster                                                      |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| create_gc_cycles         | 1.49 ms                                                               | 1.41 ms: 1.05x faster                                                     |
| async_generators         | 447 ms                                                                | 425 ms: 1.05x faster                                                      |
| nbody                    | 92.4 ms                                                               | 88.1 ms: 1.05x faster                                                     |
| spectral_norm            | 107 ms                                                                | 103 ms: 1.04x faster                                                      |
| regex_effbot             | 3.54 ms                                                               | 3.42 ms: 1.04x faster                                                     |
| logging_silent           | 106 ns                                                                | 102 ns: 1.03x faster                                                      |
| pycparser                | 1.15 sec                                                              | 1.12 sec: 1.03x faster                                                    |
| tornado_http             | 95.7 ms                                                               | 93.4 ms: 1.03x faster                                                     |
| xml_etree_generate       | 83.4 ms                                                               | 81.3 ms: 1.03x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 37.5 us: 1.03x faster                                                     |
| xml_etree_process        | 58.1 ms                                                               | 56.9 ms: 1.02x faster                                                     |
| coverage                 | 95.0 ms                                                               | 93.0 ms: 1.02x faster                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.26 ms: 1.02x faster                                                     |
| mako                     | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                     |
| scimark_fft              | 358 ms                                                                | 352 ms: 1.02x faster                                                      |
| sqlglot_transpile        | 1.61 ms                                                               | 1.58 ms: 1.02x faster                                                     |
| deltablue                | 3.20 ms                                                               | 3.15 ms: 1.02x faster                                                     |
| deepcopy_reduce          | 3.21 us                                                               | 3.16 us: 1.02x faster                                                     |
| crypto_pyaes             | 70.0 ms                                                               | 69.0 ms: 1.01x faster                                                     |
| pickle_pure_python       | 299 us                                                                | 295 us: 1.01x faster                                                      |
| richards_super           | 54.2 ms                                                               | 53.6 ms: 1.01x faster                                                     |
| deepcopy                 | 356 us                                                                | 352 us: 1.01x faster                                                      |
| regex_compile            | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| scimark_monte_carlo      | 68.0 ms                                                               | 67.4 ms: 1.01x faster                                                     |
| go                       | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| pathlib                  | 18.5 ms                                                               | 18.4 ms: 1.01x faster                                                     |
| python_startup           | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| comprehensions           | 20.4 us                                                               | 20.3 us: 1.01x faster                                                     |
| dulwich_log              | 66.4 ms                                                               | 66.0 ms: 1.01x faster                                                     |
| fannkuch                 | 394 ms                                                                | 392 ms: 1.01x faster                                                      |
| python_startup_no_site   | 6.83 ms                                                               | 6.79 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| regex_v8                 | 21.9 ms                                                               | 21.8 ms: 1.00x faster                                                     |
| bench_thread_pool        | 824 us                                                                | 826 us: 1.00x slower                                                      |
| json_loads               | 25.7 us                                                               | 25.7 us: 1.00x slower                                                     |
| unpickle_pure_python     | 212 us                                                                | 213 us: 1.01x slower                                                      |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| mypy2                    | 337 ms                                                                | 339 ms: 1.01x slower                                                      |
| asyncio_tcp              | 483 ms                                                                | 487 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 716 ms                                                                | 723 ms: 1.01x slower                                                      |
| chaos                    | 58.9 ms                                                               | 59.5 ms: 1.01x slower                                                     |
| hexiom                   | 6.02 ms                                                               | 6.08 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 145 us                                                                | 147 us: 1.01x slower                                                      |
| pprint_pformat           | 1.46 sec                                                              | 1.48 sec: 1.01x slower                                                    |
| pyflate                  | 446 ms                                                                | 451 ms: 1.01x slower                                                      |
| regex_dna                | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| telco                    | 7.80 ms                                                               | 7.90 ms: 1.01x slower                                                     |
| nqueens                  | 80.8 ms                                                               | 81.9 ms: 1.01x slower                                                     |
| raytrace                 | 266 ms                                                                | 270 ms: 1.02x slower                                                      |
| json_dumps               | 9.71 ms                                                               | 9.88 ms: 1.02x slower                                                     |
| sqlite_synth             | 2.73 us                                                               | 2.79 us: 1.02x slower                                                     |
| tomli_loads              | 2.29 sec                                                              | 2.34 sec: 1.02x slower                                                    |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.68 ms: 1.02x slower                                                     |
| generators               | 27.8 ms                                                               | 28.5 ms: 1.02x slower                                                     |
| scimark_lu               | 110 ms                                                                | 113 ms: 1.02x slower                                                      |
| pickle_dict              | 31.7 us                                                               | 32.6 us: 1.03x slower                                                     |
| pickle_list              | 4.51 us                                                               | 4.64 us: 1.03x slower                                                     |
| coroutines               | 21.6 ms                                                               | 22.3 ms: 1.03x slower                                                     |
| unpickle                 | 14.9 us                                                               | 15.4 us: 1.03x slower                                                     |
| unpack_sequence          | 42.2 ns                                                               | 45.1 ns: 1.07x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (11): unpickle_list, pickle, scimark_sor, logging_format, meteor_contest, mdp, logging_simple, bench_mp_pool, sqlglot_optimize, json, richards


# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
