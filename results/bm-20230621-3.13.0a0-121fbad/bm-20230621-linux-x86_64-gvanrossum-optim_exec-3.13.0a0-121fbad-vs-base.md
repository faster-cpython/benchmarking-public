
# Results vs. base

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 121fbad
- commit date: 2023-06-21
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                          |
| tornado_http   | 97.1 ms                                                               | 96.2 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x faster                                            |
| float          | 79.7 ms                                                               | 80.7 ms: 1.01x slower                                           |
| nbody          | 88.3 ms                                                               | 90.5 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                               | 3.39 ms: 1.08x faster                                           |
| regex_dna      | 209 ms                                                                | 201 ms: 1.04x faster                                            |
| regex_v8       | 22.3 ms                                                               | 21.7 ms: 1.03x faster                                           |
| regex_compile  | 135 ms                                                                | 138 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_list        | 5.01 us                                                               | 4.91 us: 1.02x faster                                           |
| json_dumps           | 9.96 ms                                                               | 9.81 ms: 1.02x faster                                           |
| xml_etree_process    | 57.6 ms                                                               | 57.4 ms: 1.00x faster                                           |
| pickle_dict          | 31.1 us                                                               | 31.3 us: 1.00x slower                                           |
| json_loads           | 24.9 us                                                               | 25.2 us: 1.01x slower                                           |
| pickle               | 10.8 us                                                               | 10.9 us: 1.01x slower                                           |
| xml_etree_iterparse  | 103 ms                                                                | 105 ms: 1.02x slower                                            |
| unpickle_pure_python | 212 us                                                                | 218 us: 1.03x slower                                            |
| pickle_list          | 4.47 us                                                               | 4.63 us: 1.04x slower                                           |
| tomli_loads          | 2.19 sec                                                              | 2.34 sec: 1.07x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.69 ms                                                               | 6.66 ms: 1.00x faster                                           |
| python_startup         | 9.22 ms                                                               | 9.18 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20230619-linux-x86_64-python-7f97c8e367869e2aebe9-3.13.0a0-7f97c8e | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot             | 3.66 ms                                                               | 3.39 ms: 1.08x faster                                           |
| gc_traversal             | 3.83 ms                                                               | 3.58 ms: 1.07x faster                                           |
| unpack_sequence          | 45.6 ns                                                               | 43.8 ns: 1.04x faster                                           |
| regex_dna                | 209 ms                                                                | 201 ms: 1.04x faster                                            |
| generators               | 30.3 ms                                                               | 29.3 ms: 1.03x faster                                           |
| regex_v8                 | 22.3 ms                                                               | 21.7 ms: 1.03x faster                                           |
| unpickle_list            | 5.01 us                                                               | 4.91 us: 1.02x faster                                           |
| telco                    | 6.94 ms                                                               | 6.81 ms: 1.02x faster                                           |
| deepcopy_reduce          | 3.16 us                                                               | 3.10 us: 1.02x faster                                           |
| json_dumps               | 9.96 ms                                                               | 9.81 ms: 1.02x faster                                           |
| dask                     | 522 ms                                                                | 515 ms: 1.01x faster                                            |
| coroutines               | 22.4 ms                                                               | 22.1 ms: 1.01x faster                                           |
| coverage                 | 94.3 ms                                                               | 93.2 ms: 1.01x faster                                           |
| tornado_http             | 97.1 ms                                                               | 96.2 ms: 1.01x faster                                           |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                          |
| logging_format           | 6.49 us                                                               | 6.44 us: 1.01x faster                                           |
| mako                     | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                           |
| mypy2                    | 337 ms                                                                | 335 ms: 1.01x faster                                            |
| python_startup_no_site   | 6.69 ms                                                               | 6.66 ms: 1.00x faster                                           |
| python_startup           | 9.22 ms                                                               | 9.18 ms: 1.00x faster                                           |
| xml_etree_process        | 57.6 ms                                                               | 57.4 ms: 1.00x faster                                           |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x faster                                            |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                          |
| pickle_dict              | 31.1 us                                                               | 31.3 us: 1.00x slower                                           |
| docutils                 | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                          |
| deepcopy                 | 347 us                                                                | 349 us: 1.00x slower                                            |
| sqlglot_parse            | 1.30 ms                                                               | 1.31 ms: 1.01x slower                                           |
| pycparser                | 1.15 sec                                                              | 1.15 sec: 1.01x slower                                          |
| richards_super           | 50.1 ms                                                               | 50.4 ms: 1.01x slower                                           |
| sqlglot_optimize         | 52.4 ms                                                               | 52.8 ms: 1.01x slower                                           |
| crypto_pyaes             | 77.8 ms                                                               | 78.4 ms: 1.01x slower                                           |
| pprint_safe_repr         | 713 ms                                                                | 719 ms: 1.01x slower                                            |
| sqlglot_transpile        | 1.62 ms                                                               | 1.63 ms: 1.01x slower                                           |
| scimark_sor              | 118 ms                                                                | 119 ms: 1.01x slower                                            |
| json_loads               | 24.9 us                                                               | 25.2 us: 1.01x slower                                           |
| sqlglot_normalize        | 105 ms                                                                | 107 ms: 1.01x slower                                            |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                            |
| richards                 | 43.6 ms                                                               | 44.1 ms: 1.01x slower                                           |
| json                     | 4.73 ms                                                               | 4.78 ms: 1.01x slower                                           |
| logging_silent           | 95.6 ns                                                               | 96.7 ns: 1.01x slower                                           |
| pickle                   | 10.8 us                                                               | 10.9 us: 1.01x slower                                           |
| pprint_pformat           | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                          |
| float                    | 79.7 ms                                                               | 80.7 ms: 1.01x slower                                           |
| regex_compile            | 135 ms                                                                | 138 ms: 1.02x slower                                            |
| bench_thread_pool        | 818 us                                                                | 831 us: 1.02x slower                                            |
| go                       | 134 ms                                                                | 137 ms: 1.02x slower                                            |
| deltablue                | 3.25 ms                                                               | 3.31 ms: 1.02x slower                                           |
| asyncio_tcp              | 495 ms                                                                | 505 ms: 1.02x slower                                            |
| chaos                    | 61.4 ms                                                               | 62.7 ms: 1.02x slower                                           |
| xml_etree_iterparse      | 103 ms                                                                | 105 ms: 1.02x slower                                            |
| pyflate                  | 439 ms                                                                | 449 ms: 1.02x slower                                            |
| nbody                    | 88.3 ms                                                               | 90.5 ms: 1.02x slower                                           |
| meteor_contest           | 106 ms                                                                | 109 ms: 1.02x slower                                            |
| typing_runtime_protocols | 145 us                                                                | 149 us: 1.03x slower                                            |
| async_generators         | 450 ms                                                                | 463 ms: 1.03x slower                                            |
| unpickle_pure_python     | 212 us                                                                | 218 us: 1.03x slower                                            |
| pickle_list              | 4.47 us                                                               | 4.63 us: 1.04x slower                                           |
| hexiom                   | 5.97 ms                                                               | 6.23 ms: 1.04x slower                                           |
| scimark_fft              | 347 ms                                                                | 363 ms: 1.05x slower                                            |
| deepcopy_memo            | 36.6 us                                                               | 38.3 us: 1.05x slower                                           |
| scimark_sparse_mat_mult  | 4.77 ms                                                               | 5.06 ms: 1.06x slower                                           |
| nqueens                  | 79.0 ms                                                               | 84.1 ms: 1.06x slower                                           |
| mdp                      | 2.55 sec                                                              | 2.72 sec: 1.07x slower                                          |
| spectral_norm            | 104 ms                                                                | 111 ms: 1.07x slower                                            |
| tomli_loads              | 2.19 sec                                                              | 2.34 sec: 1.07x slower                                          |
| comprehensions           | 20.3 us                                                               | 21.7 us: 1.07x slower                                           |
| fannkuch                 | 394 ms                                                                | 427 ms: 1.08x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (15): unpickle, xml_etree_parse, sqlite_synth, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, create_gc_cycles, scimark_monte_carlo, logging_simple, pickle_pure_python, pathlib, bench_mp_pool, raytrace, dulwich_log, xml_etree_generate
