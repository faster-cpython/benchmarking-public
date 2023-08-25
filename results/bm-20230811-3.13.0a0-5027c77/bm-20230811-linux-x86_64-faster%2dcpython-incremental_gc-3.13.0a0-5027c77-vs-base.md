
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 5027c77
- commit date: 2023-08-11
- overall geometric mean: 1.04x faster
- HPT reliability: 91.48%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.38 sec: 1.11x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 94.1 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 72.7 ms: 1.09x faster                                                     |
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| regex_v8       | 21.9 ms                                                               | 22.4 ms: 1.03x slower                                                     |
| regex_effbot   | 3.54 ms                                                               | 3.66 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse | 103 ms                                                                | 94.0 ms: 1.10x faster                                                     |
| xml_etree_parse     | 152 ms                                                                | 140 ms: 1.09x faster                                                      |
| xml_etree_generate  | 83.4 ms                                                               | 80.9 ms: 1.03x faster                                                     |
| xml_etree_process   | 58.1 ms                                                               | 56.6 ms: 1.03x faster                                                     |
| pickle              | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| json_loads          | 25.7 us                                                               | 25.4 us: 1.01x faster                                                     |
| pickle_dict         | 31.7 us                                                               | 31.5 us: 1.01x faster                                                     |
| json_dumps          | 9.71 ms                                                               | 9.76 ms: 1.01x slower                                                     |
| pickle_list         | 4.51 us                                                               | 4.61 us: 1.02x slower                                                     |
| unpickle_list       | 4.94 us                                                               | 5.13 us: 1.04x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.79 ms: 1.00x faster                                                     |
| python_startup         | 9.33 ms                                                               | 9.30 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 562 ms: 2.12x faster                                                      |
| async_tree_none          | 478 ms                                                                | 274 ms: 1.75x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 337 ms: 1.74x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 498 ms: 1.45x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.46 ms: 1.24x faster                                                     |
| docutils                 | 2.65 sec                                                              | 2.38 sec: 1.11x faster                                                    |
| xml_etree_iterparse      | 103 ms                                                                | 94.0 ms: 1.10x faster                                                     |
| xml_etree_parse          | 152 ms                                                                | 140 ms: 1.09x faster                                                      |
| float                    | 79.2 ms                                                               | 72.7 ms: 1.09x faster                                                     |
| pycparser                | 1.15 sec                                                              | 1.06 sec: 1.09x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                               | 1.37 ms: 1.08x faster                                                     |
| async_generators         | 447 ms                                                                | 416 ms: 1.07x faster                                                      |
| dask                     | 520 ms                                                                | 484 ms: 1.07x faster                                                      |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| deltablue                | 3.20 ms                                                               | 3.08 ms: 1.04x faster                                                     |
| xml_etree_generate       | 83.4 ms                                                               | 80.9 ms: 1.03x faster                                                     |
| xml_etree_process        | 58.1 ms                                                               | 56.6 ms: 1.03x faster                                                     |
| richards                 | 47.8 ms                                                               | 46.6 ms: 1.03x faster                                                     |
| mako                     | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |
| logging_silent           | 106 ns                                                                | 103 ns: 1.02x faster                                                      |
| tornado_http             | 95.7 ms                                                               | 94.1 ms: 1.02x faster                                                     |
| pyflate                  | 446 ms                                                                | 438 ms: 1.02x faster                                                      |
| pickle                   | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| scimark_monte_carlo      | 68.0 ms                                                               | 67.3 ms: 1.01x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 38.0 us: 1.01x faster                                                     |
| json_loads               | 25.7 us                                                               | 25.4 us: 1.01x faster                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                     |
| richards_super           | 54.2 ms                                                               | 53.7 ms: 1.01x faster                                                     |
| coverage                 | 95.0 ms                                                               | 94.3 ms: 1.01x faster                                                     |
| typing_runtime_protocols | 145 us                                                                | 144 us: 1.01x faster                                                      |
| comprehensions           | 20.4 us                                                               | 20.3 us: 1.01x faster                                                     |
| sqlglot_transpile        | 1.61 ms                                                               | 1.60 ms: 1.01x faster                                                     |
| dulwich_log              | 66.4 ms                                                               | 66.0 ms: 1.01x faster                                                     |
| pickle_dict              | 31.7 us                                                               | 31.5 us: 1.01x faster                                                     |
| python_startup_no_site   | 6.83 ms                                                               | 6.79 ms: 1.00x faster                                                     |
| python_startup           | 9.33 ms                                                               | 9.30 ms: 1.00x faster                                                     |
| go                       | 137 ms                                                                | 137 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| hexiom                   | 6.02 ms                                                               | 6.04 ms: 1.00x slower                                                     |
| raytrace                 | 266 ms                                                                | 266 ms: 1.00x slower                                                      |
| fannkuch                 | 394 ms                                                                | 395 ms: 1.00x slower                                                      |
| mypy2                    | 337 ms                                                                | 338 ms: 1.00x slower                                                      |
| json_dumps               | 9.71 ms                                                               | 9.76 ms: 1.01x slower                                                     |
| bench_thread_pool        | 824 us                                                                | 828 us: 1.01x slower                                                      |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| generators               | 27.8 ms                                                               | 28.0 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                    |
| nqueens                  | 80.8 ms                                                               | 81.4 ms: 1.01x slower                                                     |
| json                     | 4.82 ms                                                               | 4.85 ms: 1.01x slower                                                     |
| pathlib                  | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| scimark_fft              | 358 ms                                                                | 361 ms: 1.01x slower                                                      |
| regex_dna                | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.02x slower                                                      |
| crypto_pyaes             | 70.0 ms                                                               | 71.5 ms: 1.02x slower                                                     |
| pickle_list              | 4.51 us                                                               | 4.61 us: 1.02x slower                                                     |
| telco                    | 7.80 ms                                                               | 8.00 ms: 1.03x slower                                                     |
| regex_v8                 | 21.9 ms                                                               | 22.4 ms: 1.03x slower                                                     |
| regex_effbot             | 3.54 ms                                                               | 3.66 ms: 1.03x slower                                                     |
| unpickle_list            | 4.94 us                                                               | 5.13 us: 1.04x slower                                                     |
| coroutines               | 21.6 ms                                                               | 22.5 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.78 ms: 1.04x slower                                                     |
| mdp                      | 2.53 sec                                                              | 2.72 sec: 1.07x slower                                                    |
| unpack_sequence          | 42.2 ns                                                               | 48.7 ns: 1.15x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (19): deepcopy, logging_format, pprint_safe_repr, meteor_contest, deepcopy_reduce, bench_mp_pool, pickle_pure_python, chaos, asyncio_tcp, sqlglot_optimize, unpickle_pure_python, regex_compile, logging_simple, tomli_loads, sqlite_synth, unpickle, nbody, spectral_norm, scimark_sor


# HPT report

- Reliability score: 91.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
