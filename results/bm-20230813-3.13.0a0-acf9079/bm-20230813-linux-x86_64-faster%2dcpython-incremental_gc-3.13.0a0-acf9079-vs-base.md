
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: acf9079
- commit date: 2023-08-13
- overall geometric mean: 1.03x faster
- HPT reliability: 95.66%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.43 sec: 1.09x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 93.6 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| float          | 79.2 ms                                                               | 75.4 ms: 1.05x faster                                                     |
| nbody          | 92.4 ms                                                               | 89.6 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 137 ms: 1.00x faster                                                      |
| regex_dna      | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| regex_effbot   | 3.54 ms                                                               | 3.59 ms: 1.01x slower                                                     |
| regex_v8       | 21.9 ms                                                               | 22.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                | 100 ms: 1.03x faster                                                      |
| pickle               | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| xml_etree_process    | 58.1 ms                                                               | 57.2 ms: 1.02x faster                                                     |
| pickle_dict          | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| pickle_list          | 4.51 us                                                               | 4.55 us: 1.01x slower                                                     |
| json_dumps           | 9.71 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.01x slower                                                      |
| tomli_loads          | 2.29 sec                                                              | 2.33 sec: 1.02x slower                                                    |
| unpickle             | 14.9 us                                                               | 15.2 us: 1.02x slower                                                     |
| unpickle_list        | 4.94 us                                                               | 5.11 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.73 ms: 1.01x faster                                                     |
| python_startup         | 9.33 ms                                                               | 9.25 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-acf9079 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 677 ms: 1.76x faster                                                      |
| async_tree_none          | 478 ms                                                                | 311 ms: 1.54x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 395 ms: 1.48x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 562 ms: 1.28x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.64 ms: 1.18x faster                                                     |
| docutils                 | 2.65 sec                                                              | 2.43 sec: 1.09x faster                                                    |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| dask                     | 520 ms                                                                | 494 ms: 1.05x faster                                                      |
| float                    | 79.2 ms                                                               | 75.4 ms: 1.05x faster                                                     |
| async_generators         | 447 ms                                                                | 431 ms: 1.04x faster                                                      |
| coverage                 | 95.0 ms                                                               | 91.8 ms: 1.03x faster                                                     |
| nbody                    | 92.4 ms                                                               | 89.6 ms: 1.03x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                               | 1.44 ms: 1.03x faster                                                     |
| xml_etree_iterparse      | 103 ms                                                                | 100 ms: 1.03x faster                                                      |
| pickle                   | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| richards_super           | 54.2 ms                                                               | 52.9 ms: 1.02x faster                                                     |
| crypto_pyaes             | 70.0 ms                                                               | 68.3 ms: 1.02x faster                                                     |
| tornado_http             | 95.7 ms                                                               | 93.6 ms: 1.02x faster                                                     |
| mako                     | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |
| richards                 | 47.8 ms                                                               | 46.8 ms: 1.02x faster                                                     |
| deltablue                | 3.20 ms                                                               | 3.14 ms: 1.02x faster                                                     |
| logging_silent           | 106 ns                                                                | 104 ns: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.0 ms                                                               | 66.8 ms: 1.02x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 37.8 us: 1.02x faster                                                     |
| xml_etree_process        | 58.1 ms                                                               | 57.2 ms: 1.02x faster                                                     |
| pycparser                | 1.15 sec                                                              | 1.14 sec: 1.01x faster                                                    |
| python_startup_no_site   | 6.83 ms                                                               | 6.73 ms: 1.01x faster                                                     |
| deepcopy                 | 356 us                                                                | 351 us: 1.01x faster                                                      |
| comprehensions           | 20.4 us                                                               | 20.2 us: 1.01x faster                                                     |
| hexiom                   | 6.02 ms                                                               | 5.97 ms: 1.01x faster                                                     |
| python_startup           | 9.33 ms                                                               | 9.25 ms: 1.01x faster                                                     |
| nqueens                  | 80.8 ms                                                               | 80.2 ms: 1.01x faster                                                     |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                                      |
| scimark_fft              | 358 ms                                                                | 356 ms: 1.01x faster                                                      |
| deepcopy_reduce          | 3.21 us                                                               | 3.19 us: 1.01x faster                                                     |
| pathlib                  | 18.5 ms                                                               | 18.4 ms: 1.00x faster                                                     |
| pyflate                  | 446 ms                                                                | 444 ms: 1.00x faster                                                      |
| pickle_dict              | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| regex_compile            | 137 ms                                                                | 137 ms: 1.00x faster                                                      |
| mdp                      | 2.53 sec                                                              | 2.54 sec: 1.00x slower                                                    |
| regex_dna                | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| pickle_list              | 4.51 us                                                               | 4.55 us: 1.01x slower                                                     |
| logging_format           | 6.45 us                                                               | 6.53 us: 1.01x slower                                                     |
| logging_simple           | 5.88 us                                                               | 5.95 us: 1.01x slower                                                     |
| pprint_safe_repr         | 716 ms                                                                | 725 ms: 1.01x slower                                                      |
| regex_effbot             | 3.54 ms                                                               | 3.59 ms: 1.01x slower                                                     |
| json_dumps               | 9.71 ms                                                               | 9.84 ms: 1.01x slower                                                     |
| json                     | 4.82 ms                                                               | 4.88 ms: 1.01x slower                                                     |
| go                       | 137 ms                                                                | 139 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 212 us                                                                | 215 us: 1.01x slower                                                      |
| pprint_pformat           | 1.46 sec                                                              | 1.48 sec: 1.02x slower                                                    |
| raytrace                 | 266 ms                                                                | 270 ms: 1.02x slower                                                      |
| regex_v8                 | 21.9 ms                                                               | 22.2 ms: 1.02x slower                                                     |
| tomli_loads              | 2.29 sec                                                              | 2.33 sec: 1.02x slower                                                    |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.02x slower                                                      |
| telco                    | 7.80 ms                                                               | 7.96 ms: 1.02x slower                                                     |
| unpickle                 | 14.9 us                                                               | 15.2 us: 1.02x slower                                                     |
| typing_runtime_protocols | 145 us                                                                | 149 us: 1.02x slower                                                      |
| unpack_sequence          | 42.2 ns                                                               | 43.2 ns: 1.02x slower                                                     |
| generators               | 27.8 ms                                                               | 28.5 ms: 1.03x slower                                                     |
| mypy2                    | 337 ms                                                                | 347 ms: 1.03x slower                                                      |
| coroutines               | 21.6 ms                                                               | 22.2 ms: 1.03x slower                                                     |
| sqlite_synth             | 2.73 us                                                               | 2.82 us: 1.03x slower                                                     |
| unpickle_list            | 4.94 us                                                               | 5.11 us: 1.03x slower                                                     |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.86 ms: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.03x faster                                                              |

Benchmark hidden because not significant (16): spectral_norm, bench_thread_pool, chaos, xml_etree_generate, sqlglot_parse, dulwich_log, asyncio_tcp_ssl, bench_mp_pool, json_loads, sqlglot_transpile, pickle_pure_python, xml_etree_parse, sqlglot_optimize, fannkuch, asyncio_tcp, scimark_sor


# HPT report

- Reliability score: 95.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
