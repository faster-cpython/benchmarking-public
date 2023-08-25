
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: fed9a7f
- commit date: 2023-08-11
- overall geometric mean: 1.01x slower
- HPT reliability: 58.33%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.57 sec: 1.03x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 99.6 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 92.4 ms                                                               | 87.7 ms: 1.05x faster                                                     |
| pidigits       | 201 ms                                                                | 201 ms: 1.00x slower                                                      |
| float          | 79.2 ms                                                               | 87.7 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                               | 3.57 ms: 1.01x slower                                                     |
| regex_v8       | 21.9 ms                                                               | 22.8 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python  | 299 us                                                                | 293 us: 1.02x faster                                                      |
| json_loads          | 25.7 us                                                               | 25.3 us: 1.01x faster                                                     |
| pickle              | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| pickle_dict         | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| tomli_loads         | 2.29 sec                                                              | 2.30 sec: 1.01x slower                                                    |
| pickle_list         | 4.51 us                                                               | 4.63 us: 1.03x slower                                                     |
| xml_etree_process   | 58.1 ms                                                               | 60.0 ms: 1.03x slower                                                     |
| xml_etree_generate  | 83.4 ms                                                               | 88.1 ms: 1.06x slower                                                     |
| xml_etree_parse     | 152 ms                                                                | 346 ms: 2.27x slower                                                      |
| xml_etree_iterparse | 103 ms                                                                | 323 ms: 3.13x slower                                                      |
| Geometric mean      | (ref)                                                                 | 1.16x slower                                                              |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.92 ms: 1.01x slower                                                     |
| python_startup         | 9.33 ms                                                               | 9.52 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-fed9a7f |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.19 sec                                                              | 706 ms: 1.69x faster                                                      |
| async_tree_none         | 478 ms                                                                | 327 ms: 1.46x faster                                                      |
| async_tree_memoization  | 586 ms                                                                | 446 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed | 720 ms                                                                | 578 ms: 1.25x faster                                                      |
| gc_traversal            | 4.29 ms                                                               | 3.94 ms: 1.09x faster                                                     |
| nbody                   | 92.4 ms                                                               | 87.7 ms: 1.05x faster                                                     |
| async_generators        | 447 ms                                                                | 432 ms: 1.03x faster                                                      |
| richards                | 47.8 ms                                                               | 46.4 ms: 1.03x faster                                                     |
| richards_super          | 54.2 ms                                                               | 52.6 ms: 1.03x faster                                                     |
| docutils                | 2.65 sec                                                              | 2.57 sec: 1.03x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                               | 1.44 ms: 1.03x faster                                                     |
| logging_silent          | 106 ns                                                                | 103 ns: 1.03x faster                                                      |
| deepcopy                | 356 us                                                                | 347 us: 1.02x faster                                                      |
| deepcopy_memo           | 38.4 us                                                               | 37.6 us: 1.02x faster                                                     |
| pickle_pure_python      | 299 us                                                                | 293 us: 1.02x faster                                                      |
| nqueens                 | 80.8 ms                                                               | 79.2 ms: 1.02x faster                                                     |
| spectral_norm           | 107 ms                                                                | 105 ms: 1.02x faster                                                      |
| mako                    | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |
| coverage                | 95.0 ms                                                               | 93.3 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 3.21 us                                                               | 3.15 us: 1.02x faster                                                     |
| json_loads              | 25.7 us                                                               | 25.3 us: 1.01x faster                                                     |
| pickle                  | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| fannkuch                | 394 ms                                                                | 389 ms: 1.01x faster                                                      |
| json                    | 4.82 ms                                                               | 4.76 ms: 1.01x faster                                                     |
| telco                   | 7.80 ms                                                               | 7.72 ms: 1.01x faster                                                     |
| scimark_sor             | 121 ms                                                                | 120 ms: 1.01x faster                                                      |
| pprint_safe_repr        | 716 ms                                                                | 710 ms: 1.01x faster                                                      |
| meteor_contest          | 106 ms                                                                | 105 ms: 1.01x faster                                                      |
| dulwich_log             | 66.4 ms                                                               | 65.9 ms: 1.01x faster                                                     |
| pycparser               | 1.15 sec                                                              | 1.15 sec: 1.01x faster                                                    |
| pickle_dict             | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| bench_thread_pool       | 824 us                                                                | 822 us: 1.00x faster                                                      |
| pidigits                | 201 ms                                                                | 201 ms: 1.00x slower                                                      |
| comprehensions          | 20.4 us                                                               | 20.5 us: 1.00x slower                                                     |
| tomli_loads             | 2.29 sec                                                              | 2.30 sec: 1.01x slower                                                    |
| crypto_pyaes            | 70.0 ms                                                               | 70.4 ms: 1.01x slower                                                     |
| pathlib                 | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| regex_effbot            | 3.54 ms                                                               | 3.57 ms: 1.01x slower                                                     |
| pyflate                 | 446 ms                                                                | 449 ms: 1.01x slower                                                      |
| mdp                     | 2.53 sec                                                              | 2.55 sec: 1.01x slower                                                    |
| sqlglot_transpile       | 1.61 ms                                                               | 1.62 ms: 1.01x slower                                                     |
| chaos                   | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                     |
| sqlite_synth            | 2.73 us                                                               | 2.76 us: 1.01x slower                                                     |
| scimark_lu              | 110 ms                                                                | 111 ms: 1.01x slower                                                      |
| raytrace                | 266 ms                                                                | 269 ms: 1.01x slower                                                      |
| python_startup_no_site  | 6.83 ms                                                               | 6.92 ms: 1.01x slower                                                     |
| generators              | 27.8 ms                                                               | 28.2 ms: 1.01x slower                                                     |
| coroutines              | 21.6 ms                                                               | 21.9 ms: 1.02x slower                                                     |
| sqlglot_parse           | 1.29 ms                                                               | 1.31 ms: 1.02x slower                                                     |
| scimark_monte_carlo     | 68.0 ms                                                               | 69.1 ms: 1.02x slower                                                     |
| python_startup          | 9.33 ms                                                               | 9.52 ms: 1.02x slower                                                     |
| pickle_list             | 4.51 us                                                               | 4.63 us: 1.03x slower                                                     |
| xml_etree_process       | 58.1 ms                                                               | 60.0 ms: 1.03x slower                                                     |
| tornado_http            | 95.7 ms                                                               | 99.6 ms: 1.04x slower                                                     |
| regex_v8                | 21.9 ms                                                               | 22.8 ms: 1.04x slower                                                     |
| unpack_sequence         | 42.2 ns                                                               | 44.4 ns: 1.05x slower                                                     |
| scimark_sparse_mat_mult | 4.57 ms                                                               | 4.82 ms: 1.06x slower                                                     |
| xml_etree_generate      | 83.4 ms                                                               | 88.1 ms: 1.06x slower                                                     |
| float                   | 79.2 ms                                                               | 87.7 ms: 1.11x slower                                                     |
| mypy2                   | 337 ms                                                                | 397 ms: 1.18x slower                                                      |
| xml_etree_parse         | 152 ms                                                                | 346 ms: 2.27x slower                                                      |
| xml_etree_iterparse     | 103 ms                                                                | 323 ms: 3.13x slower                                                      |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (20): scimark_fft, logging_format, json_dumps, sqlglot_normalize, unpickle_pure_python, go, asyncio_tcp_ssl, regex_compile, bench_mp_pool, asyncio_tcp, hexiom, regex_dna, pprint_pformat, logging_simple, deltablue, sqlglot_optimize, typing_runtime_protocols, unpickle, dask, unpickle_list


# HPT report

- Reliability score: 58.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
