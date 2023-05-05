
# Results vs. base

- fork: mdboom
- ref: bolt_experiment
- machine: linux-x86_64
- commit hash: b488f91
- commit date: 2023-05-05
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 271 ms                                                                 | 270 ms: 1.00x faster                                              |
| docutils       | 2.71 sec                                                               | 2.73 sec: 1.01x slower                                            |
| tornado_http   | 99.8 ms                                                                | 102 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 189 ms: 1.04x faster                                              |
| nbody          | 90.0 ms                                                                | 87.7 ms: 1.03x faster                                             |
| float          | 82.1 ms                                                                | 81.6 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 207 ms                                                                 | 203 ms: 1.02x faster                                              |
| regex_compile  | 145 ms                                                                 | 146 ms: 1.01x slower                                              |
| regex_effbot   | 3.71 ms                                                                | 3.81 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_list        | 5.06 us                                                                | 4.88 us: 1.04x faster                                             |
| unpickle             | 15.6 us                                                                | 15.0 us: 1.04x faster                                             |
| json_loads           | 26.3 us                                                                | 25.7 us: 1.03x faster                                             |
| xml_etree_iterparse  | 105 ms                                                                 | 104 ms: 1.01x faster                                              |
| pickle               | 10.7 us                                                                | 10.6 us: 1.01x faster                                             |
| xml_etree_generate   | 85.0 ms                                                                | 85.3 ms: 1.00x slower                                             |
| pickle_dict          | 31.4 us                                                                | 31.7 us: 1.01x slower                                             |
| unpickle_pure_python | 218 us                                                                 | 220 us: 1.01x slower                                              |
| xml_etree_process    | 59.2 ms                                                                | 59.7 ms: 1.01x slower                                             |
| pickle_list          | 4.51 us                                                                | 4.57 us: 1.01x slower                                             |
| pickle_pure_python   | 313 us                                                                 | 323 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 9.14 ms                                                                | 9.14 ms: 1.00x faster                                             |
| python_startup_no_site | 6.66 ms                                                                | 6.67 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-----------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako      | 10.7 ms                                                                | 10.9 ms: 1.02x slower                                             |

All benchmarks:
===============

