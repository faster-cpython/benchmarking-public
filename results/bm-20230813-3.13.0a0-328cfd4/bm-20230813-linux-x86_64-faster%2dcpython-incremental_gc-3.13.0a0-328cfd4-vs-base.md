
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 328cfd4
- commit date: 2023-08-13
- overall geometric mean: 1.02x faster
- HPT reliability: 55.06%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.42 sec: 1.09x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 93.6 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 75.0 ms: 1.06x faster                                                     |
| nbody          | 92.4 ms                                                               | 88.7 ms: 1.04x faster                                                     |
| pidigits       | 201 ms                                                                | 201 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                     |
| regex_dna      | 208 ms                                                                | 213 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                                | 101 ms: 1.03x faster                                                      |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.01x slower                                                      |
| xml_etree_generate   | 83.4 ms                                                               | 84.1 ms: 1.01x slower                                                     |
| tomli_loads          | 2.29 sec                                                              | 2.32 sec: 1.01x slower                                                    |
| pickle_dict          | 31.7 us                                                               | 32.2 us: 1.02x slower                                                     |
| pickle_list          | 4.51 us                                                               | 4.63 us: 1.03x slower                                                     |
| unpickle_list        | 4.94 us                                                               | 5.16 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_parse, pickle_pure_python, json_loads, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.74 ms: 1.01x faster                                                     |
| python_startup         | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.8 ms: 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.19 sec                                                              | 676 ms: 1.76x faster                                                      |
| async_tree_none         | 478 ms                                                                | 308 ms: 1.55x faster                                                      |
| async_tree_memoization  | 586 ms                                                                | 393 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed | 720 ms                                                                | 560 ms: 1.29x faster                                                      |
| gc_traversal            | 4.29 ms                                                               | 3.79 ms: 1.13x faster                                                     |
| docutils                | 2.65 sec                                                              | 2.42 sec: 1.09x faster                                                    |
| logging_silent          | 106 ns                                                                | 99.7 ns: 1.06x faster                                                     |
| dask                    | 520 ms                                                                | 492 ms: 1.06x faster                                                      |
| float                   | 79.2 ms                                                               | 75.0 ms: 1.06x faster                                                     |
| nbody                   | 92.4 ms                                                               | 88.7 ms: 1.04x faster                                                     |
| async_generators        | 447 ms                                                                | 430 ms: 1.04x faster                                                      |
| richards_super          | 54.2 ms                                                               | 52.5 ms: 1.03x faster                                                     |
| pycparser               | 1.15 sec                                                              | 1.12 sec: 1.03x faster                                                    |
| coverage                | 95.0 ms                                                               | 92.5 ms: 1.03x faster                                                     |
| pickle                  | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| xml_etree_iterparse     | 103 ms                                                                | 101 ms: 1.03x faster                                                      |
| richards                | 47.8 ms                                                               | 46.6 ms: 1.03x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                               | 1.45 ms: 1.02x faster                                                     |
| tornado_http            | 95.7 ms                                                               | 93.6 ms: 1.02x faster                                                     |
| spectral_norm           | 107 ms                                                                | 105 ms: 1.02x faster                                                      |
| python_startup_no_site  | 6.83 ms                                                               | 6.74 ms: 1.01x faster                                                     |
| mako                    | 11.0 ms                                                               | 10.8 ms: 1.01x faster                                                     |
| deepcopy_memo           | 38.4 us                                                               | 38.0 us: 1.01x faster                                                     |
| python_startup          | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| logging_simple          | 5.88 us                                                               | 5.84 us: 1.01x faster                                                     |
| logging_format          | 6.45 us                                                               | 6.41 us: 1.01x faster                                                     |
| pidigits                | 201 ms                                                                | 201 ms: 1.00x faster                                                      |
| sqlglot_optimize        | 52.8 ms                                                               | 53.0 ms: 1.00x slower                                                     |
| pprint_pformat          | 1.46 sec                                                              | 1.46 sec: 1.00x slower                                                    |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.01x slower                                                      |
| unpickle_pure_python    | 212 us                                                                | 213 us: 1.01x slower                                                      |
| asyncio_tcp             | 483 ms                                                                | 487 ms: 1.01x slower                                                      |
| bench_thread_pool       | 824 us                                                                | 830 us: 1.01x slower                                                      |
| deepcopy_reduce         | 3.21 us                                                               | 3.23 us: 1.01x slower                                                     |
| go                      | 137 ms                                                                | 138 ms: 1.01x slower                                                      |
| sqlglot_normalize       | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| xml_etree_generate      | 83.4 ms                                                               | 84.1 ms: 1.01x slower                                                     |
| scimark_sor             | 121 ms                                                                | 122 ms: 1.01x slower                                                      |
| fannkuch                | 394 ms                                                                | 398 ms: 1.01x slower                                                      |
| chaos                   | 58.9 ms                                                               | 59.6 ms: 1.01x slower                                                     |
| sqlite_synth            | 2.73 us                                                               | 2.76 us: 1.01x slower                                                     |
| mdp                     | 2.53 sec                                                              | 2.56 sec: 1.01x slower                                                    |
| regex_v8                | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                     |
| tomli_loads             | 2.29 sec                                                              | 2.32 sec: 1.01x slower                                                    |
| scimark_fft             | 358 ms                                                                | 364 ms: 1.02x slower                                                      |
| pickle_dict             | 31.7 us                                                               | 32.2 us: 1.02x slower                                                     |
| generators              | 27.8 ms                                                               | 28.4 ms: 1.02x slower                                                     |
| nqueens                 | 80.8 ms                                                               | 82.7 ms: 1.02x slower                                                     |
| raytrace                | 266 ms                                                                | 272 ms: 1.02x slower                                                      |
| regex_dna               | 208 ms                                                                | 213 ms: 1.03x slower                                                      |
| hexiom                  | 6.02 ms                                                               | 6.18 ms: 1.03x slower                                                     |
| pickle_list             | 4.51 us                                                               | 4.63 us: 1.03x slower                                                     |
| mypy2                   | 337 ms                                                                | 347 ms: 1.03x slower                                                      |
| scimark_lu              | 110 ms                                                                | 113 ms: 1.03x slower                                                      |
| coroutines              | 21.6 ms                                                               | 22.2 ms: 1.03x slower                                                     |
| unpickle_list           | 4.94 us                                                               | 5.16 us: 1.04x slower                                                     |
| telco                   | 7.80 ms                                                               | 8.16 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult | 4.57 ms                                                               | 4.80 ms: 1.05x slower                                                     |
| unpack_sequence         | 42.2 ns                                                               | 45.7 ns: 1.08x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (23): regex_effbot, typing_runtime_protocols, sqlglot_parse, xml_etree_process, xml_etree_parse, pickle_pure_python, dulwich_log, deltablue, json_loads, asyncio_tcp_ssl, bench_mp_pool, deepcopy, pyflate, regex_compile, sqlglot_transpile, json_dumps, pprint_safe_repr, crypto_pyaes, json, pathlib, scimark_monte_carlo, comprehensions, unpickle


# HPT report

- Reliability score: 55.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
