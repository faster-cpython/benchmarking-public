
# Results vs. base

- fork: brandtbucher
- ref: immortal_increfs
- machine: linux-x86_64
- commit hash: 8abbc6a
- commit date: 2023-08-03
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.64 sec: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                    |
| float          | 80.5 ms                                                               | 79.8 ms: 1.01x faster                                                   |
| nbody          | 92.4 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                | 205 ms: 1.03x faster                                                    |
| regex_v8       | 22.4 ms                                                               | 21.8 ms: 1.02x faster                                                   |
| regex_compile  | 137 ms                                                                | 137 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                                              | 2.30 sec: 1.01x faster                                                  |
| json_loads           | 26.1 us                                                               | 25.8 us: 1.01x faster                                                   |
| xml_etree_process    | 57.7 ms                                                               | 57.9 ms: 1.00x slower                                                   |
| pickle_dict          | 31.6 us                                                               | 31.8 us: 1.01x slower                                                   |
| unpickle_pure_python | 212 us                                                                | 214 us: 1.01x slower                                                    |
| xml_etree_generate   | 83.3 ms                                                               | 84.1 ms: 1.01x slower                                                   |
| pickle               | 10.4 us                                                               | 10.6 us: 1.02x slower                                                   |
| pickle_list          | 4.57 us                                                               | 4.72 us: 1.03x slower                                                   |
| unpickle_list        | 4.99 us                                                               | 5.18 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, json_dumps, unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.84 ms: 1.00x slower                                                   |
| python_startup         | 9.33 ms                                                               | 9.35 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|-----------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 11.0 ms: 1.01x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e | bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpack_sequence         | 48.0 ns                                                               | 43.3 ns: 1.11x faster                                                   |
| pidigits                | 201 ms                                                                | 189 ms: 1.06x faster                                                    |
| richards                | 47.5 ms                                                               | 46.0 ms: 1.03x faster                                                   |
| regex_dna               | 211 ms                                                                | 205 ms: 1.03x faster                                                    |
| scimark_fft             | 366 ms                                                                | 356 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult | 4.85 ms                                                               | 4.73 ms: 1.02x faster                                                   |
| regex_v8                | 22.4 ms                                                               | 21.8 ms: 1.02x faster                                                   |
| deepcopy_memo           | 38.5 us                                                               | 37.6 us: 1.02x faster                                                   |
| logging_simple          | 5.96 us                                                               | 5.86 us: 1.02x faster                                                   |
| pyflate                 | 450 ms                                                                | 444 ms: 1.01x faster                                                    |
| richards_super          | 54.1 ms                                                               | 53.4 ms: 1.01x faster                                                   |
| pycparser               | 1.15 sec                                                              | 1.14 sec: 1.01x faster                                                  |
| deltablue               | 3.28 ms                                                               | 3.25 ms: 1.01x faster                                                   |
| pprint_pformat          | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                  |
| tomli_loads             | 2.33 sec                                                              | 2.30 sec: 1.01x faster                                                  |
| pprint_safe_repr        | 724 ms                                                                | 717 ms: 1.01x faster                                                    |
| json_loads              | 26.1 us                                                               | 25.8 us: 1.01x faster                                                   |
| float                   | 80.5 ms                                                               | 79.8 ms: 1.01x faster                                                   |
| fannkuch                | 394 ms                                                                | 391 ms: 1.01x faster                                                    |
| logging_format          | 6.48 us                                                               | 6.44 us: 1.01x faster                                                   |
| mako                    | 11.0 ms                                                               | 11.0 ms: 1.01x faster                                                   |
| scimark_sor             | 121 ms                                                                | 121 ms: 1.01x faster                                                    |
| docutils                | 2.65 sec                                                              | 2.64 sec: 1.00x faster                                                  |
| asyncio_tcp             | 484 ms                                                                | 483 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                  |
| gc_traversal            | 3.66 ms                                                               | 3.67 ms: 1.00x slower                                                   |
| python_startup_no_site  | 6.83 ms                                                               | 6.84 ms: 1.00x slower                                                   |
| python_startup          | 9.33 ms                                                               | 9.35 ms: 1.00x slower                                                   |
| bench_thread_pool       | 825 us                                                                | 827 us: 1.00x slower                                                    |
| deepcopy                | 355 us                                                                | 356 us: 1.00x slower                                                    |
| xml_etree_process       | 57.7 ms                                                               | 57.9 ms: 1.00x slower                                                   |
| go                      | 137 ms                                                                | 137 ms: 1.00x slower                                                    |
| regex_compile           | 137 ms                                                                | 137 ms: 1.00x slower                                                    |
| pickle_dict             | 31.6 us                                                               | 31.8 us: 1.01x slower                                                   |
| async_tree_io           | 1.19 sec                                                              | 1.19 sec: 1.01x slower                                                  |
| nqueens                 | 79.5 ms                                                               | 79.9 ms: 1.01x slower                                                   |
| sqlglot_parse           | 1.29 ms                                                               | 1.29 ms: 1.01x slower                                                   |
| nbody                   | 92.4 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| chaos                   | 59.2 ms                                                               | 59.6 ms: 1.01x slower                                                   |
| async_generators        | 444 ms                                                                | 448 ms: 1.01x slower                                                    |
| unpickle_pure_python    | 212 us                                                                | 214 us: 1.01x slower                                                    |
| xml_etree_generate      | 83.3 ms                                                               | 84.1 ms: 1.01x slower                                                   |
| dulwich_log             | 65.9 ms                                                               | 66.5 ms: 1.01x slower                                                   |
| hexiom                  | 6.01 ms                                                               | 6.08 ms: 1.01x slower                                                   |
| comprehensions          | 20.3 us                                                               | 20.6 us: 1.01x slower                                                   |
| telco                   | 7.84 ms                                                               | 7.99 ms: 1.02x slower                                                   |
| pickle                  | 10.4 us                                                               | 10.6 us: 1.02x slower                                                   |
| pickle_list             | 4.57 us                                                               | 4.72 us: 1.03x slower                                                   |
| crypto_pyaes            | 68.7 ms                                                               | 70.9 ms: 1.03x slower                                                   |
| unpickle_list           | 4.99 us                                                               | 5.18 us: 1.04x slower                                                   |
| generators              | 28.2 ms                                                               | 29.4 ms: 1.04x slower                                                   |
| coroutines              | 21.7 ms                                                               | 22.8 ms: 1.05x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (30): logging_silent, json, deepcopy_reduce, xml_etree_parse, pathlib, regex_effbot, xml_etree_iterparse, json_dumps, raytrace, scimark_monte_carlo, mdp, mypy2, coverage, bench_mp_pool, sqlglot_normalize, sqlglot_optimize, tornado_http, create_gc_cycles, meteor_contest, async_tree_cpu_io_mixed, unpickle, spectral_norm, typing_runtime_protocols, sqlite_synth, async_tree_memoization, sqlglot_transpile, dask, pickle_pure_python, async_tree_none, scimark_lu