| Benchmark              | bm-20230505-linux-x86_64-python-45a9e3834a6ed20ee250-3.12.0a7+-45a9e38 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpack_sequence        | 51.6 ns                                                                | 46.6 ns: 1.11x faster                                             |
| gc_traversal           | 3.95 ms                                                                | 3.68 ms: 1.07x faster                                             |
| pidigits               | 197 ms                                                                 | 189 ms: 1.04x faster                                              |
| mdp                    | 2.73 sec                                                               | 2.61 sec: 1.04x faster                                            |
| unpickle_list          | 5.06 us                                                                | 4.88 us: 1.04x faster                                             |
| unpickle               | 15.6 us                                                                | 15.0 us: 1.04x faster                                             |
| coroutines             | 23.0 ms                                                                | 22.2 ms: 1.03x faster                                             |
| nbody                  | 90.0 ms                                                                | 87.7 ms: 1.03x faster                                             |
| json_loads             | 26.3 us                                                                | 25.7 us: 1.03x faster                                             |
| fannkuch               | 384 ms                                                                 | 375 ms: 1.02x faster                                              |
| pycparser              | 1.16 sec                                                               | 1.14 sec: 1.02x faster                                            |
| regex_dna              | 207 ms                                                                 | 203 ms: 1.02x faster                                              |
| telco                  | 6.93 ms                                                                | 6.82 ms: 1.02x faster                                             |
| generators             | 31.1 ms                                                                | 30.7 ms: 1.01x faster                                             |
| xml_etree_iterparse    | 105 ms                                                                 | 104 ms: 1.01x faster                                              |
| pyflate                | 450 ms                                                                 | 447 ms: 1.01x faster                                              |
| crypto_pyaes           | 81.0 ms                                                                | 80.4 ms: 1.01x faster                                             |
| scimark_fft            | 358 ms                                                                 | 355 ms: 1.01x faster                                              |
| pickle                 | 10.7 us                                                                | 10.6 us: 1.01x faster                                             |
| float                  | 82.1 ms                                                                | 81.6 ms: 1.01x faster                                             |
| meteor_contest         | 105 ms                                                                 | 104 ms: 1.01x faster                                              |
| create_gc_cycles       | 1.48 ms                                                                | 1.48 ms: 1.00x faster                                             |
| 2to3                   | 271 ms                                                                 | 270 ms: 1.00x faster                                              |
| python_startup         | 9.14 ms                                                                | 9.14 ms: 1.00x faster                                             |
| python_startup_no_site | 6.66 ms                                                                | 6.67 ms: 1.00x slower                                             |
| dulwich_log            | 68.1 ms                                                                | 68.3 ms: 1.00x slower                                             |
| xml_etree_generate     | 85.0 ms                                                                | 85.3 ms: 1.00x slower                                             |
| mypy2                  | 351 ms                                                                 | 353 ms: 1.01x slower                                              |
| regex_compile          | 145 ms                                                                 | 146 ms: 1.01x slower                                              |
| bench_thread_pool      | 832 us                                                                 | 837 us: 1.01x slower                                              |
| deepcopy_memo          | 38.1 us                                                                | 38.3 us: 1.01x slower                                             |
| coverage               | 102 ms                                                                 | 103 ms: 1.01x slower                                              |
| docutils               | 2.71 sec                                                               | 2.73 sec: 1.01x slower                                            |
| pickle_dict            | 31.4 us                                                                | 31.7 us: 1.01x slower                                             |
| unpickle_pure_python   | 218 us                                                                 | 220 us: 1.01x slower                                              |
| comprehensions         | 23.1 us                                                                | 23.3 us: 1.01x slower                                             |
| xml_etree_process      | 59.2 ms                                                                | 59.7 ms: 1.01x slower                                             |
| nqueens                | 81.1 ms                                                                | 82.1 ms: 1.01x slower                                             |
| go                     | 136 ms                                                                 | 138 ms: 1.01x slower                                              |
| chaos                  | 68.9 ms                                                                | 69.8 ms: 1.01x slower                                             |
| pickle_list            | 4.51 us                                                                | 4.57 us: 1.01x slower                                             |
| pprint_safe_repr       | 739 ms                                                                 | 750 ms: 1.01x slower                                              |
| pprint_pformat         | 1.51 sec                                                               | 1.53 sec: 1.02x slower                                            |
| richards               | 43.8 ms                                                                | 44.6 ms: 1.02x slower                                             |
| logging_simple         | 6.36 us                                                                | 6.47 us: 1.02x slower                                             |
| mako                   | 10.7 ms                                                                | 10.9 ms: 1.02x slower                                             |
| scimark_sor            | 122 ms                                                                 | 124 ms: 1.02x slower                                              |
| scimark_lu             | 114 ms                                                                 | 116 ms: 1.02x slower                                              |
| raytrace               | 303 ms                                                                 | 310 ms: 1.02x slower                                              |
| async_generators       | 449 ms                                                                 | 459 ms: 1.02x slower                                              |
| sqlalchemy_imperative  | 18.9 ms                                                                | 19.3 ms: 1.02x slower                                             |
| tornado_http           | 99.8 ms                                                                | 102 ms: 1.02x slower                                              |
| regex_effbot           | 3.71 ms                                                                | 3.81 ms: 1.03x slower                                             |
| hexiom                 | 6.21 ms                                                                | 6.41 ms: 1.03x slower                                             |
| pickle_pure_python     | 313 us                                                                 | 323 us: 1.03x slower                                              |
| spectral_norm          | 106 ms                                                                 | 111 ms: 1.04x slower                                              |
| logging_silent         | 98.0 ns                                                                | 104 ns: 1.06x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (24): sqlite_synth, scimark_sparse_mat_mult, xml_etree_parse, logging_format, json, regex_v8, deepcopy, scimark_monte_carlo, pathlib, asyncio_tcp, async_tree_none, async_tree_cpu_io_mixed, bench_mp_pool, sqlglot_parse, sqlglot_transpile, json_dumps, sqlglot_optimize, dask, deltablue, sqlglot_normalize, deepcopy_reduce, async_tree_io, sqlalchemy_declarative, async_tree_memoization
