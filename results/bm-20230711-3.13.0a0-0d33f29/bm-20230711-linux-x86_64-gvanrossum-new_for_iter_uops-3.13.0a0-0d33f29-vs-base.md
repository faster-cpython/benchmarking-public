
# Results vs. base

- fork: gvanrossum
- ref: new_for_iter_uops
- machine: linux-x86_64
- commit hash: 0d33f29
- commit date: 2023-07-11
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                                   |
| nbody          | 89.8 ms                                                               | 92.3 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                | 210 ms: 1.02x faster                                                   |
| regex_compile  | 136 ms                                                                | 138 ms: 1.01x slower                                                   |
| regex_effbot   | 3.52 ms                                                               | 3.67 ms: 1.04x slower                                                  |
| regex_v8       | 21.8 ms                                                               | 22.9 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                                              | 2.31 sec: 1.01x faster                                                 |
| pickle               | 10.5 us                                                               | 10.4 us: 1.00x faster                                                  |
| pickle_pure_python   | 294 us                                                                | 295 us: 1.00x slower                                                   |
| pickle_list          | 4.58 us                                                               | 4.63 us: 1.01x slower                                                  |
| unpickle_pure_python | 210 us                                                                | 214 us: 1.02x slower                                                   |
| unpickle_list        | 4.99 us                                                               | 5.15 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (8): xml_etree_generate, json_loads, xml_etree_iterparse, xml_etree_process, pickle_dict, json_dumps, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.70 ms                                                               | 6.70 ms: 1.00x slower                                                  |
| python_startup         | 9.21 ms                                                               | 9.22 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|-----------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.8 ms: 1.02x slower                                                  |

All benchmarks:
===============

| Benchmark               | bm-20230711-linux-x86_64-python-d0b7e18262e69dd4b825-3.13.0a0-d0b7e18 | bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_fft             | 375 ms                                                                | 362 ms: 1.04x faster                                                   |
| pycparser               | 1.19 sec                                                              | 1.17 sec: 1.02x faster                                                 |
| regex_dna               | 214 ms                                                                | 210 ms: 1.02x faster                                                   |
| deepcopy                | 355 us                                                                | 351 us: 1.01x faster                                                   |
| pathlib                 | 18.8 ms                                                               | 18.6 ms: 1.01x faster                                                  |
| async_generators        | 455 ms                                                                | 451 ms: 1.01x faster                                                   |
| tomli_loads             | 2.33 sec                                                              | 2.31 sec: 1.01x faster                                                 |
| async_tree_io           | 1.18 sec                                                              | 1.18 sec: 1.00x faster                                                 |
| pickle                  | 10.5 us                                                               | 10.4 us: 1.00x faster                                                  |
| asyncio_tcp             | 507 ms                                                                | 505 ms: 1.00x faster                                                   |
| python_startup_no_site  | 6.70 ms                                                               | 6.70 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                 |
| pidigits                | 197 ms                                                                | 197 ms: 1.00x slower                                                   |
| python_startup          | 9.21 ms                                                               | 9.22 ms: 1.00x slower                                                  |
| pprint_pformat          | 1.46 sec                                                              | 1.47 sec: 1.00x slower                                                 |
| bench_thread_pool       | 815 us                                                                | 818 us: 1.00x slower                                                   |
| pickle_pure_python      | 294 us                                                                | 295 us: 1.00x slower                                                   |
| mypy2                   | 335 ms                                                                | 337 ms: 1.01x slower                                                   |
| pyflate                 | 444 ms                                                                | 446 ms: 1.01x slower                                                   |
| docutils                | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                                 |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.01x slower                                                   |
| nqueens                 | 79.4 ms                                                               | 80.1 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                  |
| async_tree_none         | 480 ms                                                                | 484 ms: 1.01x slower                                                   |
| pickle_list             | 4.58 us                                                               | 4.63 us: 1.01x slower                                                  |
| sqlglot_transpile       | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                                  |
| regex_compile           | 136 ms                                                                | 138 ms: 1.01x slower                                                   |
| coverage                | 92.5 ms                                                               | 93.4 ms: 1.01x slower                                                  |
| mdp                     | 2.64 sec                                                              | 2.67 sec: 1.01x slower                                                 |
| comprehensions          | 20.3 us                                                               | 20.5 us: 1.01x slower                                                  |
| scimark_sor             | 120 ms                                                                | 122 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| generators              | 28.3 ms                                                               | 28.7 ms: 1.01x slower                                                  |
| dulwich_log             | 65.7 ms                                                               | 66.6 ms: 1.01x slower                                                  |
| logging_format          | 6.51 us                                                               | 6.61 us: 1.01x slower                                                  |
| telco                   | 7.11 ms                                                               | 7.22 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 210 us                                                                | 214 us: 1.02x slower                                                   |
| deltablue               | 3.24 ms                                                               | 3.30 ms: 1.02x slower                                                  |
| richards_super          | 52.8 ms                                                               | 53.8 ms: 1.02x slower                                                  |
| coroutines              | 22.7 ms                                                               | 23.1 ms: 1.02x slower                                                  |
| deepcopy_reduce         | 3.10 us                                                               | 3.16 us: 1.02x slower                                                  |
| fannkuch                | 391 ms                                                                | 399 ms: 1.02x slower                                                   |
| chaos                   | 58.9 ms                                                               | 60.1 ms: 1.02x slower                                                  |
| raytrace                | 267 ms                                                                | 273 ms: 1.02x slower                                                   |
| mako                    | 10.6 ms                                                               | 10.8 ms: 1.02x slower                                                  |
| richards                | 46.5 ms                                                               | 47.6 ms: 1.02x slower                                                  |
| hexiom                  | 5.95 ms                                                               | 6.11 ms: 1.03x slower                                                  |
| nbody                   | 89.8 ms                                                               | 92.3 ms: 1.03x slower                                                  |
| unpickle_list           | 4.99 us                                                               | 5.15 us: 1.03x slower                                                  |
| spectral_norm           | 107 ms                                                                | 111 ms: 1.04x slower                                                   |
| regex_effbot            | 3.52 ms                                                               | 3.67 ms: 1.04x slower                                                  |
| crypto_pyaes            | 68.4 ms                                                               | 71.5 ms: 1.04x slower                                                  |
| logging_silent          | 99.2 ns                                                               | 104 ns: 1.05x slower                                                   |
| regex_v8                | 21.8 ms                                                               | 22.9 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (27): sqlite_synth, unpack_sequence, deepcopy_memo, create_gc_cycles, xml_etree_generate, gc_traversal, sqlglot_optimize, async_tree_memoization, json_loads, bench_mp_pool, xml_etree_iterparse, pprint_safe_repr, xml_etree_process, float, pickle_dict, logging_simple, json_dumps, xml_etree_parse, go, scimark_monte_carlo, typing_runtime_protocols, scimark_lu, tornado_http, async_tree_cpu_io_mixed, json, dask, unpickle
