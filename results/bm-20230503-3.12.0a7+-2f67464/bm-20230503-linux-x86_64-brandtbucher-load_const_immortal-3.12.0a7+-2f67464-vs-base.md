
# Results vs. base

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 2f67464
- commit date: 2023-05-03
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.72 sec                                                               | 2.76 sec: 1.01x slower                                                      |
| tornado_http   | 102 ms                                                                 | 99.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 82.4 ms                                                                | 81.9 ms: 1.01x faster                                                       |
| nbody          | 89.7 ms                                                                | 89.2 ms: 1.00x faster                                                       |
| pidigits       | 197 ms                                                                 | 197 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 22.5 ms                                                                | 22.3 ms: 1.01x faster                                                       |
| regex_dna      | 207 ms                                                                 | 209 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                                 | 153 ms: 1.02x faster                                                        |
| unpickle_list        | 5.02 us                                                                | 4.94 us: 1.02x faster                                                       |
| unpickle_pure_python | 222 us                                                                 | 219 us: 1.01x faster                                                        |
| xml_etree_process    | 60.0 ms                                                                | 60.4 ms: 1.01x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                                | 86.3 ms: 1.01x slower                                                       |
| pickle               | 10.7 us                                                                | 10.8 us: 1.01x slower                                                       |
| pickle_dict          | 31.8 us                                                                | 32.1 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                                | 15.0 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (5): pickle_list, xml_etree_iterparse, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.70 ms                                                                | 6.68 ms: 1.00x faster                                                       |
| python_startup         | 9.19 ms                                                                | 9.16 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-----------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                                | 10.7 ms: 1.03x faster                                                       |

All benchmarks:
===============

| Benchmark              | bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7+-f5c3838 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| meteor_contest         | 116 ms                                                                 | 105 ms: 1.11x faster                                                        |
| mako                   | 11.0 ms                                                                | 10.7 ms: 1.03x faster                                                       |
| chaos                  | 71.5 ms                                                                | 69.4 ms: 1.03x faster                                                       |
| generators             | 31.9 ms                                                                | 31.0 ms: 1.03x faster                                                       |
| fannkuch               | 389 ms                                                                 | 379 ms: 1.03x faster                                                        |
| tornado_http           | 102 ms                                                                 | 99.8 ms: 1.03x faster                                                       |
| scimark_monte_carlo    | 74.9 ms                                                                | 73.4 ms: 1.02x faster                                                       |
| xml_etree_parse        | 156 ms                                                                 | 153 ms: 1.02x faster                                                        |
| scimark_lu             | 115 ms                                                                 | 113 ms: 1.02x faster                                                        |
| unpickle_list          | 5.02 us                                                                | 4.94 us: 1.02x faster                                                       |
| sqlglot_normalize      | 115 ms                                                                 | 113 ms: 1.02x faster                                                        |
| pprint_safe_repr       | 751 ms                                                                 | 740 ms: 1.02x faster                                                        |
| coroutines             | 22.7 ms                                                                | 22.3 ms: 1.02x faster                                                       |
| unpickle_pure_python   | 222 us                                                                 | 219 us: 1.01x faster                                                        |
| scimark_fft            | 358 ms                                                                 | 353 ms: 1.01x faster                                                        |
| logging_simple         | 6.38 us                                                                | 6.31 us: 1.01x faster                                                       |
| deepcopy_memo          | 39.3 us                                                                | 38.8 us: 1.01x faster                                                       |
| async_generators       | 459 ms                                                                 | 455 ms: 1.01x faster                                                        |
| scimark_sor            | 124 ms                                                                 | 123 ms: 1.01x faster                                                        |
| pathlib                | 18.7 ms                                                                | 18.5 ms: 1.01x faster                                                       |
| hexiom                 | 6.36 ms                                                                | 6.30 ms: 1.01x faster                                                       |
| pprint_pformat         | 1.53 sec                                                               | 1.51 sec: 1.01x faster                                                      |
| pycparser              | 1.16 sec                                                               | 1.15 sec: 1.01x faster                                                      |
| regex_v8               | 22.5 ms                                                                | 22.3 ms: 1.01x faster                                                       |
| logging_silent         | 102 ns                                                                 | 102 ns: 1.01x faster                                                        |
| create_gc_cycles       | 1.51 ms                                                                | 1.49 ms: 1.01x faster                                                       |
| bench_thread_pool      | 838 us                                                                 | 833 us: 1.01x faster                                                        |
| float                  | 82.4 ms                                                                | 81.9 ms: 1.01x faster                                                       |
| raytrace               | 307 ms                                                                 | 306 ms: 1.01x faster                                                        |
| sqlglot_optimize       | 55.7 ms                                                                | 55.4 ms: 1.01x faster                                                       |
| nbody                  | 89.7 ms                                                                | 89.2 ms: 1.00x faster                                                       |
| deepcopy_reduce        | 3.24 us                                                                | 3.23 us: 1.00x faster                                                       |
| python_startup_no_site | 6.70 ms                                                                | 6.68 ms: 1.00x faster                                                       |
| python_startup         | 9.19 ms                                                                | 9.16 ms: 1.00x faster                                                       |
| pidigits               | 197 ms                                                                 | 197 ms: 1.00x slower                                                        |
| asyncio_tcp            | 509 ms                                                                 | 510 ms: 1.00x slower                                                        |
| sqlglot_parse          | 1.34 ms                                                                | 1.35 ms: 1.00x slower                                                       |
| mypy2                  | 352 ms                                                                 | 354 ms: 1.00x slower                                                        |
| crypto_pyaes           | 80.1 ms                                                                | 80.5 ms: 1.01x slower                                                       |
| xml_etree_process      | 60.0 ms                                                                | 60.4 ms: 1.01x slower                                                       |
| xml_etree_generate     | 85.7 ms                                                                | 86.3 ms: 1.01x slower                                                       |
| regex_dna              | 207 ms                                                                 | 209 ms: 1.01x slower                                                        |
| unpack_sequence        | 49.5 ns                                                                | 50.0 ns: 1.01x slower                                                       |
| pickle                 | 10.7 us                                                                | 10.8 us: 1.01x slower                                                       |
| nqueens                | 82.4 ms                                                                | 83.3 ms: 1.01x slower                                                       |
| pickle_dict            | 31.8 us                                                                | 32.1 us: 1.01x slower                                                       |
| docutils               | 2.72 sec                                                               | 2.76 sec: 1.01x slower                                                      |
| deltablue              | 3.53 ms                                                                | 3.57 ms: 1.01x slower                                                       |
| mdp                    | 2.58 sec                                                               | 2.62 sec: 1.01x slower                                                      |
| unpickle               | 14.8 us                                                                | 15.0 us: 1.01x slower                                                       |
| telco                  | 6.91 ms                                                                | 7.05 ms: 1.02x slower                                                       |
| gc_traversal           | 3.82 ms                                                                | 3.94 ms: 1.03x slower                                                       |
| richards               | 43.6 ms                                                                | 45.4 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (28): json, sqlite_synth, dask, pyflate, sqlalchemy_declarative, pickle_list, xml_etree_iterparse, go, deepcopy, async_tree_cpu_io_mixed, regex_compile, spectral_norm, sqlglot_transpile, async_tree_none, json_dumps, scimark_sparse_mat_mult, 2to3, bench_mp_pool, json_loads, dulwich_log, regex_effbot, comprehensions, async_tree_memoization, pickle_pure_python, logging_format, coverage, sqlalchemy_imperative, async_tree_io
