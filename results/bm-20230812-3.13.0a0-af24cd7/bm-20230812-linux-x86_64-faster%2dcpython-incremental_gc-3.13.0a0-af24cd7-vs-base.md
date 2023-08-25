
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: af24cd7
- commit date: 2023-08-12
- overall geometric mean: 1.02x faster
- HPT reliability: 75.46%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark    | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|--------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tornado_http | 95.7 ms                                                               | 92.9 ms: 1.03x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 88.8 ms: 1.04x faster                                                     |
| float          | 79.2 ms                                                               | 76.8 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| regex_dna      | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| regex_v8       | 21.9 ms                                                               | 22.3 ms: 1.02x slower                                                     |
| regex_effbot   | 3.54 ms                                                               | 3.73 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 299 us                                                                | 293 us: 1.02x faster                                                      |
| pickle               | 10.7 us                                                               | 10.5 us: 1.02x faster                                                     |
| xml_etree_process    | 58.1 ms                                                               | 57.3 ms: 1.01x faster                                                     |
| json_loads           | 25.7 us                                                               | 25.4 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                                | 105 ms: 1.02x slower                                                      |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.02x slower                                                      |
| unpickle_list        | 4.94 us                                                               | 5.08 us: 1.03x slower                                                     |
| json_dumps           | 9.71 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| pickle_dict          | 31.7 us                                                               | 32.7 us: 1.03x slower                                                     |
| pickle_list          | 4.51 us                                                               | 4.70 us: 1.04x slower                                                     |
| xml_etree_parse      | 152 ms                                                                | 168 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.75 ms: 1.01x faster                                                     |
| python_startup         | 9.33 ms                                                               | 9.29 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.19 sec                                                              | 717 ms: 1.66x faster                                                      |
| async_tree_memoization  | 586 ms                                                                | 406 ms: 1.44x faster                                                      |
| async_tree_none         | 478 ms                                                                | 341 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed | 720 ms                                                                | 575 ms: 1.25x faster                                                      |
| gc_traversal            | 4.29 ms                                                               | 3.60 ms: 1.19x faster                                                     |
| logging_silent          | 106 ns                                                                | 98.1 ns: 1.08x faster                                                     |
| pidigits                | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| dask                    | 520 ms                                                                | 499 ms: 1.04x faster                                                      |
| nbody                   | 92.4 ms                                                               | 88.8 ms: 1.04x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                               | 1.44 ms: 1.03x faster                                                     |
| float                   | 79.2 ms                                                               | 76.8 ms: 1.03x faster                                                     |
| tornado_http            | 95.7 ms                                                               | 92.9 ms: 1.03x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                               | 66.1 ms: 1.03x faster                                                     |
| coverage                | 95.0 ms                                                               | 92.6 ms: 1.03x faster                                                     |
| async_generators        | 447 ms                                                                | 437 ms: 1.02x faster                                                      |
| mako                    | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |
| pickle_pure_python      | 299 us                                                                | 293 us: 1.02x faster                                                      |
| pickle                  | 10.7 us                                                               | 10.5 us: 1.02x faster                                                     |
| richards_super          | 54.2 ms                                                               | 53.3 ms: 1.02x faster                                                     |
| deepcopy_memo           | 38.4 us                                                               | 37.8 us: 1.02x faster                                                     |
| nqueens                 | 80.8 ms                                                               | 79.6 ms: 1.02x faster                                                     |
| scimark_fft             | 358 ms                                                                | 353 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 1.61 ms                                                               | 1.58 ms: 1.01x faster                                                     |
| deltablue               | 3.20 ms                                                               | 3.16 ms: 1.01x faster                                                     |
| xml_etree_process       | 58.1 ms                                                               | 57.3 ms: 1.01x faster                                                     |
| richards                | 47.8 ms                                                               | 47.2 ms: 1.01x faster                                                     |
| pyflate                 | 446 ms                                                                | 440 ms: 1.01x faster                                                      |
| python_startup_no_site  | 6.83 ms                                                               | 6.75 ms: 1.01x faster                                                     |
| sqlglot_parse           | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                     |
| comprehensions          | 20.4 us                                                               | 20.2 us: 1.01x faster                                                     |
| json_loads              | 25.7 us                                                               | 25.4 us: 1.01x faster                                                     |
| crypto_pyaes            | 70.0 ms                                                               | 69.6 ms: 1.01x faster                                                     |
| regex_compile           | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 3.21 us                                                               | 3.19 us: 1.01x faster                                                     |
| python_startup          | 9.33 ms                                                               | 9.29 ms: 1.00x faster                                                     |
| hexiom                  | 6.02 ms                                                               | 6.01 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| dulwich_log             | 66.4 ms                                                               | 66.5 ms: 1.00x slower                                                     |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.01x slower                                                      |
| pprint_pformat          | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                    |
| fannkuch                | 394 ms                                                                | 396 ms: 1.01x slower                                                      |
| regex_dna               | 208 ms                                                                | 209 ms: 1.01x slower                                                      |
| pathlib                 | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| sqlglot_normalize       | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| chaos                   | 58.9 ms                                                               | 59.4 ms: 1.01x slower                                                     |
| sqlite_synth            | 2.73 us                                                               | 2.76 us: 1.01x slower                                                     |
| sqlglot_optimize        | 52.8 ms                                                               | 53.4 ms: 1.01x slower                                                     |
| scimark_lu              | 110 ms                                                                | 111 ms: 1.01x slower                                                      |
| generators              | 27.8 ms                                                               | 28.2 ms: 1.01x slower                                                     |
| xml_etree_iterparse     | 103 ms                                                                | 105 ms: 1.02x slower                                                      |
| unpickle_pure_python    | 212 us                                                                | 215 us: 1.02x slower                                                      |
| telco                   | 7.80 ms                                                               | 7.95 ms: 1.02x slower                                                     |
| regex_v8                | 21.9 ms                                                               | 22.3 ms: 1.02x slower                                                     |
| unpickle_list           | 4.94 us                                                               | 5.08 us: 1.03x slower                                                     |
| json_dumps              | 9.71 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| coroutines              | 21.6 ms                                                               | 22.2 ms: 1.03x slower                                                     |
| pickle_dict             | 31.7 us                                                               | 32.7 us: 1.03x slower                                                     |
| scimark_sparse_mat_mult | 4.57 ms                                                               | 4.73 ms: 1.03x slower                                                     |
| pickle_list             | 4.51 us                                                               | 4.70 us: 1.04x slower                                                     |
| mdp                     | 2.53 sec                                                              | 2.65 sec: 1.05x slower                                                    |
| regex_effbot            | 3.54 ms                                                               | 3.73 ms: 1.05x slower                                                     |
| mypy2                   | 337 ms                                                                | 359 ms: 1.06x slower                                                      |
| unpack_sequence         | 42.2 ns                                                               | 46.0 ns: 1.09x slower                                                     |
| xml_etree_parse         | 152 ms                                                                | 168 ms: 1.10x slower                                                      |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (15): spectral_norm, logging_format, scimark_sor, xml_etree_generate, pprint_safe_repr, bench_mp_pool, deepcopy, bench_thread_pool, typing_runtime_protocols, raytrace, logging_simple, go, asyncio_tcp, json, unpickle
Ignored benchmarks (3) of results/bm-20230807-3.13.0a0-2ac103c/bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c.json: docutils, pycparser, tomli_loads


# HPT report

- Reliability score: 75.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
